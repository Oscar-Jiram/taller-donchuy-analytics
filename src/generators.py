import random
import pandas as pd
from faker import Faker

fake = Faker('es_MX')


def generate_servicios(n=50) -> pd.DataFrame:
  tipos = ['Cambio', 'Ajuste', 'Revisión', 'Mantenimiento', 'Diagnóstico']
  partes = [
      'Aceite',
      'Frenos',
      'Motor',
      'Filtro',
      'Batería',
      'Bujías',
      'Radiador',
      'Embrague',
      'Amortiguador',
      'Escape',
  ]
  nombres_unicos = set()
  i = 1
  while len(nombres_unicos) < n:
    nombre = f'{random.choice(tipos)} {random.choice(partes)} #{i}'
    nombres_unicos.add(nombre[:25])
    i += 1

  servicios = [
      {
          'servicio': nombre,
          'precio_piezas': random.randint(200, 3500),
          'horas_mano_obra': random.randint(1, 5),
      }
      for nombre in nombres_unicos
  ]
  return pd.DataFrame(servicios)


def generate_clientes(n=50) -> pd.DataFrame:
  clientes = [
      {
          'cliente': fake.name()[:50],
          'direccion': fake.address().replace('\n', ' ')[:50],
          'telefono': fake.random_int(min=1000000000, max=2147483647),
      }
      for _ in range(n)
  ]
  return pd.DataFrame(clientes)


def generate_vehiculos(n=50) -> pd.DataFrame:
  marcas_modelos = {
      'Nissan': ['Sentra', 'Versa', 'Altima'],
      'Toyota': ['Corolla', 'Yaris', 'RAV4'],
      'Volkswagen': ['Jetta', 'Golf', 'Polo'],
      'Ford': ['Focus', 'Fiesta', 'Mustang'],
      'Chevrolet': ['Aveo', 'Onix', 'Cruze'],
  }
  vehiculos = []
  for _ in range(n):
    marca = random.choice(list(marcas_modelos.keys()))
    vehiculos.append({
        'matricula': fake.bothify(text='???-####').upper()[:10],
        'marca': marca[:15],
        'modelo': random.choice(marcas_modelos[marca])[:15],
    })
  return pd.DataFrame(vehiculos)


def generate_reparaciones(
    cliente_ids, vehiculo_ids, servicios_data
) -> pd.DataFrame:
  n = len(cliente_ids)
  c_unicos = random.sample(cliente_ids, n)
  v_unicos = random.sample(vehiculo_ids, n)
  s_unicos = random.sample(servicios_data, n)

  reparaciones = []
  costo_hora = 350

  for i in range(n):
    serv_id, precio_p, hrs_mo = s_unicos[i]
    importe_total = precio_p + (hrs_mo * costo_hora)
    reparaciones.append({
        'cliente_id': c_unicos[i],
        'vehiculo_id': v_unicos[i],
        'servicio_id': serv_id,
        'importe': float(importe_total),
    })

  return pd.DataFrame(reparaciones)