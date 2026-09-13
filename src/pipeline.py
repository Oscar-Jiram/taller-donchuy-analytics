import logging
import pandas as pd
from sqlalchemy import text
from config.database import get_engine
from src.generators import (
    generate_clientes,
    generate_reparaciones,
    generate_servicios,
    generate_vehiculos,
)


def run_pipeline():
  logging.info('🚀 Iniciando ejecución del pipeline modular ETL...')
  engine = get_engine()

  # 1. Limpieza de tablas (Idempotencia)
  with engine.begin() as conn:
    conn.execute(text('SET FOREIGN_KEY_CHECKS = 0;'))
    conn.execute(text('TRUNCATE TABLE reparacion;'))
    conn.execute(text('TRUNCATE TABLE vehiculo;'))
    conn.execute(text('TRUNCATE TABLE cliente;'))
    conn.execute(text('TRUNCATE TABLE servicio;'))
    conn.execute(text('SET FOREIGN_KEY_CHECKS = 1;'))
  logging.info('🧹 Tablas limpiadas correctamente.')

  # 2. Ingesta de Servicios
  df_servicios = generate_servicios(50)
  df_servicios.to_sql(
      name='servicio', con=engine, if_exists='append', index=False
  )
  logging.info('✅ Tabla SERVICIO poblada con 50 registros.')

  # 3. Ingesta de Clientes
  df_clientes = generate_clientes(50)
  df_clientes.to_sql(
      name='cliente', con=engine, if_exists='append', index=False
  )
  logging.info('✅ Tabla CLIENTE poblada con 50 registros.')

  # 4. Ingesta de Vehículos
  df_vehiculos = generate_vehiculos(50)
  df_vehiculos.to_sql(
      name='vehiculo', con=engine, if_exists='append', index=False
  )
  logging.info('✅ Tabla VEHICULO poblada con 50 registros.')

  # 5. Extracción de IDs e Ingesta de Reparaciones
  with engine.connect() as conn:
    c_ids = [
        r[0]
        for r in conn.execute(text('SELECT cliente_id FROM cliente')).fetchall()
    ]
    v_ids = [
        r[0]
        for r in conn.execute(
            text('SELECT vehiculo_id FROM vehiculo')
        ).fetchall()
    ]
    s_data = conn.execute(
        text('SELECT servicio_id, precio_piezas, horas_mano_obra FROM servicio')
    ).fetchall()

  df_reparaciones = generate_reparaciones(c_ids, v_ids, s_data)
  df_reparaciones.to_sql(
      name='reparacion', con=engine, if_exists='append', index=False
  )
  logging.info(
      '✅ Tabla REPARACION poblada con 50 registros (Restricciones 1:1'
      ' respetadas).'
  )

  logging.info('🎉 Pipeline completado con éxito.')