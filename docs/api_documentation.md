# API overview

Base URL: `/api/v1`. Interactive OpenAPI docs: `/docs`. Except login and health, routes require `Authorization: Bearer <JWT>`. Roles are `admin`, `teacher`, `student`, and `parent`.

| Area | Routes |
|---|---|
| Auth | `POST /auth/register` (parent/guardian self-registration), `POST /auth/login`, `POST /auth/logout`, `GET /auth/me` |
| Students | `GET/POST /students`, `PATCH/DELETE /students/{id}`, `POST /students/{id}/face-profile`, `DELETE /students/{id}/face-profile` |
| Teachers | `GET/POST /teachers`, `PATCH/DELETE /teachers/{id}` |
| Classes | `GET/POST /classes`, `PATCH/DELETE /classes/{id}`, `PUT /classes/{id}/students/{student_id}` |
| Parents | `GET/POST /parents`, `PUT /parents/{parent_id}/children/{student_id}`, `GET /parents/children`, `POST /parents/children/requests`, `GET /parents/children/requests`, `POST /parents/children/{student_id}/consent` |
| Parent link review | `GET /admin/parent-link-requests`, `POST /admin/parent-link-requests/{request_id}/review` |
| Face & attendance | `POST /attendance/sessions`, `POST /attendance/sessions/{id}/recognize`, `POST /attendance/sessions/{id}/manual`, `POST /attendance/sessions/{id}/stop`, `GET /attendance/sessions/{id}`, `GET /attendance/history` |
| Reports and settings | `GET /attendance/report.csv?class_id=&start_date=&end_date=`, `GET /dashboard/summary`, `GET /settings`, `PUT /settings/{key}`, `GET /audit-logs` |

Public registration creates only a parent/guardian role; student and teacher accounts are provisioned by school administrators. New parents can sign in immediately but must be linked to a child by an administrator before child records or consent workflows are available.

Parents request a link by submitting a student number. The request does not reveal whether the number exists and does not grant record access. An administrator reviews matching requests and approves or rejects them. A student already linked to another parent cannot be reassigned through an approval.

Face enrollment/recognition uses multipart form data with an `image` file (maximum 5 MB). Enrollment is denied until the linked parent has recorded consent. Recognition only searches students enrolled in the selected session's class and possessing an active consent record. The API returns `matched: false` for an unknown/low-similarity face and never invents model output.

When auto-mark is disabled, an authorized teacher confirms a result with `POST /attendance/sessions/{id}/manual` and `{ "student_id": 1, "status": "present" }`. Closing a session inserts absent records for all enrolled students not already recorded. Manual changes and session actions are audit logged. CSV report access is staff-only.

