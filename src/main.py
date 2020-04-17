from requests_html import HTMLSession

def get_html_obj(url):
    try:
        session = HTMLSession()
        response = session.get(url)
    except ConnectionError as ex:
        print(ex)
        exit()
    except Exception as ex:
        print(ex)
        exit()

    print(response)
    return response.html

"""
MAIN PROGRAM
"""
url = 'https://time.com/section/tech/'
html = get_html_obj(url)
articles = html.find('.article-info a')
article_links = []

for article in articles:
    link = url[:-1] + article.attrs['href']
    article_links.append(link)

print(article_links)
