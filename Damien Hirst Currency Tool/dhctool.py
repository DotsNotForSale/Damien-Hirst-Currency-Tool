import os

import pyfiglet
from termcolor import cprint
import questionary
import json

# Get the current directory that this file exists in.
this_dir = os.path.dirname(os.path.abspath(__file__))
# Get paths for all files
files = [
    os.path.join(this_dir, 'Alphabetically Ascending.txt'),
    os.path.join(this_dir, 'Characters Ascending.txt'),
    os.path.join(this_dir, 'Alphabetically Descending.txt'),
    os.path.join(this_dir, 'Characters Descending.txt'),
    os.path.join(this_dir, 'Ordered List.txt'),
    os.path.join(this_dir, 'Density.txt'),
    os.path.join(this_dir, 'Drips.txt'),
    os.path.join(this_dir, 'Weight.txt'),
    os.path.join(this_dir, 'Overlaps.txt'),
    os.path.join(this_dir, 'Red.txt'),
    os.path.join(this_dir, 'Blue.txt'),
    os.path.join(this_dir, 'Yellow.txt'),
    os.path.join(this_dir, 'Green.txt'),
    os.path.join(this_dir, 'Magenta.txt'),
    os.path.join(this_dir, 'White.txt'),
    os.path.join(this_dir, 'Black.txt'),
    os.path.join(this_dir, 'info.txt')
]

with open(os.path.join(this_dir, 'list.json'), 'r') as f:
    list_obj = json.load(f)

# This is a helper function for questionary.select
# It will return the index of the selection rather
# than the selection itself.
def ask_select(prompt : str, choices : list) -> int:
    result = questionary.select(prompt, choices).ask()
    return choices.index(result)

# This is a helper function to read an integer from
# terminal
# If the user does not input an integer, it will try
# again.
def prompt_num(prompt : str, min=None, max=None):
    # Check if the last character is ':'
    # If not, add ':'.
    if prompt[-1] != ':':
        prompt += ':'
    while True:
        result = input(prompt)
        if result.isdigit():
            num = int(result, base=10)
            failed = False
            if type(min) is int and num < min:
                failed = True
            if type(max) is int and num > max:
                failed = True
            if not failed:
                return num

# This is a helper function for questionary to
# confirm selection
# it will return either True (Yes) or False (No)
def confirm_select(prompt : str = 'Are you sure?'):
    return questionary.select(prompt, ['Yes', 'No']).ask() == 'Yes'

def view_search(search_result):
    print(f'{search_result["ID"]:05d}: "{search_result["Title"]}" | {search_result["URL"]}')

def search_id():
    search_id = prompt_num('Enter an ID between 1 and 10,000', 1, 10000)
    search_result = list_obj[search_id - 1]
    view_search(search_result)

def search_title():
    keys = input('Enter search term:').lower().split(' ')
    results = []
    for i, v in enumerate(list_obj):
        match = 0
        for k in keys:
            if k in v['Search']:
                match += 1
            else:
                break
        if match == len(keys):
            results.append(v)
    print('═════════════█ SEARCH RESULTS █═════════════\n')
    for res in results:
        view_search(res)
    print('\n═════════════█ END SEARCH RESULTS █═════════════')
        

def search_tender():
    result = ask_select('What would you like to search?', [' ID', ' Title'])
    # result is 'ID'
    if result == 0:
        search_id()
    # result is 'Title'
    elif result == 1:
        search_title()

def view_list():
    options = [
        '╔ Top 100 Alphbetical Least',
        '╠ Top 100 Character Count Least',
        '╠ Top 100 Alphabetical Most',
        '╠ Top 100 Character Count Most',
        '╠ Top 100 Ordered List',
        '╠ Top 10 Density',
        '╠ Top 10 Drips',
        '╠ Top 10 Weight',
        '╠ Top 10 Overlaps',
        '╠ Top 10 Red',
        '╠ Top 10 Blue',
        '╠ Top 10 Yellow',
        '╠ Top 10 Green',
        '╠ Top 10 Magenta',
        '╠ Top 10 White',
        '╠ Top 10 Black',
        '╚ Info'
        
    ]
    choice = ask_select('Choose a list to view.', options)
    file_path = files[choice]
    # There are better ways to view these lists.
    with open(file_path, 'r', encoding='utf-8') as fin:
        print(fin.read())

# This is the main entry point for this script.
def main():
    
    cprint(pyfiglet.figlet_format("            DH Currency"), 'red')
    cprint(pyfiglet.figlet_format("                             Tool"), 'white')
    print("\n")
    cprint(' • • • • • • • • • • • Made With <3 by DotsNotForSale • • • • • • • • • • •', 'white', 'on_red')

    # Create options for main menu
    main_options = [
        'Search for a Tender',
        'View a List',
        'Exit Program'
    ]

    confirm_options = ['Yes', 'No']

    break_condition = False
    # Loop forever (but not really, because a menu option will allow exiting)
    while not break_condition:
        choice = ask_select('\nWhat would you like to do?\n', main_options)
        # choice is 2 which means 'Exit Program'
        if choice == 2:
            # We confirm with the user that they would like to exit.
            if confirm_select('Are you sure you would like to Exit?'):
                break
        # choice is 'Search for a Tender'
        elif choice == 0:
            search_tender()
        # choice is 'View a List'
        elif choice == 1:
            view_list()

# We check if __name__ is '__main__', which means that this
# script was called from the command line rather than imported
if __name__ == '__main__':
    # call main(), that's it.
    main()


    # <3 DotsDotsDots 