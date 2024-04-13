'''
This file contains the core logic for fetching and processing 
data from OpenAlex
'''

import requests

def fetch_abstracts(keyword):
    url = "https://api.openalex.org/works"
    params = {'filter': f'abstract.search:{keyword}', 'per-page': 200}  # Adjust based on API limits
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    return data



def rank_publications_by_citation(data):
    publications = data.get('results', [])
    sorted_publications = sorted(publications, key=lambda x: x.get('cited_by_count', 0), reverse=True)
    return sorted_publications
