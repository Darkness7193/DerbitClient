from alembic import op
import sqlalchemy as sa


revision = "9a4eaeebee55"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "tickers_data",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("ticker", sa.String(), nullable=False),
        sa.Column("btc_usd", sa.Numeric(20, 8), nullable=False),
        sa.Column("eth_usd", sa.Numeric(20, 8), nullable=False),
        sa.Column("timestamp", sa.BigInteger(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )


def downgrade() -> None:
    op.drop_table("tickers_data")