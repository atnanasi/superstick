# -*- coding: utf-8 -*-
import configparser

goods = configparser.ConfigParser()
goods.read('config/goods.ini', encoding="utf-8")

def main():
    print("Superstick v1.0")
    print("0:owari 1~:subtotal")

    while True:
        c = input("> ")
        if c=="0":
            print("OK-Woman")
            break

        else:
            if c in goods:
                pass


if __name__ == '__main__':
    main()