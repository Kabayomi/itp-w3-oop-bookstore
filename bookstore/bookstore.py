class Bookstore(object):
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []
    
    def add_book(self, book):
        self.books.append(book)
        
    def get_books(self):
        return self.books   
        
    def search_books(self, title=None, author=None):
        search_result = []
        
        if title and author:     #Search by both book an Author
            for book in self.books:
                if author == book.author and title.lower() in book.title.lower():
                    search_result.append(book)
        elif title is None and author is not None:  #Search by Author alone
            for book in self.books:
                if author == book.author:
                    search_result.append(book)
        elif title is not None and author is None:  #Search by Title alone
            for book in self.books:
                if title.lower() in book.title.lower():
                    search_result.append(book)
        return search_result
            
        
    



class Author(object):
    def __init__(self, name, nationality):
        self.name = name
        self.nationality = nationality
        self.books = []
    
    def get_books(self):
        return self.books


class Book(object):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        author.books.append(self)
