"""empty message

Revision ID: 764062616ab2
Revises: adf703b2f7b1
Create Date: 2022-08-13 15:10:53.749944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '764062616ab2'
down_revision = 'adf703b2f7b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('complete', sa.Boolean(), nullable=False))
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.BOOLEAN(), autoincrement=False, nullable=False))
    op.alter_column('todos', 'list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.drop_column('todos', 'complete')
    # ### end Alembic commands ###
