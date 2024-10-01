#prog for demonstrating creating a table
import oracledb as orc
try:
    con=orc.connect("system/rama@localhost/XE")
    cur=con.cursor()
    tc="create table employee(eno number(2) primary key,name varchar2(15) not null,sal number(6,2) not null,compname varchar2(20) not null)"
    cur.execute(tc)
    print("Table created successfully in oracle db--verify")
except orc.DatabaseError as db:
    print("problem in oracle db:",db)