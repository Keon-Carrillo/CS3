'''
Keon P. Carrillo
9-Samat
10/16/2026
'''
#creates the parent class which Book and Magazine will be derived from
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

#creating a Book, inherits from Publication
class Book(Publication):
    def __init__(self, title, author, number_pages):
        super().__init__(title, author)
        self.__number_pages = number_pages

    #validates the value of the pages
    def set_number_of_pages(self, number_pages):
        if number_pages < 0:
            print("Number of pages should be positive.")

    #displays information about the pages
    def get_number_of_pages(self):
        print("Number of pages:", self.__number_pages)
        return ""

#creating a Magazine, inherits from Publication
class Magazine(Publication):
    def __init__(self, title, author, issue_number):
        super().__init__(title, author)
        self.__issue_number = issue_number

    #validates the value of the issue number
    def set_issue_number(self, issue_number):
        if issue_number < 0:
            print("Issue number should be positive.")

    #displays information about the issue number
    def get_issue_number(self):
        print("Issue number:", self.__issue_number)
        return ""

#creating library materials
pub1 = Publication("Journal of Experimental Psychology", "Ratchiff, R. & Van Dongen, H.")
book1 = Book("The Hobbit", "J.R.R. Tolkien", 310)
mag1 = Magazine("National Geographic", "Various Authors", 202)

#printing information
print("Publication Information:")
pub1.display_info()

print("\nBook Information:")
book1.set_number_of_pages(310)
book1.display_info()
print(book1.get_number_of_pages())

print("Magazine Information:")
mag1.display_info()
print(mag1.get_issue_number())