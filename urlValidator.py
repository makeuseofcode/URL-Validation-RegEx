import re

def validateURL(url):
    regex = "^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$"
    r = re.compile(regex)

    if(re.search(r, url)):
        print("Valid")
    else:
        print("Not Valid")

url1 = "https://www.something.com/"
validateURL(url1)

url2 = "http://www.something.com/"
validateURL(url2)

url3 = "https://www.something.edu.co.in"
validateURL(url3)

url4 = "https://www.url-with-querystring.com/?url=has-querystring"
validateURL(url4)

url5 = "http://url-without-www-subdomain.com/"
validateURL(url5)

url6 = "https://mail.google.com"
validateURL(url6)

url7 = "http://wrhgv675376.commmmsexxx/path"
validateURL(url7)