import datetime
from django_mongoengine import Document, EmbeddedDocument, fields
import mongoengine as db


class User(Document):
    created_at = db.DateTimeField(
        default=datetime.datetime.now, editable=False,
    )
    username = db.StringField(max_length=100)

    def as_dict(self):
        return {
            'id': str(self.id),
            'username': self.username,
        }

    def created_datetime(self):
        return self.created_at


    meta = {
        'shard_key': ('username'),
        'indexes': ['username'],
    }


class Like(EmbeddedDocument):
    created_at = db.DateTimeField(
        default=datetime.datetime.now, editable=False,
    )
    liker = db.StringField(max_length=100)

    def as_dict(self):
        return {
            'liker': self.liker,
        }

    def created_datetime(self):
        return self.created_at

    meta = {
        'shard_key': ('liker'),
        'indexes': ['liker']
    }


class Comment(EmbeddedDocument):
    created_at = db.DateTimeField(
        default=datetime.datetime.now, editable=False,
    )
    author = db.StringField(max_length=100)
    text = db.StringField(verbose_name="Comment")

    def as_dict(self):
        return {
            'author': self.author,
            'text': self.text,
        }

    def created_datetime(self):
        return self.created_at

    meta = {
        'shard_key': ('author'),
        'indexes': ['author']
    }


class Post(Document):
    created_at = db.DateTimeField(
        default=datetime.datetime.now, editable=False,
    )
    owner = db.ReferenceField(User, max_lenght=100)
    likes = db.ListField(
        db.EmbeddedDocumentField('Like'), blank=True,
    )
    content = db.StringField(max_length=255)
    comments = db.ListField(
        db.EmbeddedDocumentField('Comment'), blank=True,
    )

    def as_dict(self):
        return {
            'id': str(self.id),
            'owner': self.owner,
            'likes': self.likes,
            'content': self.content,
            'comments': self.comments,
            'created_at': self.created_at
        }

    meta = {
        'shard_key': ('owner'),
        'indexes': ['owner']
    }
