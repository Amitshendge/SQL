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
        
        self.cursor.execute(query['query']['show all'])
        data = self.cursor.fetchall()
        for i in data:
            print(i)

    def query(self):
        sum="select department,sum(salary) over(partition by department) as'sal_sum' from employee;"
        rank="select department,salary,rank() over(partition by `department` order by salary desc) as'rank' from employee;"
        denserank="select department,salary,dense_rank() over(partition by `department` order by salary desc) as'denserank' from employee;"
        rownumber="select department,salary,row_number() over(partition by `department` order by salary desc) as 'row number'from employee;"
        ntile="select department,salary,ntile(4) over(order by salary desc) as 'row number'from employee;"
        lag="select department,salary,lag(salary) over(order by salary desc) as 'previous'from employee;"
        lead="select department,salary,lead(salary) over(order by salary desc) as 'next'from employee;"
        firstvalue="select department,salary,first_value(salary) over(order by salary desc) as 'first'from employee;"
        self.cursor.execute(firstvalue)
        data = self.cursor.fetchall()
        for i in data:
            print(i)

if __name__ == "__main__":
    with open('config.json') as json_file:
        data = json.load(json_file)
    a = Database(data['HOST_NAME'],data['USER'],data['PASSWORD'])
    # a.show()
    a.query()

