import ui

from models import add_item as m_add_item, find_items_by_id, start_transaction, add_items_to_transaction, get_amount_of_transaction, end_transaction

def payment():
    print('> payment')
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
    print("start transaction (tran_id: {})".format(tran_id))

    tran_item_ids = []
    for k, v in items.items():
        tran_item_ids += [k] * v

    add_items_to_transaction(tran_id, tran_item_ids)

    amount = get_amount_of_transaction(tran_id)
    print("Amount: ¥{}".format(amount))

    while True:
        receipt = int(ui.question("Receipt?"))

        change = receipt - amount

        if (0 > change):
            print('! change is minus or not number, re-input or request re-payment.')
            continue

        print("Change: ¥{}".format(change))
        
        if ui.isok("Is correct?"):
            break

    end_transaction(tran_id, amount, receipt, change)

    print('end transaction (tran_id: {})'.format(tran_id))

def add_item():
    while True:
        name = ui.question('Name?')
        price = int(ui.question('Price?'))

        if (0 > price):
            print('! price is minus or not number.')
            continue

        print("{} (¥{})".format(name, price))
        if ui.isok("Is correct?"):
            break

    m_add_item(name, price)
