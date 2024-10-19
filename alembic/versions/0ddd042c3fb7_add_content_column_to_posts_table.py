"""add content column to posts table

Revision ID: 0ddd042c3fb7
Revises: 4da4381a555e
Create Date: 2024-10-19 14:17:16.165943

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0ddd042c3fb7'
down_revision: Union[str, None] = '4da4381a555e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column("posts", "content")
    pass
