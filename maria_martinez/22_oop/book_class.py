class Booklist():
	def __init__(self):
		self.books = []


	def add(self, title, author):
		book = {}
		book['title'] = title
		book['author'] = author
		self.books.append(book)
	

	def count_books(self):
		return len(self.books)
		

	def remove_title(self, title):
		for title in self.books:
			if title == self.books:
				self.books.remove(title)
				
	

	def display_titles(self):
		temp = []
		for book in self.books:
			temp.append(book['title'])
		temp.sort()
		print(temp)
		

