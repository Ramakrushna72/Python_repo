#prog for inserting record in employee table
import oracledb as orc
def recordinsert():
    try:
        con=orc.connect("system/rama@localhost/XE")
        cur=con.cursor()
        iq="insert into employee values(22,'rama',4.7,'siba transport')"
        cur.execute(iq)
        con.commit()
        print("employee record inserted successfully---verify")
    except orc.DatabaseError as db:
        print("problem in oracledb:",db)
#main prog
recordinsert()
