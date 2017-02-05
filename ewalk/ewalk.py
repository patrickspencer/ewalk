# -*- coding: utf-8 -*-

import requests
import settings
import pprint

url = 'http://svcs.ebay.com/services/search/FindingService/v1'
url += "?OPERATION-NAME=findItemsByKeywords"
url += "&SERVICE-VERSION=1.0.0"
url += "&SECURITY-APPNAME="
url += settings.APP_ID
url += "&GLOBAL-ID=EBAY-US"
url += "&RESPONSE-DATA-FORMAT=JSON"
url += "&callback=_cb_findItemsByKeywords"
url += "&REST-PAYLOAD"
url += "&keywords=harry%20potter"
url += "&paginationInput.entriesPerPage=3"
r = requests.post(url)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(r.text)
