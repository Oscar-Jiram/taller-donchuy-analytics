import logging
from src.pipeline import run_pipeline

if __name__ == '__main__':
  try:
    run_pipeline()
  except Exception as e:
    logging.error(f'❌ El pipeline falló durante la ejecución: {e}')