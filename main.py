from library import *
from cli import create_parser

LIBRARY_FILENAME = 'library.json'


def main():
    parser = create_parser()
    args = parser.parse_args()
    library_ = get_list_from_json_lib(LIBRARY_FILENAME)
    if args.name_subparser == 'delete':
        library_ = delete_book(library_, args.title)
        get_json_file(library_, LIBRARY_FILENAME)
    elif args.name_subparser == 'add':
        library_ = add_book(library_, args.title, args.year, args.page, args.author)
        get_json_file(library_, LIBRARY_FILENAME)
    elif args.name_subparser == 'add_author':
        library_ = add_author(library_, args.title, args.author)
        get_json_file(library_, LIBRARY_FILENAME)
    elif args.name_subparser == 'delete_author':
        delete_author(library_, args.title, args.author)
        get_json_file(library_, LIBRARY_FILENAME)
    elif args.name_subparser == 'search':
        if args.title:
            print(search_book_by_title(library_, args.title))
        else:
            print(search_book_by_author(library_, args.author))


if __name__ == '__main__':
    main()

# C:\Python\Python39\python.exe
