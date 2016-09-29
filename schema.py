from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, Text, Boolean

from db_setup import DbSetup

db_setup = DbSetup()
Base = db_setup.base


def to_list_of_dicts(lm):
    return [to_dict(m) for m in lm]


def to_dict(m):
    return {c.name: make_serializable(getattr(m, c.name)) for c in m.__table__.columns}


def make_serializable(v):
    if isinstance(v, datetime):
        return v.strftime("%m-%d-%Y %H:%M:%S")
    else:
        return v


class Authorizations(Base):
    __tablename__ = 'authorizations'
    authorization_id = Column(Integer(), primary_key=True)
    alexa_state = Column(Text)
    alexa_client_id = Column(Text)
    alexa_scope = Column(Text)
    alexa_response_type = Column(Text)
    access_token = Column(Text)
    salesforce_access_token = Column(Text)
    salesforce_authorization_token = Column(Text)
    user_name = Column(Text())
    name = Column(Text())
    email = Column(Text())
    created = Column(DateTime(), default=datetime.now, index=True)
    updated = Column(DateTime(), default=datetime.now, index=True)

    def __init__(self, alexa_state = None, alexa_client_id = None, alexa_scope = None, alexa_response_type = None, access_token = None, salesforce_access_token = None, salesforce_authorization_token = None, user_name = None,name = None,    email = None):
        self.alexa_state = alexa_state
        self.alexa_client_id = alexa_client_id
        self.alexa_scope = alexa_scope
        self.alexa_response_type = alexa_response_type
        self.access_token = access_token
        self.salesforce_access_token = salesforce_access_token
        self.salesforce_authorization_token = salesforce_authorization_token
        self.user_name = user_name
        self.name = name
        self.email = email


class Debug(Base):
    __tablename__ = 'debug'
    debug_id = Column(Integer(), primary_key=True)
    step = Column(Text(), index=True)
    value = Column(Text())
    created = Column(DateTime(), default=datetime.now, index=True)

    def __init__(self, step=None, value=None):
        self.step = step
        self.value = value
