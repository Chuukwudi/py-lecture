import requests
import json
# TODO: replace with your own app_id and app_key
app_id = 'f106cf6a'
app_key = '037706d64818d4eba56840f988aee965'

language = 'en-gb'
word_id = 'Ace'
fields = 'pronunciations'
strictMatch = 'false'

url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/' + \
      language + '/' + word_id.lower() + '?fields=' + fields + \
      '&strictMatch=' + strictMatch;

my_headers = {'app_id': app_id, 'app_key': app_key}
r = requests.get(url, headers=my_headers)

print("code {}\n".format(r.status_code))
print("text \n" + r.text)
print("json \n" + json.dumps(r.json()))

# Note you must update the app_id and app_key values to those provided by your account
