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
    abducted = Column(Boolean, default=False, index=True)
    probed = Column(Boolean, default=False, index=True)


class ProbeReport(Base):
    __tablename__ = 'probe_report'

    id = Column(Integer, primary_key=True)
    alien_id = Column(ForeignKey('alien.id'), index=True)
    info = Column(String(1024), nullable=False)

    alien = relationship('Alien')

