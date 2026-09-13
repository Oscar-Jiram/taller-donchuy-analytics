import logging
import os
import sys
from sqlalchemy import create_engine

# --- CONFIGURACIÓN DE LOGS ---
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, 'execution.log')

# Handlers explícitos con UTF-8 para evitar errores de codificación en Windows
file_handler = logging.FileHandler(LOG_FILE, encoding='utf-8')
stream_handler = logging.StreamHandler(sys.stdout)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[file_handler, stream_handler],
)

# --- CREDENCIALES Y CONEXIÓN A MYSQL ---
DB_USER = 'dev_python'
DB_PASS = 'oscar123'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'taller_donchuy'

DATABASE_URL = (
    f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
)


def get_engine():
  """Crea y retorna el motor de conexión a la base de datos."""
  try:
    engine = create_engine(DATABASE_URL)
    return engine
  except Exception as e:
    logging.error(f'Error al crear el engine de base de datos: {e}')
    raise e