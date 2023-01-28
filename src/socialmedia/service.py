
from .models import User, Like, Comment, Post
import orjson


class PostCRUD:

    def __init__(self):
        self.post = Post.objects

    def retrive_by_user(self, user_id: str):
        res = self.post.filter(owner=user_id)
        print(res)

        if res:
            _posts = [_post.as_dict() for _post in res]
            for _post in _posts:
                _post['id'] = str(_post['id'])
                if not _post.get('owner') is None:
                    _post['owner'] = _post['owner'].as_dict()['username']
                _post = self._remove_nested_items(_post)
            return _posts

    def retrive_by_id(self, post_id: str):
        res = self.post.get(id=post_id)
        if res:
            res = res.as_dict()
            if not res.get('owner') is None:
                res['owner'] = res['owner'].as_dict()['username']
            res = self._remove_nested_items(res)
            return res

    # TODO set limit
    def retrive_comments(self, post_id: str, offset=None, limit=None):
        res = self.post.get(id=post_id)
        if res:
            print(res.to_json())
            document_comments = res.as_dict()['comments']
            _comments = []
            # for _comment in document_comments[offset:limit]:
            for _comment in document_comments:
                print(_comment)
                _comments.append(_comment.as_dict())
            return _comments

    def retrive_likes(self, post_id: str):
        res = self.post.get(id=post_id)
        if res:
            document_likes = res.as_dict()['likes']
            _likes = []
            for _like in document_likes:
                print(_like)
                _likes.append(_like.as_dict())
            return _likes

    def remove(self):
        ...

    def add_new(self, item: dict):
        res = self.post.create(**item.dict())
        return orjson.loads(res.to_json())

    def update_by_comment(self, post_id: str, comment_body: dict):
        res = self.post(id=post_id)
        if res:
            _comment = Comment()
            _comment.text, _comment.author = comment_body['text'], comment_body['author']
            res.update_one(push__comments=_comment)
            return _comment.as_dict()

    def update_by_like(self, post_id: str, like_body: dict):
        res = self.post(id=post_id)
        if res:
            _like = Like()
            _like.liker = like_body['liker']
            res.update_one(push__likes=_like)
            return _like.as_dict()



    @staticmethod
    def _remove_nested_items(document: dict):
        del document['likes']
        del document['comments']
        return document


post = PostCRUD()


class UserCRUD:

    def __init__(self):
        ...

    def retrive(self, user_id: str):
        res = User.objects.get(id=user_id)
        return res.as_dict()

    def remove(self, user_id: str):
        res = User.objects.delete(id=user_id)
        return orjson.loads(res.to_json())

    def add(self, item: dict):
        res = User.objects.create(**item.dict())
        return orjson.loads(res.to_json())

    def update(self):
        ...


user = UserCRUD()



