# -*- coding: utf-8 -*-

import re
import pprint
import settings
import datetime
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

try:
    api = Connection(appid=settings.APP_ID, config_file=None)
    response = api.execute('findItemsAdvanced', {'keywords': 'legos'})

    assert(response.reply.ack == 'Success')
    assert(type(response.reply.timestamp) == datetime.datetime)
    assert(type(response.reply.searchResult.item) == list)

    item = response.reply.searchResult.item[0]
    assert(type(item.listingInfo.endTime) == datetime.datetime)
    assert(type(response.dict()) == dict)

except ConnectionError as e:
    print(e)
    print(e.response.dict())

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(response.dict())

