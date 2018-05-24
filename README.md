this script write mysql  grant command here is an example :

grants.py -H host1,host2,host3 -u user1 -d database_name -p password
GRANT ALL PRIVILEGES ON database_name.* to user1@'host1' IDENTIFIED BY 'password' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON database_name.* to user1@'host2' IDENTIFIED BY 'password' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON database_name.* to user1@'host3' IDENTIFIED BY 'password' WITH GRANT OPTION;
FLUSH PRIVILEGES;

