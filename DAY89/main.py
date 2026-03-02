from bs4 import BeautifulSoup
import requests



# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": 'foo',
#     "body": 'bar',
#     "userId": 1,
#   }

# headers =  {
#     'Content-type': 'application/json; charset=UTF-8',
#   }

# response = requests.post(url, headers=headers, json=data)

# print(response.text)

                  #### BS4 module ####

url = "https://www.waqarzaka.net/#services"

r = requests.get(url)
# print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
# for h in soup.find_all("meta"):
#     print(h.text)