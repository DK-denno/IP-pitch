"""added a comments table

Revision ID: 539dba8f72ed
Revises: b0be9b7b37fc
Create Date: 2018-09-07 12:19:10.848937

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '539dba8f72ed'
down_revision = 'b0be9b7b37fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###
