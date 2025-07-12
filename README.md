# MulePractice
## dbactions
### Flujos
#### dbinsert-flw
Inserta una prenda.
#### dbqueryone-flw
Consulta una prenda con su id.
#### dbquerymany-flw
Consulta todas las prendas que tengan el tipo indicado en ```attributes.queryParams```
### Esquema
Se utiliza el siguiente esquema:
```sql
-- prueba.prenda definition

CREATE TABLE `prenda` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_tipo` int DEFAULT NULL,
  `nombre` varchar(25) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_tipo` (`id_tipo`),
  CONSTRAINT `prenda_ibfk_1` FOREIGN KEY (`id_tipo`) REFERENCES `tipo` (`id`)
)ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- prueba.tipo definition

CREATE TABLE `tipo` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
```
### Datos
Y estos son los datos ya ingresados:
```sql
INSERT INTO prueba.tipo (nombre) VALUES
	 ('Camiseta'),
	 ('Pantalón'),
	 ('Sudadera'),
	 ('Chaqueta'),
	 ('Short');

INSERT INTO prueba.prenda (id_tipo,nombre) VALUES
	 (1,'Camiseta Blanca'),
	 (2,'Jeans Azul'),
	 (3,'Sudadera Negra'),
	 (4,'Chaqueta Cuero'),
	 (5,'Short Deportivo'),
	 (3,'Sudadera Rosa'),
	 (1,'Camiseta Verde'),
	 (2,'Jeans Blancos'),
	 (2,'Jeans Rosas'),
	 (2,'Jeans Negros'),
	 (2,'Jeans Rotos'),
	 (2,'Jeans Cortos'),
	 (4,'Chaqueta Esponjosa');
```
