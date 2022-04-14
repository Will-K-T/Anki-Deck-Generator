import genanki
import random

# print(random.randrange(1 << 30, 1 << 31))

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

# Test note using the Korean model
test_note2 = genanki.Note(
    model=korean_model,
    fields=['안녕 세계!', 'Hello World!']
)

# Test deck
deck_id = 1129258273
test_deck = genanki.Deck(
    deck_id,
    'Test Deck'
)

# Adding note to deck
test_deck.add_note(test_note2)

# Creating the anki package
genanki.Package(test_deck).write_to_file('../decks/test_deck.apkg')
