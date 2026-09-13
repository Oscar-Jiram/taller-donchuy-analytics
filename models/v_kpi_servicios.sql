USE taller_donchuy;

-- Data Mart: KPIs por Tipo de Servicio
CREATE OR REPLACE VIEW v_kpi_servicios AS
SELECT 
    nombre_servicio,
    COUNT(reparacion_id) AS total_reparaciones,
    SUM(precio_piezas) AS ingresos_piezas,
    SUM(costo_mano_obra) AS ingresos_mano_obra,
    SUM(importe_total) AS ingresos_totales,
    ROUND(AVG(importe_total), 2) AS ticket_promedio
FROM v_fact_reparaciones
GROUP BY nombre_servicio;