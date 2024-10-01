#prog for updating sal and comp name of employee based on empname
import oracledb as orc
def updaterecord():
    while(True):
        try:
            con=orc.connect("system/rama@localhost/XE")
            cur=con.cursor()
            #accept emp details
            empno=int(input("Enter employee number for updating sal and compname:"))
            empsal=float(input("enter employee new salary:"))
            cname=input("enter employee new company name:")
            #queries with dynamic values
            uq="update employee set sal=%f,compname='%s' where eno=%d"
            cur.execute(uq%(empsal,cname,empno))
            con.commit()
            if(cur.rowcount>0):
                print("{} employee record update".format(cur.rowcount))
            else:
                print("employee record does not exit")
            print("-"*50)
            ch=input("do u want to update another record(yes/no):")
            if(ch.lower()=="no"):
                print("Thx for using program")
                break
        except orc.DatabaseError as db:
            print("problem in oracle db: ",db)
        except ValueError:
            print("don't enter alnum,str and symbols for emp number and salary")
updaterecord()
