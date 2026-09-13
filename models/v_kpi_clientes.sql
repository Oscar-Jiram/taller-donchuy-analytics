USE taller_donchuy;

-- Data Mart: Análisis de Clientes
CREATE OR REPLACE VIEW v_kpi_clientes AS
SELECT 
    cliente_id,
    nombre_cliente,
    COUNT(reparacion_id) AS total_visitas,
    SUM(importe_total) AS gasto_total_cliente,
    ROUND(AVG(importe_total), 2) AS ticket_promedio_cliente
FROM v_fact_reparaciones
GROUP BY cliente_id, nombre_cliente;