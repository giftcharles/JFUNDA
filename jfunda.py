import feedparser
import time
import codecs
import json

class Jfunda():
    """
    the initialization of the appwide variables
    """
    def __init__(self):

        # the url links for all rss feeds for
        # each jamiiforum category
        self.urls = {'thinkers' : 'https://www.jamiiforums.com/forums/great-thinkers.110/index.rss',
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
    
    def feeds(self):
        
        counter = 0
        json_data = []
        
        for key,value in self.urls.items():
            f = feedparser.parse(value)
            
            for entry in f.entries:
            
                if 'slash_comments' in entry:
                    comments = f.entries[counter].slash_comments
                else:
                    comments = 0
                    
                if 'title' in entry:
                    title = f.entries[counter].title
                else:
                    title = '(No Title Here)'                
                
                
                title = f.entries[counter].title
                author = f.entries[counter].author
                pub = f.entries[counter].published
                link = f.entries[counter].link                
                
                thread_data = {"title":title,
                               "author":author,
                               "comments":comments,
                               "published":pub,
                               "link":link,
                               "category":key}

                json_data.append(thread_data)
                
                print("done with the thread {0} of position {1}".format(title, counter))
                counter = counter + 1
            
            counter = 0                
            
            print("entires saved for {0} \n".format(key))
            time.sleep(1)
            
        with codecs.open("feeds.json", "w", "utf-8") as file:
            file.write(json.dumps(json_data, indent=4, separators=(',', ': ')))        
            
        print("All feeds downloaded into feed.json!")
        
        
inst = Jfunda()

inst.feeds()