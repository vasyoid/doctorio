"""add feedback table

Revision ID: 879f54af1ebc
Revises: 9c70fdb4c701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '879f54af1ebc'
down_revision = '9c70fdb4c701'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "feedback",
        sa.Column("doctor", sa.Integer, nullable=False),
        sa.Column("rating", sa.Integer(), nullable=True),
        sa.Column("comment", sa.Unicode(), nullable=True),
        sa.ForeignKeyConstraint(("doctor",), ("doctors.id",)),
    )


def downgrade():
    op.drop_table("feedback")
