import json


def get_json_file(obj: list, filename):
    with open(filename, 'w', encoding='utf-8') as json_output_file:
        json.dump(obj, json_output_file, indent=4)


def get_list_from_json_lib(file):
    """
    Get Python object (list) from json. Json stores a list of dictionaries with fields:
    title: "Title of book"
    year: "Year"
    pages: "Pages"
    author: [List of authors]
    :param file:
    :return:
    """
    with open(file, 'r', encoding='utf-8') as lib_json_file:
        sorted_library = sorted(json.load(lib_json_file), key=lambda k: k['title'])
        return sorted_library


def search_book_by_title(list_: list, name: list):
    """
    Searches for a book title. Returns a pair (Title, Author)
    :param list_:
    :param name:
    :return:
    """
    searched = [item for item in list_ if ' '.join(name).title() in item['title']]
    if not searched:
        print(f"The book with the title {' '.join(name)} does not exist")
    else:
        print(f"Search results for {' '.join(name)}")
    return searched


def search_book_by_author(list_: list, name: list):
    """
    Searches for a book author. Returns a pair (Title, Author)
    :param list_:
    :param name:
    :return:
    """
    searched = []
    for i in range(len(list_)):
        for j in range(len(list_[i]['author'])):
            if ' '.join(name).title() in list_[i]['author'][j]:
                searched.append((list_[i]['author'][j], list_[i]['title']))
    if not searched:
        print(f"The book with the author {' '.join(name)} does not exist")
    else:
        print(f"Search results for {' '.join(name)}")
    return searched
    # return [item for item in list_ if item['author'] == ' '.join(name).title()]
    # ' '.join(name).title()
    # ' '.join(title).title()


def add_author(list_: list, title: list, name: list):
    """
    Adds the author to an existing book in the library, if not, displays an error message
    :param list_:
    :param title:
    :param name:
    :return:
    """
    for item in list_:
        if item['title'] == ' '.join(title).title():
            item['author'].append(' '.join(name).title())
    return list_


def delete_author(list_: list, title: list, name: list):
    """
    Adds the author to an existing book in the library, if not, displays an error message
    :param list_:
    :param title:
    :param name:
    :return:
    """
    for item in list_:
        if item['title'] == ' '.join(title).title():
            try:
                item['author'].remove(' '.join(name).title())
            except ValueError:
                print(f"Author {' '.join(name)} does not exist")
    return list_


def delete_book(list_: list, name: list):
    """
    Delete book by title
    :param list_:
    :param name:
    :return:
    """
    return [item for item in list_ if item['title'] != ' '.join(name).title()]


def add_book(list_: list, title: list, year: int, pages: int, author: list):
    list_.append(
        {
            "title": ' '.join(title).title(),
            "year": year,
            "pages": pages,
            "author": [' '.join(author).title(),
                       ]
        }
    )
    return list_

