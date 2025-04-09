# 📝 Aplicación de Gestión de Tareas (MVC con Docker)

Esta es una aplicación sencilla de gestión de tareas desarrollada utilizando el patrón de arquitectura **MVC (Modelo - Vista - Controlador)**, contenedores Docker y Flask como backend.

## 🚀 ¿Qué hace esta app?

- Permite agregar nuevas tareas.
- Visualiza la lista de tareas.
- Puedes marcar tareas como completas o incompletas.
- Puedes eliminar tareas.
- Todos los datos se guardan en una base de datos PostgreSQL.

## 🧱 Estructura por contenedores

La aplicación se divide en **3 contenedores independientes**:

1. **Frontend (Vista)**  
   Servido por NGINX, muestra una interfaz web sencilla con HTML, CSS y JS para interactuar con las tareas.

2. **Backend (Controlador + Lógica)**  
   Aplicación Flask que expone una API REST (`/api/tasks`) para manejar operaciones CRUD.

3. **Base de Datos (Modelo)**  
   PostgreSQL como motor de base de datos, con persistencia de tareas.

## 📁 Estructura del proyecto

```bash
.
├── backend/
│   ├── app.py                # Servidor Flask con la lógica de la API
│   ├── requirements.txt      # Dependencias Python
│   └── Dockerfile            # Imagen para el backend
│
├── frontend/
│   ├── index.html            # Interfaz de usuario (Vista)
│   ├── app.js                # Lógica en el navegador (fetch, eventos)
│   ├── style.css             # (opcional) Estilos personalizados
│   ├── nginx.conf            # Configuración de NGINX
│   └── Dockerfile            # Imagen para el frontend
│
├── database/
│   ├── init.sql              # Script para crear tabla de tareas
│   └── Dockerfile (opcional)
│
├── docker-compose.yml        # Orquestador de todos los servicios
└── README.md                 # Este archivo
