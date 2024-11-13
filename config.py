import os

class Config(object):
    SECRET_KEY =  os.environ.get('SECRET_KEY') or b"\xd1\xa0{\xd4f'R'A\x02\xf0FM\xa2\xfb>"
    MONGODB_SETTINGS ={'db':'UTA_Enrollment',
                       'username':'florashek24',
                       'password':'5aujbLlxkX76pbxh',
                       'host':"mongodb+srv://florashek24:5aujbLlxkX76pbxh@uta-enrollment.7dmnt.mongodb.net/UTA_Enrollment"
                        }
 