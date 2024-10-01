#prog for removing the table from oracle database
import oracledb as orc
def removetable():
    try:
        con=orc.connect("system/rama@localhost/XE")
        cur=con.cursor()
        aq="drop table temp"
        cur.execute(aq)
        print("table dropped sucessfully---verify")
    except orc.DatabaseError as db:
        print("problem in oracle db:",db)
#main prog
removetable()