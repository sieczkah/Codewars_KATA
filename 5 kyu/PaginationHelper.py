"""https://www.codewars.com/kata/515bb423de843ea99400000a"""

# TODO: complete this class

class PaginationHelper:

# The constructor takes in an array of items and a integer indicating
# how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.page_cap = items_per_page
        self.pages = self.create_pages()
        
    def create_pages(self):
        pages_qty = self.page_count()
        cap = self.page_cap
        return {pg_ind: self.collection[pg_ind * cap: pg_ind * cap + cap] for pg_ind in range(pages_qty)}
        
        
# returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)

# returns the number of pages
    def page_count(self):
        return len(self.collection) // self.page_cap + 1
	
# returns the number of items on the current page. page_index is zero based
# this method should return -1 for page_index values that are out of range
    def page_item_count(self,page_index):
        items = self.pages.get(page_index, None)
        return len(items) if items else -1

# determines what page an item is on. Zero based indexes.
# this method should return -1 for item_index values that are out of range
    def page_index(self,item_index):
        if item_index in range(len(self.collection)):
            item = self.collection[item_index]
            for page, items in self.pages.items():
                if item in items:
                    return page
        return -1
