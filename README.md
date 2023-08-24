# Charla de docker

## Requisitos
- [Git (bash)](https://git-scm.com/downloads)
- [Visual Studio Code](https://code.visualstudio.com/download)
- [Docker](https://www.docker.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Workbench](https://www.mysql.com/products/workbench/) o  similar

## Validacion

```shell
# git version
git -v
# docker version
docker -v
```

--- 

## Objetivo
- Levantar una imagen con MySql
- Crear una base de datos
- Crear una tabla
- Interactuar con la tabla
- Automatizar un poco el proceso

---

## Docker - validacion contenido

### Listado de contenedores
```shell
docker ps -a
```

### Listado de imagenes
```shell
docker images -a
```

### Listado de volumenes
```shell
docker volume ls
```

## Docker - Limpieza

### Eliminar contenedores
```shell
docker stop [nombre_contenedor]
docker rm [nombre_contenedor]
```

### Eliminar volumenes
```shell
docker volume ls
docker volume rm [nombre_o_ID_del_volumen]
docker volume prune
```

### Eliminar imagenes
```shell
docker images
docker stop [nombre_contenedor]
docker rmi [nombre_de_la_imagen]:[etiqueta]
docker image prune -a
```