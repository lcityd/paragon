#!/usr/bin/python
# ==============================================================================
# Copyright 2018 The Paragon Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


def wifi():
    '''
    Pings google.com to check if you're connected to the internet
    '''
    REMOTE_SERVER = "www.google.com"
    def is_connected():
        try:
            host = socket.gethostbyname(REMOTE_SERVER)
            s = socket.create_connection((host, 80), 2)
            return True
        except:
            pass
        return False

#get the top google result when saying "google for this"
def gsearch(name):
    #google search once i get the bridge online
    return 'none'
    import requests

    page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
    page
   
#search arxiv for papers
def search(name):

    import urllib
    import feedparser

    # Base api query url
    base_url = 'http://export.arxiv.org/api/query?';

    # Search parameters
    search_query = name # search for electron in all fields
    start = 0                     # retreive the first 5 results
    max_results = 1

    query = 'search_query=%s&start=%i&max_results=%i' % (search_query,
                                                         start,
                                                         max_results)

    # Opensearch metadata such as totalResults, startIndex,
    # and itemsPerPage live in the opensearch namespase.
    # Some entry metadata lives in the arXiv namespace.
    # This is a hack to expose both of these namespaces in
    # feedparser v4.1
    feedparser._FeedParserMixin.namespaces['http://a9.com/-/spec/opensearch/1.1/'] = 'opensearch'
    feedparser._FeedParserMixin.namespaces['http://arxiv.org/schemas/atom'] = 'arxiv'

    # perform a GET request using the base_url and query
    response = urllib.request.urlopen(base_url+query).read()

    # parse the response using feedparser
    feed = feedparser.parse(response)
   
   
    # Run through each entry, and print out information
    for entry in feed.entries:
        print(entry.summary)

#Define math functions for higher operations
class mathfuncs_calc():
    #extensive upper math, one time functions. Bulk calculations need to be hand programmed.
    def diff(func,d):
        sympy.diff(func,d)

    def inte(func,d):
        sympy.integrate(func, d)

    def lim(func,d):
        sympy.limit(func,x,0)

class mathfuncs_lina():
    #variables
    x = 0
    def Mach_FFT(x):
        #Compute a fast fourier transform on a seperate computer to ease loads
        x1 = arange(x)
        return fft(x1)

    def Matr_Det(x):
        #Computes the determinate of matrice X
        answer = sp.det(x)
        return answer

name = "na"
def price(name):
    url =  name # https://www.google.com/finance
    req = urllib.request.Request(url)
    url_full = url + "?" + urllib.parse.urlencode({"q": name})
    req = urllib.request.Request(url_full)
    resp = urllib.request.urlopen(req)
    data = resp.read()
    bs = bs4.BeautifulSoup(data)
    div_price = bs.find(attrs={"id": "price-panel"})
    span_price = div_price.find(attrs={"class": "pr"})
    return float(span_price.text.strip())

def stock_price(message):
    #Checks the stock price on Google stocks, since Google is more accurate.abs
    message = message.replace("stock price", "")

    #Search the stock database for the given company name
    df[df['Name'].str.contains(message)]

    #Further break down the stock table, and find the first hit.
    TableDi = x.iloc[-1]['Symbol']

    #Now it's easy sailing. x2
    TableConv = stocks.Share(TableDi)
    xrand = ['The price value of' + message + 'is: ' + TableConv.get_price()]

    
#note this is a diagnostics class, so.
class HardWare_Test():
    import psutil as util
    #Define the class globals here
    def Hardware_CPU():
        print('CPU percent: ' + str(util.cpu_percent(interval=1, percpu=True)))
        print('Total count of CPUs: ' + str(util.cpu_count(logical=True)))
        print('Total count of CPUs [Excluding Logical Cores]: '+ str(util.cpu_count(logical=False)))
        print('Frequency of each CPU core:' + str(psutil.cpu_freq(percpu=True)))
    def Hardware_VolMem():
        #Tests the RAM, or volatile memory.
        mem = util.virtual_memory()
        print('Entire Memory:\n ' + 'percent; ' + mem[2] + '\n')
        print('Swap Memory: \n' + str(util.swap_memory()))
    def Hardware_Drive():
        return 'Not yet implemented.'

def plug(message):
    #Call the plugin based on number
    from subprocess import call
    if "first" in message:
        #call the first plugin
        call("gcc -Wall net_01.cpp", shell=True) and call("a.out") #compile, then run the g++ file.
    if "second" in message:
        #call the second program
        call("gcc -Wall net_02.cpp -lcrypto -lssl ", shell=True) and call("a.out") #compile then run the file.
    if "third" in message:
        #third
        call("gcc -Wall net_03.cpp", shell=True) and call("a.out") #compile then run the file.
    if "fourth" in message:
        #fourth
        call("gcc -Wall net_04.cpp", shell=True) and call("a.out") #compile then run the file.

