store_name = []

class ListManager:
    def __init__(self):
        self.grocery_lists = {}
        self.grocery_items = []
        self.new_list_name = ""

    def user_options(self):

        print("Menu: ")
        print('-' * 10 )
        print("Press 'N' to create new list")
        print("Press 'A' to access existing list")
        print("Press 'D' to display lists:")
        print("Press 'Q' to quit:")
        print('-' * 10 )
        choice = input(" Press 'N'. to create a new list, Press 'A'. to add a new item to the current list, Press 'D'. to view your current lists, Press 'Q' to quit the application: ").upper()

        if (choice == 'N'):
            print('-' * 10 )
            self.create_new_list()

        if (choice == 'A'):
            if (self.new_list_name == ""):
                print('-' * 10 )
                print("No list to add the items to. Please create a new list.")
                print('-' * 10 )
                self.user_options()
            else:
                self.add_items_to_list(self.new_list_name)

        if (choice == 'D'):
            print('-' * 10 )
            self.view_list()

        if (choice == 'Q'):
            print('-' * 10 )
            print("Goodbye")
            exit()

        else:
            print("That is an invalid option.")
            print('-' * 10 )
            self.user_options()

    def create_new_list(self):

        new_list_name = input("Enter tile of new list: ")
        if (new_list_name == 'q'):
            print("Goodbye")
            exit()


        self.grocery_lists[new_list_name] = []
        self.add_items_to_list(new_list_name)

T
    def add_items_to_list(self, new_list_name):
        self.new_list_name = new_list_name
        item = input("Enter grocery item: ")
        self.grocery_lists[self.new_list_name].append(item)
        
        if (item == "q"):
            self.grocery_lists[self.new_list_name].remove(item)
            dictionary_list = self.grocery_items
            print(self.grocery_lists)
            self.user_options()

        self.add_items_to_list(self.new_list_name)

    def view_list(self):
        print(self.grocery_lists)

        self.user_options()




list_manager = ListManager()
list_manager.user_options()
