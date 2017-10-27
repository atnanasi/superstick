import ui

from models import add_item, find_items_by_id, start_transaction, add_items_to_transaction, get_subtotal_of_transaction

def payment():
    while True:
        items = {}

        # parse items
        for item in ui.question("Input items").split("+"):
            its = item.split("*")
            items[its[0]] = int(its[1]) if len(its)==2 else 1

        itemdata = find_items_by_id(items.keys())

        print('\n'.join([
            "'{}' (¥{}) x{}".format(item.name, item.price, items[str(item.id)])
            for item in itemdata
        ]))

        if ui.isok("Is correct?"):
            break

    tran_id = start_transaction()
    print("tran_id: {}".format(tran_id))

    tran_item_ids = []
    print(items)
    for k, v in items.items():
        tran_item_ids += [k] * v


    add_items_to_transaction(tran_id, tran_item_ids)

    print("Subtotal: ¥{}".format(get_subtotal_of_transaction(tran_id)))

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
