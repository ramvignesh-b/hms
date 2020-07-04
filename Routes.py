from hms import app
from datetime import datetime, date
from flask import render_template, session, url_for, request, redirect, flash, session, g
from .Forms import Login_form, Patient_create, Patient_delete, delete_result, Patient_update, issue_medicine_form, add_diagnosis
from .Models import UserStore, Patient_test, Patient_Medicine, Patient_details, Diagnosis, Medicine
from .Config import db

# store patient ID for querying
pid = 0
issue_med = None
quantity = []
add_test = None


@app.context_processor
def inject_now():
    return {'now': date.today()}


# Function to implement session management and check the category of stakeholder accessing the website


def check_session():
    if 'user' not in session or not session['user']:
        return None
    else:
        stakeholder_type = session['user'][-1]
        if stakeholder_type == 'A':
            session['stakeholder'] = 'registration_desk_executive'
            return 'registration_desk_executive'
        elif stakeholder_type == 'D':
            session['stakeholder'] = 'diagnostic_executive'
            return 'diagnostic_executive'
        elif stakeholder_type == 'P':
            session['stakeholder'] = 'pharmacy_executive'
            return 'pharmacy_executive'


# ==================================================================================
#                                   Home and Login
# ==================================================================================


@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def main():
    if check_session():
        return render_template('index.html', user=session['user'])
    form = Login_form()
    if request.method == 'POST':
        # Validate the form
        if form.validate_on_submit():
            # Check the credentials
            if UserStore.query.filter_by(login=request.form.get('username'), password=request.form.get('password')).first():
                flash("Login successful!", "success")
                session['user'] = request.form.get('username')
                return redirect(url_for('main'))
            else:
                flash("Invalid credentials!", "danger")
                return render_template('login.html', title="Login", form=form)
    return render_template('login.html', title="Login", form=form)


@app.route("/index")
def index():
    if not check_session():
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))
    return render_template("index.html")

# ==================================================================================
#                                 Patient Registration
# ==================================================================================


@app.route("/CreatePatient", methods=['GET', 'POST'])
def create_patient():

    # Check that an authorised user only can access this functionality
    if check_session() != 'registration_desk_executive':
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))

    # If form has been submitted
    form = Patient_create()
    if request.method == 'POST':
        if form.validate_on_submit():
            ssn_id = form.ssn_id.data
            name = form.patient_name.data
            age = form.patient_age.data
            date = form.date.data
            bed_type = form.Type_of_bed.data
            address = form.address.data
            state = request.form.get('stt')
            city = request.form.get('state_list')
            # Add the patient to the database
            details = Patient_details(
                name, age, ssn_id, date, bed_type, address, city, state, status="Admitted")
            db.session.add(details)
            db.session.commit()
            flash("Patient creation initiated successfully", "success")
    return render_template("create_patient.html", title="Create Patient", form=form)


# ==================================================================================
#                              Delete an existing patient
# ==================================================================================


@app.route("/DeletePatient", methods=["GET", "POST"])
def delete_patient():

    # Check that an authorised user only can access this functionality
    if check_session() != 'registration_desk_executive':
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))

    form = Patient_delete()
    if form.validate_on_submit():
        global pid
        pid = int(form.patient_id.data)
        # Query for patient_details
        patient = Patient_details.query.filter(
            Patient_details.id == int(form.patient_id.data))
        for patient_1 in patient:
            if patient_1:
                form2 = delete_result()
                flash("patient found", "success")
                return render_template("delete_patient2.html", title="Delete patient", patient=patient, form=form2)
        flash("patient not found", "danger")
    return render_template("delete_patient.html", title="Delete Patient", form=form)


@app.route("/deletepatient2", methods=["GET", "POST"])
def delete_patient2():

    # Check that an authorised user only can access this functionality
    if check_session() != 'registration_desk_executive':
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))

    form2 = delete_result()
    if form2.validate_on_submit():
        global pid
        print(pid)
        # delete query
        Patient_details.query.filter_by(id=pid).delete()
        db.session.commit()
        flash("patient deleted successfully", "success")

        return redirect(url_for('delete_patient'))
    else:
        flash("patient delete failed . Please try again", "danger")
        return redirect(url_for('delete_patient'))


# ==================================================================================
#                       Search for existing patient using Patient ID
# ==================================================================================


@app.route("/SearchPatient", methods=["GET", "POST"])
def search_patient():

    # Check that an authorised user only can access this functionality
    if check_session() != 'registration_desk_executive':
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))

    form = Patient_delete()
    if request.method == 'POST':
        if form.validate_on_submit():
            global pid
            pid = int(form.patient_id.data)
            # Query for patient_details
            patient = Patient_details.query.filter(
                Patient_details.id == int(form.patient_id.data))
            for patient_1 in patient:
                if patient_1:
                    flash("patient found", "success")
                    return render_template("search_patient.html", title="Search patient", patient=patient, form=form)
            flash("patient not found", "danger")
    return render_template("search_patient.html", title="Search Patient", form=form)


