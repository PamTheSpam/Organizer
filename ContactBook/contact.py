#!/usr/bin/python3

from os import name
import click
import time, pyautogui
from click.decorators import command
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

@click.command()
@click.argument('name')

def main(name):

    Name = name.upper()

        # Turns the elements for the text file into a python list

    f = open("D:\Misc\MyProjects\ContactBook\contacts.txt")
    contact = f.readlines()
    Contacts = [x.replace('\n', '') for x in contact]    

        # Makes a new list without the \n 
    
        

    if Name in Contacts:
        IndexPosOfName = Contacts.index(Name)
        IndexPosOfNumb = IndexPosOfName + 1
        NameOfTheContact = Contacts[int(IndexPosOfName)]
        NumOfContact = Contacts[IndexPosOfNumb]
            
        click.echo(NameOfTheContact)
        click.echo(NumOfContact)

        # Checks if the name you entered is in the list of contacts

    if Name not in Contacts:
        print("The name is not in contacts.txt")

main()

