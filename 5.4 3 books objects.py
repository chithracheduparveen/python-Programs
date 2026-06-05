class Book:
  def __init__(self,title):
    self.title=title
  def create_book_list():
    return[Book("python 101"),Book("AI Basics"),Book("data science")]
books=Book.create_book_list()
for b in books:
    print("Book titel:",b.title)
