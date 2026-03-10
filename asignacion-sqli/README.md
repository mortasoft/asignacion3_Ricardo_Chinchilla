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

## Pruebas de SQL Injection (App Vulnerable)

Puedes probar las siguientes inyecciones en la aplicación vulnerable (puerto 5000):

### 1. Inyección en Parámetro GET (Extraer todos los usuarios)
Accede a la siguiente URL para obtener todos los registros de la tabla `users` mediante una condición siempre verdadera:

`http://localhost:5000/users?id=1 OR 1=1`

### 2. Bypass de Login (POST)
Simula un inicio de sesión exitoso sin conocer la contraseña del administrador usando el carácter de comentario (`-- `):

- **URL:** `http://localhost:5000/login`
- **Body (form-data):**
  - `username`: `admin' -- `
  - `password`: `cualquiera`

**Ejemplo con cURL:**
```bash
curl -X POST -F "username=admin' -- " -F "password=x" http://localhost:5000/login
```

### 3. UNION-based Inyección (Extraer nombres de tablas)
Utiliza `UNION` para extraer información administrativa del esquema de la base de datos:

`http://localhost:5000/users?id=1 UNION SELECT 1, table_name, 'info', 'schema' FROM information_schema.tables`

## Mitigación (App Segura)
La versión en `secure-app/` mitiga estos ataques utilizando **consultas parametrizadas (Prepared Statements)**, lo que impide que la entrada del usuario sea interpretada como código SQL. Intenta los mismos ataques en `http://localhost:5001` para verificar que ya no funcionan.
