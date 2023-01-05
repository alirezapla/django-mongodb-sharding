from ninja import NinjaAPI

api = NinjaAPI(title='SocialMedia', version='0.0.1')


@api.get("/")
def root():
    return {"message": "Welcome to Django with MongoDB"}


@api.post("/post")
def new_post(request, a: int, b: int):
    return {"result": a + b}


@api.post("/comment/{post_id}")
def new_comment(request, post_id: str):
    return {"result": post_id}


@api.post("/like/{post_id}")
def like_it(request, post_id: str):
    return {"result": post_id}


@api.get("/posts/{user_id}")
def user_posts(request, user_id: str):
    return {"result": user_id}


@api.get("/likes/{post_id}")
def add(request, post_id: str):
    return {"result": post_id}


@api.get("/comments/{post_id}")
def add(request, post_id: str):
    return {"result": post_id}
