from ninja import NinjaAPI
from .controller import post, user
from .schema import UserSchema, PostSchema, CommentSchema, LikeSchema
from .utils import validation_object_id
api = NinjaAPI(title='SocialMedia', version='0.0.1')


@api.get("/")
def root(request):
    return {"message": "Welcome to Django with MongoDB"}


@api.post("/user", tags=['Users'])
def new_user(request, user_body: UserSchema):
    res = user.new(user_body)
    return {"response": res}


@api.get("/user/{user_id}", tags=['Users'])
def retrive_user(request, user_id: str):
    validation_object_id(user_id)
    res = user.retrive(user_id)
    return {"response": res}


@api.delete("/user/{user_id}", tags=['Users'])
def remove_user(request, user_id: str):
    validation_object_id(user_id)
    res = user.remove(user_id)
    return {"response": res}


@api.post("/post", tags=['Posts'])
def add_post(request, post_body: PostSchema):
    res = post.add_new(post_body)
    return {"response": res}


@api.get("/posts/{user_id}", tags=['Posts'])
def user_posts(request, user_id: str):
    validation_object_id(user_id)
    res = post.retrive_by_user(user_id)
    return {"response": res}


@api.post("/like/{post_id}", tags=['Likes'])
def like_it(request, post_id: str, like_body: LikeSchema):
    validation_object_id(post_id)
    res = post.update_by_like(post_id, like_body.dict())
    return {"response": res}


@api.get("/likes/{post_id}", tags=['Likes'])
def likes_of_post(request, post_id: str):
    validation_object_id(post_id)
    res = post.retrive_likes(post_id)
    return {"response": res}


@api.get("/comments/{post_id}", tags=['Comments'])
def comments_of_post(request, post_id: str):
    validation_object_id(post_id)
    res = post.retrive_comments(post_id)
    return {"response": res}


@api.post("/comment/{post_id}", tags=['Comments'])
def new_comment(request, post_id: str, comment_body: CommentSchema):
    validation_object_id(post_id)
    res = post.update_by_comment(post_id, comment_body.dict())
    return {"response": res}
