import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, BigInteger, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
SERVER_ID = int(os.getenv('SERVER_ID', 0))

engine = create_engine(DATABASE_URL)

Base = declarative_base()

class Entry(Base):
	__tablename__ = 'entries'
	id = Column(BigInteger, primary_key=True)
	lang = Column(String(2))
	prefix = Column(String)
	presets = relationship('Preset', back_populates='entry')

	def __init__ (self, id):
		self.id = id

class Preset(Base):
	__tablename__ = 'presets'
	id = Column(Integer, primary_key=True)
	entry_id = Column(BigInteger, ForeignKey('entries.id'))
	entry = relationship('Entry', back_populates='presets')
	name = Column(String)
	command = Column(String)

	def __init__ (self, entry_id, name):
		self.entry_id = entry_id
		self.name = name

# Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)

def get_entry(session, id):
	return session.query(Entry).filter_by(id=id).one_or_none()

def get_attr(user_id, server_id, attr):
	if not attr:
		return
	session = Session()
	for id in [user_id, server_id, SERVER_ID]:
		if not id:
			continue
		entry = get_entry(session, id)
		if hasattr(entry, attr) and getattr(entry, attr) != None:
			return getattr(entry, attr)
	session.close()

def set_attr(id, attr, val):
	if not id or not attr or not val:
		return
	session = Session()
	entry = get_entry(session, id)
	if not entry:
		entry = Entry(id)
	setattr(entry, attr, val)
	session.add(entry)
	session.commit()
	session.close()

def get_lang(user_id, server_id):
	return get_attr(user_id, server_id, 'lang')

def set_lang(id, lang):
	set_attr(id, 'lang', lang)

def get_prefix(server_id):
	return get_attr(None, server_id, 'prefix')

def set_prefix(id, prefix):
	set_attr(id, 'prefix', prefix)

def get_preset(session, id, name):
	return session.query(Preset).filter_by(entry_id=id).filter_by(name=name).one_or_none()

def get_presets(user_id, server_id):
	session = Session()
	results = session.query(Preset).filter((Preset.entry_id == user_id) | (Preset.entry_id == server_id)).order_by(Preset.name).all()
	session.close()
	return results

def set_preset(id, name, command):
	if not id or not name or not command:
		return
	session = Session()
	preset = get_preset(session, id, name)
	if not preset:
		entry = get_entry(session, id)
		if not entry:
			entry = Entry(id)
			session.add(entry)
		preset = Preset(id, name)
	preset.command = command
	session.add(preset)
	session.commit()
	session.close()

def del_preset(id, name):
	if not id or not name:
		return
	result = False
	session = Session()
	preset = get_preset(session, id, name)
	if preset:
		session.delete(preset)
		session.commit()
		result = True
	session.close()
	return result
