"""first migrations

Revision ID: 476d48834aa0
Revises: 8a0e7d386ea9
Create Date: 2025-02-17 16:44:44.619123

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '476d48834aa0'
down_revision: Union[str, None] = '8a0e7d386ea9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
