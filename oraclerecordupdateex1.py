#prog for updating sal and comp name of employee baseed on emp table
import oracledb as orc
def updaterecord():
    try:
        con=orc.connect("system/rama@localhost/XE")
        cur=con.cursor()
        uq="update employee set sal=sal+sal*50/100,compname='wipro' where eno=20"
        cur.execute(uq)
        con.commit()
        if(cur.rowcount>0):
            print("{} employee record update".format(cur.rowcount))
        else:
            print("employee record does not exit")
    except orc.DatabaseError as db:
        print("problem in oracledb: ,db")
#main prog
updaterecord()