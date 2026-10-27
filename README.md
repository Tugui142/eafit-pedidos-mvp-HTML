# EAFIT Pedidos (Restaurantes EAFIT)
Plataforma web para la gestión de pedidos anticipados en los restaurantes de la Universidad EAFIT.

**Sitio publicado:** https://tugui142.github.io/eafit-pedidos-mvp-HTML/
**Repositorio:** https://github.com/Tugui142/eafit-pedidos-mvp-HTML
**Equipo:** Verónica Mejía, Alejandra Fonseca, Juan Pablo Gutiérrez Quintero
**Curso:** Experiencia de Usuario - Semestre 2026-2
**Universidad:** Universidad EAFIT

## Qué es
EAFIT Pedidos soluciona el problema de las largas filas y el colapso logístico en los restaurantes del campus universitario durante las horas pico. Inspirado en modelos como Rappi, permite a la comunidad programar la recogida de sus alimentos, pagar con el saldo del carnet institucional y ofrece un sistema de delivery colaborativo (Peer-to-Peer) donde los mismos estudiantes realizan entregas exactas en los bloques para generar ingresos extra.

## Cómo ver el sitio en tu computador
1. Descarga o clona la carpeta del proyecto.
2. Abre el archivo `index.html` en el navegador web.

## Cómo se publica
**Servicio:** GitHub Pages
**Pasos:** Hacer *commit* y *push* de los archivos a la rama `main`. GitHub Pages publica automáticamente la actualización.
**Administra la cuenta:** Juan Pablo Gutiérrez Quintero

## Analítica y privacidad
**Herramienta:** Google Analytics 4
**Eventos medidos:** Páginas vistas, clics (especialmente en botones de "Seguir comprando") y desplazamientos.
**Dónde ver los datos:** Panel de Google Analytics de la cuenta (Propiedad EAFIT Pedidos).
**Fecha de activación:** 2026-10-20
**Aviso de privacidad y consentimiento:** Incluido como banner/texto en la plataforma web y solicitud de permisos de ubicación en el Onboarding.

## Estructura de la carpeta
```
eafit-pedidos-mvp-HTML/
├── README.md               (Este archivo)
├── CONTEXTO.md             (Contexto del proyecto para la IA)
├── BITACORA.md             (Decisiones y uso de IA)
├── index.html              (Página de inicio, Onboarding y mapa)
├── ajustes.html            (Ajustes de usuario)
├── catalogo.html           (Exploración de platos y combos)
├── dashboard.html          (Panel de gestión para restaurantes)
├── historial.html          (Compras anteriores)
├── pago.html               (Carrito acumulativo, checkout y turnos)
├── producto.html           (Personalización del plato)
├── restaurantes.html       (Lista de restaurantes)
├── seguimiento.html        (Status tracker / Estado del pedido)
├── restaurantes/           (Páginas específicas de locales)
├── style.css               (Hoja de estilos principal)
├── main.py                 (Backend API FastAPI)
└── requirements.txt        (Dependencias backend)
```

## Uso de IA
**Herramientas:** Gemini y NotebookLM
**Para qué se usaron:** Generación de la estructura base HTML, guía de implementación de Google Analytics y consolidación de la documentación final a partir de los hallazgos de las pruebas Lean UX.
**Qué decidió el equipo sin la IA:** La investigación de usuarios (6 entrevistas a estudiantes), la ejecución del Paseo Cognitivo, la aplicación de la Escala Likert, el Prototipado Colaborativo y el análisis de Benchmark con Rappi.
Registro completo: ver `BITACORA.md`.

## Créditos y licencias
**Tipografías:** Fuentes de sistema estándar y Google Fonts.
**Otros recursos:** FastAPI para prototipado del backend.
