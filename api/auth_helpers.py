from flask import request


class MissingUserHeaderError(Exception):
    pass


class InvalidUserHeaderError(Exception):
    pass


def get_required_user_id():
    user_id = request.headers.get("X-User-Id")
    if not user_id:
        raise MissingUserHeaderError("Header X-User-Id required")

    try:
        return int(user_id)
    except ValueError:
        raise InvalidUserHeaderError("Header X-User-Id must be an integer")
