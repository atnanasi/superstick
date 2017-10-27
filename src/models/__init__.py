from .schemas import Base, Item, TransactionCharge, TransactionItem, Transaction

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from uuid import uuid4 as uuid
from datetime import datetime

from typing import List

# initialize database
engine = create_engine('sqlite:///superstick.sqlite3')
Base.metadata.create_all(engine)

# Session sub-class
Session = sessionmaker(bind=engine)


def add_item (name: str, price: int) -> int:
  session = Session()

  item = Item(name=name, price=price)

  session.add(item)
  session.commit()

  id = item.id

  session.close()

  return id


def get_items () -> List[Item]:
  session = Session()

  query = session.query(Item)
  results = query.all()

  session.close

  return results


def find_items_by_id (ids: tuple) -> List[Item]:
  session = Session()

  query = session.query(Item).filter(Item.id.in_(ids))
  results = query.all()

  session.close()

  return results


# () -> id
def start_transaction () -> str:
  session = Session()
  id = str(uuid())

  transaction = Transaction(id=id, datetime=datetime.now())

  session.add(transaction)
  session.commit()
  session.close()

  return id


# (transactionID, itemID)
def add_items_to_transaction (transaction: str, items: List[int]) -> None:
  session = Session()

  tis = [TransactionItem(id=str(uuid()), transaction=transaction, item=item) for item in items]

  session.add_all(tis)

  session.commit()
  session.close()


def get_subtotal_of_transaction (transaction: str) -> int:
  session = Session()

  query = session.query(TransactionItem).filter_by(transaction=transaction)
  results = query.all()

  subtotal = sum([result.Item.price for result in results])

  session.commit()
  session.close()

  return subtotal

def end_transaction (transaction: str, amount: int, receipt: int = None, charge: int = None) -> None:
  session = Session()

  tc = TransactionCharge(id=str(uuid()), amount=int, receipt=receipt, charge=charge)

  session.add(tc)

  session.commit()
  session.close()
