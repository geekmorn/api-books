from uuid import uuid4
from sqlalchemy.future import select
from src.common.config.database import db
from sqlalchemy.exc import DatabaseError
from .exceptions import not_acceptable


async def commit_change() -> None:
    try:
        await db.commit()
    except DatabaseError:
        await db.rollback()
        raise not_acceptable()


def by(field_name, value) -> dict:
    return {
        "field_name": field_name,
        "value": value
    }


async def create(Model, **kwargs):
    record = Model(id=str(uuid4()), **kwargs)
    db.add(record)
    await commit_change()

    return record


async def read(Model, options: dict | None = None):

    async def all():
        query = select(Model)
        records = await db.execute(query)
        result = records.scalars().all()
        return result

    async def selected():
        query = select(Model).where(options["field_name"] == options["value"])
        record = await db.execute(query)
        result = record.scalars().first()
        return result

    return await (
        selected()
        if options
        else all()
    )


async def destroy(record):
    await db.delete(record)
    await commit_change()
    return record
