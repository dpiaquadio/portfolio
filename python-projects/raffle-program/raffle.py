#!usr/bin/python 

import string
import random

## Welcome to my Raffle program ##

# The object of this program is to randomly pick someone out of a list of people stored in 
# a file

## Ingredients ##
CHARS = string.ascii_uppercase + string.digits

def code_generator(chars, size):
    '''
    To make each user unique, a code will be generated at random
    '''
    return ''.join(random.choice(chars) for _ in range(size))

class Person_Info(object):
    '''
    This class will take care of creating a person object, adding the code associated
    with the person, and provide their email address.
    '''
    def __init__(self, name, email):
        self.code = code_generator(CHARS, 6)
        self.name = name
        self.email = email
      
    def format(self):
        '''
        Takes the person's information and makes it readable
        '''
        return "%s - %s - %s\n" % (self.code, self.name, self.email)
    
def add_person(person_info, source):
    '''
    When a user chooses to add a person to their list, this function will run until the user
    types 'no'
    '''
    s = source
    s.write(person_info)
    s.close()
    
    print "%s has been added to the raffle list!" % person_info.split(' - ')[1]

def choose_person(code, source):
    '''
    With the code provided as input, this function will iterate through each line until the
    person associated with the code matches.
    '''
    
    winner = ''
    source = open(source)
    for line in source.readlines():
        if code in line:
            winner = "Congratulations, %s! You've won!" % line.split(' - ')[1]
            print ""
    return winner

def options(choice):
    '''
    Depending on the choice made, the user can either run the add_person function or the
    choose_person function.  
    '''
    source_inquiry = raw_input("What is the name of your raffle list?: ")
    source = open(source_inquiry, 'a+')
    
    if choice == '1':
        name = raw_input("What is the name you wish to add?: ")
        email = raw_input("What is their email address?: ")
       
        person = Person_Info(name, email).format()
        
        add_person(person, source)
    
    elif choice == '2':
        code_list = []
        for i in source.readlines():
            decomp = i.split(' - ')
            code_list.append(decomp[0])
        source.close()
        chars = code_list
        code = code_generator(chars, 1)
        print "Looking for someone with code %s" % code
        print ""
        winner = choose_person(code, source_inquiry)
        print winner    

def main():
    print "Welcome to the Raffle Program!"
    print "Enter 1 if you'd like to add someone to your raffle list."
    print "Enter 2 if you wish to choose a random person"
     
    while 1:
        print ""
        choice = raw_input("Please enter 1 or 2 or type 'quit': ")
        
        if choice == 'quit':
            break
        elif choice == '1' or choice == '2':
            options(choice)
        else:
            print "Your choice is invalid, please press 1 or 2, or type exit: " 
main()   
            
    
        
    
    