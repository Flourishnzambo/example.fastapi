"""add content coloumn to posts table

Revision ID: 476b4ad87e6f
Revises: 7db264d3acfe
Create Date: 2025-07-21 10:46:03.983341

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '476b4ad87e6f'
down_revision: Union[str, Sequence[str], None] = '7db264d3acfe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    """Downgrade schema."""
    pass
