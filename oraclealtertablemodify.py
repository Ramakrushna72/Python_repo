import oracledb as orc
def altertable():
    try:
        con=orc.connect("system/rama@localhost/XE")
        cur=con.cursor()
        aq="alter table temp modify(tno number(3),name varchar2(15))"
        cur.execute(aq)
        print("table altered---verify")
    except orc.DatabaseError as db:
        print("problem in oracle db:",db)
#main prog
altertable()