import web


db = web.database(dbn='postgres', db='sms', user='postgres', pw='')
def get_messages():
   	return db.select('message')

def new_mesagge(listdata):
   	db.insert('message', sid=listdata[0], date_created=listdata[1], account_sid=listdata[2], to_=listdata[3], from_=listdata[4], body=listdata[5], status=listdata[6])

def get_message(id):
	return db.select('message', where="sid='"+id+"'")