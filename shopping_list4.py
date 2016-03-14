shopping_list = []
def remove_item(idx):
    index = idx-1
    item = shopping_list.pop(index)
    print("Removed {}".format(item))

def show_help():
    print("Separate each item with a comma \n")
    print("DONE to finish, REMOVE to remove an item with its index, HELP for this method and SHOW for the list")

def show_list():
    count = 1
    for item in shopping_list:
        print("{}: {} ".format(count, item))
        count += 1

print("Enter a list of things you need")
show_help()

while True:
    new_stuff = input("> ")

    if new_stuff == 'DONE':
        print("Here's your list \n")
        show_list()
        break
    elif new_stuff == 'HELP':
        show_help()
        continue
    elif new_stuff == 'SHOW':
        show_list()
        continue
    elif new_stuff == "REMOVE":
        show_list()
        idx = input("Which item number: ")
        remove_item(int(idx))
    else:
        new_list = new_stuff.split(",")
        index = input("Add at certain place? currently {} ".format(len(shopping_list)))
        if index:
            spot = int(index) - 1
            for item in new_list:
                shopping_list.insert(spot, item.strip())
                spot += 1
        else:
            for item in new_list:
                shopping_list.append(item.strip())
