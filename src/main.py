from requests_html import HTMLSession

try:
    url = 'https://time.com'
    session = HTMLSession()
    response = session.get(url)
except ConnectionError as ex:
    print(ex)
    exit()
except Exception as ex:
    print(ex)
    exit()

print(response)

html = response.html
briefs = html.find('.column-tout')

for brief in briefs:
    print(brief.links)