from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///images.db", echo=False)
Session = sessionmaker(bind=engine)

class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    timestamp = Column(DateTime)

Base.metadata.create_all(engine)

def list_images_between(start_time_str, end_time_str):
    """
    Return image filenames whose timestamps fall between start_time and end_time (inclusive).
    Time format: HH:MM
    """
    start = datetime.strptime(start_time_str, "%H:%M")
    end = datetime.strptime(end_time_str, "%H:%M")

    session = Session()
    results = session.query(Image).all()

    filtered = []
    for img in results:
        img_time = img.timestamp.time()
        if start.time() <= img_time <= end.time():
            filtered.append(img.name)

    return filtered

