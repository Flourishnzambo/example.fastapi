"""add users table

Revision ID: 7d79eef81e0b
Revises: 476b4ad87e6f
Create Date: 2025-07-21 10:54:45.994921

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d79eef81e0b'
down_revision: Union[str, Sequence[str], None] = '476b4ad87e6f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table (
        "users",
        sa.Column("id", sa.Integer(), nullable=False, ),
        sa.Column("email", sa.String(), nullable=False, ),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("created_at", sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email")
        )
        
    
   
    pass


def downgrade() -> None:
    op.drop_table("users")
    """Downgrade schema."""
    pass
