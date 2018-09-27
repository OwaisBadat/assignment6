
#shopping list
class Shopping_list:
    def __init__(self, title, description, grocery_items):
        self.title = title
        self.description = description
        self.grocery_items = grocery_items

    def display_list(self):
        print("-" * 10)
        print("{0} grocery list:\n".format(self.title))
        for items in self.grocery_items:
            print("->",items)

class Grocery_item:
    def __init__(self, item_name):
        self.item_name = item_name

    def __repr__(self):
        return self.item_name



while True:

    print("Menu List:")
    print("-" * 10)
    print("Press 'N' to create new list")
    print("Press 'A' to access existing list")
    print("Press 'D' to display lists")
    print("Press 'Q' to quit")
    print("-" * 10)

    choice = input("Enter a letter corresponding to the function you would like to perform:  ").lower()
    if choice == 'q':
        print("-" * 10)
        print('Goodbye!')
        print("-" * 10)
        break

    elif choice == 'n':
        print("-" * 10)
        title = input("Enter title of list: ")
        description = input("Enter description of list: ")
        print("-" * 10)
        shopping_lists.append(Shopping_list(title, description, []))
        list_index = len(shopping_lists) - 1
        add_item(list_index)

    elif choice == 'd':
        print("-" * 10)
        if len(shopping_lists) == 0:
            print("There are no lists!")
        else:
            display_all_lists()

    elif choice == 'a':
        print("-" * 10)
        if len(shopping_lists) == 0:
            print("There are no lists!")
        else:
            display_all_lists()
