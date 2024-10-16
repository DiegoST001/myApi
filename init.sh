# Conectar a la base de datos PostgreSQL
# pip install psycopg2-binary

# Conecta a la base de datos por una url
# pip install dj-database-url

# White noise es una librería que sirve para servir archivos estáticos
# pip install 'whitenoise[brotli]'

# Uvicorn es un servidor ASGI que se utiliza para desplegar aplicaciones ASGI
# Gunicorn es un servidor WSGI que se utiliza para desplegar aplicaciones WSGI
# pip install uvicorn
# pip install gunicorn

# Para desplegar la aplicación en producción se debe ejecutar el siguiente comando
# python -m gunicorn myApi.asgi:application -k uvicorn.workers.UvicornWorker