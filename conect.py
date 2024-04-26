import json
from mongoengine import connect
from models import Author, Quote

connect(
    db='Goose',
    host='mongodb+srv://fedoryshynjuliia:<asdrtygcn76>@goose.gbei9ew.mongodb.net/?retryWrites=true&w=majority&appName=Goose',
    username='fedoryshynjuliia',
    password='asdrtygcn76')

# Підключення до MongoDB Atlas
connect("your_mongodb_uri")

# Завантаження даних з authors.json
with open('authors.json', 'r') as file:
    authors_data = json.load(file)

# Завантаження авторів
for author_data in authors_data:
    author = Author(
        fullname=author_data['fullname'],
        born_date=author_data['born_date'],
        born_location=author_data['born_location'],
        description=author_data['description']
    )
    author.save()

# Завантаження даних з quotes.json
with open('quotes.json', 'r') as file:
    quotes_data = json.load(file)

# Завантаження цитат
for quote_data in quotes_data:
    author = Author.objects(fullname=quote_data['author']).first()
    quote = Quote(
        tags=quote_data['tags'],
        author=author,
        quote=quote_data['quote']
    )
    quote.save()

