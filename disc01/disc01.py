def evens(list_of_ints):
    """Returns a copy of the list but keeping only the even numbers."""
    return_list = []
    for num in list_of_ints:
        if num % 2 == 0:
            return_list.append(num)
    return return_list


def count_words(list_of_words):
    """Returns a map from each word to its count."""
    counts = {}


class Dog:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return "Dog({}, {})".format(self.name, self.size)

    
dogs = [Dog("maya", 1000), Dog("yipster", 5), Dog("scott", 25)]
print(dogs[0])

