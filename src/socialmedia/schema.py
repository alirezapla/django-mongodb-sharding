from datetime import datetime
from ninja import Schema


# Todo add validation
class UserSchema(Schema):
    username: str
    created_at: datetime = None


# Todo add validation
class LikeSchema(Schema):
    liker: str
    created_at: datetime = None


# Todo add validation
class CommentSchema(Schema):
    author: str
    text: str
    created_at: datetime = None


# Todo add validation
class PostSchema(Schema):
    owner_id: str
    content: str
    created_at: datetime = None
