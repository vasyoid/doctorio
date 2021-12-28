"""add doctors and hospitals

Revision ID: 9c70fdb4c701
Revises: 

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c70fdb4c701'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "hospitals",
        sa.Column("id", sa.Integer, nullable=False),
        sa.Column("name", sa.Unicode(), nullable=True),
        sa.Column("address", sa.Unicode(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "doctors",
        sa.Column("id", sa.Integer, nullable=False),
        sa.Column("hospital", sa.Integer, nullable=False),
        sa.Column("name", sa.Unicode(), nullable=True),
        sa.Column("surname", sa.Unicode(), nullable=True),
        sa.Column("cost", sa.Integer, nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(("hospital",), ("hospitals.id",))
    )
    op.create_table(
        "competences",
        sa.Column("doctor", sa.Integer, nullable=False),
        sa.Column("title", sa.Unicode(), nullable=True),
        sa.ForeignKeyConstraint(("doctor",), ("doctors.id",))
    )


def downgrade():
    op.drop_table("hospitals")
    op.drop_table("doctors")
    op.drop_table("competences")
