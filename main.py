import tweepy, settings, string, re, time, os, sys

flags = "".join(sys.argv[1:])
notifications = 'notify' in flags

def notify(title, message): # do [sudo] gem install terminal-notifier first
	if not notifications:
		return
	t = '-title {!r}'.format(title)
	m = '-message {!r}'.format(message)
	os.system('terminal-notifier {}'.format(' '.join([m, t])))

auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET)
auth.set_access_token(settings.ACCESS_TOKEN, settings.TOKEN_SECRET)

api = tweepy.API(auth)

def respond(tweet, text):
	if text == "":
		print "Something funky with this tweet:", tweet.text
		notify(title = 'Empty Tweet!', message = 'Not Sent...')
		return
	response = '@' + tweet.user.screen_name + ' ' + text
	try:
		api.update_status(response, tweet.id)
		# Calling the function
		notify(title = 'Tweet Sent!', message = response)
	except Exception,e:
		print "Something went wrong responding to tweet with:", response
		print str(e)
		notify(title = 'Error sending tweet!', message = response)

def replyTo(tweet):
	print "Replying to:", tweet.text, tweet.created_at

	filtered = re.sub(r'([^0-9\s\-])+', '', tweet.text)
	numbers = [ int(s) for s in filtered.split() if (s.isdigit() or s[0] == '-' and s[1:].isdigit()) ]

	sortedNumbers = sorted(numbers)

	text = ", ".join(str(x) for x in sortedNumbers)
	
	respond(tweet, text)

mostRecent = 555535840063930368

while True:
	if mostRecent == None:
		questions = api.search(q="sort these numbers")
	else:
		questions = api.search(q="sort these numbers", since_id=mostRecent)

	questions = [ t for t in questions if  "Can you sort these numbers" in t.text ]

	print "Processing", len(questions), "tweets..."

	if len(questions) > 0:

		mostRecent = questions[0].id

		print mostRecent

		for tweet in questions:
			if "Can you sort these numbers" in tweet.text:
				replyTo(tweet)

	time.sleep(5)






