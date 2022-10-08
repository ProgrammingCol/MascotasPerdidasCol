
import os,sys
from dotenv import load_dotenv
from app import create_app


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
load_dotenv()


settings_module = os.getenv('APP_SETTINGS_MODULE')

app=create_app(settings_module)
# if __name__ == '__main__':
    # app.run()