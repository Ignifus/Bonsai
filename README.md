# Bonsai
Linux and web server diagnostics front end application.

# Dependencies
* Unix
* Python 3.X
* Django (pip)
* Redis-Server (Standalone)
* ASGI_Redis (pip)
* Channels (pip)
* Celery (pip)
* Psutil (pip)
* tcpdump (Standalone)

# Instructions
* Tener debug en false, y la contraseña para la base de datos en settings.py.
* Tener todas las dependencias instaladas
* Correr primero redis-server en una consola y asegurarse que escucha en puerto 6379 (default)
* Correr el proyecto django y asegurarse que no lanza errores en consola.
* Ir a al root del proyecto y en consola correr: celery -A bonsai worker -l info
* Ir a localhost:8000/watchdog y ver la magia. Generen logs del tcpdump metiendose a paginas web o lo que sea.
