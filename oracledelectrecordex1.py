import oracledb as orc
def deleterecord():
    try:
        con=orc.connect("system/rama@localhost/XE")
        cur=con.cursor()
        dq="delete from employee where eno=7"
        cur.execute(dq)
        con.commit()
        if(cur.rowcount):
            print("{} employee record deleted".format(cur.rowcount))
        else:
            print("employee record doesn't exit")
    except orc.DatabaseError as db:
        print("problem in oracle db:",db)
deleterecord()