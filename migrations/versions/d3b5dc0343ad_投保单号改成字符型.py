"""投保单号改成字符型

Revision ID: d3b5dc0343ad
Revises: 98dbf6af31d8
Create Date: 2020-06-07 18:54:28.734194

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3b5dc0343ad'
down_revision = '98dbf6af31d8'
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
