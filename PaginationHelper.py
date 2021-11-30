import math
# import math library to using math.ceil function to rounds a number Up to the nearest integer
class PaginationHelper:

	# The constructor take in an array of values and an integer indicating
	# 	how many items will be allowed per each page.

	def __init__(self, array, items_on_page):
		self.array = array
		self.items_on_page = items_on_page


	# using len fnction counting lenght of array/list

	def itemCount(self):
		return len(self.array)


	# divide items in list on items on page and dureturnting
	# 	using math.ceil function to rounds a number Up to the nearest integer

	def pageCount(self):
		page_count = self.itemCount() / self.items_on_page
		return math.ceil(page_count)


	# return how many items existing on current page
	# for 0 page mathing input page number with items on page if they <= return them self
	# for pages 1/2/3 etc if input page multiply with items less then condition and bigger then lenght items in list
	# return modulo of list leght on items on page
	# 	other wise return -1 since the page is invalid

	def pageItemCount(self, page):
		if (page+1) * self.items_on_page <= self.itemCount():
				return self.items_on_page
		if page*self.items_on_page < self.itemCount() and (page+1) * self.items_on_page > self.itemCount():
				return self.itemCount()%self.items_on_page
		return -1



	# return on what page item exist
	# devide item index on items on page if item index in leght items in list
	#	otherwise return -1 it mean item not exist or negative indexes

	def pageIndex(self, item):
		if item < self.itemCount() and item >= 0 :
					return int(item/self.items_on_page)
		return -1

help = PaginationHelper(['a','b','c','d','e','f'], 4)
print(help.pageCount()) # should == 2
print(help.itemCount()) # should == 6
print(help.pageItemCount(0)) # should == 4
print(help.pageItemCount(1)) # last page - should == 4
print(help.pageItemCount(2)) # should == -1 since the page is invalid
# page_index takes an item index and returns the page that it belongs on
print(help.pageIndex(5)) # should == 1 (zero based index)
print(help.pageIndex(2)) # should == 0
print(help.pageIndex(20)) # should == -1
print(help.pageIndex(-10)) # should == -1 because negative indexes are invalid




