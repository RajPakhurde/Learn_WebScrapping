# Importing requests module
import requests
# Beautiful Soup is the perfect module to parse or transverse through HTML code. We can easily target any div, table, td, tr, class, id, etc. The basic template(boilerplate code) which is used everytime is:
from bs4 import BeautifulSoup


# Declaring url & Initializing url which is going to scrap
url = "https://www.codewithharry.com/videos/python-web-scraping-tutorial-in-hindi"


# r variable has all the html code
r = requests.get(url)
# r will return response so if we want the code we write 'r.content'
html_content = r.content
# Here we are just printing html code
# print(html_content)
# r.text is the response in Unicode and r.content is the response in bytes.
html_content2 = r.text
# print(html_content2)


# Once the HTML is fetched using requests the next step will be to parse the HTML content. For that we will use python’s BeautifulSoup module which will create a tree like structure for our DOM. This line is parsing the data:
soup = BeautifulSoup(html_content, 'html.parser')
# prettify() will print html code in proper format / tree structure
# print(soup.prettify())

# If we want to scrap title of the page
title = soup.title
# print(title)

# Yes! It scrapped all the codes on this page! 
# for i in soup.find_all("code"):
#     print(i.text)

# find():
# It is used to get first element in the HTML page. It could be any element. For eg:
# print(soup.find('p'))

# find_all():
# This line will get you all p tags of the page:
# print(soup.find_all('p'))

# for i in soup.find_all('p'):
#     print(i)

# print(soup.find('title').text)

# anchors = soup.find_all('a')
# for i in anchors:
#     print(i['href'])

# Taking HTML from a variable instead of requests:
# Bs4 just needs the HTML. It doesn't matter where it came from. We can also make a variable, write HTML in that and give it to bs4. It can be done like this:
html = '''
<body>
    <ul>
        <li class= raj>This is a class</li>
        <li><a>This</a>This</li>
        <li>This</li>
        <li>This</li>
        <li id="li">This</li>
        <li>    This    </li>
    </ul>
</body>
'''
soup1 = BeautifulSoup(html, 'html.parser') 
# print(soup1.find('li',class_='raj'))
# print(soup1.find('ul').contents)

# for i in soup1.find('ul').contents:
    # print(i)