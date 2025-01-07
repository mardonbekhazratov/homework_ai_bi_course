class BookNotFoundException(Exception):
    
    def __init__(self, msg, *args, **kwargs):
        super().__init__(args,kwargs)
        self.msg = msg
    
    def __str__(self):
        return self.msg


class BookAlreadyBorrowedException(Exception):
    
    def __init__(self, msg, *args, **kwargs):
        super().__init__(args,kwargs)
        self.msg = msg
    
    def __str__(self):
        return self.msg


class MemberLimitExceededException(Exception):
    
    def __init__(self, msg, *args, **kwargs):
        super().__init__(args,kwargs)
        self.msg = msg
    
    def __str__(self):
        return self.msg


class MemberNotFound(Exception):
    
    def __init__(self, msg, *args, **kwargs):
        super().__init__(args,kwargs)
        self.msg = msg
    
    def __str__(self):
        return self.msg


class Book:

    count = 0

    def __init__(self, title: str, author: str, is_borrowed = False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed
        self.id = Book.count
        Book.count += 1
    
    def __str__(self):
        return f"{self.title}, {self.author}"
    
    def __repr__(self):
        return f"\"{self.title}, {self.author}\""


class Member:

    count = 0

    def __init__(self, name, borrowed_books = None):
        self.name = name
        self.borrowed_books = list() if borrowed_books==None else borrowed_books
        self.id = Member.count
        Member.count += 1
    
class Library:

    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, *args):
        for book in args:
            self.books.append(book)

    def add_member(self, *args):
        for member in args:
            self.members.append(member)

    def borrow_book(self, name_of_member: str, title_of_book: str):
        id_of_book = -1
        for book in self.books:
            if book.title == title_of_book:
                id_of_book = book.id

        if id_of_book == -1:
            raise BookNotFoundException("Book not found.")
        
        id_of_member = -1
        for member in self.members:
            # print(member.id)
            if member.name == name_of_member:
                id_of_member = member.id
            
        if id_of_member == -1:
            raise MemberNotFound("Member not found.")
        
        if self.books[id_of_book].is_borrowed:
            raise BookAlreadyBorrowedException("Book already borrowed.")
        
        # debug
        # for i in (self.members[id_of_member]).borrowed_books:
        #     print(i)

        if len(self.members[id_of_member].borrowed_books) >= 3:
            raise MemberLimitExceededException("A member can not borrow more than 3 books at a time.")
        
        self.members[id_of_member].borrowed_books.append(self.books[id_of_book])
        self.books[id_of_book].is_borrowed = True

        print(f"{name_of_member} borrowed \"{title_of_book}, {self.books[id_of_book].author}\"")

    def return_book(self, name_of_member: str, title_of_book: str):
        id_of_book = -1
        for book in self.books:
            if book.title == title_of_book:
                id_of_book = book.id

        if id_of_book == -1:
            raise BookNotFoundException("Book not found.")
        
        id_of_member = -1
        for member in self.members:
            if member.name == name_of_member:
                id_of_member = member.id
            
        if id_of_member == -1:
            raise MemberNotFound("Member not found.")

        if self.books[id_of_book] not in self.members[id_of_member].borrowed_books:
            raise BookNotFoundException(f"{name_of_member} didn't borrow this book.")
        
        self.books[id_of_book].is_borrowed = False
        self.members[id_of_member].borrowed_books.remove(self.books[id_of_book])

        print(f"{name_of_member} returned \"{self.books[id_of_book]}\"")

def main():
    library = Library()
    book1 = Book("Harry Potter", "Rowling")
    book2 = Book("The Lord of the Rings", "Tolkien")
    book3 = Book("The Alchemist", "Paulo Coelho")
    book4 = Book("The Hobbit", "Tolkien")
    member1 = Member("Someone")
    member2 = Member("Mardon")
    member3 = Member("Anyone")
    library.add_book(book1,book2,book3,book4)
    library.add_member(member1,member2,member3)
    library.borrow_book("Mardon","The Alchemist")
    library.borrow_book("Mardon","Harry Potter")
    library.borrow_book("Mardon","The Lord of the Rings")
    library.borrow_book("Someone","The Hobbit")
    library.return_book("Mardon","The Alchemist")

if __name__ == "__main__":
    main()