import re

def validateURL(url):
    regex = "((http|https)://)(www.)?[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)"
    r = re.compile(regex)

    if(re.search(r, url)):
        print("Valid")
    else:
        print("Not Valid")

url1 = "https://www.linkedin.com/"
validateURL(url1)

url2 = "http://apple"
validateURL(url2)

url3 = "iywegfuykegf"
validateURL(url3)

url4 = "https://w"
validateURL(url4)