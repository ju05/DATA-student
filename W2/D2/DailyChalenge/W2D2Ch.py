import math


class Pagination:
    def __init__(self, items=[], page_size=10):
        self.items = items
        self.page_size = page_size
        self.current_index = 0  # Current page
        self.total_pages = math.ceil(len(items) / page_size)

    def get_visible_items(self):
        stat_index = self.current_index*self.page_size
        end_index = stat_index + self.page_size
        if end_index <= len(self.items):
            return self.items[stat_index:end_index]
        else:
            return self.items[stat_index:]

    def go_to_page(self, page_number):
        page_number_inside = page_number - 1
        if 0 <= page_number_inside <= self.total_pages:
            self.current_index = page_number
            return self.get_visible_items()
        else:
            raise ValueError ('ValueError')

    def first_page(self):
        self.current_index = 0
        return self.get_visible_items()

    def last_page(self):
        self.current_index = self.total_pages - 1
        return self.get_visible_items()

    def next_page(self):
        if self.current_index == self.total_pages - 1:
            print("You at the last page")
            return self.get_visible_items()
        else:
            self.current_index += 1
            return self.get_visible_items()

    def previous_page(self):
        if self.current_index == 0:
            print("You at the first page")
            return self.get_visible_items()
        else:
            self.current_index -= 1
            return self.get_visible_items()

    def __str__(self):
        output_string = ""
        stat_index = self.current_index*self.page_size
        end_index = stat_index + self.page_size
        if end_index <= len(self.items):
            for character in self.items[stat_index:end_index]:
                output_string += character + "\n"
        else:
            for character in self.items[stat_index:]:
                output_string += character + "\n"
        return output_string


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

# p.go_to_page(10)
# print(p.get_visible_items())
print(p.current_index + 1)
# Output: 7

p.first_page()
p.previous_page()
print(str(p))