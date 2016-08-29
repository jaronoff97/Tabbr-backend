"""empty message

Revision ID: 47e14f991473
Revises: 8a27d0f019e6
Create Date: 2016-08-28 23:56:39.951319

"""

# revision identifiers, used by Alembic.
revision = '47e14f991473'
down_revision = '8a27d0f019e6'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('account_holder_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'accounts', ['account_holder_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'account_holder_id')
    ### end Alembic commands ###
