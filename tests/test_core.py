'''
unit tests for the package
'''

from openalex_search.core import fetch_abstracts, rank_publications_by_citation


def test_fetch_abstracts():
    results = fetch_abstracts("machine learning")
    assert isinstance(results, dict)  # ensure results is a list

def test_rank_publications_by_citation():
    publications = {'results':
                    [{'title': 'Test 1', 'cited_by_count': 10}, 
                     {'title': 'Test 2', 'cited_by_count': 20}]}
    ranked = rank_publications_by_citation(publications)
    assert ranked[0]['title'] == 'Test 2'
