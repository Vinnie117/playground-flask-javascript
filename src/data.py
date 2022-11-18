# import pandas as pd
# from html.parser import HTMLParser
# #import urllib2
# import requests

# session = requests.Session()
# session.trust_env = False

# http://192.168.1.67:5000
# http://127.0.0.1:5000


#data = pd.read_html('https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list')

# proxy_handler = urllib2.ProxyHandler({})
# opener = urllib2.build_opener(proxy_handler)
# urllib2.install_opener(opener)


#############################################################################
# data = pd.read_html('http://127.0.0.1:5000')

#############################################################################

# from html.parser import HTMLParser

# class TableParser(HTMLParser):
#     def handle_starttag(self, tag, attrs):
#         for attr, val in attrs:
#             if attr == "class" and tag == "td":
#                 print(f"Found table: {val!r}")

# with open("gallery.html", mode="r", encoding="utf-8") as html_file:
#     html_content = html_file.read()

# parser = TableParser()
# parser.feed(html_content)

#############################################################################





