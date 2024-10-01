#write a python prog whicch demonstrates obtaining the connection from oracle database
import oracledb as orc
try:
    conn=orc.connect("system/rama@localhost/XE")
    print("python prog obtains connection from oracledb")
    print("type of conn=",type(conn))
except orc.DatabaseError as db:
    print("invalid username/password;login denied")
