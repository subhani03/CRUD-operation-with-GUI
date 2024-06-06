create database studentregistration;
use studentregistration;
create table studentregistrationtable(name varchar(250),dob int not null,gender varchar(50),email varchar(50),contact int(15),course varchar(100),qualification varchar(100),address varchar(250));
select * from studentregistrationtable;

set SQL_SAFE_UPDATES=0;