# MulePractice
## dbactions💾
```dbactions``` es una app Mule con tres flujos: [dbinsert-flw](#dbinsert-flw), [dbqueryone-flw](#dbqueryone-flw) y [dbquerymany-flw](#dbquerymany-flw).
### Flujos🔃
#### dbinsert-flw
1. Recibe una solicitud HTTP POST como la siguiente:

![Ejemplo insert.](https://github.com/ana-rosales/MulePractice/blob/main/readme/insert-eg.png)

3. Inserta la prenda indicada.
#### dbqueryone-flw
1. Cada 5 segundos revisa si hay una prenda nueva registrada.
2. Si la hay, muestra en consola: el ```id```, el ```nombre``` y el ```tipo``` de la prenda, por ejemplo:
```
Prenda ingresada: [{id=14, prenda=Short Diamantado, tipo=Short}]
```
#### dbquerymany-flw
1. Recibe una solicitud HTTP GET con ```attributes.queryParams.tipos```.
2. Trae de la BD todas las prendas que tengan el tipo indicado en los parámetros.
3. Los devuelve en la respuesta HTTP.

![Ejemplo insert.](https://github.com/ana-rosales/MulePractice/blob/main/readme/query-eg.png)
### Esquema🔨
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
### Datos🛠️
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
