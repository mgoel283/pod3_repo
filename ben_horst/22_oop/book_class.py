class Booklist():
	def __init__(self):
		self.books = []

	def add(self, title, author):
		book = {}
		book['title'] = title
		book['author'] = author
		self.books.append(book)
 
	def count_books(self):
		return(len(self.books))

	def remove_title(self, title):
		for book in self.books:
			if  title == book['title']:
				self.books.remove(book)
				return
		print(f'{title} is not in your book list!')


	def display_titles(self):
		titles = []
		for book in self.books:
			titles.append(book['title'])

		titles.sort()
		print(titles)
		return

'''
BONUS Part #6:
Define a display_titles() method to display all the titles of the books in an object of class Booklist
The titles should be displayed in alphabetical order!
-The method requires no parameters other than self

HINT: there's a quick way to sort a list in alphabetical order

Once you have completed this method, test it out on both my_library and nyt_bestsellers
'''