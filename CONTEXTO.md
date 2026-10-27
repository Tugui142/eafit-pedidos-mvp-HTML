# Contexto del proyecto: EAFIT Pedidos

## 1. Propósito
Reducir la congestión y los tiempos de espera en los restaurantes del campus de EAFIT en horas pico, permitiendo a la comunidad universitaria programar, pagar y recibir sus alimentos de forma anticipada.

## 2. Usuarios y tareas principales
- **Estudiantes, profesores y empleados:** Necesitan optimizar su tiempo de descanso (pausas cortas), consultar el menú, evitar las filas y hacer seguimiento transparente a sus pedidos.
- **Restaurantes y emprendedores:** Necesitan gestionar comandas digitales sin colapsar la cocina, limitando cupos por franjas horarias.
- **Personal de entrega (Delivery P2P):** Estudiantes que necesitan hacer entregas exactas en los bloques (ej. "Bloque lectura P1") para generar ingresos extra.

## 3. Evidencia clave de la investigación
- **Hallazgo 1:** Fricción con el flujo rígido de compra -> **Decisión para el sitio:** Diseñar un carrito de compras flexible y acumulativo con un botón claro de "Seguir comprando" antes del checkout.
- **Hallazgo 2:** Incertidumbre logística y ansiedad -> **Decisión para el sitio:** Incorporar una línea de tiempo interactiva (Status Tracker) desde "pedido recibido" hasta "llegó al bloque".
- **Hallazgo 3:** Desorientación de usuarios nuevos -> **Decisión para el sitio:** Implementar una pantalla inicial (Onboarding) que solicite el permiso de ubicación en tiempo real.
- **Hallazgo 4:** Necesidad de ecosistema unificado -> **Decisión para el sitio:** Integrar facilidades financieras como el uso de saldo institucional del carnet (similar a RappiCuenta).

## 4. Alcance del MVP
- **Entra:** Catálogo destacando combos/promociones, Onboarding de ubicación, vista de producto, carrito acumulativo, seguimiento de pedidos (status tracker), panel de gestión y delivery P2P.
- **No entra por ahora:** Integración real con pasarelas de pago bancarias (se simula la vista de pago con carnet/saldo).

## 5. Tecnología y restricciones
- **Tipo de sitio:** Frontend estático (HTML, CSS) con maquetación móvil.
- **Dónde se publica:** GitHub Pages (para el HTML).
- **Analítica:** Google Analytics 4.
- **Referente Visual (Benchmark):** Rappi (visualización de categorías, carrito flexible, pasarela integrada).

## 6. Estructura del sitio
- **restaurantes/nombrederestaurante.html**
- **ajustes.html**
- **catalogo.html**
- **dashboard.html**
- **historial.html**
- **index.html**
- **main.py**
- **pago.html**
- **producto.html**
- **requirements.txt**
- **restaurantes.html**
- **seguimiento.html**
- **style.css**

## 7. Sistema visual
- **Hoja de estilos:** `style.css` (Manejo centralizado de UI y colores).
- **Enfoque:** Diseño responsivo (Mobile First), ya que el celular es el canal principal. El panel para los restaurantes se puede ver en una pantalla horizontal.

## 8. Reglas para la IA
1. Usa los textos exactos que se te entregan. No inventes datos.
2. Si falta información, pregúntame antes de escribir.
3. Muestra un plan antes de codificar.
4. No uses estilos en línea dentro del HTML; todo va a `style.css`.
5. Marca lo pendiente como "Disponible próximamente".

## 9. Estado actual
- **Terminado:** Investigación Lean UX (6 entrevistas), validación mediante Paseo Cognitivo y Escala Likert, Prototipado Colaborativo, análisis benchmark (Rappi) y diseño del MVP funcional.
- **En curso:** Preparación de la entrega final y sustentación.
- **Siguiente paso:** Evaluación Heurística profunda de la interfaz.
- **Última actualización:** 2026-10-27 por Verónica Mejía, Alejandra Fonseca y Juan Pablo Gutiérrez.
