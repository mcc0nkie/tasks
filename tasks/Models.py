from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Campaign(Base):
    __tablename__ = 'campaigns'
    campaign_id = Column(Integer, primary_key=True)
    campaign_name = Column(String)

    offer_codes = relationship('OfferCode', back_populates='campaign')


class OfferCode(Base):
    __tablename__ = 'offer_codes'
    offer_code_id = Column(Integer, primary_key=True)
    offer_code = Column(String)
    campaign_id = Column(Integer, ForeignKey('campaigns.campaign_id'))

    campaign = relationship('Campaign', back_populates='offer_codes')
    channels = relationship('Channel', back_populates='offer_code')


class Channel(Base):
    __tablename__ = 'channels'
    channel_id = Column(Integer, primary_key=True)
    channel_name = Column(String)
    offer_code_id = Column(Integer, ForeignKey('offer_codes.offer_code_id'))

    offer_code = relationship('OfferCode', back_populates='channels')
    segments = relationship('Segment', back_populates='channel')


class Segment(Base):
    __tablename__ = 'segments'
    segment_id = Column(Integer, primary_key=True)
    segment_name = Column(String)
    channel_id = Column(Integer, ForeignKey('channels.channel_id'))

    channel = relationship('Channel', back_populates='segments')


class Project(Base):
    __tablename__ = 'projects'
    project_id = Column(Integer, primary_key=True)
    project_name = Column(String)
    project_status = Column(String)
    communication_designation = Column(String)
    segment_partner_name = Column(String)
    project_request_number = Column(String, nullable=True)
    ucra_number = Column(String, nullable=True)
    ucra_proof_of_approval = Column(String, nullable=True)
    model_number = Column(String, nullable=True)
    model_proof_of_approval = Column(String, nullable=True)
    map_number = Column(String, nullable=True)
    map_approval_date = Column(Date, nullable=True)

    changes = relationship('ProjectChange', back_populates='project')


class ProjectChange(Base):
    __tablename__ = 'project_changes'
    change_id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'))
    affected_entity_type = Column(String)
    affected_entity_id = Column(Integer)
    change_type = Column(String)
    change_date = Column(Date)
    new_value = Column(String, nullable=True)

    project = relationship('Project', back_populates='changes')


