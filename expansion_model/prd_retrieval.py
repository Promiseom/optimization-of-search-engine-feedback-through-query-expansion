# author: Promise Anendah
# Pseudo-Relevant Document Retrieval from Wikipedia given a query

from bs4 import BeautifulSoup
import requests
import json
import time

def clear_html_tags(html):
    return BeautifulSoup(html,'html.parser').text.strip()

def validate_title(title):
    ''' Returns true if the title contains \'(disambiguation)\' else returns false '''
    return 'disambiguation' not in title



def get_relevant_snippets(document_count, query):
    '''  Returns a maximum of 20 search results with title and snippets relating search query. '''

    if document_count > 20: document_count = 20     # 20 is the maximum document count
    requestSearch = "https://en.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch=" + query + "&exintro=&prop=extracts&format=json&gsrlimit=" + str(document_count)
    relevant_documents = {}

    try:
        print("connecting to 'Wikipedia.org'...")
        result = requests.get(requestSearch)

        if result.status_code == 200:
            print('Processing response...')
            result_content = json.loads(result.content)

            relevant_documents['title'] = []
            relevant_documents['content'] = []

            # get the search content
            wiki_pages = result_content['query']['pages']

            for page in wiki_pages:
                result_page = wiki_pages[page]
                title = result_page['title']
                snippet = 'No Info'

                if 'extract' in result_page:
                    snippet = clear_html_tags(result_page['extract'])

                relevant_documents['title'].append(title)
                relevant_documents['content'].append(snippet)
            print('Done retrieving documents!')
        else:
            print('Bad response! please try again.')
    except ConnectionError as error:
        print('Communication error!, check your internet connection and try again')
    return relevant_documents

def get_relevant_titles(num, query):
    '''  Returns relevant wikipedia article titles related search query, the maximum  number of titles return is based on the maximum number of hits. '''

    # obtain relevant titles
    title_request = 'https://en.wikipedia.org/w/api.php?action=query&list=search&prop=info&inprop=url&utf8=&format=json&srlimit={}&srsearch={}'.format(str(num), query)
    titles = {'titlesinfo': [], 'totalhits': 0}

    try:
        print('Connecting to \'Wikipedia.org\'...')
        result = requests.get(title_request)
        if result.status_code == 200:
            print('Processing results...')
            result_content = json.loads(result.content)

            titles['totalhits'] = result_content['query']['searchinfo']['totalhits']

            # get the search content
            sresults = result_content['query']['search']

            for sresult in sresults:
                if not validate_title(sresult['title']): continue
                titleinfo = {'title': sresult['title'], 'wordcount': sresult['wordcount']}
                titles['titlesinfo'].append(titleinfo)

            print('Done retrieving documents!')
        else:
            print('Bad response! please try again.')
    except ConnectionError as e:
        print('Communication error!, Failed to get relevant titles! Please check your internet connection and try again')
    return titles

def get_documents_by_title(titles):
    relevant_docs = []
    for title in titles['titlesinfo']:
        docs_request = 'https://en.wikipedia.org/w/api.php?action=query&titles=' + title['title'] + '&prop=extracts&format=json'
        try:
            print('Connecting to \'Wikipedia.org\'...')
            result = requests.get(docs_request)
            if result.status_code == 200:
                pages = json.loads(result.content)['query']['pages']
                for pageid in pages:
                    relevant_docs.append(clear_html_tags(pages[pageid]['extract']))
                print('Done retrieving document!')
            else:
                print('Bad response! please try again.')
        except ConnectionError as e:
            print(
                'Communication error!, Failed to get relevant documents! Please check your internet connection and try again')

    return relevant_docs

def get_documents(limit, query):
    titles = get_relevant_titles(limit, query)
    return get_documents_by_title(titles)

if __name__ == '__main__':
    document_count = 3
    # while(True):
    #     try:
    #         document_count = int(input('Enter the number of documents to get: '))
    #         break
    #     except ValueError as error:
    #         print('Invalid number!')

    query = input('Input Query: ')

    start_time = time.time()
    titles = get_relevant_titles(document_count, query)
    documents = get_documents_by_title(titles)

    retrieval_time = time.time() - start_time
    print('Retrieved {} documents in {} seconds'.format(document_count, retrieval_time))

    print('Printing relevant results:')
    for i in range(len(titles['titlesinfo'])):
        print('Title {}: {}'.format(i, titles['titlesinfo'][i]['title']))
        print(documents[i])
        print('--------------------------------------')

#requestArticle = "https://en.wikipedia.org/w/api.php?action=query&generator=search&gsrsearch=" + query + "&exintro=&prop=extracts|pageimages&format=json"
#requestResults = "https://en.wikipedia.org/w/api.php?action=query&list=search&prop=info&inprop=url&utf8=&format=json&srlimit=20&srsearch=" + query

#result = open('wiki_mission.json', 'r', encoding='utf8')
