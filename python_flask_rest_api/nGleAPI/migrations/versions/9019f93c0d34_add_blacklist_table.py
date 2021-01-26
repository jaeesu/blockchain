"""add blacklist table

Revision ID: 9019f93c0d34
Revises: 61bbe58cfc9b
Create Date: 2021-01-25 23:22:26.884858

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9019f93c0d34'
down_revision = '61bbe58cfc9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blacklist_tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.Column('blacklisted_on', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blacklist_tokens')
    # ### end Alembic commands ###
