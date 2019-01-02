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

#=====================================================================================================

__main__ = '''
******************************************************************************************************************************
        The athena framework made in python, C++, and C.

        External Libraries are not mine, cubecorps, or owned representivavely of any individual
        associated with CubeCorps or the athena project currently. All respected rights are of the
        copyright owner.

                                        Simulated Artificially Intelligent Companion

                                            -= Author: Klam =-
                                          -= Project Name: The Paragon Project =-

        About:

        Simulates intelligence using external libraries and inside code to parse data,
        graph and predict the modeled equation. On top of the neural networks here, we also have an interface.

******************************************************************************************************************************
'''

#=====================================================================================================

__about__ = '''
******************************************************************************************************************************
Simulates intelligence using external libraries and inside code to parse data,
graph and predict the modeled equation. Uses modern approaches and algorithms to attempt to
simulate intelligence, though partial, through data and mathematical applications.
******************************************************************************************************************************
'''
__version__ = '1.3.4'
print('Using native enviroment')

#========================
#   System wide Imports
#========================

from mpi4py import MPI
import numpy
import sys, os, urllib

#========================
#EXCEPTIONS
#========================
def NoWifi(Exception):
    return "Connect to the internet to aquire full use of Athena"
    pass

comm = MPI.COMM_WORLD
rank = comm.Get_rank()  #Applies computer ranking for the backend servers
null_error = '//NULL//ERROR' #we need a null for everything
ERR_W = "Error, No access to the web!"
ERR_G = "General Error!"
enable_s = False #hardcode a switch for this


        
class spn():

    '''
    This contains all the classes and functions that is utilized by the master node; also used as the "core" of the software.
    '''
    def chrome(x):
        message = x
        message = message.replace("chrome-func", "")
        if ('wolfram') in message:
         #Que wolfram alpha with questions.
            message = message.replace("wolfram", "")
            import wolframalpha
            client = wolframalpha.Client("929P8L-QQPL5L6XT2") #Need to get a wolfram api
            res = client.query(message)
            for pod in res.pods:
                for sub in pod.subpods:
                    if enable_s == True:
                        Speech.say(rand,n,mixer)
                    else:
                        print(sub.text)

        if ('google') in message:
            message = message.replace("google","")
            message = message.replace(" ", "+")
            from bs4 import BeautifulSoup
            import requests
            page = requests.get("https://www.google.com/search?q=" + message)
            page
            soup = BeautifulSoup(page.content, 'html.parser') 
            resp = soup.find_all('div')[27].get_text()
            resp = resp.replace("\n","")
            rand = ["There are" + str(soup.find_all('div')[22].get_text()) + " " + resp]
            if enable_s == True:
                Speech.say(rand,n,mixer)
            else:
                ref_rand = ''.join(str(e) for e in rand)
                print(ref_rand)

        if ('wikipedia') in message:
            print(message)
            import requests
            message = message.replace("wikipedia", "")
            message = message.replace(" ", "_")
            message = message.capitalize()
            proxies = {
            }
            headers = {
                "User-Agent": "Definitions/1.0"
            }
            params = {
                'action':'query',
                'prop':'extracts',
                'format':'json',
                'exintro':1,
                'explaintext':1,
                'generator':'search',
                'gsrsearch':message,
                'gsrlimit':1,
                'continue':''
            }
            r = requests.get('http://en.wikipedia.org/w/api.php',
                            params=params,
                            headers=headers,
                            proxies=proxies)
            json1 = r.json()
            result = list(json1["query"]["pages"].items())[0][1]["extract"]
            rand = [(result) + '.']
            rand = ''.join(str(e) for e in rand)
            #Chrome = ("google-chrome %s")
            #webbrowser.get(Chrome)
            #webbrowser.open('https://en.wikipedia.org/wiki/' + message, new=2, autoraise=True)
            print(rand) #Speech.say(rand,n,mixer)


        if ('.com') in message :
            rand = ['Opening' + message]
            Chrome = ("google-chrome %s")
            webbrowser.get(Chrome).open('http://www.'+message)
            if enable_s == True:
                Speech.say(rand,n,mixer)
            else:
                ref_rand = ''.join(str(e) for e in rand)
                print(ref_rand)

        if ('youtube') in message:
            rand = ['Searching for ' + message + 'on youtube.']
            import urllib.request, urllib.parse, re
            #Search youtube and request the link from it.
            query_string = urllib.parse.urlencode({"search_query" : input()})
            html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
            search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            #Open the link in chrome
            Chrome = ("google-chrome %s")
            webbrowser.get(Chrome).open("http://www.youtube.com/watch?v=" + search_results[0])

        if ('.net') in message :
            rand = ['Opening' + message]
            Chrome = ("google-chrome %s")         
            webbrowser.get(Chrome).open('http://www.'+message)
            if enable_s == True:
                Speech.say(rand,n,mixer)
            else:
                ref_rand = ''.join(str(e) for e in rand)
                print(ref_rand)

        if ('.org') in message:
            rand = ['Opening' + message]
            Chrome = ("google-chrome %s")
            Speech.say(rand,n,mixer)
            webbrowser.get(Chrome).open('http://www.'+ message)
            if enable_s == True:
                Speech.say(rand,n,mixer)
            else:
                ref_rand = ''.join(str(e) for e in rand)
                print(ref_rand)

        if ('paper') in message:
            name = message.replace("search for papers on", "")
            embed_prot.search(name)

    def main():
        #Start by loading all libraries and files
        sys.path.append('./include/')
        print("******************************************\n" + 
        "   Importing all modules from system\n" +
        "******************************************")

        try:
            import requests, pywapi, feedparser, json, os, subprocess, signal, time, datetime, random, Speech, funcs
            import pyaudio, json, nltk, scipy, math, textblob, webbrowser, keras
            import speech_recognition as sr
            from pygame import mixer
            import yahoo_finance as fc
            from time import strftime
            import tensorflow as tf
            import numpy as np
            from multiprocessing import Process
            from keras.applications.resnet50 import ResNet50
            from keras.preprocessing import image
            from keras.applications.resnet50 import preprocess_input, decode_predictions
            import googlemaps as gmaps

            
        except ImportError:
            print("It appears as if you do not have all the packages!")
            #raise SystemExit

        print(requests, pywapi, feedparser, feedparser, json, os, subprocess, signal, time, datetime, random, Speech)
        #The users personal data, which will be edited when running the inst.py
        datafile = json.loads(open('./Data/Databases/Data/data.json').read())
        ct = time.strftime("%I:%M, %p")
        n = 0

        #outprint the version
        print("[System] Running Version: " + __version__)

        #Start other processes within the script.

        #subprocess.call("ipython3 ./include/Pitch.py &", shell=True)
        #If you're moving from older versions up, this code was removed duCurtainse to future improvements
        #made on the system. Just keep that in mind, they are now in /lib/VISION, and yes I know that
        #the caps make people want to jump off their building, but live with it. My software My rules.

        #Start with a little terminal spam
        print(__about__)
        print(__main__)
 
        rand = ["Hello" + (datafile["Identity"][0]["nameFirst"]) + ", welcome back. The current time is" + repr(ct)] #go ahead and welcome whatever you set this to.
        print(rand)

        class start():

            '''
            The main class, other classes might be related to this or not, really
            classes are just used in this program as a case around any other systems or infrastructures.
            '''

            def Interface():
                def runtime(message):
                    try:

                        #Que wikipedia using a bot and some clever json manipulations, gets the entire article
                        #TODO: Find ways to speak only certain portions of the article, or summarize it, find that in nltk.
                        if ("chrome-func") in message:
                            x = message
                            x.replace("chrome-func", "")
                            spn.chrome(x)
                        
                        #Just some nice etiquit
                        if ('goodbye') in message:

                            rand = ['Goodbye ' + (datafile["Identity"][0]["pronouns"]), 'athena powering off']
                            Speech.say(rand,n,mixer)

                        if ('evening') in message:

                            rand = ['Good evening ' + (datafile["Identity"][0]["pronouns"])]
                            if enable_s == True:
                                Speech.say(rand,n,mixer)
                            else:
                                ref_rand = ''.join(str(e) for e in rand)
                                print(ref_rand)
                        if ('morning') in message:

                            mTime = time.strftime('%B:%d:%Y')
                            rand = ['Good morning ' + (datafile["Identity"][0]["pronouns"]) + ', I grabbed the news for,' + mTime]
                            Chrome = ("google-chrome %s")

                            webbrowser.get(Chrome)
                            webbrowser.open('https://www.sciencenews.org/topic/math-technology', new=2, autoraise=True)

                            if enable_s == True:
                                Speech.say(rand,n,mixer)
                            else:
                                ref_rand = ''.join(str(e) for e in rand)
                                print(ref_rand)

                        if message == ('athena'):

                            rand = ['Yes Sir?', 'What can I, do for you ' + (datafile["Identity"][0]["pronouns"])]
                            if enable_s == True:
                                Speech.say(rand,n,mixer)
                            else:
                                ref_rand = ''.join(str(e) for e in rand)
                                print(ref_rand)

                        #Handle ques on the internet connection
                        #if ('on') and ('display') and ('power') in message:
                            #find a way to make ipv4 addresses all static, so I don't have to make a script to constantly 'brute force' the network for ipv4 addresses and specifically state they are mine
                            
                        if ('are we connected') in message:

                            REMOTE_SERVER = "www.google.com"
                            Speech.wifi()
                            rand = ['We are connected']
                            if enable_s == True:
                                Speech.say(rand,n,mixer)
                            else:
                                ref_rand = ''.join(str(e) for e in rand)
                                print(ref_rand)

                        

                        if ('what is the time') in message or ('what time is it') in message or ('can you get me the current time') in message or ('can you tell me the time') in message:

                            lTime = time.strftime('%I:%M')
                            rand = ['the time is,' + lTime + ',sir.']
                            if enable_s == True:
                                Speech.say(rand,n,mixer)
                            else:
                                ref_rand = ''.join(str(e) for e in rand)
                                print(ref_rand)

                        if ('what day is it') in message or ('what is the date') in message or ('date please') in message:
                            
                            tDate = time.strftime('%B:%d:%Y')
                            rand = ['Today is,' + tDate + (datafile["Identity"][0]["pronouns"])]
                            if enable_s == True:
                                Speech.say(rand,n,mixer)
                            else:
                                ref_rand = ''.join(str(e) for e in rand)
                                print(ref_rand)

                        if ('athena can you get me the weather') in message or ('can you get the weather') in message or ('athena weather please') in message or ('weather please') in message:
                           
                            noaa_result = pywapi.get_weather_from_noaa('KPWT')
                            rand = ["I've fetched the weather for you." + "It is currently" + noaa_result['weather'] + '\n' + 'Current Temperature is: ' + noaa_result['temp_f'] +  'Degrees.'+ '\n' + 'Information grabbed from' + noaa_result['location']]
                            if enable_s == True:
                                Speech.say(rand,n,mixer)
                            else:
                                ref_rand = ''.join(str(e) for e in rand)
                                print(ref_rand)
                        
                        if ('can you get the news') in message or ('get the news please') in message or ('athena get the news please') in message:
                           
                            rand = ['Fetching todays headlines, sir, please wait.']
                            if enable_s == True:
                                Speech.say(rand,n,mixer)
                            else:
                                ref_rand = ''.join(str(e) for e in rand)
                                print(ref_rand)
                            time.sleep(5)

                            d = feedparser.parse('http://rss.nytimes.com/services/xml/rss/nyt/Science.xml')
                            rand = [d.feed['title'] + d.feed['description']]
                            Speech.say(rand,n,mixer)

                        if ('where is') in message:

                            rand = ['Searching for' + message + ', please wait.']
                            LocSrch_Message = message.replace("where is", "")
                            Chrome = ("google-chrome %s")
                            webbrowser.get(Chrome).open('http://www.'+ message)
                            if enable_s == True:
                                Speech.say(rand,n,mixer)
                            else:
                                ref_rand = ''.join(str(e) for e in rand)
                                print(ref_rand)

                        if ('what is a') in message or ("what is an") in message:
                            from nltk.corpus import wordnet as Word

                            if "an" in message:

                                message = message.replace("an ","")

                            if "a" in message:
                                message = message.replace("a ","")

                            spoken_def = Word.synset(message + '.n.1')
                            colist = str(len(spoken_def))
                            rand = ['Sir, there are ' + colist + 'entries, reading the first one: ' + spoken_def]

                            webbrowser.get(Chrome)
                            webbrowser.open("http://www.dictionary.com/browse/" + message)
                            if enable_s == True:
                                Speech.say(rand,n,mixer)
                            else:
                                ref_rand = ''.join(str(e) for e in rand)
                                print(ref_rand)

                        if ('medical') in message:
                            #Searches the entire medical dictionary for a term of definition

                            term = message.replace("medical","")
                            import nltk.corpus
                            medical = open('./athena/Data/Databases/Medical_Dictionary.txt')

                            #Converts the text file into an actual corpus, the reason it isn't converted or loaded above,
                            #is because it would consume to many resources if it were constantly loaded.
                            text = medical.read()
                            text1 = text.split()
                            conc_term = nltk.corpus.nltk.Text(text1)
                            med_term = conc_term.concordance(term)
                            rand = [med_term]
                            if enable_s == True:
                                Speech.say(rand,n,mixer)
                            else:
                                ref_rand = ''.join(str(e) for e in rand)
                                print(ref_rand)



                        
                            
                        else:

                            temporal_save1 = open("./include/test.txt", "r+") #temp1 -> train.en
                            temporal_save1.write(message)
                            temporal_save1.close()
                            print(null_error)

                    #exceptions
                    except (KeyboardInterrupt,SystemExit):
                        print("Goodbye, athena powering down now")
                        #temp_train()
                    except sr.UnknownValueError:
                        print("error")
                    except sr.RequestError as e:
                        print("Error, no internet found.")


                doss = os.getcwd()
                i=0
                n=0

                while (i<1):
                    if enable_s == True:
                        r = sr.Recognizer()
                        with sr.Microphone() as source:
                            audio = r.adjust_for_ambient_noise(source)
                            n = (n+1)
                            audio = r.listen(source)
                            #funcs.detect()
                            s = (r.recognize_google(audio))
                            print(s)
                            message = (s.lower())
                            runtime(message)
                    else:
                        #funcs.detect()
                        s = input(">>>") 
                        print(s)
                        message = (s.lower())
                        message = message.replace(">>>", "")
                        runtime(message)

                            

                    
                        

        if __name__ == '__main__':
            start.Interface()


#========================
#   System wide Imports
#========================
#Checking if certain system packages are installed.
#note, only install this package if you have a computing
#cluster like I did, and then allow it to install packages as needed
#It may require sudo access.

import numpy
import sys, os, urllib

try:
    from mpi4py import MPI

except ImportError:
    print("Not configured for cluster computing; continuing with single computer computing.")

    if __name__ == '__main__':
        spn.main()

    if rank == 0:

        #Node 1 and the linguistics
        import apt
        cache = apt.Cache()
        if cache['mpich'].is_installed:
            print('Mpich installed')
        print("none")

    if rank == 2:

        #Node 2 and the mathmatical node.
        #===========================
        try:
            import theano as th
            import sympy as sp
            import numpy as np
        except ImportError:
            print("\033[0;31m[System] |Warning! Import Warning!| System failed to import a library!")
        #============================
        # Just as a fallback to basic
        # operations
        #============================

    if rank == 3:

        print("none")

    if rank == 4:

        print("none")
else:
    #Continue the program as if nothing really happens
    if __name__ == '__main__':
        spn.main()
