#!/usr/bin/env python
from fona800 import *
from phonebook import *
from colors import *
import sys
import os

menu_color = partial(color, fg='green', style='bold')
selection_color  = partial(color, fg='blue', style='bold+underline')


def main_menu ():
    os.system('clear')
    print (menu_color('''
    ################################################
    ################## SMS program #################
    ################################################
    ####                                        ####
    ####                                        ####
    ####      1) Send message                   ####
    ####      2) send sms to contact            ####
    ####      3) contacts                       ####
    ####      4) Read new messages              ####
    ####      5) Read all messages              ####
    ####      6) Delete a message               ####
    ####      7) check credit                   ####
    ####      99)Quit                           ####
    ####                                        ####
    ####                                        ####
    ####                                        ####
    ################################################
    ################################################
    '''))
    selection = input(selection_color('enter an option from menu : '))
    if selection == '1':#send sms
        os.system('clear')
        number = input('enter number to send sms to : ')
        message = input('enter message to send to ' + str(number) + ' : ')
        send(number,message)
        input('press enter to return to menu')
        main_menu()
    elif selection == '2':#send sms using contacts
        os.system('clear')
        view()
        id_no = input('enter contact id to send to : ')
        number = get_number(id=id_no)
        message = input('enter message to send to ' + str(number) + ' : ')
        send(number,message)
    elif selection == '3':#phonebook
        os.system('clear')
        phonebook_menu()
    elif selection == '4':#read new messsages
        os.system('clear')
        read_unread()
        input('press enter to return to menu')
        main_menu()
    elif selection == '5':#read all messages
        os.system('clear')
        read_all()
        input('press enter to return to menu')
        main_menu()
    elif selection == '6':#delete a message
        os.system('clear')
        delete_one()
        input('press enter to return to menu')
        main_menu()
    if selection == '7':#check credit
        os.system('clear')
#        credit()
        input('press enter to return to menu')
        main_menu()
    elif selection == '99':#exit program
        os.system('clear')
        raise SystemExit
    else:
        print(selection_color('enter a valid option from menu : '))
        main_menu()

def phonebook_menu ():
    os.system('clear')
    print (menu_color('''
    ################################################
    ################## SMS program #################
    ################################################
    ####                                        ####
    ####                                        ####
    ####      1) list contacts                  ####
    ####      2) search contact name            ####
    ####      3) add contact                    ####
    ####      4) update contact                 ####
    ####      5) Delete contact                 ####
    ####      6) Main Menu                      ####
    ####      99)Quit                           ####
    ####                                        ####
    ####                                        ####
    ################################################
    ################################################
    '''))
    selection = input(selection_color('enter an option from menu : '))
    if selection == '1':#list all contacts
        os.system('clear')
        view()
        input('press enter to return to menu')
        phonebook_menu()
    elif selection == '2':#search using contact name
        os.system('clear')
        name = input('enter contact name to find : ')
        find(name=name)
        input('press enter to return to menu')
        phonebook_menu()
    elif selection == '3':#add contact
        os.system('clear')
        name_opt = input('enter name for new contact : ')
        number_opt = input('enter number for new contact : ')
        add(name_opt,number_opt)
        print('new contact added')
        find(name=name_opt)
        input('press enter to return to menu')
        phonebook_menu()
    elif selection == '4':#update contact
        os.system('clear')
        view()
        id_opt = input('enter the Id number of contact you want to update : ')
        name_opt = input('enter name/new name for contact : ')
        number_opt = input('enter number/new number for contact : ')
        update(id_opt,name_opt,number_opt)
        print('contact updated')
        find(id=id_opt)
        input('press enter to return to menu')
        phonebook_menu()
    elif selection == '5':#delete contact
        os.system('clear')
        view()
        id_opt = input('enter id of contact you want to delete : ')
        find(id=id_opt)
        confirm = input('is this the contact you want to delete yes/no type [y/n] : ')
        while True:
            if confirm == 'y':
                delete(id_opt)
                break
            elif confirm == 'n':
                phonebook_menu()
                break
            else:
                confirm = input('type [y/n] y for to delete or n to return to menu!!! : ')
        input('press enter to return to menu')
        phonebook_menu()
    elif selection == '6':#main menu
        os.system('clear')
        main_menu()
    elif selection == '99':#exit program
        os.system('clear')
        raise SystemExit
    else:
        print(selection_color('enter a valid option from menu : '))
        main_menu()
main_menu()
