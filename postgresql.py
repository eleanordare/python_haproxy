#!/usr/bin/env python
__author__ = 'Eleanor Mehlenbacher'

from jenkins import jenkinsMethods, jenkinsMain
import psycopg2

# import jenkins instances from psql database
# periodically run jenkinsMethods main call on each instance
# save time of last ping?

class postgreSQL():

    # connect to local database of jenkins instances
    # create array of urls (vals)
    def connect(self):
        try:
            con = psycopg2.connect("dbname='jenkins' user='root'")
            cur = con.cursor()
            cur.execute('SELECT * FROM instances')
            vals = []
            val = cur.fetchone()
            while (val):
                vals.append(val)
                val = cur.fetchone()
            return vals

        except:
            print "I am unable to connect to the database."

    # cycle through instances in vals, check data etc.
    def main(self, jenkinsMethods, jenkinsMain):
        vals = postgreSQL.connect()
        for v in vals:
            jenkinsMain.main(jenkinsMethods, v[0])



if __name__ == '__main__':
    postgreSQL = postgreSQL()
    jenkinsMethods = jenkinsMethods()
    jenkinsMain = jenkinsMain()

    postgreSQL.main(jenkinsMethods, jenkinsMain)
