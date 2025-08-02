
#creates a connection engine to the db
from sqlalchemy import create_engine
#creates sessiion objects
from sqlalchemy.orm import sessionmaker
from model import Base
DATABASE_URL = "postgresql://williammayhood@localhost:5432/finance_tracker"

engine = create_engine(DATABASE_URL, echo=True)

#Bind models to engine, creates tables from models
Base.metadata.create_all(engine)

#create session factory object
SessionLocal = sessionmaker(bind=engine)