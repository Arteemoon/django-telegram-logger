class TGLogger(object):
    def __init__(self):
        self._to_response = False
        self._messages = []

    def message(self, message):
        self._messages.append(message)

    def __iter__(self):
        self._to_response = not self._to_response
        if self._to_response:
            return iter(self._messages)
        return iter([])

    def __delitem__(self, index):
        del self._messages[index]


