"""ee22

Revision ID: 5633a7229963
Revises: 7b81660378f5
Create Date: 2020-06-07 15:05:11.877301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5633a7229963'
down_revision = '7b81660378f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('insurancese', sa.Column('tbname', sa.String(length=64), nullable=True))
    op.create_unique_constraint(None, 'posts', ['phnumber'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='unique')
    op.drop_column('insurancese', 'tbname')
    # ### end Alembic commands ###
