# -*- coding: utf-8 -*-
import sys
import controller

args = sys.argv

def main():
    if args[1]=="start":
        payment()

    elif args[1]=="add":
        add_item()

    elif args[1]=="items":
        print(get_items)

    elif "item@" in args[1]:
        edit_item(args[1].split("@")[1:])

    else:
        print("superstick: start,item,items,item@%n")

if __name__ == '__main__':
    main()