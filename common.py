import urllib
import config
import json
import random
import base64

def bing_search(query, search_type, limit):
        #search_type: Web, Image, News, Video
        key= ':%s' % config.BING_API_KEY
        credentials = base64.b64encode(bytes(key,'ascii'))
        auth = ('Basic %s' % str(credentials,'ascii'))
        query = urllib.parse.quote(query)
        # create credential for authentication
        user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
        url = 'https://api.datamarket.azure.com/Data.ashx/Bing/Search/'+search_type+'?Query=%27'+query+'%27&$top=+'+str(limit)+'&$format=json'
<<<<<<< HEAD
        request = urllib.request(url)
        request.add_header('Authorization', auth)
        request.add_header('User-Agent', user_agent)
        request_opener = urllib2.build_opener()
        response = request.urlopen(request) 
=======
        request = urllib.request.Request(url)
        request.add_header('Authorization', auth)
        request.add_header('User-Agent', user_agent)
        request_opener = urllib.request.build_opener()
        response = request_opener.open(request) 
>>>>>>> 65e984208292876fb50ff9b0fcd373907a1b017e
        response_data = response.read()
        json_result = json.loads(str(response_data,'utf-8'))
        result_list = json_result['d']['results']
        if len(result_list)==0:
                result_list = list([{
                        'Url':'Наркоман штоле?',
                        'MediaUrl':'Наркоман штоле?'
                        }])
        return result_list
        
def dice(max):
        return random.randint(1, max)
        
