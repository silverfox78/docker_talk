# MySql - Creacion de data

## ROOT - Accedemos al contenedor de la BD

- docker exec -it **[nombre_contenedor]**, en este caso 'bd-mysql'
- comandos para el contenedor: mysql -uroot -pclave_root
- **-u** es el usuario 'root' en este caso
- **-p** es la clave, 'clave_root' en este caso

```shell
docker exec -it bd-mysql mysql -uroot -pclave_root
```

## ADMIN - Accedemos al contenedor de la BD

> GRANT ALL PRIVILEGES ON CHARLA.*  TO 'admin'@'localhost';

- docker exec -it **[nombre_contenedor]**, en este caso 'bd-mysql'
- comandos para el contenedor: mysql -uadmin -pclave_admin
- **-u** es el usuario 'admin' en este caso
- **-p** es la clave, 'clave_admin' en este caso

```shell
docker exec -it bd-mysql mysql -uadmin -pclave_admin
```

---

## Ya en la terminal:

- Listamos las BD 
```shell
SHOW DATABASES;
```

- Creamos una BD
```shell
CREATE DATABASE CHARLA;
```

- Usamos la BD que creamos:
```shell
USE CHARLA;
```

- Creamos una tabla:
```shell
CREATE TABLE alumnos (id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(30) NOT NULL);
```

- Listamos las tablas:
```shell
SHOW TABLES;
```

- Vemos la descripcion de la tabla 'Alumnos':
```shell
DESCRIBE alumnos;
```

- Insertamos un registro
```shell
INSERT INTO alumnos (nombre) VALUES ('John Doe');
```

- Consultamos los registros
```shell
SELECT * FROM alumnos;
```

- Salimos de la consila
```shell
EXIT;
```