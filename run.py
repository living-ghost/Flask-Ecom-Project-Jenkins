import os
import dotenv
from app import create_app


dotenv.load_dotenv()


config_name = os.getenv('FLASK_CONFIG')


app = create_app(config_name)


if __name__=='__main__':
    app.run(debug=True)