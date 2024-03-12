# Description: This program allows users to choose what happens to a list based on menu options.

# Constants for the menu choices
DISPLAY_THE_LIST = 1
ADD_TO_LIST = 2
DELETE_FROM_LIST = 3
CHANGE_LIST_ITEM = 4
SORT_THE_LIST = 5
QUIT_CHOICE = 6

#Main Function
def main():
    
    #Create a list of programming classes
    classes = ['Java', 'C#', 'COBOL', 'Mobile Apps', 'VB', 'JSP']
    
    #Choice Variable Controls the loop
    choice = 0
    
    #Loop
    while choice != QUIT_CHOICE:
        
        #Display the menu
        display_menu()
    
        #Get the user's choice
        choice = int(input('Enter your choice: '))
    
        #Perform the selected action
        if choice == DISPLAY_THE_LIST:
            newList = display_list(classes)
        
        elif choice == ADD_TO_LIST:
            classes = addTo_list(classes)
        
        elif choice == DELETE_FROM_LIST:
            classes = deleteFrom_list(classes)
        
        elif choice == CHANGE_LIST_ITEM:
            classes = change_list(classes)
        
        elif choice == SORT_THE_LIST:
            classes = sort_list(classes)
        
        elif choice == QUIT_CHOICE:
            print('Exit the program')
        
        else:
            print('\n')
            print('Error: invalid selection')
            print('\n')
        
# This function displays a menu for the user to pick from.
def display_menu():
    print('      MENU')
    print('1) Display the list')
    print('2) Add to the list')
    print('3) Delete from the list')
    print('4) Change a list item')
    print('5) Sort the list item')
    print('6) Quit')
    print('\n')

#Display list of classes
def display_list(classes):
    print('\n')
    print('Here are the items in the class list: ')
    print(classes)
    print('\n')
     
#Add to the list
def addTo_list(classes):
    new_Class = input('Enter a class to add to class list: ')
    classes.append(new_Class)
    print('\n')
    print(new_Class, 'Added to the list')
    print('\n')
    return classes
    
#Delete from classes list
def deleteFrom_list(classes):
    item = input('Which item should I remove? ')
    item_index = classes.index(item)
    del classes[item_index]
    print('\n')
    print(item, 'removed from list')
    print('\n')
    return classes
    
#Change a list item
def change_list(classes):
    progIndex = input('Which class would you like to change? (Example VB): ')
    item_index = classes.index(progIndex)
    new_class = input('Enter new value: ')
    classes[item_index] = new_class
    print('\n')
    print(progIndex,'Replaced with ', new_class)
    print('\n')
    return classes
    

#Display Sorted list
def sort_list(classes):
    classes.sort()
    return classes

main()
    