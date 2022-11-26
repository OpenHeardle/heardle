import requests
import requests
from bs4 import BeautifulSoup
import os


# File name to save the songs to
tema = "movingchiquilinas"
# Playlist URL
url = 'https://open.spotify.com/playlist/72ucVWJFYYRRZFwla5wQ5q?si=82dc5332d19c4794'


r = requests.get(url)
mystr = r.text
# write content to file
with open(tema+'.html', 'w', encoding='utf-8') as f:
    print(mystr, file=f)

songs = []
# Open the Spotify source code file
with open(tema+".html", encoding='utf-8') as fp:
    soup = BeautifulSoup(fp,features="html.parser")
    mydivs = soup.find_all("button", {"data-testid": "entity-row-v2-button"})
    for div in mydivs:
        song_name = div['aria-label'].replace("track ","")
        # get span tag
        span = div.find_all("span")[2]
        # get the text
        artist_name = span.text
        #artist_name 
        full_song = song_name +" - "+ artist_name
        songs.append(full_song)
        

# write songs to txt file
with open("lists_txt/"+tema+'.txt', 'w', encoding='utf-8') as f:
    for item in songs:
        print(item, file=f)

# remove the html file
os.remove(tema+".html")
