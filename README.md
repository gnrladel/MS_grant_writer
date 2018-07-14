This Script to multiple option, by generating different statment commands , to make it easy to copy past the command and use the on mysql console:

1-Generate the Statement to provide privileges to a specific database for a specific user here is an example :

grants.py -g -H host1,host2,host3 -u user1 -d database_name -p password
--------------------------------------------------------------------------------------------------------------------------------------------------
GRANT ALL PRIVILEGES ON database_name.* to user1@'host1' IDENTIFIED BY 'password' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON database_name.* to user1@'host2' IDENTIFIED BY 'password' WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON database_name.* to user1@'host3' IDENTIFIED BY 'password' WITH GRANT OPTION;
FLUSH PRIVILEGES;
--------------------------------------------------------------------------------------------------------------------------------------------------

2-Generate the statment to check the collation of database,  table or even a stored procedure:

grants.py -c -d database
--------------------------------------------------------------------------------------------------------------------------------------------------
SELECT SCHEMA_NAME 'database', default_character_set_name 'charset', DEFAULT_COLLATION_NAME 'collation' FROM information_schema.SCHEMATA;
--------------------------------------------------------------------------------------------------------------------------------------------------

grants.py -c -t -d database
--------------------------------------------------------------------------------------------------------------------------------------------------
select TABLE_SCHEMA,table_name,TABLE_COLLATION FROM INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA='database';
--------------------------------------------------------------------------------------------------------------------------------------------------

grants.py -c -s -d database
--------------------------------------------------------------------------------------------------------------------------------------------------
SELECT ROUTINE_SCHEMA,SPECIFIC_NAME,CHARACTER_SET_CLIENT,COLLATION_CONNECTION,database_collation FROM INFORMATION_SCHEMA.ROUTINES WHERE ROUTINE_SCHEMA='database';
--------------------------------------------------------------------------------------------------------------------------------------------------

3-Generate the statment to check the engine type of tables for a specific database:

grants.py -e -d database
--------------------------------------------------------------------------------------------------------------------------------------------------
SELECT TABLE_NAME,ENGINE FROM information_schema.TABLES WHERE  TABLE_SCHEMA ='database';
--------------------------------------------------------------------------------------------------------------------------------------------------
