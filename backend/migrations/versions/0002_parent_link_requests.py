"""Add parent child-link requests."""
from alembic import op

from app.models import ParentLinkRequest

revision = "0002_parent_link_requests"
down_revision = "0001_initial"
branch_labels = None
depends_on = None


def upgrade():
    ParentLinkRequest.__table__.create(bind=op.get_bind(), checkfirst=True)


def downgrade():
    ParentLinkRequest.__table__.drop(bind=op.get_bind(), checkfirst=True)

