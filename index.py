import requests
from bs4 import BeautifulSoup
import datetime
import codecs
import time
import sqlite3
import re
class index():

    def __init__(self):
        
        self.creator = ''
        self.comments = ''
        self.title = ''
        self.pubdate = ''
        self.link = ''
        self.vals = ()

        # the url links for all rss feeds for
        # each jamiiforum category
        self.urls = {'home' : 'https://www.jamiiforums.com/forums/-/index.rss',
                     'thinkers' : 'https://www.jamiiforums.com/forums/great-thinkers.110/index.rss',
                     'siasa' : 'https://www.jamiiforums.com/forums/jukwaa-la-siasa.6/index.rss',
                     'hoja' : 'https://www.jamiiforums.com/forums/habari-na-hoja-mchanganyiko.42/index.rss',
                     'intelligence' : 'https://www.jamiiforums.com/forums/jamii-intelligence.51/index.rss',
                     'international' : 'https://www.jamiiforums.com/forums/international-forum.28/index.rss',
                     'ujasiriamali' : 'https://www.jamiiforums.com/forums/ujasiriamali.114/index.rss',
                     'biashara' : 'https://www.jamiiforums.com/forums/jukwaa-la-biashara-na-uchumi.84/index.rss',
                     'matangazo' : 'https://www.jamiiforums.com/forums/matangazo-madogo.65/index.rss',
                     'tenda' : 'https://www.jamiiforums.com/forums/nafasi-za-kazi-na-tenda.8/index.rss',
                     'events' : 'https://www.jamiiforums.com/forums/news-current-events.125/index.rss',
                     'politics_palace' : 'https://www.jamiiforums.com/forums/politics-palace.128/index.rss',
                     'the_palace' : 'https://www.jamiiforums.com/forums/the-palace.126/index.rss',
                     'kenyan_politics' : 'https://www.jamiiforums.com/forums/kenyan-politics.115/index.rss',
                     'uganda_news' : 'https://www.jamiiforums.com/forums/ugandan-news-and-politics.131/index.rss',
                     'the_lounge' : 'https://www.jamiiforums.com/forums/the-lounge.120/index.rss',
                     'chat' : 'https://www.jamiiforums.com/forums/jf-chit-chat.103/index.rss',
                     'urembo_na_utanashati' : 'https://www.jamiiforums.com/forums/urembo-mitindo-na-utanashati.129/index.rss',
                     'photos' : 'https://www.jamiiforums.com/forums/jamii-photos.92/index.rss',
                     'celebrities' : 'https://www.jamiiforums.com/forums/celebrities-forum.53/index.rss',
                     'mahusiano' : 'https://www.jamiiforums.com/forums/mahusiano-mapenzi-urafiki.62/index.rss',
                     'jokes' : 'https://www.jamiiforums.com/forums/jokes-utani-udaku-gossips.23/index.rss',
                     'utambulisho' : 'https://www.jamiiforums.com/forums/utambulisho-member-intro-forum.88/index.rss',
                     'sports' : 'https://www.jamiiforums.com/forums/sports.105/index.rss',
                     'entertainment' : 'https://www.jamiiforums.com/forums/entertainment.106/index.rss',
                     'jf-doctor' : 'https://www.jamiiforums.com/forums/jf-doctor.61/index.rss',
                     'garage_na_usafiri' : 'https://www.jamiiforums.com/forums/jf-garage-magari-na-vyombo-vya-usafiri.130/index.rss',
                     'tech' : 'https://www.jamiiforums.com/forums/tech-gadgets-science-forum.20/index.rss',
                     'chef' : 'https://www.jamiiforums.com/forums/jf-chef.122/index.rss',
                     'sheria' : 'https://www.jamiiforums.com/forums/jukwaa-la-sheria-the-law-forum.87/index.rss',
                     'elimu' : 'https://www.jamiiforums.com/forums/jukwaa-la-elimu-education-forum.11/index.rss',
                     'lugha' : 'https://www.jamiiforums.com/forums/jukwaa-la-lugha.81/index.rss',
                     'store' : 'https://www.jamiiforums.com/forums/jf-store-enjoy-this.77/index.rss',
                     'complaints' : 'https://www.jamiiforums.com/forums/complaints-congrats-advice.80/index.rss',
                     'imani' : 'https://www.jamiiforums.com/forums/dini-imani.24/index.rss'}

    def ombi(self):

        # download the xml for each category rss
        for key, value in self.urls.items():
            self.ombi = requests.get(value)

            # set the name of the rss corresponding file
            self.fName ='indices\\raw\\' + key + '.xml'

            # write the corresponding files downloaded xml
            with codecs.open(self.fName, 'w', 'utf-8') as f:
                f.write(self.ombi.text)

            print("rss ya " + key + " imefanikiwa kupakuliwa")

            time.sleep(1)

        print('Kazi imemalizika')


    def db(self):

        self.cont_ID = 1

        # open up a connection to a database
        con = sqlite3.connect("indices\database")

        c = con.cursor()

        c.execute('CREATE TABLE IF NOT EXISTS posts (ID int AUTO INCREMENT, title text, pubdate text, link text, author text, comments text, cont_ID int)')

        # for each file in the expected urls
        for key, value in self.urls.items():

            # set the name of the file
            self.fName = 'indices\\raw\\' + key + '.xml'

            # stri the important info and store in a database
            with open(self.fName, 'r') as f:
                self.xml = f.read()

            self.soup = BeautifulSoup(self.xml)

            # for each item in the xml files we add to the database
            for uzi in self.soup.find_all("item"):
            
                self.title = uzi.title.string
                self.pubdate = uzi.pubdate.string
                self.link = uzi.link.string
                self.vals = (self.title,self.pubdate,self.link,self.cont_ID)

                c.execute('INSERT INTO posts (title,pubdate,link,cont_ID) VALUES (?,?,?,?)', self.vals)

            self.cont_ID = self.cont_ID + 1
            self.xml = ''

        # close the database connection
        c.close()
        print("the whole operation was successfull")

