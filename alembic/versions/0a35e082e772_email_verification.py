"""Email verification

Revision ID: 0a35e082e772
Revises: 166f8d9e46bd
Create Date: 2021-03-03 05:07:03.118654

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '0a35e082e772'
down_revision = '166f8d9e46bd'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "email",
        sa.Column("address", sa.String, primary_key=True),
        sa.Column("uuid", sa.String, index=True),
        sa.Column("verified", sa.Boolean, default=False),
        sa.Column("verification_string", sa.String, nullable=False),
    )
    op.create_foreign_key(
        constraint_name="user_emails_address_fk",
        source_table="user",
        referent_table="email",
        local_cols=["email"],
        remote_cols=["address"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint(
        constraint_name="user_emails_address_fk",
        table_name="user",
        type_="foreignkey"
    )
    op.drop_table("email")
