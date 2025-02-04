"""remove task

Revision ID: ce0cdfd66450
Revises: 9e7637b22cc1
Create Date: 2022-03-21 12:07:46.718864

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce0cdfd66450'
down_revision = '9e7637b22cc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_task_name', table_name='task')
    op.drop_table('task')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.VARCHAR(length=36), nullable=False),
    sa.Column('name', sa.VARCHAR(length=128), nullable=True),
    sa.Column('description', sa.VARCHAR(length=128), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.Column('complete', sa.BOOLEAN(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('ix_task_name', 'task', ['name'], unique=False)
    # ### end Alembic commands ###
