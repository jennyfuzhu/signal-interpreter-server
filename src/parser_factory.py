
class ParseFactory:
    def __init__(self):
        self._parsers = {}
        self._signal_database_format = None

    def set_signal_database_format(self, signal_database_format):
        self._signal_database_format = signal_database_format

    def register_format(self, signal_database_format, parser):
        self._parsers[signal_database_format] = parser()

    def get_parser(self):
        parser = self._parsers.get(self._signal_database_format)
        if not parser:
            raise ValueError(self._signal_database_format)
        return parser