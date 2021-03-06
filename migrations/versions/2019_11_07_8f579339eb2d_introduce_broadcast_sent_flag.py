"""Introduce broadcast_sent flag

Revision ID: 8f579339eb2d
Revises: c4feb636bb05
Create Date: 2019-11-07 15:48:23.587967

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f579339eb2d'
down_revision = 'c4feb636bb05'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('broadcast_sent', sa.Boolean(), server_default='false', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'broadcast_sent')
    # ### end Alembic commands ###
