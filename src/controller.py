import ui

from models import add_item as m_add_item, find_items_by_id, start_transaction, add_items_to_transaction, get_amount_of_transaction, end_transaction

def payment():
    print('* On your mark...')
    while True:
        items = {}

        # parse items
        for item in ui.question("Input items").split("+"):
            its = item.split("*")
            items[its[0]] = int(its[1]) if len(its)==2 else 1

        item_keys = items.keys()
        itemdata = find_items_by_id(item_keys)

        if (len(item_keys) is not len(itemdata)):
            ui.warn('something went wrong, there are no items that has some IDs. please re-input.')
            continue

        ui.info('\n'.join([
            "'{}' (¥{}) x{}".format(item.name, item.price, items[str(item.id)])
            for item in itemdata
        ]))

        if ui.isok("Is correct?"):
            break

    tran_id = start_transaction()
    ui.info("start transaction (tran_id: {})".format(tran_id))

    tran_item_ids = []
    for k, v in items.items():
        tran_item_ids += [k] * v

    add_items_to_transaction(tran_id, tran_item_ids)

    amount = get_amount_of_transaction(tran_id)
    ui.info("Amount: ¥{}".format(amount))

    while True:
        receipt = int(ui.question("Receipt?"))

        change = receipt - amount

        if (0 > change):
            ui.warn('change is minus or not number, re-input or request re-payment.')
            continue

        ui.info("Change: ¥{}".format(change))
        
        if ui.isok("receipt amount and give change?"):
            break

    end_transaction(tran_id, amount, receipt, change)

    ui.info('end transaction (tran_id: {})'.format(tran_id))

def add_item():
    while True:
        name = ui.question('Name?')
        price = int(ui.question('Price?'))

        if (0 > price):
            ui.warn('price is minus or not number.')
            continue

        ui.info("{} (¥{})".format(name, price))
        if ui.isok("Is correct?"):
            break

    m_add_item(name, price)
