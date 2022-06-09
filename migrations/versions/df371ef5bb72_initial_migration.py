"""Initial migration.

Revision ID: df371ef5bb72
Revises: 
Create Date: 2022-06-09 17:30:00.017213

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df371ef5bb72'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_marks')
    op.add_column('assignments', sa.Column('maxnum', sa.Integer(), nullable=True))
    op.alter_column('marks', 'mid',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.create_foreign_key(None, 'marks', 'assignments', ['assi'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'marks', type_='foreignkey')
    op.alter_column('marks', 'mid',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('assignments', 'maxnum')
    op.create_table('_alembic_tmp_marks',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('student', sa.INTEGER(), nullable=True),
    sa.Column('subject', sa.INTEGER(), nullable=True),
    sa.Column('sem', sa.INTEGER(), nullable=True),
    sa.Column('mark', sa.INTEGER(), nullable=False),
    sa.Column('assi', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['sem'], ['sems.id'], ),
    sa.ForeignKeyConstraint(['student'], ['student.sid'], ),
    sa.ForeignKeyConstraint(['subject'], ['subjects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
