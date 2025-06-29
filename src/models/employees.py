from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import PasswordType, EmailType
from src.models import database


class Employees(database.Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    email = Column(EmailType, unique=True)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']))
    is_active = Column(Boolean, default=True)