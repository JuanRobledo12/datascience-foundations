'''
Area Calculator
Python is especially useful for doing math and can be used to automate many calculations. 
In this project, we’ll create a calculator that can compute the area of the following shapes:

Circle
Triangle
The program should do the following:

Prompt the user to select a shape.
Calculate the area of that shape.
Print the area of that shape to the user.
Let’s begin!
'''

import math

def get_data_from_user():

    while True:
        figure_type = input('Please input the figure type, C for Circle and T for Triangle:\n')
        if figure_type == 'C' or figure_type == 'T':
            break
        else:
            print('Invalid Input...')
    return figure_type

def get_area(figure_type):
    
    if figure_type == 'C':
        r = int(input("What's the circle's radius?\n"))
        calc_area = math.pi * (r**2)
        print(f'the area of the Circle is: {calc_area}')
    
    elif figure_type == 'T':
        b = int(input("What's the Triangle's base value?\n"))
        h = int(input("What's the Triangles height?\n"))
        calc_area = (1/2) * b *h
        print(f'the area of the Triangle is: {calc_area}')
    
    return calc_area


print('Welcome to the area calculator program!')
while True:
    figure_type = get_data_from_user()
    area = get_area(figure_type)
    continue_q = input('Do you want to input another figure (yes/no):\n')
    if continue_q == 'no':
        break
    else:
        continue






