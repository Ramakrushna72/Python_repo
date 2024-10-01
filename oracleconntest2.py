import oracledb as orc
try:
    conn=orc.connect("system/rama@127.0.0.1/XE")
except orc.DatabaseError as db:
    print("invali username/password;login denied")
else:
    print("python prog obtains connection from oracle db")
    print("type of conn=",type(conn))