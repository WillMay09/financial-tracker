from db import engine, Base
from model import user, expense, category

Base.metadata.create_all(bind=engine)