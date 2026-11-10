"""Hosts without a pre-deploy step (Render free tier): migrate, then serve."""

from alembic import command
from alembic.config import Config

from forge_api.serve import main


def run() -> None:
    command.upgrade(Config("/app/api/alembic.ini"), "head")
    main()


if __name__ == "__main__":
    run()
