import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base

metadata = sql.MetaData(
    naming_convention={
        "ix": "ix__%(column_0_label)s",
        "uq": "uq__%(table_name)s__%(column_0_name)s",
        "ck": "ck__%(table_name)s__%(constraint_name)s",
        "fk": "fk__%(table_name)s__%(column_0_name)s__%(referred_table_name)s",
        "pk": "pk__%(table_name)s"
    }
)

Base = declarative_base(metadata=metadata)