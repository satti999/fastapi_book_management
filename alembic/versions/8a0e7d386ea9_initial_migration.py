from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa  # ✅ Import SQLAlchemy instead of sqlmodel

# revision identifiers, used by Alembic.
revision: str = '8a0e7d386ea9'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=False),  # ✅ Use sa.String()
        sa.Column('email', sa.String(), nullable=False),  # ✅ Use sa.String()
        sa.Column('password', sa.String(), nullable=False),  # ✅ Use sa.String()
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)

    op.create_table('book',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('title', sa.String(), nullable=False),  # ✅ Use sa.String()
        sa.Column('author', sa.String(), nullable=False),  # ✅ Use sa.String()
        sa.Column('description', sa.String(), nullable=True),  # ✅ Use sa.String()
        sa.Column('cover_image', sa.String(), nullable=True),  # ✅ Use sa.String()
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
