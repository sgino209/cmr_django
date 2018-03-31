import sys
import sqlite3
import csv

table_name = "catalog_person"
#table_name = "auth_user"

conn=sqlite3.connect("db.sqlite3")
c=conn.cursor()
conn.row_factory=sqlite3.Row
crsr=conn.execute("select * from %s" % table_name)
row=crsr.fetchone()
titles=row.keys()

data = c.execute("select * from %s" % table_name)
if sys.version_info < (3,):
    f = open(table_name + '.csv', 'wb')
else:
    f = open(table_name + '.csv', 'w', newline="")

writer = csv.writer(f,delimiter=',')
writer.writerow(titles)
writer.writerows(data)
f.close()
