import os
import json
from dotenv import load_dotenv, find_dotenv

load_dotenv()
print(f"- .env: {find_dotenv()}")
print("- reading dd07modules/fsw_config/config.py")
print(f"- FSW_CONFIG_TYPE: {os.environ.get('FSW_CONFIG_TYPE')}")
print(f"- FLASK_DEBUG: {os.environ.get('FLASK_DEBUG')}")


with open(os.path.join(os.environ.get('CONFIG_ROOT'), os.environ.get('CONFIG_FILE_NAME'))) as config_json_file:
    # config_json_dict = json.load(env_file)
    config_json_dict = json.load(config_json_file)
        # os.environ["PROJECT_ROOT"] = "/Users/nick/Documents/exFlaskBlueprintFrameworkStarterWithLogin/"


class ConfigBasic():

    def __init__(self):
        self.SECRET_KEY = config_json_dict.get('SECRET_KEY')

        #Email stuff
        self.MAIL_SERVER = config_json_dict.get('MAIL_SERVER_MSOFFICE')
        self.MAIL_PORT = config_json_dict.get('MAIL_PORT')
        self.MAIL_USE_TLS = True
        self.MAIL_USERNAME = config_json_dict.get('MAIL_EMAIL')
        self.MAIL_PASSWORD = config_json_dict.get('MAIL_PASSWORD')

        #web Guest
        self.GUEST_EMAIL = config_json_dict.get('GUEST_EMAIL')
        self.GUEST_PASSWORD = config_json_dict.get('GUEST_PASSWORD')

        #API
        self.API_URL = os.environ.get("API_URL")

        #Admin stuff
        self.ADMIN_EMAILS = config_json_dict.get('ADMIN_EMAILS')
        self.REGISTRATION_KEY =config_json_dict.get('REGISTRATION_KEY')
        self.BLS_API_URL = config_json_dict.get('BLS_API_URL')

        # # Auxiliary and directories
        # self.PROJECT_RESOURCES = os.environ.get('PROJECT_RESOURCES')
        # self.DIR_LOGS = os.path.join(self.PROJECT_RESOURCES,"logs")
        # self.WEBSITE_FILES = os.path.join(self.PROJECT_RESOURCES,"website_files")
        # self.DIR_WEBSITE_IMAGES = os.path.join(self.WEBSITE_FILES,"website_images")
        # self.DIR_WEBSITE_VIDEOS = os.path.join(self.WEBSITE_FILES,"website_videos")
        # self.DATABASE_HELPERS = os.path.join(self.PROJECT_RESOURCES,"database_helpers")
        # self.DB_UPLOAD = os.path.join(self.DATABASE_HELPERS,"db_upload")

        # DIR_DATABASE
        self.DATABASE_ROOT = os.environ.get('DATABASE_ROOT')
        self.DIR_DB_UPLOAD = os.path.join(self.DATABASE_ROOT,"db_upload")
        # Database
        self.MYSQL_USER = config_json_dict.get('MYSQL_USER')
        self.MYSQL_PASSWORD = config_json_dict.get('MYSQL_PASSWORD')
        ## MySQL
        self.MYSQL_SERVER = config_json_dict.get('MYSQL_SERVER')
        self.MYSQL_DATABASE_NAME = config_json_dict.get('MYSQL_DATABASE_NAME')
        self.MYSQL_DB_URI = f"mysql+pymysql://{self.MYSQL_USER}:{self.MYSQL_PASSWORD}@{self.MYSQL_SERVER}/{self.MYSQL_DATABASE_NAME}"
        ## SQLite
        self.SQLITE_DB_URI = f"sqlite:///{self.DATABASE_ROOT}{os.environ.get('DB_NAME')}"
        self.DB_TYPE=os.environ.get('DB_TYPE')

        # PROJECT_RESOURCES directories
        self.PROJECT_RESOURCES_ROOT = os.environ.get('PROJECT_RESOURCES_ROOT')
        self.DIR_ASSETS = os.path.join(self.PROJECT_RESOURCES_ROOT,"assets")# website files like icons, favicons, other images
        self.DIR_ASSETS_IMAGES = os.path.join(self.DIR_ASSETS,"images")
        self.DIR_ASSETS_FAVICONS = os.path.join(self.DIR_ASSETS,"favicons")
        self.DIR_BLOG = os.path.join(self.PROJECT_RESOURCES_ROOT,"blog")
        self.DIR_BLOG_POSTS = os.path.join(self.DIR_BLOG,"posts")# contains a folder for each posts, 
        # which may contain subfolders such as word_docs, images, and/or videos
        self.DIR_LOGS = os.path.join(self.PROJECT_RESOURCES_ROOT,"logs")# all .log files
        self.DIR_MEDIA = os.path.join(self.PROJECT_RESOURCES_ROOT,"media")

        #Captcha
        self.SITE_KEY_CAPTCHA = config_json_dict.get('SITE_KEY_CAPTCHA')
        self.SECRET_KEY_CAPTCHA = config_json_dict.get('SECRET_KEY_CAPTCHA')
        self.VERIFY_URL_CAPTCHA = 'https://www.google.com/recaptcha/api/siteverify'

        self.LIST_NO_CONFIRMASTION_EMAILS = config_json_dict.get('LIST_NO_CONFIRMASTION_EMAILS')

class ConfigWorkstation(ConfigBasic):
    
    def __init__(self):
        super().__init__()
        # self.PROJECT_ROOT = os.environ.get('PROJECT_LOCAL_ROOT')

    DEBUG = True


class ConfigDev(ConfigBasic):

    def __init__(self):
        super().__init__()

    DEBUG = True
    # SQL_URI = config_json_dict.get('SQL_URI_DEVELOPMENT')
    TEMPLATES_AUTO_RELOAD = True
    # SCHED_CONFIG_STRING = "ConfigDev"
    # CONFIG_TYPE='dev'


class ConfigProd(ConfigBasic):
        
    def __init__(self):
        super().__init__()

    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    # SCHED_CONFIG_STRING = "ConfigProd"
    # CONFIG_TYPE='prod'