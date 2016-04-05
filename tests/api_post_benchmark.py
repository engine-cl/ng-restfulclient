#!/usr/bin/env python
from restfulclient import client

__copyright__ = "Copyright (C) 2016 eNgine.cl"
__revision__ = "$Revision$"
__license__ = "BSD License"
__version__ = "$Version$"
__author__ = "Jorge A. Medina"
__date__ = "21/10/16"

MAX_CON = 2
API_URL = "url_endpoint"
payload = b"""{
    "device_type":"iPhone 5s",
    "download_time":"2015-07-09 14:10:00",
    "click_time":"2015-07-09 14:09:49",
    "agency":null, "ip":"99.127.160.101",
    "cost_per_install":null,
    "is_retargeting":false,
    "app_name":"your app",
    "re_targeting_conversion_type":null,
    "city":"London",
    "af_subl":null,
    "idfv":"F067712E-3170-4247-8A50-4901B1123456",
    "af_sub2":null,
    "event_value":{
        "af_revenue":11,
        "af_currency":null,
        "af_content_id":"1907401",
        "af_content_type":"daily"
    },
    "af_sub3":null,
    "af_sub4":null,
    "customer_user_id":"156802",
    "mac":null, "af_sub5":null,
    "campaign":"unspecified",
    "event_name":null,
    "currency":"",
    "installtime":"2015-07-09 14:10:32",
    "event_time":"2015-11-17 13:55:18",
    "platform":"ios",
    "sdk_version":"v2.5.3.16",
    "appsflyer_device_id":"1436433014000-6348412",
    "device_name":" Ann Marie",
    "wifi":true,
    "media_source":"Facebook Ads",
    "country_code":"GB",
    "http_referrer":"http://apps.com/",
    "idfa":"21951847-97CC-49DC-88E1-E0680E1D3456",
    "click_ur1":"http://your.url.com",
    "language":"en-gb",
    "app_id":"id499097243",
    "app_version":"248",
    "attribution_type":"regular",
    "af_siteid":null,
    "os_version":"9.1",
    "event_type":"in-app-event",
    "af_ad":"a86721874",
    "af_ad_id":"123245353",
    "af_ad_type":"Banner_210X600",
    "af_adset":"3gvow",
    "af_adset_id":"3gvow",
    "af_c_id":"3e025",
    "af_channel":"Facebook",
    "af_cost_currency":"GBP",
    "af_cost_model":"cpi",
    "af_cost_value":"0.0750",
    "afkeywords":"testing Sasha3 wrap24"
}"""

async def main():
    for x in range(0, MAX_CON):
        print(await client.post(url=API_URL, payload=payload))

client.event_loop(callback=main)
