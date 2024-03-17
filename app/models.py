from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, create_engine, Date, Float
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

DB_URI = 'sqlite:///fantasy_game.db'

# Create engine
engine = create_engine(DB_URI)

# Create base definitions
Base = declarative_base()
  
# driver table
class Driver(Base):
    __tablename__ = 'drivers'
    id = Column(String(3), primary_key=True)
    name = Column(String(24), nullable=False)
    team = Column(String(48), nullable=False)
    price = Column(Float, nullable=False)
    points = Column(Float, nullable=False)
    
# race table
class Race(Base):
    __tablename__ = 'races'
    id = Column(Integer, primary_key=True)
    track_name = Column(String(48), unique=True, nullable=False)
    country = Column(String(24), nullable=False)
    date = Column(Date, nullable=False)

# race results table
class RaceResult(Base):
    __tablename__ = 'race_results'
    id = Column(Integer, primary_key=True)
    race_id = Column(Integer, ForeignKey('races.id'), nullable=False)
    driver_id = Column(Integer, ForeignKey('driver.id'), nullable=False)
    position = Column(String(3), nullable=False)
    fastest_lap = Column(Boolean, nullable=False)
    
# define realtionship between tables
race = relationship('Race', backref='race_results')
driver = relationship('Driver', backref='race_results')