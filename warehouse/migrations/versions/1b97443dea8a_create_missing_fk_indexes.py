# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
create missing FK indexes

Revision ID: 1b97443dea8a
Revises: d18d443f89f0
Create Date: 2022-01-03 20:52:20.615419
"""

from alembic import op

revision = "1b97443dea8a"
down_revision = "d18d443f89f0"


def upgrade():
    # CREATE INDEX CONCURRENTLY cannot happen inside a transaction. We'll close
    # our transaction here and issue the statement.
    op.execute("COMMIT")

    op.create_index(
        op.f("ix_macaroons_user_id"),
        "macaroons",
        ["user_id"],
        unique=False,
        postgresql_concurrently=True,
    )
    op.create_index(
        op.f("ix_project_events_project_id"),
        "project_events",
        ["project_id"],
        unique=False,
        postgresql_concurrently=True,
    )
    op.create_index(
        op.f("ix_release_vulnerabilities_release_id"),
        "release_vulnerabilities",
        ["release_id"],
        unique=False,
        postgresql_concurrently=True,
    )
    op.create_index(
        op.f("ix_releases_description_id"),
        "releases",
        ["description_id"],
        unique=False,
        postgresql_concurrently=True,
    )
    op.create_index(
        op.f("ix_role_invitations_project_id"),
        "role_invitations",
        ["project_id"],
        unique=False,
        postgresql_concurrently=True,
    )
    op.create_index(
        op.f("ix_role_invitations_user_id"),
        "role_invitations",
        ["user_id"],
        unique=False,
        postgresql_concurrently=True,
    )
    op.create_index(
        op.f("ix_user_events_user_id"),
        "user_events",
        ["user_id"],
        unique=False,
        postgresql_concurrently=True,
    )
    op.create_index(
        op.f("ix_user_recovery_codes_user_id"),
        "user_recovery_codes",
        ["user_id"],
        unique=False,
        postgresql_concurrently=True,
    )
    op.create_index(
        op.f("ix_user_security_keys_user_id"),
        "user_security_keys",
        ["user_id"],
        unique=False,
        postgresql_concurrently=True,
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_user_security_keys_user_id"), table_name="user_security_keys"
    )
    op.drop_index(
        op.f("ix_user_recovery_codes_user_id"), table_name="user_recovery_codes"
    )
    op.drop_index(op.f("ix_user_events_user_id"), table_name="user_events")
    op.drop_index(op.f("ix_role_invitations_user_id"), table_name="role_invitations")
    op.drop_index(op.f("ix_role_invitations_project_id"), table_name="role_invitations")
    op.drop_index(op.f("ix_releases_description_id"), table_name="releases")
    op.drop_index(
        op.f("ix_release_vulnerabilities_release_id"),
        table_name="release_vulnerabilities",
    )
    op.drop_index(op.f("ix_project_events_project_id"), table_name="project_events")
    op.drop_index(op.f("ix_macaroons_user_id"), table_name="macaroons")
    # ### end Alembic commands ###
