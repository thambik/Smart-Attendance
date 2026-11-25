import argparse
import getpass
import hmac
import os

from sqlalchemy import func, select

from app.config import settings
from app.database import SessionLocal
from app.models import User
from app.security import hash_password


def ensure_admin_bootstrap_available(db):
    if db.scalar(select(func.count(User.id)).where(User.role == "admin")) != 0:
        raise SystemExit("Bootstrap is only permitted while no administrator exists.")


def main():
    parser = argparse.ArgumentParser(description="Create the initial SmartAttend administrator.")
    parser.add_argument("--email", required=True)
    parser.add_argument("--name", required=True)
    args = parser.parse_args()
    token = getpass.getpass("Bootstrap token: ")
    if not settings.bootstrap_token or not hmac.compare_digest(token, settings.bootstrap_token):
        raise SystemExit("Invalid bootstrap token; configure BOOTSTRAP_TOKEN in the backend environment.")
    password = getpass.getpass("Admin password (12+ characters): ")
    if len(password) < 12:
        raise SystemExit("Password must contain at least 12 characters.")
    with SessionLocal() as db:
        ensure_admin_bootstrap_available(db)
        admin = User(email=args.email.lower(), full_name=args.name, password_hash=hash_password(password), role="admin")
        db.add(admin)
        db.commit()
    print("Administrator created.")


if __name__ == "__main__":
    main()

