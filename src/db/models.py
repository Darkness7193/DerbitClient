from decimal import Decimal

from sqlalchemy import BigInteger, Integer, Numeric, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase): pass


class TickerData(Base):
    __tablename__ = 'tickers_data'

    id:      Mapped[int] =     mapped_column(Integer, primary_key=True, autoincrement=True)
    ticker:  Mapped[str] =     mapped_column(String, nullable=False)
    btc_usd: Mapped[Decimal] = mapped_column(Numeric(20, 8), nullable=False)
    eth_usd: Mapped[Decimal] = mapped_column(Numeric(20, 8), nullable=False)
    timestamp:    Mapped[int] =     mapped_column(BigInteger, nullable=False)

    def __repr__(self):
        return f'{self.ticker}'

