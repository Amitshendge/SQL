from Input import function_intInput as intInput
from Input import function_strInput as strInput
import json
import mysql.connector as connector
import LoggerHandler as logger

class Database:
    def __init__(self,host_name,user_name,password) -> None:
        try:
            self.connection = connector.connect(host=host_name,
                                                user=user_name,
                                                passwd=password,
                                                database='emp_wage')
            self.cursor = self.connection.cursor()
        except Exception as e:
            logger.error(e)

    def show(self):
        try:
            self.cursor.execute('select * from employee;')
            data = self.cursor.fetchall()
            for i in data:
                print(i)
        except Exception as e:
            logger.error(e)

    def data():
        empid = strInput('Enter Emp ID : ')
        Fname = strInput('Enter First Name : ')
        Lname = strInput('Enter Last Name : ')
        sal = intInput('Enter Salary : ')
        dep = strInput('Enter Department : ')
        contact = intInput('Enter contact number : ')
        return {
            'empid': empid,
            'Fname': Fname,
            'Lname': Lname,
            'sal': sal,
            'dep': dep,
            'contact': contact
        }

    def add(self):
        try:
            dict = Database.data()
            self.cursor.execute(
                f"insert into employee values ({dict['empid']},'{dict['Fname']}','{dict['Lname']}',{dict['sal']},'{dict['dep']}',{dict['contact']})"
            )
            self.connection.commit()
        except Exception as e:
            logger.error(e)

    def update(self):
        try:
            userInput = intInput(
                'Enter Employee ID to Edit specific Employee data : ')
            dict = Database.data()
            self.cursor.execute(
                f"UPDATE employee SET `emp id`={dict['empid']},`First name`='{dict['Fname']}',`Last name`='{dict['Lname']}',`salary`={dict['sal']},`department`='{dict['dep']}',`contact Number`={dict['contact']} WHERE `emp id`='{userInput}'"
            )
            self.connection.commit()
        except Exception as e:
            logger.error(e)

    def delete(self):
        try:
            userInput = intInput(
                'Enter Employee ID to delete specific Employee data : ')
            self.cursor.execute(
                f"DELETE FROM employee WHERE `emp id`='{userInput}'")
            self.connection.commit()
        except Exception as e:
            logger.error(e)

    def DummyData(self):
        try:
            self.cursor.execute(
                f"insert into employee values (001,'Amit','Shendge',10000,'Fresher',9892126741),(002,'Mahesh','Sargar',11000,'Expirenced',1234567890),(003,'Rajat','Nikam',12000,'Expert',9876543210);")
            self.connection.commit()
        except Exception as e:
            logger.error(e)

    def DeleteAllData(self):
        try:
            self.cursor.execute("truncate table employee;")
            self.connection.commit()
        except Exception as e:
            logger.error(e)


if __name__ == "__main__":
    with open('config.json') as json_file:
        data = json.load(json_file)
    a = Database(data['HOST_NAME'],data['USER'],data['PASSWORD'])
    a.show()
    print()
    a.DeleteAllData()
    a.show()
