"""Subscriptions

Revision ID: b426d1c44a2f
Revises: 0a35e082e772
Create Date: 2021-03-06 20:46:57.232775

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'b426d1c44a2f'
down_revision = '0a35e082e772'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "subscription",
        sa.Column("id", sa.String, primary_key=True),
        sa.Column("email", sa.String, index=True),
        sa.Column("district", sa.String, nullable=False),
    )
    op.create_foreign_key(
        constraint_name="subscription_emails_address_fk",
        source_table="subscription",
        referent_table="email",
        local_cols=["email"],
        remote_cols=["address"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint(
        constraint_name="subscription_emails_address_fk",
        table_name="subscription",
        type_="foreignkey"
    )
    op.drop_table("subscription")
