#prog for record in employee table
import oracledb as orc
def recordinsert():
    try:
        con=orc.connect("system/rama@localhost/XE")
        cur=con.cursor()
        #accept the emplyoee values from keybord
        eno=int(input("enter employee no:"))
        empname=input("enter employee name:")
        sal=float(input("enter employee salary:"))
        cname=input("enter employee comp name:")
        #design the query
        iq="insert into employee values(%d,'%s',%f,'%s')"
        cur.execute(iq%(eno,empname,sal,cname))
        con.commit()
        print("employee record inserted successfull----verify")
    except orc.DatabaseError as db:
        print("problem in oracle db:",db)
#main prog
recordinsert()