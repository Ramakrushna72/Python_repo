#prog for demonstrating cursor object
import oracledb as orc
con=orc.connect("system/rama@localhost/XE")
print("python prog obtains connection from oracle db")
print("type of con=",type(con))
cur=con.cursor()
print("python prog created cursor object")
print("type of cur=",type(cur))
