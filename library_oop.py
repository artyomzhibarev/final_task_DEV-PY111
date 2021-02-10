import json

LIBRARY_FILENAME = 'library.json'


class Library:
    class Book:
        """
        Describes book methods in the library
        """

        def __init__(self, title: str, year: int, pages: int, author: str):
            self.title = title
            self.year = year
            self.pages = pages
            self.author = author

        def __repr__(self):
            pass


class ReadWriteFileManager:
    def __init__(self, filename):
        self.file = filename

    @staticmethod
    def check_filename(filename):
        if not isinstance(filename, str):
            raise TypeError

    @staticmethod
    def read_json_lib(filename):
        f"""
        Reads a {json} file and returns a {list} object
        :param filename: 
        :return: 
        """
        with open(filename, 'r', encoding='utf-8') as json_lib_file:
            return json.load(json_lib_file)

    @staticmethod
    def write_to_json_lib(obj: list, filename):
        f"""
        Writes the {list} library object to the {json} file
        :param obj: 
        :param filename: 
        :return: 
        """
        with open(filename, 'w', encoding='utf-8') as json_output_file:
            json.dump(obj, json_output_file, indent=4)


if __name__ == '__main__':
    list_ = ReadWriteFileManager.read_json_lib(LIBRARY_FILENAME)
    print(list_)
