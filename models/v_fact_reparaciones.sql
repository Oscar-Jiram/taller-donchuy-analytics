USE taller_donchuy;

-- Capa de Hechos Denormalizada (Fact Layer)
CREATE OR REPLACE VIEW v_fact_reparaciones AS
SELECT 
    r.reparacion_id,
    c.cliente_id,
    c.cliente AS nombre_cliente,
    c.direccion AS direccion_cliente,
    c.telefono AS telefono_cliente,
    v.vehiculo_id,
    v.matricula,
    v.marca,
    v.modelo,
    s.servicio_id,
    s.servicio AS nombre_servicio,
    s.precio_piezas,
    s.horas_mano_obra,
    (s.horas_mano_obra * 350) AS costo_mano_obra,
    r.importe AS importe_total
FROM reparacion r
INNER JOIN cliente c ON r.cliente_id = c.cliente_id
INNER JOIN vehiculo v ON r.vehiculo_id = v.vehiculo_id
INNER JOIN servicio s ON r.servicio_id = s.servicio_id;