import os

from app import create_app


setting_module = os.getenv('APP_SETTING_MODULE')
app = create_app(setting_module=setting_module)
