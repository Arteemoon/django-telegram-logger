from distutils.core import setup
setup(
  name = 'django-telegram-logger',
  packages = ['telegram_logger'],
  version = '0.1',
  license='MIT',
  description = '',
  author = 'Arteemoon',
  author_email = 'ivasheco45@gmail.com',
  url = 'https://github.com/Arteemoon',
  download_url = 'https://github.com/Arteemoon/django-telegram-logger/archive/v_01.tar.gz',
  keywords = ['logger', 'telegram', 'django'],
  install_requires=[
          'pyTelegramBotAPI',
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)