# ==================================================================================
#                    Update the detains of an existing patient
# ==================================================================================


@app.route("/UpdatePatient", methods=["GET", "POST"])
def update_patient():
    flag = 0

    # Check that an authorised user only can access this functionality
    if check_session() != 'registration_desk_executive':
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))

    form = Patient_delete()
    if form.validate_on_submit():
        global pid
        pid = int(form.patient_id.data)
        # Query for patient details
        patient = Patient_details.query.filter(
            Patient_details.id == int(form.patient_id.data))
        for patient_1 in patient:
            if patient_1:
                flash("patient found", "success")
                flag = 1
                # Display the update form
                form2 = Patient_update(Type_of_bed=patient_1.bed_type, date=patient_1.admission_date,
                                       address=patient_1.address, patient_name=patient_1.name, patient_age=patient_1.age)
                return render_template("update_patient.html", title="Update Patient", form=form, form2=form2, flag=flag, patient_s=patient)
        flash("Patient not found", "danger")
    return render_template("update_patient.html", title="Update Patient", form=form, flag=flag)


@app.route("/UpdatePatient2", methods=["GET", "POST"])
def update_result():

    # Check that an authorised user only can access this functionality
    if check_session() != 'registration_desk_executive':
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))

    form = Patient_update()
    if request.method == "POST":
        if form.validate_on_submit():
            global pid
            if request.form.get('stt') != "":
                if request.form.get('state_list') == None or request.form.get('state_list') == "":
                    # Query for patient Details
                    patient = Patient_details.query.filter(
                        Patient_details.id == pid)
                    for patient_1 in patient:
                        if patient_1:

                            flag = 1
                            flash(
                                "You have to select city if you change state", "danger")
                            form2 = Patient_update(Type_of_bed=patient_1.bed_type, date=patient_1.admission_date,
                                                   address=patient_1.address, patient_name=patient_1.name, patient_age=patient_1.age)
                            return render_template("update_patient.html", title="Update Patient", form=form, form2=form2, flag=flag, patient_s=patient)
            if request.form.get('stt') == "":
                name = form.patient_name.data
                age = form.patient_age.data
                date = form.date.data
                bed_type = form.Type_of_bed.data
                address = form.address.data
                # Update the patient_details table
                Patient_details.query.filter_by(id=pid).update({"name": name})
                Patient_details.query.filter_by(
                    id=pid).update({"admission_date": date})
                Patient_details.query.filter_by(id=pid).update({"age": age})
                Patient_details.query.filter_by(
                    id=pid).update({"bed_type": bed_type})
                Patient_details.query.filter_by(
                    id=pid).update({"address": address})
            else:
                name = form.patient_name.data
                age = form.patient_age.data
                date = form.date.data
                bed_type = form.Type_of_bed.data
                address = form.address.data
                city = request.form.get('state_list')
                state = request.form.get('stt')
                # Update the patient_details table
                Patient_details.query.filter_by(id=pid).update({"name": name})
                Patient_details.query.filter_by(
                    id=pid).update({"admission_date": date})
                Patient_details.query.filter_by(id=pid).update({"city": city})
                Patient_details.query.filter_by(
                    id=pid).update({"state": state})
                Patient_details.query.filter_by(id=pid).update({"age": age})
                Patient_details.query.filter_by(
                    id=pid).update({"bed_type": bed_type})
                Patient_details.query.filter_by(
                    id=pid).update({"address": address})
            # Commit the changes
            db.session.commit()
            flash("Patient update intiated successfully!", "success")
            return redirect(url_for('update_patient'))
        # Query for patient_details
        patient = Patient_details.query.filter(Patient_details.id == pid)
        for patient_1 in patient:
            if patient_1:
                flag = 1
                flash("Please enter AGE in integer format and less than or equal to 3 digits in length!", "danger")
                form2 = Patient_update(Type_of_bed=patient_1.bed_type, date=patient_1.admission_date,
                                       address=patient_1.address, patient_name=patient_1.name, patient_age=patient_1.age)
                return render_template("update_patient.html", title="Update Patient", form=form, form2=form2, flag=flag, patient_s=patient)


# ==================================================================================
#                   View all the admitted patients in record
# ==================================================================================


@app.route("/ViewAllPatients")
def view_patient():

    # Check that an authorised user only can access this functionality
    if check_session() != 'registration_desk_executive':
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))
    # Query for all admitted patients
    patient = Patient_details.query.filter_by(status="Admitted")
    return render_template("view_patients.html", patients=patient)


