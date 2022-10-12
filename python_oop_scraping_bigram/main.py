import re
import urllib.request

from bs4 import BeautifulSoup

from markov import MarkovChain


def parse_chapter(path):
    # Open the chapter
    url = f'http://composingprograms.com/{path}'
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError:
        print('ERROR: Chapter could not be opened', url)
        return ([], [])

    html = response.read()
    soup = BeautifulSoup(html, 'html.parser')

    # Find the right-side text content
    contents = soup.find('div', class_='inner-content')

    # Find and process the paragraphs
    paragraphs = contents.find_all('p')
    paragraphs = [paragraph.get_text().replace("\n", " ") for paragraph in paragraphs]

    # Find and process the headings
    # i.e. "<h2>2.2 Data Abstraction</h2>" -> "Data Abstraction"
    headings = contents.find_all(re.compile("^(h[1-6])$"))
    headings = [heading.get_text() for heading in headings]
    headings = [re.search(r"[\d\.]+[\s:]+(.+)$", heading).group(1) for heading in headings]
    return (paragraphs, headings)

# Open the front page with the chapter links
response = urllib.request.urlopen('http://composingprograms.com/')
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

contents = soup.find('div', class_='inner-content')
# Find and process the chapter links
# i.e. "<a href="./pages/11-getting-started.html">1.1 Getting Started</a>"
#       --------> "pages/11-getting-started.html"
links = contents.find_all('a')
urls = [link['href'][2:] for link in links if link['href'].startswith('./pages')]

all_paragraphs = []
all_headings = []
for url in urls:
    (paragraphs, headings) = parse_chapter(url)
    all_paragraphs.extend(paragraphs)
    all_headings.extend(headings)

markov_chain = MarkovChain()
for paragraph in all_paragraphs:
    markov_chain.add_phrase(paragraph)

#for x in range(0, 10):
#    print(markov_chain.generate_phrase())