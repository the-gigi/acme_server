# coding: utf-8
import datetime

from sqlalchemy import (Column,
                        DateTime,
                        ForeignKey,
                        Index,
                        Integer,
                        Numeric,
                        String,
                        Enum,
                        Boolean,
                        UniqueConstraint)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class Alien(Base):
    __tablename__ = 'alien'

    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False, unique=True)
    created = Column(DateTime, nullable=False)
    abducted = Column(DateTime, nullable=True)


class ProbeReport(Base):
    __tablename__ = 'probe_report'

    id = Column(Integer, primary_key=True)
    alien_id = Column(ForeignKey('alien.id'), index=True)
    info = Column(String(1024), nullable=False)
    created = Column(DateTime, nullable=False)

    alien = relationship('Alien')

