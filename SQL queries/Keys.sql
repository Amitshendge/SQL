create database Students;
use Students;
create table registration
(`reg_number` int primary key,
`name` varchar(50),
`previous marks` int
);
create table class
(`roll_number` int primary key auto_increment,
`reg_number` int ,
`name` varchar(50),
`Branch name` varchar(20),
foreign key(reg_number)references registration(`reg_number`)
);
insert into registration values (111,'Amit Shendge',55),(112,'Mahesh Sargar',56),(113,'Rajat Nikam',57);
select * from registration;
insert into class(`reg_number`,`name`,`Branch name`) values (111,'Amit Shendge','Mech'),(112,'Mahesh Sargar','IT'),(113,'Rajat Nikam','COMPS');
select * from class;
select * from class inner join registration on class.`reg_number` = registration.`reg_number`
