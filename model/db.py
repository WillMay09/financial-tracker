from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
DATABASE_URL = "postgresql://myuser:mypassword@localhost:5432/finance_tracker"

engine = create_engine(DATABASE_URL, echo=True)

#Bind models to engine
Base.metadata.create_all(engine)

#create session factory
SessionLocal = sessionmaker(bind=engine)