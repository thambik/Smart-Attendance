# Data model

- `users`: authentication identity and role; one-to-one profile relationship.
- `students`: school identifier, user and optional linked parent.
- `teachers`: employee identifier and user; classes point to assigned teacher.
- `parents`: user and linked children.
- `parent_consents`: current guardian consent for an individual student's biometric profile. Revoking consent deletes the profile.
- `parent_link_requests`: parent-submitted student-number requests with a pending/approved/rejected status and administrator review audit fields. Pending requests do not grant access.
- `classes`: class name/section and optional assigned teacher.
- `enrollments`: unique student-to-class enrollment.
- `face_profiles`: one encrypted embedding per student, model identifier and enrollment timestamp. The key is external configuration, not stored in the database.
- `attendance_sessions`: class, teacher, start/end timestamps, date and open state.
- `attendance`: unique session/student record, status, source and recorded time.
- `audit_logs`: actor, action, target and minimal non-biometric details.
- `school_settings`: key/value school configuration.

Apply migrations with `alembic upgrade head`. The initial Alembic revision is frozen and `0002_parent_link_requests` adds the child-link request table. Production schema evolution should use reviewed incremental revisions; never edit a migration already applied in a deployed environment.

