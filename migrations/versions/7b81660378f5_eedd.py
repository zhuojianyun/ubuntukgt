"""eedd

Revision ID: 7b81660378f5
Revises: b1fc25fbeb2f
Create Date: 2020-06-07 14:40:54.409800

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7b81660378f5'
down_revision = 'b1fc25fbeb2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'posts', ['phnumber'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='unique')
    # ### end Alembic commands ###
