"""Create SmartAttend core tables."""
from alembic import op

from app.database import Base
from app import models

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    tables = [table for table in Base.metadata.sorted_tables if table.name != "parent_link_requests"]
    Base.metadata.create_all(bind=op.get_bind(), tables=tables)


def downgrade():
    tables = [table for table in reversed(Base.metadata.sorted_tables) if table.name != "parent_link_requests"]
    Base.metadata.drop_all(bind=op.get_bind(), tables=tables)

