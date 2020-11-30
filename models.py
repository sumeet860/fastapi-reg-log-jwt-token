from sqlalchemy import Boolean, Column, ForeignKey, Integer, VARCHAR
from sqlalchemy.orm import relationship
import database
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(VARCHAR(20))
    email = Column(VARCHAR(20), unique=True, index=True)
    full_name = Column(VARCHAR(20))
    hashed_password = Column(VARCHAR(200))
    role = Column(VARCHAR(20))