# ==================================================================================
#                                   Issue Medicines
# ==================================================================================


@app.route("/GetPatientDetails/Medicine", methods=["GET", "POST"])
def get_patient():

    # Check that an authorised user only can access this functionality
    if check_session() != 'pharmacy_executive':
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))

    form = Patient_delete()
    if request.method == 'POST':
        if form.validate_on_submit():
            global pid
            global issue_med
            pid = int(form.patient_id.data)
            # Query for patient details
            patient = Patient_details.query.filter(
                Patient_details.id == int(form.patient_id.data))
            for patient_1 in patient:
                if patient_1:
                    flash("Patient found!", "success")
                    issue_med = None
                    medicine = med_patient(patient_1)
                    if medicine != None:
                        return render_template("get_patient_details.html", title="Search patient", patient=patient, medicine=medicine.all())
                    else:
                        return render_template("get_patient_details.html", title="Search patient", patient=patient)
            flash("patient not found", "danger")
    return render_template("get_patient_details.html", title="Get Patient Details", form=form)


@app.route("/IssueMedicine", methods=["GET", "POST"])
def issue_medicine():
    # Check that an authorised user only can access this functionality
    if check_session() != 'pharmacy_executive':
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))
    global issue_med
    global pid
    form = issue_medicine_form()
    form.medicine_name.choices = []
    medicine = Medicine.query.all()
    for med in medicine:
        # Populate the medicine select form
        form.medicine_name.choices += [(med.medicine_name, med.medicine_name + ' || Qty: ' + str(med.medicine_quantity))]
    if form.validate_on_submit():
        name = form.medicine_name.data
        quantity = form.quantity.data
        # Query for medicines
        med = Medicine.query.filter(
            Medicine.medicine_name == form.medicine_name.data).first()
        medid = med.id
        rate = med.medicine_amount
        # Update issue_med dict
        if issue_med == None:
            issue_med = {}
            issue_med[name] = {
                'name': name, 'quantity': quantity, 'medid': medid, 'rate': rate}
        else:
            issue_med[name] = {
                'name': name, 'quantity': quantity, 'medid': medid, 'rate': rate}
        flash("Medicine Added!", "success")
        return render_template("issue_medicine.html", form=form, medicine=issue_med)
    return render_template("issue_medicine.html", form=form, medicine=issue_med)


@app.route("/medicine_update", methods=["GET", "POST"])
def update():
    # Check that an authorised user only can access this functionality
    if check_session() != 'pharmacy_executive':
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))
    global issue_med
    global pid
    for i in issue_med:
        med_name = str(issue_med[i]['name'])
        med_id = int(issue_med[i]['medid'])
        med_quant = int(issue_med[i]['quantity'])
        # Query for Medicines
        medicine = Medicine.query.filter(
            Medicine.medicine_name == med_name).first()
        current_quant = medicine.medicine_quantity
        new_quant = current_quant-med_quant
        # Query for patient_medicines
        patient = Patient_Medicine.query.filter(
            Patient_Medicine.patient_id == pid, Patient_Medicine.medicine_id == med_id).first()
        if patient == None:
            # Query for Patient_Medicine 
            db.session.add(Patient_Medicine(
                patient_id=pid, medicine_quantity=med_quant, medicine_id=med_id))
            medicine.medicine_quantity = new_quant
            db.session.commit()
        else:
            # Update Medicine Quantity
            medicine.medicine_quantity = new_quant
            patient.medicine_quantity += med_quant
            db.session.commit()
    issue_med = None
    flash("successfully updated", "success")
    return redirect(url_for('get_patient'))


# function to retrieve patient medicines
def med_patient(patient):
    mid = patient.id
    if Patient_Medicine.query.filter(Patient_Medicine.patient_id == mid).first() == None:
        return None
    else:
        x = Patient_Medicine.query.join(Medicine, Patient_Medicine.medicine_id == Medicine.id).filter(
            Patient_Medicine.patient_id == mid)
        return x


# ==================================================================================
#                                   Diagnostics
# ==================================================================================


@app.route("/GetPatientDetails/Diagnostics", methods=["GET", "POST"])
def patient_diagnosis():

    # Check that an authorised user only can access this functionality
    if check_session() != 'diagnostic_executive':
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))

    form = Patient_delete()
    if request.method == 'POST':
        if form.validate_on_submit():
            global pid
            global add_test
            pid = int(form.patient_id.data)
            patient = Patient_details.query.filter(
                Patient_details.id == int(form.patient_id.data))
            for patient_1 in patient:
                if patient_1:
                    add_test = None
                    flash("patient found", "success")
                    # Query for patient_diagnostics
                    if Patient_test.query.filter(Patient_test.patient_id == patient_1.id).first() == None:
                        return render_template("get_patient_diagnosis.html", title="Search patient", patient=patient, pid=pid)
                    else:
                        x = Patient_test.query.join(Diagnosis, Patient_test.test_id == Diagnosis.id).filter(
                            Patient_test.patient_id == patient_1.id)
                        return render_template("get_patient_diagnosis.html", title="Search patient", patient=patient, pid=pid, tests=x)
            flash("patient not found", "danger")
    return render_template("get_patient_diagnosis.html", title="Get Patient Diagnostics", form=form)


