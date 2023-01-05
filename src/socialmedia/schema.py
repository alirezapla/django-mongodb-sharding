from datetime import date
from ninja import Schema


class User(Schema):
    username: str
    department_id: int = None
