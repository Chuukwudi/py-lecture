import requests
import matplotlib

# Retrieve BrewDog recipes from the Punk API

random_beer = None
random_beer_request = requests.get("https://api.punkapi.com/v2/beers/random")

# Print the status code
print("Status code: ", random_beer_request.status_code)

if random_beer_request.status_code == requests.codes.ok:
        #print(random_beer_request.json())

        random_beer = random_beer_request.json()[0]
        print(random_beer["id"])
        print(random_beer["name"])
        print(random_beer["tagline"])

# Ger beer by passing an id - 192 - Punk IPA
punk_ipa = None
punk_ipa_request = requests.get("https://api.punkapi.com/v2/beers/192")

# Print the status code
print("Status code: ", punk_ipa_request.status_code)

if punk_ipa_request.status_code == requests.codes.ok:
    #print(random_beer_request.json())

    punk_ipa = punk_ipa_request.json()[0]
    print(punk_ipa["id"])
    print(punk_ipa["name"])
    print(punk_ipa["tagline"])

# Get beers by passing some parameters.
# "https://api.punkapi.com/v2/beers?key1=value1&key2=value2

# params = {"key1":"value1", "key2":"value2"}
beers = None
payload = {"abv_gt": 5, "brewed_after": "12-2015"}
beers_request = requests.get("https://api.punkapi.com/v2/beers", params=payload)

# Print the status code
print("Status code: ", beers_request.status_code)

if beers_request.status_code == requests.codes.ok:
    print("-----------------------------------------------------------")
    print(beers_request.json())
    beers = beers_request.json()
    for beer in beers:
        print(beer["id"], beer["name"], beer["first_brewed"])
