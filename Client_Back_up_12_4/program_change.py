import MySQLdb

db = MySQLdb.connect("192.168.0.103","root","lsn@1994","cloud_robotics")

cursor = db.cursor()

sql = """SELECT * FROM robot_program where robot_id = 1"""

try:
    cursor.execute(sql)
    data = cursor.fetchone()
    print data[2]
    db.commit()
    if data[2] == 'circle_detection':
        print "running circle detection program"
    else:
        print "running contour detection program"
    

except:
    db.rollback()

db.close()
