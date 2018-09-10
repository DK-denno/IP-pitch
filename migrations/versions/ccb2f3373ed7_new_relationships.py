"""new relationships

Revision ID: ccb2f3373ed7
Revises: 2a300c1e3da6
Create Date: 2018-09-09 13:12:15.130703

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ccb2f3373ed7'
down_revision = '2a300c1e3da6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('post_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'users', 'posts', ['post_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='foreignkey')
    op.drop_column('users', 'post_id')
    # ### end Alembic commands ###