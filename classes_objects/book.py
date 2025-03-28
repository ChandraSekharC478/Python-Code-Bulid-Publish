class Book:

    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def discount(self,discount):
        self.price = self.price - (self.price * discount / 100)
book1 = Book("The Great Gatsby","F. Scott Fitzgerald",100)
print(f"Title: {book1.title}, Author: {book1.author}, Price: ${book1.price}, Discounted Price: ${book1.price - (book1.price * 0.10)}")
book1.discount(10)
