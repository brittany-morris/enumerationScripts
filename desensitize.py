#!/usr/bin/env python3

import sys

def remove_brackets_from_list(file_name):

    try:

        with open(file_name, 'r') as file:
            lines = file.readlines()


        modified_lines = [line.replace('[', '').replace(']','')for line in lines]

        with open(file_name, 'w') as file:
            file.writelines(modified_lines)

        print("brackets removed")

    except FileNotFoundError:
        print(f"file not found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py file_name")
    else:
        file_name = sys.argv[1]
        remove_brackets_from_list(file_name)
