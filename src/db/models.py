''' Abstrac representation of the database structure'''

from datetime import datetime
from typing import Callable, ClassVar, override
from sqlmodel import Field, SQLModel
from sqlalchemy import Column
from sqlalchemy import text as sa_text
import sqlalchemy.dialects.postgresql as pg



class LiteraryWork(SQLModel, table=True):
    ''' Abstract representation for the `literary_works` table'''
    __tablename__: ClassVar[str | Callable[..., str]] = 'literary_works'
    id: int | None = Field(
        sa_column=Column(
            pg.BIGINT,
            primary_key=True,
            nullable=False,
            server_default=sa_text("nextval('poems_id_seq'::regclass)")
        )
    )
    author: str = Field(
        sa_column=Column(
            pg.TEXT,
            nullable=False,
            default=''
        )
    )
    source: str = Field(
        sa_column=Column(
            pg.TEXT,
            nullable=False,
            default=''
        )
    )
    title: str = Field(
        sa_column=Column(
            pg.TEXT,
            nullable=False,
        )
    )
    text: str = Field(
        sa_column=Column(
            pg.TEXT,
            nullable=False,
        )
    )
    language: str = Field(
        sa_column=Column(
            pg.VARCHAR(length=2),
            nullable=False,
            default='en'
        )
    )
    type: str = Field(
        sa_column=Column(
            pg.ENUM(
                'other', 'poem', 'quote',
                name='text_type'
            ),
            nullable=False,
            server_default=sa_text("'other'::text_type")
        )
    )
    creation_date: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=False),
            nullable=True,
        )
    )

    collection_date: datetime = Field(
        sa_column=Column(
            pg.TIMESTAMP(timezone=False),
            nullable=False,
            default=datetime.now
        )
    )

    @override
    def __repr__(self) -> str:
        return f'LiteraryWork({self.id} - \'{self.title}\')'
