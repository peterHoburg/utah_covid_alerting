"""schools_cases

Revision ID: be6d854f6fed
Revises: b426d1c44a2f
Create Date: 2021-03-09 02:18:36.353213

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'be6d854f6fed'
down_revision = 'b426d1c44a2f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "schools_cases",
        sa.Column("district", sa.String, index=True, nullable=False),
        sa.Column("date", sa.Date, index=True, nullable=False),
        sa.Column("jurisdiction", sa.String, nullable=False),
        sa.Column("active_cases", sa.Integer, nullable=False),
        sa.Column("total_case", sa.Integer, nullable=False),
        sa.PrimaryKeyConstraint("district", "date", name="pk_schools_cases")
    )
    op.create_table(
        "data_fetch_job",
        sa.Column("date", sa.Date, primary_key=True),
        sa.Column("fetched", sa.Boolean, default=False, nullable=False),
        sa.Column("error", sa.String, nullable=True)
    )


def downgrade():
    op.drop_table("data_fetch_job")
    op.drop_table("schools_cases")
