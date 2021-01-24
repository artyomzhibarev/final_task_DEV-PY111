import argparse


def create_add_subparser(subparsers):
    add_subparser = subparsers.add_parser('add')
    add_subparser.add_argument('-t', '--title', required=True, help='Set the title of the book',
                               dest='title', nargs='+')
    add_subparser.add_argument('-y', '--year', required=True, help='Set the year of the book',
                               dest='year', type=int)
    add_subparser.add_argument('-p', '--page', required=True, help='Set the number of pages',
                               dest='page', type=int)
    add_subparser.add_argument('-a', '--author', required=True, help='Set the author of the book',
                               dest='author', nargs='+')


def create_delete_subparser(subparsers):
    delete_subparser = subparsers.add_parser('delete')
    delete_subparser.add_argument('-t', '--title', required=True, help='Book title to delete',
                                  dest='title', nargs='+')


def create_delete_author_subparser(subparsers):
    delete_author_subparser = subparsers.add_parser('delete_author')
    delete_author_subparser.add_argument('-a', '--author', required=True, help='Name of author',
                                         dest='author', nargs='+')
    delete_author_subparser.add_argument('-t', '--title', required=True, help='Book title',
                                         dest='title', nargs='+')


def create_add_author_subparser(subparsers):
    add_author_subparser = subparsers.add_parser('add_author')
    add_author_subparser.add_argument('-a', '--author', required=True, help='Name of author',
                                      dest='author', nargs='+')
    add_author_subparser.add_argument('-t', '--title', required=True, help='Book title',
                                      dest='title', nargs='+')


def create_search_subparser(subparsers):
    search_subparser = subparsers.add_parser('search')
    search_subparser.add_argument('-t', '--title', help='Search book from library by title', nargs='+', required=False)
    search_subparser.add_argument('-a', '--author', help='Search an author', nargs='+', required=False)


def create_parser():
    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(dest='name_subparser')
    create_add_subparser(subparsers)
    create_delete_subparser(subparsers)
    create_add_author_subparser(subparsers)
    create_search_subparser(subparsers)
    create_delete_author_subparser(subparsers)
    return parser
