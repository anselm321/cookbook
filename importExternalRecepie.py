import urllib.request, urllib.error, urllib.parse

url = 'http://dinarecept.se/recipe/#recipe/459599750'


""" # create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of None.
top_level_url = "http://dinarecept.se/"


handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

# use the opener to fetch a URL
opener.open(url)

# Install the opener.
# Now all calls to urllib.request.urlopen use our opener.
urllib.request.install_opener(opener) """





response = urllib.request.urlopen(url)
webContent = response.read()

f = open('importDR1.html', 'wb')
f.write(webContent)
f.close
