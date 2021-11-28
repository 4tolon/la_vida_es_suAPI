import sqlalchemy as alch
import os
import dotenv

dotenv.load_dotenv()

password = os.getenv('pass_sql')
dbName="LaVidaEsSueno"
connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
engine = alch.create_engine(connectionData)