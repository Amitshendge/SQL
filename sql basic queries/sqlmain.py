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
            with open('query.json') as json_file:
                query = json.load(json_file)
            self.cursor.execute(query['max'])
            data = self.cursor.fetchall()
            for i in data:
                print(i)
        except Exception as e:
            logger.error(e)

    def query(self):
        try:
            self.cursor.execute("select distinct `First Name` from employee;")
            # self.connection.commit()
            data = self.cursor.fetchall()
            for i in data:
                print(i)
        except Exception as e:
            logger.error(e)


if __name__ == "__main__":
    with open('config.json') as json_file:
        data = json.load(json_file)
    a = Database(data['HOST_NAME'],data['USER'],data['PASSWORD'])
    # a.show()
    # print()
    a.query()

