import MySQLdb
db = MySQLdb.connect("192.168.0.101","root","","cloud_robotics")
cursor = db.cursor()
sql = "INSERT INTO LOGIN(CUsername,CPass) VALUES ('lsn','lsn')"

cursor.execute(sql);
