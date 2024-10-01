#prog for demonstrating creating a table
import oracledb as orc
def tablecreate():
    try:
        con=orc.connect("system/rama@localhost/XE")
        cur=con.cursor()
        tc=input("enter ddl query for creating a table in oracle:")
        cur.execute(tc)
        print("table created sucessfully in oracle db---verify")
    except orc.DatabaseError as db:
        print("problem in oracle db:",db)
tablecreate()