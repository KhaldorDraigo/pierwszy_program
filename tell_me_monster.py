import mysql.connector

hostname = 'localhost'
username = 'root'
password = 'ZrobmyPieczen1337'
database = 'bestiary'
myConnection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )

search_message = """What do you want to search by:
type R to search monster with specific race 
type W to search only those weak to specific element
type H+ to search those with HP greater than next input
type H- to search those with HP lesser than next input
type A+ to search those with AD greater than next input
type A- to search those with AD lesser than next input
type what you want to choose: """

race_search_message = """what race do you want to list:
type O to search from Orcs
type F to search Fire spirits
type W to search Water spirits
type G to search Goblins"""

weakness_search_message = """by what weakness do you want to list:
type T to search those weak to thunder
type F to search those weak to fire
type W to search those weak to water"""

letter_to_race = {"O":"Orcs", "F":"Fire_spirits", "W":"Water_spirits", "G":"Goblins",}

letter_to_weakness = {"T":"thunder", "F":"fire", "w":"water"}

def load_monsters( conn, sql_text ):
	cur = conn.cursor()
	cur.execute(sql_text)

	return cur.fetchall()

while True:
	print("please tell me what monsters you want to list")
	print("you can search by race, weakness, HP and AD")
	while True:
		select_input = input(search_message)

		if select_input.upper() == "R":
			select_parameter = "race="
			break

		if select_input.upper() == "W":
			select_parameter = "weakness="
			break

		if select_input.upper() == "H+":
			select_parameter = "hp>="
			break

		if select_input.upper() == "H-":
			select_parameter = "hp<="
			break

		if select_input.upper() == "A+":
			select_parameter = "ad>="
			break

		if select_input.upper() == "A-":
			select_parameter = "ad<="
			break

		else:
			print("inproper input please use the ones listed")

	while True:
		if select_input == "R":
			print(race_search_message)
			race_selected = input("what race you want to choose: ")
			query_text = letter_to_race[race_selected.upper()]
			sql = """SELECT * FROM monsters WHERE %s"%s"; """ % ( select_parameter, query_text )
			break


		if select_input == "W":
			print(weakness_search_message)
			weakness = input("what weakness you want to choose: ")
			query_text = letter_to_weakness[weakness.upper()]
			sql = """SELECT * FROM monsters WHERE %s"%s";  """ % ( select_parameter, query_text )
			break

		else:
			try:
				value = input("enter value: ")
				query_value = int(value)
				sql = """SELECT * FROM monsters WHERE %s"%d";  """ % ( select_parameter, query_value )
				break

			except (valueError) :
				print("inproper value, please use numbers only!")

	table = load_monsters( myConnection, sql )
	for (name, race, hp, ad, weakness) in table:
		print("%s from %s having HP: %d and AD: %d and is weak to %s" % (name, race, hp, ad, weakness) )

	input("please press enter to continue")










