# Bitácora del proyecto: EAFIT Pedidos

## 2026-09-22 Verónica Mejía, Alejandra Fonseca, Juan Pablo Gutiérrez
- **Objetivo del cambio:** Validar las hipótesis principales y la interfaz del MVP mediante un flujo de experimentación Lean UX (Entrevistas, Paseo Cognitivo, Escala Likert y Prototipado Colaborativo).
- **Prompt clave:** N/A (Experimento realizado con usuarios reales).
- **Qué produjo la IA:** N/A.
- **Decisión del equipo:** Aceptado y ajustado. Se entrevistaron a 6 estudiantes. Se decidió implementar un "Onboarding" para solicitar permisos de ubicación, flexibilizar el carrito de compras agregando el botón "Seguir comprando" (evitando redirigir prematuramente al pago) y crear un "Status Tracker" para mitigar la ansiedad de espera. También se integró un benchmark basado en Rappi para el sistema de Delivery P2P y pagos con saldo universitario.
- **Evidencia que lo sustenta:** Resultados de las entrevistas y el Paseo Cognitivo donde los usuarios expresaron fricción con el carrito rígido y necesidad de certidumbre en los tiempos de entrega.
- **Archivos modificados:** Presentación "Restaurantes EAFIT.pdf" (Sistematización de resultados) y bocetos en papel.
- **Verificación:** Evaluaciones positivas casi perfectas (4.5 a 5.0) en la escala Likert por parte de los usuarios recurrentes.

## 2026-10-10 Verónica Mejía, Alejandra Fonseca, Juan Pablo Gutiérrez
- **Objetivo del cambio:** Maquetar el esqueleto del sitio web basado en los hallazgos del Prototipado Colaborativo.
- **Prompt clave:** Asistencia en la generación de layouts básicos responsivos incorporando carrito acumulativo, mapa no invasivo y línea de tiempo de estado de pedido.
- **Qué produjo la IA:** Archivos `.html` con la estructura base solicitada.
- **Decisión del equipo:** Ajustado. Se refinaron los componentes para que el "Status Tracker" y el flujo del carrito reflejaran exactamente el modelo mental del estudiante (ej. entrega en "Bloque Lectura"). Se extrajeron los estilos a `style.css`.
- **Evidencia que lo sustenta:** Propuestas visuales co-creadas por los usuarios durante las sesiones de prototipado colaborativo.
- **Archivos modificados:** `index.html`, `pago.html`, `seguimiento.html`, `style.css`.
- **Verificación:** Pruebas de usabilidad responsiva en celular (375px).

## 2026-10-20 Equipo de Desarrollo
- **Objetivo del cambio:** Integrar herramientas de analítica y documentar el proyecto para publicación.
- **Prompt clave:** ¿Cómo integro el Google Tag en mi repositorio de GitHub y redacto los documentos finales con la investigación previa?
- **Qué produjo la IA:** Código exacto de inserción de GA4 y consolidación de `README.md`, `CONTEXTO.md` y `BITACORA.md`.
- **Decisión del equipo:** Aceptado. Se integró el script en el `<head>` de todos los HTML. Se revisaron los documentos finales para asegurar que incluyeran a todo el equipo (Verónica, Alejandra y Juan Pablo) y el semestre (2026-2).
- **Evidencia que lo sustenta:** Requisitos de la guía de entrega y directrices de medición UX.
- **Archivos modificados:** Todos los archivos `.html` y `.md` del repositorio.
- **Verificación:** Tráfico detectado en consola de Google Analytics y estructura de repositorio completa.

## 2026-11-11 Equipo de Desarrollo
- **Objetivo del cambio:** Separar el seguimiento por rol (comprador, repartidor, emprendedor), quitar al comprador el acceso a las vistas de delivery y emprendimiento, y agregar Hotjar.
- **Prompt clave:** Revisar el flujo y la lógica del seguimiento; `seguimiento1` para el cliente, `seguimiento2` para el delivery y `seguimiento3` para el emprendedor; agregar el código de Hotjar.
- **Qué produjo la IA:** Revisión del flujo con la lista de problemas encontrados; reescritura de `seguimientos/seguimiento1.html`, `seguimiento2.html` y `seguimiento3.html`; ajustes de estados en los paneles; inserción del código de Hotjar y actualización de los documentos.
- **Decisión del equipo:** Aceptado. `seguimiento1` es del comprador y adapta su línea de tiempo a la modalidad de entrega; `seguimiento2` es del repartidor; `seguimiento3` es del emprendedor. Se eliminó `seguimiento.html` y los botones de rol del menú del comprador. Se quitaron los simuladores de estado de la vista del cliente. El carrito con restaurante y emprendimiento se divide en dos pedidos.
- **Evidencia que lo sustenta:** Revisión del flujo: el comprador veía botones hacia delivery y emprendedor, y varios estados (casillero depositado, listo en mostrador, entrega en punto fijo) no tenían quién los avanzara sin los simuladores.
- **Archivos modificados:** `seguimientos/seguimiento1.html`, `seguimientos/seguimiento2.html`, `seguimientos/seguimiento3.html`, `dashboard.html`, `delivery.html`, `emprendedor.html`, `pago.html`, `historial.html`, `catalogo.html`, todos los `.html` (Hotjar), `README.md`, `CONTEXTO.md`, `BITACORA.md`. Eliminado: `seguimiento.html`.
- **Verificación:** Pendiente la prueba manual del flujo completo en celular (375px) y la confirmación de datos en el panel de Hotjar.

