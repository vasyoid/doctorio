"""add customer and slots tables

Revision ID: 4f385b4c1265
Revises: 879f54af1ebc

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f385b4c1265'
down_revision = '879f54af1ebc'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "customers",
        sa.Column("id", sa.Integer, nullable=False),
        sa.Column("name", sa.Unicode(), nullable=True),
        sa.Column("surname", sa.Unicode(), nullable=True),
        sa.Column("misses", sa.Integer, nullable=True),
        sa.Column("bonuses", sa.Integer, nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "free_slots",
        sa.Column("doctor", sa.Integer, nullable=False),
        sa.Column("timestamp", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(("doctor",), ("doctors.id",)),
        sa.PrimaryKeyConstraint("doctor", "timestamp"),
    )
    op.create_table(
        "busy_slots",
        sa.Column("doctor", sa.Integer, nullable=False),
        sa.Column("customer", sa.Integer, nullable=False),
        sa.Column("timestamp", sa.Integer, nullable=False),
        sa.ForeignKeyConstraint(("doctor",), ("doctors.id",)),
        sa.ForeignKeyConstraint(("customer",), ("customers.id",)),
        sa.PrimaryKeyConstraint("doctor", "timestamp"),
    )


def downgrade():
    op.drop_table("customers")
    op.drop_table("free_slots")
    op.drop_table("busy_slots")
