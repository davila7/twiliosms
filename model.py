#import web to database connect
import web
#connect to database
db = web.database(host="ec2-50-17-181-147.compute-1.amazonaws.com", port="5432", dbn='postgres', db='dbgordq57q3395', user='tjasuavxsogmlk', pw='nJel9utoiLJtLqtKto5pZvjymB')

#function to select all message
def get_messages():
   	return db.select('message')

#function to insert new message
def new_mesagge(listdata):
   	db.insert('message', sid=listdata[0], date_created=listdata[1], account_sid=listdata[2], to_=listdata[3], from_=listdata[4], body=listdata[5], status=listdata[6])

#function to get a message by sid
#parameters id type varchar
def get_message(id):
	return db.select('message', where="sid='"+id+"'")