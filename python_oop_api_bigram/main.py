import json
import urllib.request

from markov import MarkovChain

def get_results(page_num):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key=b31910cdb65604e096b78abcf6e76469&language=en-US&certification=PG&certification_country=US&page={page_num}'
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        print('ERROR: URL could not be opened', url)
        return []
    response_json = json.loads(response.read())
    results = response_json["results"]
    return [result["overview"] for result in results]

all_phrases = []
for page_num in range(1, 10):
    all_phrases.extend(get_results(page_num))

chain = MarkovChain()
for phrase in all_phrases:
    chain.add_phrase(phrase)