"""l领取保险金改成保险责任

Revision ID: 2a034520d120
Revises: 5d54783443b2
Create Date: 2020-06-09 15:14:29.298917

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2a034520d120'
down_revision = '5d54783443b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments', 'meettimese')
    op.add_column('insurancese', sa.Column('bxzeren', sa.Text(), nullable=True))
    op.drop_column('insurancese', 'nextgetmoney')
    op.create_unique_constraint(None, 'posts', ['phnumber'])
    op.drop_column('posts', 'families')
    op.drop_column('posts', 'insurance')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('insurance', sa.INTEGER(), nullable=True))
    op.add_column('posts', sa.Column('families', sa.INTEGER(), nullable=True))
    op.drop_constraint(None, 'posts', type_='unique')
    op.add_column('insurancese', sa.Column('nextgetmoney', sa.INTEGER(), nullable=True))
    op.drop_column('insurancese', 'bxzeren')
    op.add_column('comments', sa.Column('meettimese', sa.INTEGER(), nullable=True))
    # ### end Alembic commands ###
