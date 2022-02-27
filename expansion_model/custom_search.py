# An implementation of google search engine in python.
# Author: anendahpromise@gmail.com

# Requirements:
# requests
# json

import requests
import json
import sys

def getGoogleResults(query, pageOffset=1, timeout=10):
    ''' Given a query searches a Google Programmable search engine for results.
    Query Parameters:
        query:          This is the query to search.
        pageOffset:     Use this to get other page results, for example 1 means result page 1, while 10 is result page 10. Max of 50
    '''
    MAX_PAGE = 50
    MIN_PAGE = 1
    if pageOffset < MIN_PAGE: pageOffset = MIN_PAGE
    elif pageOffset > MAX_PAGE: pageOffset = MAX_PAGE

    NUM_RESULT_PER_PAGE = 10
    FIRST_PAGE_OFFSET = 1
    start = NUM_RESULT_PER_PAGE * (pageOffset - 1) + FIRST_PAGE_OFFSET
    url = "https://customsearch.googleapis.com/customsearch/v1?key=AIzaSyD20ocjCnZQELvTmOSA2ogLvJyXf9tu63s&cx=047d9bfb192dc6725&q={}&start={}&alt=json".format(query, start)
    
    result = {'maxPage': MAX_PAGE, 'searchQuery': query, 'items': None}
    response = requests.get(url, timeout)    
    if response.status_code == 200:
        search = json.loads(response.content)
        result['query'] = search['queries']['request'][0]['searchTerms']
        result['totalResults'] = search['searchInformation']['totalResults']
        if 'spelling' in search: 
            result['searchQuery'] = search['spelling']['correctedQuery']
            result['spellingCorrection'] = result['searchQuery']
        
        if 'items' in search:
            items = search['items']
            result['items'] = [{'title': x['title'], 'link': x['link']} for x in items]
        return result
    else: raise Exception('Request failed, Invalid server response.')

if __name__ == '__main__':
    result = {'response_status': False, 'message': None}
    
    if len(sys.argv) > 1:
        query = sys.argv[1]
        result = getGoogleResults(query)
        # use the corrected spelling to get new results
        if "spellingCorrection" in result:
            result = getGoogleResults(result['searchQuery'])
        result['response_status'] = result
        print(result)
    else: print('Invalid query argument')
