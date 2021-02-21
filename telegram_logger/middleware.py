from django.conf import settings
from telebot import TeleBot
from .exceptions import TokenNotFoundException, UserNotFound, SendMessageError
from .tg_logger import TGLogger
from telebot.apihelper import ApiException


class TelegramLoggerMiddleware(object):
    """Add TGLogger object in request"""
    def __init__(self, get_response):
        self.get_response = get_response
        self.tg_logger = TGLogger()
        self.__dict__.update(getattr(settings, 'TELEGRAM_LOGGER_CONF', {}))
        self._create_user_id()
        self._create_bot()

    def _create_bot(self):
        token = getattr(self, 'TOKEN_BOT', None)
        if not token:
            raise TokenNotFoundException('Add token bot in settings!')
        self.bot = TeleBot(token=token)

    def _create_user_id(self):
        user_id = getattr(self, 'USER_ID', None)
        if not user_id:
            raise UserNotFound('Add User ID in settings!')
        self.user_id = user_id

    def __call__(self, request):
        request.tg_logger = self.tg_logger
        response = self.get_response(request)
        for index, message in enumerate(request.tg_logger):
            try:
                self.bot.send_message(self.user_id, message)
                del request.tg_logger[index]
            except ApiException:
                raise SendMessageError('Maybe you down write bot first message')

        return response

    def process_exception(self, request, exception):
        if getattr(self, 'SEND_EXCEPTION', None):
            self.bot.send_message(self.user_id, str(exception))



