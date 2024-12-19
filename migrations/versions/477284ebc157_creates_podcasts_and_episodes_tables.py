"""Creates podcasts and episodes tables

Revision ID: 477284ebc157
Revises: 
Create Date: 2024-12-19 19:04:58.160096

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '477284ebc157'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('podcasts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('podcast_name', sa.String(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('author', sa.String(), nullable=False),
    sa.Column('creation_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('episodes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('episode_title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('audio_url', sa.String(), nullable=False),
    sa.Column('release_date', sa.DateTime(), nullable=False),
    sa.Column('podcast_id', sa.Integer(), nullable=False),
    sa.Column('update_time', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['podcast_id'], ['podcasts.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('episodes')
    op.drop_table('podcasts')
    # ### end Alembic commands ###
