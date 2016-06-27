# coding:utf8
import urllib
import urllib2
import base64
from config import top, skip, accountKey


try:
    import json
except ImportError:
    import simplejson as json


def BingSearch(query):
    payload = {}
    payload['$top'] = top
    payload['$skip'] = skip
    payload['$format'] = 'json'
    payload['Query'] = "'" + query + "'"
    url = 'https://api.datamarket.azure.com/Bing/Search/Web?' + urllib.urlencode(payload)
    sAuth = 'Basic ' + base64.b64encode(':' + accountKey)

    headers = {}
    headers['Authorization'] = sAuth
    try:
        req = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(req)
        the_page = response.read()
        data = json.loads(the_page)
        return data
    except Exception as e:
        print e


if __name__ == '__main__':
    data = BingSearch("ip:139.129.132.156")
    for each in data['d']['results']:
        print each['Title'], each['Url']
