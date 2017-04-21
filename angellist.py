import requests
import json
import urllib.parse

url = 'https://angel.co/company_filters/search_data'
headers = {'X-CSRF-Token': '2F3FB5ers08QkMtYXkrYpUqYnHJU+Z9MHfVFFOGuadY=', 'cookie': '_angellist=eca52b21687fd60390592a1a72f2fff4'}

# just get first three pages
for i in range(1, 4):
    body = {'filter_data[company_types][]': 'Startup', 'filter_data[stage][]': 'Seed', 'filter_data[stage][]': 'Series A', 'filter_data[stage][]': 'Series B', 'filter_data[stage][]': 'Series C', 'sort': 'Total Raised', 'page': i}

    # r1 is the response of the first request
    r1 = requests.post(url, headers=headers, data=body)
    obj = json.loads(r1.text)
    print(obj)

    '''
    from the first request,
    we will get 20 company ids and other parameters.
    the response is a json
    '''

    # Generate url
    gen_url = ''

    # Add parameters
    for key in obj:
        if key != 'ids':
            gen_url += '&' + key + '=' + str(obj[key])

    # Add ids
    gen_url_ids = ''
    for _id in obj['ids']:
        gen_url_ids = gen_url_ids + '&ids%5B%5D=' + str(_id)

    gen_url += gen_url_ids

    # Append hostname
    gen_url = 'https://angel.co/companies/startups?' + gen_url[1:]

    print(gen_url)

    r2 = requests.get(gen_url)
    print(r2.content)
    '''
    r2 is the respone of the second request,
    it is a json, inside the json is a html.
    we need to parse the html
    '''






