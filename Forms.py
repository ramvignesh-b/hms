from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, Length, ValidationError
import datetime
from wtforms.fields.html5 import DateField, widgets
from .Models import UserStore, Patient_test, Patient_Medicine, Patient_details, Diagnosis, Medicine
import re

class check_alpha(FlaskForm):
    def __init__(self, message):
        if not message:
            message = "input should contain alphabets only"
        self.message = message

    def __call__(self, form, field):
        name = str(field.data)
        if not name.isalpha():
            raise ValidationError(self.message)


class check_med(FlaskForm):
    def __init__(self, message):
        if not message:
            self.message = "Medicine Unavailable"
        self.message = message

    def __call__(self, form, field):
        name = form.medicine_name.data
        quant = field.data
        '''
        if Medicine.query.filter(Medicine.medicine_name==name).first()==None:
            raise ValidationError('MEDICINE NOT FOUND IN DATABASE')
        '''
        medicines = Medicine.query.filter(Medicine.medicine_name == name)
        for medicine in medicines:
            if quant > medicine.medicine_quantity or quant < 0:
                raise ValidationError("Medicine quantity entered is more than available Quantity!. Available Quantity={}".format(
                    medicine.medicine_quantity))

# custom validator to check password while logging in


class pass_val(FlaskForm):
    def __init__(self, message):
        if not message:
            self.message = "password criteria not met"
        self.message = message

    def __call__(self, form, field):
        nflag = 0
        cflag = 0
        upflag = 0
        x = str(field.data)

        for i in x:
            if i == " ":
                raise ValidationError('Space not allowed in passwords')
                break
            if i.isnumeric():
                nflag += 1

            if (not i.isalnum()) and (not i == ' '):
                cflag += 1
            if i.isupper():
                upflag += 1
        if nflag == 0 or cflag == 0 or upflag == 0:
            raise ValidationError(self.message)
        if len(x) != 10:
            raise ValidationError("Password must be 10 characters long")


# class for login page form
class Login_form(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(
        min=8, message="ID should be atleast 8 characters long")])
    password = PasswordField('password', validators=[DataRequired(), Length(min=10, max=10, message=""), pass_val(
        message="password should have atleast 1 numeric and 1 special character and 1 uppercase and should be 10 characters long")])
    submit = SubmitField('login')


# custom validator to check length of integer input fields
class check_length(FlaskForm):
    def __init__(self, message, min=-1, max=-1):
        self.min = min
        self.max = max
        if not message:
            self.message = "input length must be between {} and {}".format(
                min, max)
        self.message = message

    def __call__(self, form, field):
        size = len(str(field.data))
        if Patient_details.query.filter_by(ssn_id=str(field.data)).first() != None:
            raise ValidationError("Patient with that id already exists!")
        if size < self.min or size > self.max:
            raise ValidationError(self.message)


# class for patient registration form
class Patient_create(FlaskForm):
    ssn_id = IntegerField('ssn id', validators=[DataRequired(
        'please enter SSN ID in integer format'), check_length(message="id must be 9 digits long", min=9, max=9)])
    patient_name = StringField('patient name', validators=[
                               DataRequired('please enter name')])
    patient_age = IntegerField('patient age', widget=widgets.Input(input_type="number"), validators=[DataRequired(
        'please enter age'), check_length(min=1, max=3, message="age should be 1-3 digits long")])
    date = DateField('enter date', format="%Y-%m-%d", validators=[
                     DataRequired('please enter date')], default=datetime.date.today())
    Type_of_bed = SelectField('bed type', choices=[('General ward', 'General ward'), (
        'Semi sharing', 'Semi sharing'), ('single room', 'single room')], validators=[DataRequired('select ward type')])
    address = StringField('enter address', validators=[
                          DataRequired('enter the address')])
    submit = SubmitField('create')

    def validate_date(form, date):
        if date.data > datetime.date.today():
            raise ValidationError("Date of Admission cannot exceed today's date!")
    
    def validate_patient_name(form,patient_name):
        if not patient_name.data.isalpha():
            raise ValidationError("Name cannot contain numbers/ symbols")

    def validate_address(form,address):
        if not re.match("^[a-zA-Z0-9,. ]*$", address.data):
            raise ValidationError("Address can only contain alphabets, numbers, comma and periods!")


# class for delete patient form
class Patient_delete(FlaskForm):
    # check_length(message="id must be 9 digits long",min=9, max=9)])
    patient_id = IntegerField('Patient id', validators=[
                              DataRequired('please enter Patient ID in integer format')])
    submit = SubmitField('Search')


class delete_result(FlaskForm):
    submit = SubmitField('delete')


class Patient_update(FlaskForm):
    patient_name = StringField('patient name', validators=[
                               DataRequired('please enter name')])
    patient_age = IntegerField('patient age', widget=widgets.Input(input_type="number"), validators=[
                               DataRequired('please enter age'), check_length(min=1, max=3, message="age should be 1-3 digits long")])
    date = DateField('enter date', format="%Y-%m-%d", validators=[
                     DataRequired('please enter date')], default=datetime.date.today())
    Type_of_bed = SelectField('bed type', choices=[('General ward', 'General ward'), (
        'Semi sharing', 'Semi sharing'), ('single room', 'single room')], validators=[DataRequired('select ward type')])
    address = StringField('enter address', validators=[
                          DataRequired('enter the address')])
    submit = SubmitField('update')

    def validate_date(form, date):
        if date.data > datetime.date.today():
            raise ValidationError("Date of Admission cannot exceed today's date!")
    
    def validate_patient_name(form,patient_name):
        if not patient_name.data.isalpha():
            raise ValidationError("Name cannot contain numbers/ symbols")

    def validate_address(form,address):
        if not re.match("^[a-zA-Z0-9,. ]*$", address.data):
            raise ValidationError("Address can only contain alphabets, numbers, comma and periods!")


# class for medicine issuing
class issue_medicine_form(FlaskForm):
    medicine = Medicine.query.all()
    meds = []
    for med in medicine:
        meds.append(med.medicine_name)
    #medicine_name=StringField('Medicine name',validators=[DataRequired('Please enter medicine name '),check_alpha('medicine name has to be alphabet only')])
    medicine_name = SelectField(
        'Select a medicine', choices=[], validators=[DataRequired()])
    quantity = IntegerField('QUANTITY', widget=widgets.Input(input_type="number"), validators=[
                            DataRequired('Please enter quantity'), check_med('medicine not found')])
    submit = SubmitField('Add')


class add_diagnosis(FlaskForm):
    x = Diagnosis.query.all()
    lst = []
    label = ""
    for i in x:
        label = str(i.test_name)+"               :-      ₹"+str(i.test_amount)
        lst.append((i.test_name, label))

    diagnosis = SelectField('diagnosis', choices=lst, validators=[
                            DataRequired('please select a test')])
    submit = SubmitField('Add')
