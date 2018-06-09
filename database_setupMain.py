import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    picture = Column(String(255))
    
    # serializable format
    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            'email' : self.email,
            'picture' : self.picture,
        }

class Brand(Base):
    __tablename__ = 'brand'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    name = Column(String(50),nullable=False)
   
    
    user = relationship(User)
    # serializable format
    @property
    def serialize(self):
        return {
            'name': self.name,
            'id': self.id,
            
        }


class Model(Base):
    __tablename__ = 'model'

    id = Column(Integer,primary_key = True)
    brand_id = Column(Integer,ForeignKey('brand.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    name = Column(String(30), nullable = False)
    os = Column(String(30))
    processor = Column(String(30))
    ram = Column(String(30))
    storage = Column(String(30))
    camera = Column(String(30))
    battery = Column(String(30))
    connectivity = Column(String(50))
    sim = Column(String(30))
    colors = Column(String(30))
    sensors = Column(String(50))
    price = Column(String(20))
    description = Column(String(500))
    picture = Column(String(500))

    brand = relationship(Brand)
    user = relationship(User)

    # serializable format
    @property
    def serialize(self):
        return {

            'id': self.id,
            'name': self.name,
            'os' : self.os,
            'processor' : self.processor,
            'ram' : self.ram,
            'storage' :  self.storage,
            'camera' : self.camera,
            'battery' : self.battery,
            'connectivity' : self.connectivity,
            'sim' : self.sim,
            'colors' : self.colors,
			'sensors' : self.sensors,
            'price' : self.price,
            'description' : self.description,
            'picture' : self.picture,
            
        }

engine = create_engine('sqlite:///mobileWorld.db')
Base.metadata.create_all(engine)
