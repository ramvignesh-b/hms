BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "patient_test" (
	"id"	INTEGER NOT NULL,
	"patient_id"	INTEGER NOT NULL,
	"test_id"	INTEGER NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "diagnosis" (
	"id"	INTEGER NOT NULL,
	"test_name"	VARCHAR(45) NOT NULL,
	"test_amount"	INTEGER NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "medicine" (
	"id"	INTEGER NOT NULL,
	"medicine_name"	VARCHAR(45) NOT NULL,
	"medicine_amount"	INTEGER NOT NULL,
	"medicine_quantity"	INTEGER NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "patient__medicine" (
	"id"	INTEGER NOT NULL,
	"patient_id"	INTEGER NOT NULL,
	"medicine_id"	INTEGER NOT NULL,
	"medicine_quantity"	INTEGER NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "patient_details" (
	"id"	INTEGER NOT NULL,
	"name"	VARCHAR(45) NOT NULL,
	"age"	INTEGER NOT NULL,
	"ssn_id"	VARCHAR(45) NOT NULL UNIQUE,
	"admission_date"	DATE NOT NULL,
	"bed_type"	VARCHAR(45) NOT NULL,
	"address"	VARCHAR(45) NOT NULL,
	"city"	VARCHAR(45) NOT NULL,
	"state"	VARCHAR(45) NOT NULL,
	"status"	VARCHAR(45) NOT NULL,
	PRIMARY KEY("id")
);
CREATE TABLE IF NOT EXISTS "user_store" (
	"id"	INTEGER NOT NULL,
	"login"	VARCHAR(45) NOT NULL,
	"password"	VARCHAR(45) NOT NULL,
	"date_created"	DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
	PRIMARY KEY("id")
);
INSERT INTO "patient_test" ("id","patient_id","test_id") VALUES (1,111111111,8);
INSERT INTO "patient_test" ("id","patient_id","test_id") VALUES (2,111111111,8);
INSERT INTO "patient_test" ("id","patient_id","test_id") VALUES (3,111111111,11);
INSERT INTO "patient_test" ("id","patient_id","test_id") VALUES (4,111111111,12);
INSERT INTO "diagnosis" ("id","test_name","test_amount") VALUES (1,'uric acid',100);
INSERT INTO "diagnosis" ("id","test_name","test_amount") VALUES (2,'blood test',200);
INSERT INTO "diagnosis" ("id","test_name","test_amount") VALUES (3,'CT SCAN',2000);
INSERT INTO "diagnosis" ("id","test_name","test_amount") VALUES (4,'MRI',3000);
INSERT INTO "diagnosis" ("id","test_name","test_amount") VALUES (5,'X-ray',400);
INSERT INTO "diagnosis" ("id","test_name","test_amount") VALUES (6,'Creatinine Test',500);
INSERT INTO "diagnosis" ("id","test_name","test_amount") VALUES (7,'Covid-19 test',2500);
INSERT INTO "diagnosis" ("id","test_name","test_amount") VALUES (8,'Full body test',10000);
INSERT INTO "diagnosis" ("id","test_name","test_amount") VALUES (9,'Ultrasound',350);
INSERT INTO "diagnosis" ("id","test_name","test_amount") VALUES (10,'ECG',300);
INSERT INTO "diagnosis" ("id","test_name","test_amount") VALUES (11,'EEG',450);
INSERT INTO "diagnosis" ("id","test_name","test_amount") VALUES (12,'Vitamin D test',100);
INSERT INTO "diagnosis" ("id","test_name","test_amount") VALUES (13,'CBP',700);
INSERT INTO "diagnosis" ("id","test_name","test_amount") VALUES (14,'Urine test',50);
INSERT INTO "diagnosis" ("id","test_name","test_amount") VALUES (15,'Eye test',150);
INSERT INTO "medicine" ("id","medicine_name","medicine_amount","medicine_quantity") VALUES (1,'paracetamol',20,70);
INSERT INTO "medicine" ("id","medicine_name","medicine_amount","medicine_quantity") VALUES (2,'cresar ',85,100);
INSERT INTO "medicine" ("id","medicine_name","medicine_amount","medicine_quantity") VALUES (3,'cinarest',10,84);
INSERT INTO "medicine" ("id","medicine_name","medicine_amount","medicine_quantity") VALUES (4,'Aminophylline',150,100);
INSERT INTO "medicine" ("id","medicine_name","medicine_amount","medicine_quantity") VALUES (5,'Vit E',82,100);
INSERT INTO "medicine" ("id","medicine_name","medicine_amount","medicine_quantity") VALUES (6,'Tolnaftate',320,100);
INSERT INTO "medicine" ("id","medicine_name","medicine_amount","medicine_quantity") VALUES (7,'Analgin ',50,100);
INSERT INTO "medicine" ("id","medicine_name","medicine_amount","medicine_quantity") VALUES (8,'Amodiaquine',78,100);
INSERT INTO "medicine" ("id","medicine_name","medicine_amount","medicine_quantity") VALUES (9,'Aspirin ',100,100);
INSERT INTO "medicine" ("id","medicine_name","medicine_amount","medicine_quantity") VALUES (10,'Bacampicillin ',42,100);
INSERT INTO "medicine" ("id","medicine_name","medicine_amount","medicine_quantity") VALUES (11,'Riboflavin',55,100);
INSERT INTO "medicine" ("id","medicine_name","medicine_amount","medicine_quantity") VALUES (12,'Verapamil',50,100);
INSERT INTO "medicine" ("id","medicine_name","medicine_amount","medicine_quantity") VALUES (13,'Theophylline ',10,100);
INSERT INTO "medicine" ("id","medicine_name","medicine_amount","medicine_quantity") VALUES (14,'Captopril ',300,100);
INSERT INTO "medicine" ("id","medicine_name","medicine_amount","medicine_quantity") VALUES (15,'Cefadroxil ',75,100);
INSERT INTO "patient__medicine" ("id","patient_id","medicine_id","medicine_quantity") VALUES (1,111111111,1,39);
INSERT INTO "patient__medicine" ("id","patient_id","medicine_id","medicine_quantity") VALUES (2,111111111,3,20);
INSERT INTO "patient__medicine" ("id","patient_id","medicine_id","medicine_quantity") VALUES (3,111111112,1,10);
INSERT INTO "patient__medicine" ("id","patient_id","medicine_id","medicine_quantity") VALUES (4,111111112,2,1);
INSERT INTO "patient__medicine" ("id","patient_id","medicine_id","medicine_quantity") VALUES (5,111111113,1,21);
INSERT INTO "patient__medicine" ("id","patient_id","medicine_id","medicine_quantity") VALUES (6,111111113,3,20);
INSERT INTO "patient__medicine" ("id","patient_id","medicine_id","medicine_quantity") VALUES (7,111111111,6,2);
INSERT INTO "patient__medicine" ("id","patient_id","medicine_id","medicine_quantity") VALUES (8,111111111,11,9);
INSERT INTO "patient__medicine" ("id","patient_id","medicine_id","medicine_quantity") VALUES (9,111111111,14,12);
INSERT INTO "patient_details" ("id","name","age","ssn_id","admission_date","bed_type","address","city","state","status") VALUES (111111111,'John Wick',38,'999888777','2020-06-24','General ward','Beach House',' Benipur ','Bihar','Admitted');
INSERT INTO "patient_details" ("id","name","age","ssn_id","admission_date","bed_type","address","city","state","status") VALUES (111111112,'Patient Zero',35,'123123123','2020-06-29','General ward','New House',' Karaikal ','Pondicherry','Admitted');
INSERT INTO "patient_details" ("id","name","age","ssn_id","admission_date","bed_type","address","city","state","status") VALUES (111111113,'Vignesh',22,'222222222','2020-06-17','single room','2855 Island Avenue',' Sanvordem ','Goa','Admitted');
INSERT INTO "patient_details" ("id","name","age","ssn_id","admission_date","bed_type","address","city","state","status") VALUES (111111114,'Ra',21,'999888727','2020-06-29','General ward','2855 Island Avenue',' Calicut ','Kerala','Discharged');
INSERT INTO "patient_details" ("id","name","age","ssn_id","admission_date","bed_type","address","city","state","status") VALUES (111111115,'sda',42,'111111111','2020-06-30','General ward','fsda',' Bangarpet ','Karnataka','Admitted');
INSERT INTO "patient_details" ("id","name","age","ssn_id","admission_date","bed_type","address","city","state","status") VALUES (111111116,'vinay chauhan',21,'234234234','2020-07-01','Semi sharing','carrebean road',' Jairampur ','Arunachal Pradesh','Admitted');
INSERT INTO "patient_details" ("id","name","age","ssn_id","admission_date","bed_type","address","city","state","status") VALUES (111111117,'Lucifer',25,'123456789','2020-07-03','General ward','2855 Island Avenue',' Daman ','Daman & Diu','Admitted');
INSERT INTO "user_store" ("id","login","password","date_created") VALUES (2,'12345678@A','12345678@A','2020-06-29 16:07:25');
INSERT INTO "user_store" ("id","login","password","date_created") VALUES (3,'12345677@A','12345677@A','2020-07-02 14:18:32');
INSERT INTO "user_store" ("id","login","password","date_created") VALUES (4,'12345678@D','12345678@D','2020-07-02 14:19:06');
INSERT INTO "user_store" ("id","login","password","date_created") VALUES (5,'12345678@P','12345678@P','2020-07-02 14:19:38');
INSERT INTO "user_store" ("id","login","password","date_created") VALUES (6,'12345677@D','12345677@D','2020-07-02 14:20:02');
INSERT INTO "user_store" ("id","login","password","date_created") VALUES (7,'12345677@P','12345677@P','2020-07-02 14:20:57');
COMMIT;
