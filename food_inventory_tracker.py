"""
With this food inventory tracker, users are able to add, remove, and query 
items. Each item stores the following attributes: location, quantity, and 
expiration date.
"""

#creates empty dictionary to store item names
items = {}

#creates empty dictionary to store locations and where items are stored
items_by_location = {}

#checks items in specific locations and prints full list of items in that location
def print_location():
    user_location = input("Please specify a location: ")
    if user_location in items_by_location: 
        for item in items_by_location[user_location]:
            print_item(item)
    else:
        print("This location does not exist in your inventory.")

#prints specific item and its attributes 
def print_item(item_to_check):
    if item_to_check in items:
        #prints item using syntax provided below
        print(item_to_check + 
              ": " + items[item_to_check]["location"] + 
              ", " + items[item_to_check]["quantity"] + 
              ", expires " + items[item_to_check]["expiration"])    
    else:
        print("This item does not exist in your inventory.")

#routes to functions that check list by location or specific item
def check_list():
    while True:
        user_response = input("Would you like to check inventory by location or item? ")
        if user_response == "location":
            print_location()
        elif user_response == "item":
            item_to_check = input("Please specify item name: ")
            print_item(item_to_check)
        else:
            print('Please specify either "location" or "item": ')
            user_response = input("Would you like to check inventory by location or item? ")
        #user is promted to confirm if they want to check inventory again before returning to main function
        check_list_again = input("Would you like to check your inventory again (yes or no)? ")
        if check_list_again == "no":
            break
        if check_list_again != "yes":
            print(str(check_list_again) + " is not a valid response.")

#user is prompted to specify item name to remove
def remove_item():
    while True:
        item_to_remove = input("Please enter item to remove: ")    
        #checks if item is in dictionary to prevent key error
        if item_to_remove in items:
            #creates item location variable by referencing items dictionary
            item_location = items[item_to_remove]['location']
            #removes item from items by location list
            items_by_location[item_location].remove(item_to_remove)
            #removes item from items dictionary
            del items[item_to_remove]
            print("This item has been removed from your inventory.")
        else:
            print("This item does not exist in your inventory.")
        #user is prompted to confim if they would like to remove another item 
        remove_again = input("Would you like to remove another item (yes or no)? ")
        if remove_again == "no":
            break
        if remove_again != "yes":
            print(str(remove_again) + " is not a valid response.")

#the functional information to add an item, separated from the loop for readability
def add_item():
    while True:
        #user is prompted to input item name and specify attributes -- attributes are added to a nested dictionary
        item_to_add = input("Please enter item name: ")
        items[item_to_add] = {"location" : " ", "quantity" : " ", "expiration" : " " }
        items[item_to_add]["location"] = input("Please enter location for " + str(item_to_add) + ": ")
        items[item_to_add]["quantity"] = input("Please enter quantity of " + str(item_to_add) + ": ")
        items[item_to_add]["expiration"] = input("Please enter expiration date for " + str(item_to_add) + ": ")

        #assigns variable for item location
        item_location = items[item_to_add]['location']
        #if the location already exists in the items by location dictionary, the item name is added to a list under that location
        if item_location in items_by_location:
            items_by_location[item_location].append(item_to_add)
        #else, the location is added to the dictionary and the item is added to a new list under that location
        else:
            items_by_location[item_location] = [item_to_add]
        #user is prompted to confirm if they would like to add another item
        add_item_again = input("Would you like to add another item (yes or no)? ")
        if add_item_again == "no":
            break
        if add_item_again != "yes":
            print(str(add_item_again) + " is not a valid response.")

def main():
    #prints welcome message
    print("Welcome to the food inventory tracker!")
    print()
    
    #while loop continues to prompt user to add, remove, or check items on list unless user selects to exit, which breaks the loop
    while True:    
        user_response = input("What would you like to do (add item, remove item, check list, exit & print)? ") 
        if user_response == "add item":
            add_item()
        elif user_response == "remove item":
            remove_item()
        elif user_response == "check list":
            check_list()
        elif user_response == "exit & print":
            break
        else:
            print('Please specify either "add item", "remove item", "check list", or "exit & print: ')

    #prints entire dictionary when user exits program
    print("Your food inventory:")
    for item in items:
        #uses print item function to match syntax to check list result
        print_item(item)

if __name__ == '__main__':
    main()