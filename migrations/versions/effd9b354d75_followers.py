"""followers

Revision ID: effd9b354d75
Revises: 9587d4943cbe
Create Date: 2018-08-28 14:26:59.305537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'effd9b354d75'
down_revision = '9587d4943cbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tyre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wheel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brand', sa.String(length=64), nullable=True),
    sa.Column('diameter', sa.String(length=2), nullable=True),
    sa.Column('width', sa.String(length=4), nullable=True),
    sa.Column('offset', sa.String(length=4), nullable=True),
    sa.Column('bcd', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wheel_bcd'), 'wheel', ['bcd'], unique=False)
    op.create_index(op.f('ix_wheel_brand'), 'wheel', ['brand'], unique=False)
    op.create_index(op.f('ix_wheel_diameter'), 'wheel', ['diameter'], unique=False)
    op.create_index(op.f('ix_wheel_offset'), 'wheel', ['offset'], unique=False)
    op.create_index(op.f('ix_wheel_width'), 'wheel', ['width'], unique=False)
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    op.drop_index(op.f('ix_wheel_width'), table_name='wheel')
    op.drop_index(op.f('ix_wheel_offset'), table_name='wheel')
    op.drop_index(op.f('ix_wheel_diameter'), table_name='wheel')
    op.drop_index(op.f('ix_wheel_brand'), table_name='wheel')
    op.drop_index(op.f('ix_wheel_bcd'), table_name='wheel')
    op.drop_table('wheel')
    op.drop_table('tyre')
    # ### end Alembic commands ###
