#make a list to hold onto items
shopping_list = []
#print instructions on how to use app
def show_help():
    print("Whatchu need foodwize")
    print("""
You have reached help, enter items that you would like to add, enter SHOW to see your current list or enter DONE to quit.
    """)

def show_list():
    print("Here is your list: ")
    for item in shopping_list:
        print(item)

def add_to_list():
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))
    
show_help()

while True:
    #ask for new items
    new_item = input("> ")
    #quit app
    if new_item == 'Done':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)
    show_list()
