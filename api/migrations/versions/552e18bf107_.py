"""empty message

Revision ID: 552e18bf107
Revises: 4613486f2a1
Create Date: 2014-12-20 23:50:22.685738

"""

# revision identifiers, used by Alembic.
revision = '552e18bf107'
down_revision = '4613486f2a1'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('match',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('playermatch',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('match', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['match'], ['match.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('playermatch')
    op.drop_table('match')
    ### end Alembic commands ###
