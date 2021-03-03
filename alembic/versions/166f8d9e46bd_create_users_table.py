"""create users table

Revision ID: 166f8d9e46bd
Revises:
Create Date: 2021-02-22 01:28:36.291735

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '166f8d9e46bd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "user",
        sa.Column("username", sa.String, primary_key=True),
        sa.Column("full_name", sa.String),
        sa.Column("email", sa.String),
        sa.Column("password", sa.String),
        sa.Column("enabled", sa.Boolean, default=True)
    )


def downgrade():
    op.drop_table("user")
