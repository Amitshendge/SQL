from Input import function_intInput as intInput
from Input import function_strInput as strInput
import json
import mysql.connector as connector

with open('query.json') as json_file:
    query = json.load(json_file)

class Database:
    def __init__(self,host_name,user_name,password) -> None:
        self.connection = connector.connect(host=host_name,
                                            user=user_name,
                                            passwd=password,
                                            database='emp_wage')
        self.cursor = self.connection.cursor()
    def show(self):
        
        self.cursor.execute(query['query']['max'])
        data = self.cursor.fetchall()
        for i in data:
            print(i)

    def query(self):
        self.cursor.execute("select distinct `First Name` from employee;")
        self.connection.commit()
        data = self.cursor.fetchall()
        for i in data:
            print(i)

    def procedure_creat(self,command):
        self.cursor.execute(query['procedure']['create'] + query['query'][command])

    def procedure2_creat(self,command):
        self.cursor.execute("create procedure pro(IN id int) " + command)

    def procedure_call(self,input=None):
        if input == None:
            self.cursor.execute(query['procedure']['call'])
            data = self.cursor.fetchall()
            for i in data:
                print(i)
        else:
            self.cursor.execute(f"call pro({str(input)});")
            data = self.cursor.fetchall()
            for i in data:
                print(i)


if __name__ == "__main__":
    with open('config.json') as json_file:
        data = json.load(json_file)
    a = Database(data['HOST_NAME'],data['USER'],data['PASSWORD'])
    # a.procedure_creat('avg')
    # a.procedure2_creat("select `First name` from employee where `emp id` = id;")
    a.procedure_call(1)
    # print()
    # a.query()

