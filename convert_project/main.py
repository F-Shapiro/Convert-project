import configparser
import os
import sys
import imp
module_file, pathname, description = imp.find_module("mariadb", [os.getcwd() + "\dependencies"])
module_mariadb = imp.load_module("_mariadb.cp36-win_amd64", module_file, pathname, description)
#sys.path.insert(0, os.getcwd() + "\dependencies")

try:
    db_connect = module_mariadb.connect(
        user="leon",
        password="dont_lock_my_pass",
        host="localhost",
        port=3306,
        database="products"
    )
except module_mariadb.Error as err:
    print(f"Error connecting to MariaDB Platform: {err}")
    sys.exit(1)

cur = db_connect.cursor()