import json
import os 
from pprint import pprint
import requests
import pandas as pd

'''
This sample makes a call to the Bing Web Search API with a query and returns relevant web search.
Documentation: https://docs.microsoft.com/en-us/bing/search-apis/bing-web-search/overview
'''

class BingWebSearchAPI():
    
    def get_search_results(self, user_query, api_key, api_endpoint="https://api.bing.microsoft.com/"):

        def make_api_request(query):
            mkt = 'en-IN'
            params = { 'q': query, 'mkt': mkt }
            subscription_key = api_key
            if api_endpoint == "https://api.bing.microsoft.com/":
                endpoint = api_endpoint + "v7.0/search"
            else:
                endpoint = api_endpoint
            headers = {'Ocp-Apim-Subscription-Key': subscription_key}

            try:
                response = requests.get(endpoint, headers=headers, params=params)
                response.raise_for_status()

                return response.json()
            except Exception as exp:
                raise exp
        
        response = make_api_request(user_query)
        if response:
            return [{'URL' : page['url'], 'Title' :  page['name'], 'Content Snippet' : page['snippet']} for page in response['webPages']['value']]

def convert_to_selectable_df(data: list):
    data = pd.DataFrame(data)
    data.insert(0, "Select", False)
    return data

def get_selected_rows(data: pd.DataFrame):
    return data[data['Select'] == True]


if __name__ == "__main__":
    search_query = input("Enter your search query: ")
    pprint(BingWebSearchAPI().get_search_results(user_query=search_query))