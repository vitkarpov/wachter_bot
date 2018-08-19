"""add on kick message

Revision ID: 2345e3de1ccc
Revises: ae0105c2205b
Create Date: 2018-08-19 18:19:30.031804

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2345e3de1ccc'
down_revision = 'ae0105c2205b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chats', sa.Column('on_kick_message', sa.Text(), nullable=False, server_default=''))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chats', 'on_kick_message')
    # ### end Alembic commands ###
