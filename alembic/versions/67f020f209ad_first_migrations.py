"""first migrations

Revision ID: 67f020f209ad
Revises: 476d48834aa0
Create Date: 2025-02-17 16:53:30.549949

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '67f020f209ad'
down_revision: Union[str, None] = '476d48834aa0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
