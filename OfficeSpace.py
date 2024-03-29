#  File: OfficeSpace.py

#  Description: set up a system to let employees make their cubicle space request

#  Student Name: Thuy Nguyen

#  Student UT EID: thn556

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 50210

#  Date Created: September 20th, 2019

#  Date Last Modified:

def total_area(w, h):
    return w * h

def main():

    # reading the file
    with open("office.txt") as file:
        lines = file.readlines()
    lines = [line.replace("\n", "") for line in lines]
    print(lines)

    n = 5   # line num for each test case
    lines = [lines[i * n:(i + 1) * n] for i in range((len(lines) + n - 1) // n)]
    print(lines)



main()