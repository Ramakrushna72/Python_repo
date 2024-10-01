#prog for inserting record in employee table
import oracledb as orc
class invalidnameError(Exception):pass
def validate(name):
    words=name.split()
    res=False
    for word in words:
        if(not word.isalpha()):
            res=True
            break
    if(res):
        raise invalidnameError
    else:
        return(name)
def recordinsert():
    while(True):
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
            print("-"*50)
            print("{} employee record inserted successfully--verify".format(cur.rowcount))
            print("-"*50)
            ch=input("do u want to insert another record(yes/no):")
            if(ch.lower()=="no"):
                print("thx for using this prog")
                break
        except orc.DatabaseError as db:
            print("problem in oracle db:",db)
        except ValueError:
            print("don't enter alnums,strs and symbols for empno and salary")
        except invalidnameError:
            print("Don't enter invalid names for emp name and comp name")
#main prog
recordinsert() #function call