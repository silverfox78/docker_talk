# BD MySQL - Docker Compose

## Creamos el archivo 'docker-compose.yml'

```yml
version: "3.9"
name: bd-mysql

services:
  bd-mysql:
    container_name: bd-mysql
    image: mysql:8.0
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: clave_root
      MYSQL_DATABASE: CHARLA
      MYSQL_USER: admin
      MYSQL_PASSWORD: clave_admin
    volumes:
      - mysql-data:/var/lib/mysql
    ports:
      - "3306:3306"
    networks:
      - network-public

networks:
  network-public:
    driver: bridge

volumes:
  mysql-data:
    driver: local
```

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