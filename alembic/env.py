from logging.config import fileConfig
from sqlalchemy import  pool
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

from db import Base # Here we import the Base class from our models module
from models import models  # Import all models to ensure they are registered with Base
target_metadata = Base.metadata

# Function for running migrations
def run_migrations_online():
    connectable = create_async_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
        future=True
    )

    async def do_run_migrations():
        async with connectable.connect() as connection:
            await connection.run_sync(run_migrations)

    def run_migrations(connection):
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()

    import asyncio
    asyncio.run(do_run_migrations())

run_migrations_online()