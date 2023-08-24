# MySQL - Consola

## Creando contenedor MySql 

Pasos
- Definimos un nombre para el contenedor: **bd-mysql** (--name: nombre del contenedor)
- Definimos una clave para la BD: **clave_root** (-e: variable de entorno)
- Definimos el puerto que expondremos (interno/externo): **3306:3306** (-p: puerto)
- Definimos que imagen de docker y que version usaremos: **mysql:latest** (-d: imagen)

```shell
docker run --name bd-mysql -e MYSQL_ROOT_PASSWORD=clave_root -p 3306:3306 -d mysql:latest
```

## Verificamos nuestros contenedores
```shell
docker ps
```

## Verificamos si esta activa la instancia de la BD en su puerto
```shell
netstat -an | grep 3306
```

## Accedemos al contenedor de la BD

- docker exec -it **[nombre_contenedor]**
- comandos para el contenedor: mysql -uroot -pclave_root
- **-u** es el usuario 'root' en este caso
- **-p** es la clave, 'clave_root' en este caso

```shell
docker exec -it mysql-01 mysql -uroot -pclave_root
```

### Ya en la terminal:

- Listamos las BD 
```shell
SHOW DATABASES;
```

- Creamos una BD
```shell
CREATE DATABASE CHARLA;
```

## Detenemos el contenedor
```shell
docker stop bd-mysql
```

## Elinminamos el contenedor
```shell
docker rm bd-mysql
```