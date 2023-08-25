from pprint import pprint
import requests
r= requests.get('')
pprint(r.json)