create database emp_wage;
use emp_wage;
create table employee(
`emp id` int,
`First Name` varchar(20),
`Last Name` varchar(20),
`Salary` int,
`Department` varchar(20),
`Contact Number` int,
primary key (`emp id`)
)
select * from employee; #show table
insert into employee values
(001,'Amit','Shendge',10000,'Fresher',9892126741),
(002,'Mahesh','Sargar',11000,'Expirenced',1234567890),
(003,'Rajat','Nikam',12000,'Expert',9876543210);
insert into employee values
(004,'Amit','Patil',10000,'Fresher',6541239875);
truncate table employee;
alter table employee modify column `Contact Number` bigint;
select `emp id`,`First name` from employee;						#Select specific column
select distinct `First Name` from employee;						#Get unique values from column
select `First Name` from employee where `salary`=10000;			#Get column with condition
select * from employee where `salary`=10000;					#Get all column with condition
select * from employee where `salary`=10000 AND `First Name`='Amit';#Get all column with and conditions
select * from employee where `salary`=10000 or `First Name`='Mahesh';#Get all column with or conditions
select * from employee order by `salary` asc;					#Sort ascending order
select * from employee order by `salary` desc;					#Sort decending order
INSERT INTO employee (`emp id`,`salary`) values (5,456);		#insert specific values only
select * from employee where `First Name` is null;				#null value data
select * from employee where `First Name` is not null;			#not null value data
update employee set `First name`='Ajit' where `emp id`=4;		#update value
SET SQL_SAFE_UPDATES = 0;										#set SQL safe mode updates OFF
delete from employee where `First name`='Ajit';					#DELETE data
delete from employee where `salary` > 10000 ;					#DELETE data on GREATER THAN CONDITION
SELECT * FROM employee order by `salary` asc limit 2;			#select limited data
select min(`salary`) from employee;								#minimum value
select max(`salary`) from employee;								#maximum value
select count(`salary`) from employee;							#minimum value
select avg(`salary`) from employee;								#maximum value
select sum(`salary`) from employee;								#maximum value
select * from employee where `First Name` Like 'a%';			#Like to get pattern
select * from employee where `First Name` in ('Rajat','Mahesh');#select multiple data with in keyword
select `emp id` as 'id',`first name` as 'Fname' from employee;	#setting alias name to selected column
create table emp_personal_data(`emp id` int,`Name` varchar(50),`Address` varchar(50),`Age` int);
insert into emp_personal_data values 
(1,'Amit Shendge','New Panvel',23),
(2,'Mahesh Sargar','Kamothe',22),
(3,'Rajat Nikam','Khanda Colony',21);
insert into emp_personal_data values 
(5,'Ajit Patil','New Panvel',23);
delete from emp_personal_data where `emp id` = 3;
select * from emp_personal_data;
select * from employee join emp_personal_data on employee.`emp id` = emp_personal_data.`emp id`;	#Join
select * from employee inner join emp_personal_data on employee.`emp id` = emp_personal_data.`emp id`;	#Inner Join
select * from employee left join emp_personal_data on employee.`emp id` = emp_personal_data.`emp id`;	#Left Join
select * from employee right join emp_personal_data on employee.`emp id` = emp_personal_data.`emp id`;	#Right Join
select * from employee , emp_personal_data order by employee.`emp id`;					#Self Join
select `emp id` from employee union select `emp id` from emp_personal_data;				#Union
select count(age),age from emp_personal_data group by age;								#Group by
select * from employee having `emp id` > 1;												#Having
select * into new_table from employee;
create table new_table(
`emp id` int,
`First Name` varchar(20),
`Last Name` varchar(20),
`Salary` int,
`Department` varchar(20),
`Contact Number` bigint);
insert into emp_personal_data(`name`) select `First name` from `employee`;				#insert into and select
SELECT `First name`, salary,															#case
CASE
    WHEN salary > 11000 THEN 'The salary is greater than 11000'
    WHEN salary = 11000 THEN 'The salary is 11000'
    ELSE 'The salary is under 11000'
END AS Salary_Range
FROM employee;
select ifnull(age,0) from emp_personal_data;											#if null replace data
create procedure asas()																	#Create proceduer
select * from employee;
call asas();																			#Call Procedure
alter view new_view as select `First name`,`Last name` from employee;					#create view
select * from new_view
