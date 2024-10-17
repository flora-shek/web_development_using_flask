import os

class Config(object):
    SECRET_KEY =  os.environ.get('SECRET_KEY') or "secret_string"
    MONGODB_SETTINGS ={'db':'UTA_Enrollment',
                       'username':'florashek24',
                       'password':'5aujbLlxkX76pbxh',
                       'host':"mongodb+srv://florashek24:5aujbLlxkX76pbxh@uta-enrollment.7dmnt.mongodb.net/UTA_Enrollment"
                        }
 