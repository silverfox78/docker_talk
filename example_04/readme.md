# API Python

## Requisitos

```shell
pip install Flask
pip install python-dotenv
```

## Codigo

```python
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_data():
    parametro = request.args.get('parametro', None)
    dato = os.getenv("DATO", "NULO")
    if not parametro:
        return jsonify({"error": "Parametro no proporcionado"}), 400
    return jsonify({"parametro": parametro, "dato": dato})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
```

## Ejecutar el Dockerfile

```shell
docker build -t miapi:latest .
docker run -p 5000:5000 miapi:latest
```

---

## Levantamos el contenedor
```shell
# docker-compose up -d
docker-compose -p bd-mysql up -d --build
```

> Que es el [-d], es el 'detached mode' que es basicamente para ejecutar el comando en segundo plano

## Ver los logs de la instalacion
```shell
docker-compose logs
```

## Verificamos nuestros contenedores
```shell
docker ps
```

## Verificamos si esta activa la instancia de la BD en su puerto
```shell
netstat -an | grep 3306
```

## Bajamos el contenedor
```shell
docker-compose down
```