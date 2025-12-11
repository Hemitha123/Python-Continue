class book():
    def __init__(self,title,author,is_available=True):
        self.title=title
        self.author=author
        self.is_available=is_available    #initializes the variables
class library():
    def __init__(self):
        self.book=[]   #stores the books
        self.borrow=[]   #stores the borrowed books
    def add_book(self,book):
        if book not in self.book:  #if the book not in the stored book
            self.book.append(book)    #then it appends the book
            print(f"The {book.title} is added")
    def borrow_book(self, title):
        for book in self.book:   #if book present in the stored book 
            if book.title == title:   #and matches the title 
                self.borrow.append(book)   #then it appends the book
                print(f"{book.title} is borrowed")

    def return_book(self, title):
        for book in self.borrow:    #if book present in the stored book 
            if book.title == title:    #and matches the title 
                self.borrow.remove(book)   #then it removes from the borrowed list
                print(f"{book.title} is returned")

book1=book("English","xyz",True)    #books to be added to the list to store
book2=book("Kannada","abc",True)
book3=book("Hindi","str",True)

my_lib=library()      #methods are called
my_lib.add_book(book1)
my_lib.add_book(book2)
my_lib.add_book(book3)

my_lib.borrow_book("Hindi")
my_lib.borrow_book("English")

my_lib.return_book("Hindi")
    