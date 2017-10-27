import ui

def payment():
    while True:
        items = {}

        # parse items
        for item in ui.question("Input items").split("+"):
            items[item.split("*")[0:]] = int(item.split("*")[1:]) if len(item.split("*"))==2 else 1

        itemdata = Call_itemdata(items)

        for item in itemdata:
            print("'{}'(¥{})x{}".format(item["name"], item["price"], item["number"]))

        if ui.isok("Is correct?"):
            break

    print("Subtotal:¥{}".format(get_subtotal(items)))

    while True:
        pay = int(ui.question("Pay"))

        change = pay - int(get_subtotal(items))

        print("Change:¥{}".format(change))
        
        if ui.isok("Is correct?"):
            break

    add_to_transaction_log()

def add_item():
    return

def get_items():
    return

def edit_item(item_id):
    return