@app.route("/Diagnostics", methods=["GET", "POST"])
def diagnostics():

    # Check that an authorised user only can access this functionality
    if check_session() != 'diagnostic_executive':
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))
    global pid
    global add_test
    form = add_diagnosis()
    if form.validate_on_submit():
        testname = form.diagnosis.data
        # Query for Diagnostics
        test = Diagnosis.query.filter(Diagnosis.test_name == testname).first()
        if add_test == None:
            add_test = {}
            add_test[testname] = {'name': testname, 'amount': test.test_amount}
        else:
            add_test[testname] = {'name': testname, 'amount': test.test_amount}
        flash("medicine added", "success")
        return render_template("diagnostics.html", pid=pid, title="Conduct Diagnostics", form=form, tests=add_test)
    return render_template("diagnostics.html", pid=pid, title="Conduct Diagnostics", form=form, tests=add_test)


@app.route('/updatetest', methods=['GET', 'POST'])
def update_test():
    if check_session() != 'diagnostic_executive':
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))
    global pid
    global add_test
    for i in add_test:
        name = add_test[i]['name']
        # Query for diagnostics
        test = Diagnosis.query.filter(Diagnosis.test_name == name).first()
        tid = test.id
        # Add the diagnostic to db
        db.session.add(Patient_test(patient_id=pid, test_id=tid))
        db.session.commit()
    add_test = None
    flash("Successfully updated", "success")
    return redirect(url_for('patient_diagnosis'))


# ==================================================================================
#                                   Patient Billing
# ==================================================================================

@app.route('/FinalBilling', methods=["GET", "POST"])
def billing():

    # Check that an authorised user only can access this functionality
    if check_session() != 'registration_desk_executive':
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))
    mbill = 0
    tbill = 0
    form = Patient_delete()
    if request.method == 'POST':
        mbill = 0
        tbill = 0
        if form.validate_on_submit():
            # Query for patient details
            patient = Patient_details.query.filter(
                Patient_details.id == int(form.patient_id.data))
            for patient_1 in patient:
                if patient_1:
                    flash("Patient found", "success")
                    mbill = 0
                    tbill = 0
                    medicine = med_patient(patient_1)
                    if medicine:
                        for m in medicine:
                            mbill = mbill + \
                                (m.medicine.medicine_amount*m.medicine_quantity)
                    # Query for patient diagnostics
                    test = Patient_test.query.join(Diagnosis, Patient_test.test_id == Diagnosis.id).filter(
                        Patient_test.patient_id == patient_1.id)
                    if test:
                        for t in test:
                            tbill = tbill+t.diagnosis.test_amount
                    # Calculate the number of days since the admission
                    days = date.today() - patient[0].admission_date
                    # Calculate the room charges
                    if patient[0].bed_type.lower() == 'general ward':
                        charges = 2000
                    elif patient[0].bed_type.lower() == 'semi sharing':
                        charges = 4000
                    elif patient[0].bed_type.lower() == 'single room':
                        charges = 8000
                    return render_template('billing.html', patient=patient, medicine=medicine, tests=test, mbill=mbill, tbill=tbill, days=days, charges=charges, total=str(days * charges).replace("days, 0:00:00", ""), pid=patient[0].id)
            flash("Patient not found!", "danger")
    return render_template('billing.html', form=form, tbill=tbill, mbill=mbill, total=0)


@app.route('/Discharge', methods=["POST"])
def discharge():
    if check_session() != 'registration_desk_executive':
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))
    patient = Patient_details.query.filter_by(
        id=request.form.get('pid')).first()
    if patient:
        # Check if the patient is already discharged
        if patient.status == 'Discharged':
            flash("Patient already Discharged!", "danger")
        else:
            # Discharge the patient
            patient.status = 'Discharged'
            db.session.commit()
            flash("Successfully Discharged the patient!", "success")
    return redirect(url_for('billing'))

# ==================================================================================
#                                 Delete the user Session
# ==================================================================================


@app.route("/logout")
def logout():
    # Remove user from the session
    if not check_session():
        flash('You are not authorised to access that! Please login with proper credentials.', 'danger')
        return redirect(url_for('main'))
    if 'user' in session:
        session['user'] = None
        flash("Successfully Logged Out!", "success")
    return redirect(url_for('main'))
