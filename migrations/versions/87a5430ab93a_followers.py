"""followers

Revision ID: 87a5430ab93a
Revises: f1abfdb8ab70
Create Date: 2022-07-21 19:08:57.899870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "87a5430ab93a"
down_revision = "f1abfdb8ab70"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "followers",
        sa.Column("follower_id", sa.Integer(), nullable=True),
        sa.Column("followed_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["followed_id"],
            ["user.id"],
        ),
        sa.ForeignKeyConstraint(
            ["follower_id"],
            ["user.id"],
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("followers")
    # ### end Alembic commands ###
