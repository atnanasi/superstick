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
        print('\n'.join(['[{}] 名称: {}, 価格: {}'.format(item.id, item.name, item.price) for item in get_items()]))

    elif "item@" in args[1]:
        controller.edit_item(args[1].split("@")[1:])

    else:
        print("superstick: start,item,items,item@%n")

if __name__ == '__main__':
    main()