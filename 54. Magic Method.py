# Magic Method = Dunder methods (double underscore) __init__, __str__, __eq__
#                They are automatically called by many of python's built in operations
#                They allow developers to define or customize the behavior of objects


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author} pages {self.pages}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.pages == other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __add__(self, other):
        return f"{self.pages + other.pages} Pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return f"key '{key}' not in Book"


book1 = Book("Hobit", "J.R.R", 310)
book2 = Book("Hobit", "J.R.R", 310)
book3 = Book("The Lion King", "LG", 250)

# print(book3)
# print(book1 == book2)
# print(book2 < book3)
# print(book2 > book3)
# print(book1 + book2)
# print("Lion" in book3)
# print(book1['title'])
# print(book1['pages'])
print(book1['audio'])