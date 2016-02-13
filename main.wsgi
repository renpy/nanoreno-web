import os
import logging
from logging.handlers import SMTPHandler

import sys

PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PATH)

import main
application = main.create_app()

mail_handler = SMTPHandler(
    ("127.0.0.1", 25),
    'no-reply@ntcip.solartechnology.com',
    [ "trothamel@solartechnology.com" ],
    'interview.sthosts.net web error',
    )

mail_handler.setLevel(logging.ERROR)
application.logger.addHandler(mail_handler)
