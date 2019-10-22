# coding: utf-8
import datetime

from sqlalchemy import (Column,
                        DateTime,
                        ForeignKey,
                        Integer,
                        String)
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

    def serialize(self):
        return dict(id=self.id,
                    name=self.name,
                    created=str(self.created),
                    abducted=str(self.abducted))


class ProbeReport(Base):
    __tablename__ = 'probe_report'

    id = Column(Integer, primary_key=True)
    alien_id = Column(ForeignKey('alien.id'), index=True)
    info = Column(String(1024), nullable=False)
    created = Column(DateTime, nullable=False)

    alien = relationship('Alien')

    def serialize(self):
        return dict(id=self.id,
                    alien_id=self.alien_id,
                    info=self.info,
                    created=str(self.created))

