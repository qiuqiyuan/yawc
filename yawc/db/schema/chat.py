from sqlalchemy import BigInteger, Column, DateTime, ForeignKey, Table, Text

from yawc.db.connection import metadata
from yawc.utils.dates import utcnow

MessagesTable = Table(
    'messages', metadata,

    Column('id', BigInteger, primary_key=True),
    Column('timestamp', DateTime(timezone=True), default=utcnow,
           nullable=False),
    Column('user_id', BigInteger, ForeignKey('users.id')),
    Column('channel', Text, index=True, nullable=False),
    Column('text', Text, index=True, nullable=False),
)
