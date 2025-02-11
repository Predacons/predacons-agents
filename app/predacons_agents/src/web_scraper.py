
import requests
from bs4 import BeautifulSoup
from googlesearch import search


class WebScraper:
    """
    A class to manage web scraping operations including fetching and parsing HTML content.
    """

    def __init__(self):
        pass

    def google_search_extract(self,query, num_results=5):
        results = []
        try:
            # Perform Google search
            search_results =  search(term = query, num_results=10, advanced = True)
            i =0
            for search_result in search_results:
                url = search_result.url
                title = search_result.title
                description = search_result.description
                results.append(title +"  "+ description)
                if i == num_results:
                    break
                try:
                    # Fetch the content of the URL
                    response = requests.get(url)
                    response.raise_for_status()

                    # Parse the content using BeautifulSoup
                    soup = BeautifulSoup(response.text, 'html.parser')

                    # Extract text from the website
                    text = ' '.join([p.get_text() for p in soup.find_all('p')])
                    # make sure text is not too big
                    text = text[:5000]
                    # Append the extracted text to results
                    results.append(text)
                    i = i+1
                    print(url)
                except requests.RequestException as e:
                    # print(f"Failed to fetch {url}: {e}")
                    pass
                except Exception as e:
                    # print(f"Failed to parse {url}: {e}")
                    pass
        except Exception as e:
            print(f"Failed to perform Google search: {e}")

        return results

    def get_web_data(self, query,num_results = 5):
        extracted_texts = self.google_search_extract(query, num_results)
        extracted_texts_string = "\n\n---\n\n".join(extracted_texts)
        return extracted_texts_string

    
