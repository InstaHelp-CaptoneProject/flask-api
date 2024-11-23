"""add column description in institutions

Revision ID: 411720ea3de4
Revises: c98d4c93fd9d
Create Date: 2024-11-23 09:49:27.799589

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '411720ea3de4'
down_revision = 'c98d4c93fd9d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('institutions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.Text(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('institutions', schema=None) as batch_op:
        batch_op.drop_column('description')

    # ### end Alembic commands ###