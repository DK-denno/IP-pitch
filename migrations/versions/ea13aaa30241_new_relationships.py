"""new relationships

Revision ID: ea13aaa30241
Revises: e02f6c180333
Create Date: 2018-09-10 19:12:39.833437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ea13aaa30241'
down_revision = 'e02f6c180333'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('pitch_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'comments', 'posts', ['pitch_id'], ['id'])
    op.add_column('posts', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'users', ['user_id'], ['id'])
    op.drop_constraint('users_post_id_fkey', 'users', type_='foreignkey')
    op.drop_column('users', 'post_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('users_post_id_fkey', 'users', 'posts', ['post_id'], ['id'])
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'user_id')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_column('comments', 'pitch_id')
    # ### end Alembic commands ###
