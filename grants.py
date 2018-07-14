#!/usr/bin/python3

import argparse
import sys
'''
this script create the grant statment for mysql databases to provide privileges
'''


parser = argparse.ArgumentParser(description='this script provide MySQL grant privilege statment')
parser.add_argument('-d', '--database', type=str, metavar='', required='required' in sys.argv  , help='Specify the database to provide access, the collation or the engine for different tables.' )
parser.add_argument('-t', '--table', action='store_true', required='--collation' in sys.argv , help='Specify the table to provide the collation or the engine .' )
parser.add_argument('-u', '--user', type=str, metavar='', required='--grants' in sys.argv , help='Specify the user to provide access.' )
parser.add_argument('-p', '--password', type=str, metavar='', required='--grants' in sys.argv , help='Specify the password for access.' )
parser.add_argument('-H', '--hosts', type=str, metavar='', required='--grants' in sys.argv , help='Specify the hosts to provide access to with comma separated values, ex: db1,db2,br1,br2' )
parser.add_argument('-s', '--stored_procedure', action='store_true', required='--collation' in sys.argv  , help='Specify the collation of stored procedure.' )
parser.add_argument('-g', '--grants', action='store_true', required=False, help='This Option is used to generate the grant statement, it requires -d , -u, -p, -H Arguments')

parser.add_argument('-c', '--collation', action='store_true', required=False, help='This Option is used to generate the statement to check collation schema of databases, tables or stored procedures, require -d to specify database' )
parser.add_argument('-e', '--engine', action='store_true', required=False, help='This Option is used to generate the statement to check tables engine for specific database.' )
args=parser.parse_args()

if __name__ == '__main__':
	if args.grants and args.database and args.user and args.hosts and args.password:
    		for host in args.hosts.split(','):
    			print("GRANT ALL PRIVILEGES ON {}.* to {}@'{}' IDENTIFIED BY '{}' WITH GRANT OPTION;".format(args.database, args.user, args.hosts, args.password))
		print("FLUSH PRIVILEGES;")
	elif args.grants and (args.database is None or args.user is None or args.hosts is None or args.password is None):
		print("-d , -u, -H, -p params are required to generate the proper grant statement.")
	elif args.collation and args.stored_procedure:
		print("SELECT ROUTINE_SCHEMA,SPECIFIC_NAME,CHARACTER_SET_CLIENT,COLLATION_CONNECTION,database_collation FROM INFORMATION_SCHEMA.ROUTINES WHERE ROUTINE_SCHEMA='{}';".format(args.database))
	elif args.collation and args.database and args.table:
		print("select TABLE_SCHEMA,table_name,TABLE_COLLATION FROM INFORMATION_SCHEMA.TABLES where TABLE_SCHEMA='{}';".format(args.database))
	elif args.collation and args.database and not args.table:
		print("SELECT SCHEMA_NAME 'database', default_character_set_name 'charset', DEFAULT_COLLATION_NAME 'collation' FROM information_schema.SCHEMATA;")
	elif args.engine and args.database:
		print("SELECT TABLE_NAME,ENGINE FROM information_schema.TABLES WHERE  TABLE_SCHEMA ='{}';".format(args.database))
	else:
		print('Missing Arguments, please use -g, -c or -e as main arguments to generate grant statement, collation check command or table  engine statement commands.')
