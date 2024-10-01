#prog for delecting the record from employee table
import oracledb as orc
def delectrecord():
    while(True):
        try:
            con=orc.connect("system/rama@localhost/XE")
            cur=con.cursor()
            #accept employee number from kbd
            empno=int(input("enter employee number:"))
            cur.execute("delete from employee where eno=%d"%empno)
            con.commit()
            if(cur.rowcount>0):
                print("{} employee record deleted".format(cur.rowcount))
            else:
                print("employee record does not exit")
            print("-"*50)
            ch=input("do u want to delete another record(yes/no):")
            if(ch.lower()=="no"):
                print("thx for using the program")
        except orc.DatabaseError as db:
            print("problem in oracle db:",db)
        except ValueError:
            print("Don't enter alnums,strs and symbols for employee number")
delectrecord()