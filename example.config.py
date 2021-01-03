import mysql.connector

token = 'AUTHTOKEN'

color = (COLOR)
red = (REDCOLOR)
green = (GREENCOLOR)
orange = (YELLOWCOLOR)
#  Color codes must be in hex, for example: 
#  red = (c93838)

support = "support server link"
ninvite = "needed permissions oauth invite link" ### ONLY FOR NEEDED PERMISSIONS ### To hyperlink this in main.py: [invite me!]({config.ninvite})
ainvite = "admin permissions oauth invite link" ### ONLY FOR ADMIN PERMISSIONS ### To hyperlink this in main.py: [invite me!]({config.ainvite})
zinvite = "zero permissions oauth invite link" ### ONLY FOR ZERO PERMISSIONS ### To hyperlink this in main.py: [invite me!]({config.zinvite})
review = "link to review page" ### To hyperlink this in main.py: [review me!]({config.review})
pp = "privacy policy link" ### To hyperlink this in main.py: [privacy policy]({config.pp})
status = "status page link" ### For your bot's statuspage
dev1 = "discord user profile link" ### user profile links look like this: https://discord.com/users/(the user's ID)
dev2 = "discord user profile link" ### user profile links look like this: https://discord.com/users/(the user's ID)

### API's 
pixabaykey = 'pixabay api key'

e621key = 'apikey' # Your e621 api key (you need an account)
e621username = 'username' # Your e621 username (you need an account)
e621agent = 'examplegithubaccount/repo' # User agent, some way e621 can reach you, for example discord username#0000

nsfwexceptions = [channelid, channelid, channelid] # Add channel IDs here the bot will still send NSFW in, regardless of the NSFW setting

DBdata = mysql.connector.connect(
  host="localhost",
  user="username",
  password="password",
  database="database name"
)

DELTOKEN = 'TOKEN FOR DEL'
