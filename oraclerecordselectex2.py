import oracledb as orc
def selectrecord():
    try:
        con=orc.connect("system/rama@localhost/XE")
        cur=con.cursor()
        #queries for reading the records
        sq="select * from employee"
        cur.execute(sq)
        #get the record using fetchmany()
        print("-"*50)
        records=cur.fetchmany()
        for record in records:
            for val in record:
                print(" {} ".format(val),end="\t")
            print()
        print("-"*50)
    except orc.DatabaseError as db:
        print("problem in oracle db:",db)
#main prog
selectrecord()