class Publication:
    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def display_info(self):
        print("Title:", self.__title)
        print("Author:", self.__author)

class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_pages = number_pages

    def set_number_of_pages(self, number_pages):
        if number_pages < 0:
            self.__number_pages = number_pages

    def get_number_of_pages(self):
        return self.__number_pages
        


pub1 = Publication("Journal of, "Abraham Lincoln")


pub1.display_info()
