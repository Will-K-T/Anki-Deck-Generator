import genanki
import requests
from bs4 import BeautifulSoup

URL = "https://learn.dict.naver.com/wordbook/koendict/#/my/cards?wbId=c67e217668794f2e93cc2653144169c4&qt=0&st=0&name=TOPIK%20Beginner%20Vocab.%20List%201&tab=list"
URL2 = "https://korean.dict.naver.com/koendict/#/main"
page = requests.get(URL2)

soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())

cards = soup.find_all("div", class_="card_word")
print(soup.find(id="section_word_card"))

print(len(cards))
for card in cards:
    koreanWord = card.find("a", class_="title")
    print(koreanWord)

# Styling for the notes
CSS = """.card{
font-family: arial;
font-size: 20px;
text-align: center;
color: black;
background-color: white;
}
"""

# Model for Korean notes
kmodel_id = 1540084157
korean_model = genanki.Model(
    kmodel_id,
    'Korean Model',
    fields=[
        {'name': 'Korean'},
        {'name': 'English'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '<span style="font-family: nanumgothic; font-size: 25px">{{Korean}}</span>',
            'afmt': '{{FrontSide}}<hr id="answer"><span style="">{{English}}</span>',
        },
    ],
    css=CSS
)




