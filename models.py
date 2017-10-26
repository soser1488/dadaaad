from sqlalchemy import create_engine
from sqlalchemy import Column, Boolean, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///users_subs.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50))

    def __init__(self, user_id=None, first_name=None, last_name=None, username=None):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def __repr__(self):
        return '<User {} {} {} {}>'.format(self.user_id, self.first_name, self.last_name, self.username)
        

class Subscription(Base):
    __tablename__ = 'subscriptions'
    sub_id = Column(Integer, primary_key = True, autoincrement = True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    streamer_id = Column(Integer, ForeignKey('streamers.id'))

    def __init__(self, sub_id = None, user_id=None, streamer_id=None):
        self.sub_id = sub_id
        self.user_id = user_id
        self.streamer_id = streamer_id


    def __repr__(self):
        return '<Subscription {} {} {}>'.format(self.sub_id, self.user_id, self.streamer_id)


class Streamers(Base):
    __tablename__ = 'streamers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    streamer_name = Column(String(140))
    stream_type =  Column(String(4))

    def __init__(self, streamer_name=None, stream_type = None):
        self.streamer_name = streamer_name
        self.stream_type = stream_type


    def __repr__(self):
        return '<Streamers {} {} {}>'.format(self.id, self.streamer_name, self.stream_type) 


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)