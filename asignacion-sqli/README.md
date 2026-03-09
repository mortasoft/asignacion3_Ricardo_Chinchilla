# Asignación #3 - Desarrollo de aplicaciones seguras

Este repositorio contiene dos versiones de una aplicación web:

- `vulnerable-app/`: versión intencionalmente vulnerable a SQL Injection.
- `secure-app/`: versión corregida mediante validación de entradas y consultas parametrizadas.

## Tecnologías
- Python
- Flask
- MySQL
- Docker Compose

## Ejecución

### Versión vulnerable
```bash
cd vulnerable-app
docker compose up --build
```

Aplicación disponible en: `http://localhost:5000`

### Versión segura
```bash
cd secure-app
docker compose up --build
```

Aplicación disponible en: `http://localhost:5001`

## Detalles de la aplicación
Esta aplicación es un API simple que conecta con una base de datos. 
Para mostrar información en pantalla o guardar información, se deben introducir los parámetros que se muestran en pantalla al iniciar la aplicacion.
El parametro vulnerable es `/users?id=1`
