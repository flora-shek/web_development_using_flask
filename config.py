import os

class Config(object):
    SECRET_KEY =  os.environ.get('SECRET_KEY') or b"\xd1\xa0{\xd4f'R'A\x02\xf0FM\xa2\xfb>"
    MONGODB_SETTINGS ={'db':os.environ.get('m_db'),
                       'username':os.environ.get('m_user'),
                       'password':os.environ.get('m_pass'),
                       'host':os.environ.get('m_host'),
                        }
 