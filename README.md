# Tarea 2 - API de Gestión de Biblioteca con Litestar

Este proyecto implementa una API REST completa para la gestión de una biblioteca, desarrollada utilizando el framework **Litestar**, **SQLAlchemy** para el ORM y **MySQL** como base de datos relacional.

## 📋 Descripción del Proyecto
El sistema permite administrar usuarios, libros, categorías, préstamos y reseñas. Incluye lógica de negocio avanzada como cálculo automático de fechas de vencimiento, multas por atraso, control de stock y validaciones de datos mediante DTOs.

## 🛠️ Decisiones de Diseño
* **Motor de Base de Datos:** Se utilizó **MySQL** (vía driver `pymysql`) debido a la disponibilidad del entorno de desarrollo local, reemplazando la configuración por defecto de PostgreSQL.
* **Migraciones:** Se implementó **Alembic** para el control de versiones del esquema de la base de datos.
* **Patrón de Diseño:** Se utilizó el patrón **Controlador-Repositorio** para separar la lógica de negocio de la capa de acceso a datos.
* **Validaciones:** Se configuraron **DTOs (Data Transfer Objects)** estrictos para controlar qué datos entran y salen de la API, protegiendo campos sensibles como contraseñas y calculados como las multas.

## ✅ Tabla de Cumplimiento de Requerimientos

| Requerimiento | Estado | Observación |
| :--- | :---: | :--- |
| **1. Modelo Category (M-to-M)** | Cumplido | Implementada tabla intermedia `book_categories` y endpoints CRUD. |
| **2. Modelo Review** | Cumplido | Implementado con validación de rating (1-5) y relaciones con User/Book. |
| **3. Actualizar Book** | Cumplido | Agregados campos `stock`, `publisher`, `language`. Validación de stock positivo. |
| **4. Actualizar User** | Cumplido | Agregados campos `email`, `phone`, `address`. Validación regex para email. |
| **5. Actualizar Loan** | Cumplido | Enum `LoanStatus`, cálculo de `due_date` (+14 días) y `fine_amount`. |
| **6. BookRepository** | Cumplido | Métodos: búsqueda por autor, filtro por categoría, top reseñas y stock disponible. |
| **7. LoanRepository** | Cumplido | Lógica de negocio para: multas ($500/día), devoluciones y actualizar stock. |
| **8. Base de Datos Inicial** | Cumplido | Se incluye script `semilla.py` y respaldo `initial_data.sql` con datos reales. |

## 🚀 Instrucciones de Instalación y Ejecución

Sigue estos pasos para levantar el proyecto desde cero:

### 1. Preparar el Entorno
Crear y activar el entorno virtual e instalar las dependencias:
```bash
# Crear entorno
py -m venv venv

# Activar (Windows)
.\venv\Scripts\Activate

# Instalar librerías
pip install litestar[standard] uvicorn sqlalchemy alembic asyncpg pymysql cryptography pydantic-settings advanced-alchemy pyjwt pwdlib argon2-cffi

2. Configurar Base de Datos
Crear una base de datos vacía en MySQL llamada library_db.

3. Ejecutar Migraciones
Generar las tablas en la base de datos usando Alembic:

python -m alembic upgrade head

4. Iniciar el Servidor

litestar run

La API estará disponible en: http://127.0.0.1:8000/schema/swagger

📂 Estructura del Proyecto
app/controllers: Endpoints de la API (Rutas).

app/models: Definición de tablas SQLAlchemy.

app/repositories: Lógica de negocio y consultas a la BD.

app/dtos: Esquemas de validación de entrada/salida.

migrations/: Archivos de control de versiones de BD.

initial_data.sql: Respaldo completo de la base de datos exigido.
