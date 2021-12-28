"""add tasks

Revision ID: 77f8b9931f59
Revises: 4f385b4c1265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77f8b9931f59'
down_revision = '4f385b4c1265'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer, nullable=False),
        sa.Column("hospital", sa.Unicode(), nullable=True),
        sa.Column("address", sa.Unicode(), nullable=True),
        sa.Column("name", sa.Unicode(), nullable=True),
        sa.Column("surname", sa.Unicode(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "done_tasks",
        sa.Column("id", sa.Integer, nullable=False),
        sa.Column("customer", sa.Integer, nullable=False),
        sa.Column("verdict", sa.Boolean, nullable=True),
        sa.ForeignKeyConstraint(("id",), ("tasks.id",)),
        sa.ForeignKeyConstraint(("customer",), ("customers.id",)),
        sa.PrimaryKeyConstraint("id", "customer"),
    )


def downgrade():
    op.drop_table("tasks")
    op.drop_table("done_tasks")
