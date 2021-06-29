exit_code = 0


class JsonError(Exception):
    """Json error"""

    def __init__(self, message):
        self.message = message
        global exit_code
        exit_code = 10


class GetTitleError(Exception):
    """Get title error"""

