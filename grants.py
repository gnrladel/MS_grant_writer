#!/usr/bin/python3

import argparse
'''
this script create the grant statment for mysql databases to provide privileges
'''


parser = argparse.ArgumentParser(description='this script provide MySQL grant privilege statment')
parser.add_argument('-d', '--database', type=str, metavar='', required=True, help='Specify the database to provide access.' )
parser.add_argument('-u', '--user', type=str, metavar='', required=True, help='Specify the user to provide access.' )
parser.add_argument('-p', '--password', type=str, metavar='', required=True, help='Specify the password for access.' )
parser.add_argument('-H', '--hosts', type=str, metavar='', required=True, help='Specify the hosts to provide access to with comma separated values, ex: db1,db2,br1,br2' )
args=parser.parse_args()

if __name__ == '__main__':

	for host in args.hosts.split(','):
    		print("GRANT ALL PRIVILEGES ON {}.* to {}@'{}' IDENTIFIED BY '{}' WITH GRANT OPTION;".format(args.database, args.user, host, args.password))
	print('FLUSH PRIVILEGES;')
