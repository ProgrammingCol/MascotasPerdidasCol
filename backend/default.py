from dotenv import load_dotenv
import os

load_dotenv()

#base de datos
USER_NAME = os.environ['USER_NAME']
PASSWORD = os.environ['PASSWORD']
HOST_ADRESS = os.environ['HOST_ADRESS']
PORT = os.environ['PORT']
DATABASE_NAME = os.environ['DATABASE_NAME']
SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER_NAME}:{PASSWORD}@{HOST_ADRESS}:{PORT}/{DATABASE_NAME}'



#auth
SECRET_KEY = os.environ['SECRET_KEY']

