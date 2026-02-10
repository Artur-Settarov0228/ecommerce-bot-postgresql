from sqlalchemy.orm import sessionmaker

from app.core.database import engine

SessionLocal = sessionmaker(engine)