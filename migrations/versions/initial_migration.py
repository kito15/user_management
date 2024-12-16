
"""Initial database setup

Revision ID: ...existing id...
Revises: 
Create Date: ...existing date...
"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # Enable uuid-ossp extension
    op.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp";')
    
    # Create UserRole enum type first
    op.execute("CREATE TYPE userrole AS ENUM ('ANONYMOUS', 'AUTHENTICATED', 'MANAGER', 'ADMIN');")
    
    # Create users table (keep existing creation)
    op.create_table('users',
        sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
        sa.Column('nickname', sa.String(50), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        # ...rest of existing user columns...
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email'),
        sa.UniqueConstraint('nickname')
    )
    
    # Create user_profile_audit table
    op.create_table('user_profile_audit',
        sa.Column('audit_id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
        sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=False),
        sa.Column('updated_by', postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column('profile_data', postgresql.JSONB, nullable=False),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.ForeignKeyConstraint(['updated_by'], ['users.id'], ),
        sa.PrimaryKeyConstraint('audit_id')
    )

def downgrade():
    # Drop tables in reverse order
    op.drop_table('user_profile_audit')
    op.drop_table('users')
    op.execute('DROP TYPE userrole;')
    # Don't drop uuid-ossp as other databases might use it
