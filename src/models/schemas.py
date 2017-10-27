from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Item(Base):
    __tablename__ = 'Items'

    id = Column(Integer, primary_key=True)
    name = Column(String(2000), nullable=False)
    price = Column(Integer, nullable=False)


class TransactionCharge(Base):
    __tablename__ = 'TransactionCharges'

    id = Column(String(36), primary_key=True)
    amount = Column(Integer, nullable=False)
    receipt = Column(Integer)
    change = Column(Integer)
    transaction = Column(ForeignKey('Transactions.id'), nullable=False, index=True)

    Transaction = relationship('Transaction')


class TransactionItem(Base):
    __tablename__ = 'TransactionItems'

    id = Column(String(36), primary_key=True)
    item = Column(ForeignKey('Items.id'), nullable=False, index=True)
    transaction = Column(ForeignKey('Transactions.id'), nullable=False, index=True)

    Item = relationship('Item')
    Transaction = relationship('Transaction')


class Transaction(Base):
    __tablename__ = 'Transactions'

    id = Column(String(36), primary_key=True)
    datetime = Column(DateTime, nullable=False)
