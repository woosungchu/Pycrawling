#http://creativeworks.tistory.com/entry/PYTHON-3-Tutorials-24-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%9F%AClike-Google-%EB%A7%8C%EB%93%A4%EA%B8%B0-1-How-to-build-a-web-crawler

# import requests
# from bs4 import BeautifulSoup
#
# def spider(max_pages):
#     page = 1
#     while page < max_pages:
#         url = 'https://odototo.com/'+ str(page)
#         source_code = requests.get(url)
#         plain_text = source_code.text
#         soup = BeautifulSoup(plain_text, 'lxml')
#         print(soup)
#
#         text = ''
#         for item in soup.find_all('div', class='odo-panel'):
#             text = text + str(item.find_all(text=True))
#             print(text)
#         # return text
#
#         # for link in soup.select('h3 > a'):
#         #     href = 'http://creativeworks.tistory.com/' + link.get('href')
#         #     title = link.string
#         #     print(href)
#         #     print(title)
#
#         page += 1
#
# spider(2)
