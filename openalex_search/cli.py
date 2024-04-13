'''
This file handles the command-line interface part
'''

import argparse
from openalex_search.core import fetch_abstracts, rank_publications_by_citation

def main():
    parser = argparse.ArgumentParser(description="Search and rank publications from OpenAlex by keyword.")
    parser.add_argument("keywords", nargs="+", help="Keywords to search for in publication abstracts.")
    args = parser.parse_args()

    for keyword in args.keywords:
        print(f"Searching for keyword: {keyword}")
        data = fetch_abstracts(keyword)
        ranked_publications = rank_publications_by_citation(data)
        for pub in ranked_publications:
            print(pub['title'], pub['cited_by_count'])

if __name__ == "__main__":
    main()
