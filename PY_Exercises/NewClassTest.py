class MyTest:
    def instanceTestMethod(self):
        print(f"This is a test class {self}")  
    
    @classmethod
    def classTestMethod(cls):
        print(f"This is a class method {cls}")
    
    @staticmethod
    def staticTestMethod():
        print("This is a static method")
    def __init__(self):
        print("This is a constructor method")
    def __del__(self):
        print("This is a destructor method")
    def __str__(self):
        return "This is a string representation of the object"
    def __repr__(self):
        return "This is a string representation of the object for debugging"
    def __len__(self):
        return 0
    def __getitem__(self, key):
        return None 
    def __setitem__(self, key, value):
        pass    
    def __delitem__(self, key):
        pass
    def __contains__(self, item):
        return False        
    
class Book:
    def __init__(self, title, author, book_type=None):
        self.title = title
        self.author = author
        self.book_type = book_type
    TYPES = ("hardcover", "paperback", "ebook")
    def print_book_info(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nTypes: {self.TYPES}")
    def __repr__(self):
        return f"Book(title={self.title}, author={self.author}, types={self.TYPES})"
    @classmethod
    def hardcover(cls, title, author):
        return cls(title, author, Book.TYPES[0] )
    
    
book = Book("1984", "George Orwell")
#book.print_book_info()
 
#print(book)      
book2 = Book.hardcover("To Kill a Mockingbird", "Harper Lee")
print(book2)    
print(book)
  