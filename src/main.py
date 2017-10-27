# -*- coding: utf-8 -*-
import sys
import controller

from models import get_items

args = sys.argv

def main():
    if args[1]=="start":
        while True:
            controller.payment()

    elif args[1]=="add":
        controller.add_item()

    elif args[1]=="items":
        print('\n'.join(['[{}] {} (¥{})'.format(item.id, item.name, item.price) for item in get_items()]))

    else:
        print("superstick: start, add, items")

if __name__ == '__main__':
    main()