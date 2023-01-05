import datetime
from django_mongoengine import Document, EmbeddedDocument, fields


class Comment(EmbeddedDocument):
    created_at = fields.DateTimeField(
        default=datetime.datetime.now, editable=False,
    )
    author = fields.StringField(verbose_name="Name", max_length=100)
    text = fields.StringField(verbose_name="Comment")
    # replay_to=


class Post(Document):
    created_at = fields.DateTimeField(
        default=datetime.datetime.now, editable=False,
    )
    content = fields.StringField(max_length=255)
    comments = fields.ListField(
        fields.EmbeddedDocumentField('Comment'), blank=True,
    )


class User(Document):
    created_at = fields.DateTimeField(
        default=datetime.datetime.now, editable=False,
    )
    username = fields.StringField(max_length=100)

