from twilio.rest import TwilioRestClient
#send function
#parameters body message
def send(text):
	# Your Account Sid and Auth Token from twilio.com/user/account
	account_sid = "ACf8a5060ccb6c8fbc954f16c6068f0485"
	auth_token  = "b6963ab82fa977905c276f07e6668c41"
	client = TwilioRestClient(account_sid, auth_token)
	message = client.messages.create(body=text,
	    to="+56950012660",    # Replace with your phone number
	    from_="+19284408443") # Replace with your Twilio number
	#return data from message
	listdata = [message.sid, message.date_created, message.account_sid, message.to, message.from_, message.body, message.status];
	return listdata