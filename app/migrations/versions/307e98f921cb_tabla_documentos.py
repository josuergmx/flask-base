"""Tabla documentos

Revision ID: 307e98f921cb
Revises: ee209177a340
Create Date: 2024-11-26 13:36:36.632464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '307e98f921cb'
down_revision = 'ee209177a340'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('documents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('ext', sa.String(length=8), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.add_column(sa.Column('document_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'documents', ['document_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tasks', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('document_id')

    op.drop_table('documents')
    # ### end Alembic commands ###
