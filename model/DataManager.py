import sqlite3
import pandas as pd

def getDataToDisplay():
	db_file = 'chinook.db'
	
	cnx = sqlite3.connect(db_file)

	df = pd.read_sql_query("SELECT * FROM employees", cnx)
	
	cnx.close()
	
	return df
	
def getUpdatedData():
	return True 