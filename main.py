import json
import csv


# read json file of users
def read_users_json():
    file = open('data/users.json')
    users_data = json.load(file)
    return users_data


# read csv file of books
def read_books_csv():
    file = open('data/books.csv', 'r')
    books_data = csv.DictReader(file)
    return books_data


# count books (211)
books_count = 0
for row in read_books_csv():
    books_count += 1

# count users (28)
users_count = len(read_users_json())

# count books per user (7)
books_per_user = int(books_count / users_count)

# count books will spend (196 books will spend by 7 books for each user)
division = books_per_user * users_count

# count books left (15)
books_left = books_count-division

# create list of all books with all info
all_books_list = []
for row in read_books_csv():
    all_books_list.append(dict(row))

# create list of all books with needed info
books_list = []
users_book = {}

for book in all_books_list:
    # read book's data
    title = book['Title']
    author = book['Author']
    pages = int(book['Pages'])
    genre = book['Genre']

    # add book's data to dict
    users_book.update({"title": title})
    users_book.update({"author": author})
    users_book.update({"pages": pages})
    users_book.update({"genre": genre})

    # add book data to result list of books
    books_list.append(users_book)
    users_book = {}

# create result list of users
result_list = []
result_data = {}

for user in read_users_json():
    # read user's data
    name = user['name']
    gender = user['gender']
    address = user['address']
    age = int(user['age'])

    # add user's data to dict
    result_data.update({"name": name})
    result_data.update({"gender": gender})
    result_data.update({"address": address})
    result_data.update({"age": age})
    result_data.update({"books": None})

    # add data to result list of users with empty books list
    result_list.append(result_data)
    result_data = {}

# add books to each user
users_books_list = []
q = 1
for current_user in result_list:
    # condition for users who will get equal count of books +1 book
    if q <= books_left:
        # create list of books for current user
        users_books_list = books_list[0:(books_per_user + 1)]
        # add list of books to dict of current user
        current_user['books'] = users_books_list
        # delete added books from list of books
        for i in range(books_per_user + 1):
            books_list.pop(0)

    # condition for users who will get equal count of books
    else:
        # create list of books for current user
        users_books_list = books_list[0:books_per_user]
        # add list of books to dict of current user
        current_user['books'] = users_books_list
        # delete added books from list of books
        for i in range(books_per_user):
            books_list.pop(0)
    q += 1

# convert our resul_list to json
json_data = json.dumps(result_list, indent=4)

with open('result.json', 'w') as f:
    f.write(json_data)
