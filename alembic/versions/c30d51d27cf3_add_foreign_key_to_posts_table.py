"""add Foreign_Key to posts table

Revision ID: c30d51d27cf3
Revises: 7d79eef81e0b
Create Date: 2025-07-21 11:07:47.449167

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c30d51d27cf3'
down_revision: Union[str, Sequence[str], None] = '7d79eef81e0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk',source_table='posts',referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    """Upgrade schema."""
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    """Downgrade schema."""
    pass
