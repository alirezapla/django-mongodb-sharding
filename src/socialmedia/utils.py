from ninja.errors import HttpError


def rise_http_exception_if_notfound(result, message: str):
    if result is None:
        raise HttpError(404, "message")


def validation_object_id(object_id: str):
    if len(object_id) != 24:
        raise HttpError(422, "ObjectId must be 24-character")
