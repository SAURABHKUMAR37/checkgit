class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.reviews=[]
    def areview(self,review):
        self.reviews.append(review)
        print(f"review added is{review}")
    def countr(self):
        return len(self.reviews)
    def display(self):
        return self.reviews
c=Book("network","saurabh")
c.areview("good")
print(c.countr())
print(c.display())

