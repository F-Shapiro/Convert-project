import configparser
import os
import sys
import imp
#module_file, pathname, description = imp.find_module("mariadb", [os.getcwd() + "/dependencies"])
#module_mariadb = imp.load_module("mariadb", module_file, pathname, description)
#sys.path.insert(0, os.getcwd() + "/dependencies")
#mariadb_module = imp.load_source("mariadb", os.getcwd() + "\dependencies\mariadb-connector-c-3.1.9-centos7-amd64\lib\mariadb\libmariadb")
import mariadb

try:
    db_connect = mariadb.connect(
        user="leon",
        password="dont_lock_my_pass",
        host="localhost",
        port=3306,
        database="products"
    )
except mariadb.Error as err:
    print(f"Error connecting to MariaDB Platform: {err}")
    sys.exit(1)

cur = db_connect.cursor()