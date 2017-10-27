from sqlalchemy import create_engine
from .schemas import Base, Item, TransactionCharge, TransactionItem, Transaction

# initialize database
engine = create_engine('sqlite:///superstick.sqlite3', echo=True)
Base.metadata.create_all(engine)
