-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: segwaydb
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `segway`
--

DROP TABLE IF EXISTS `segway`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `segway` (
  `id` int NOT NULL AUTO_INCREMENT,
  `modelo` varchar(50) NOT NULL,
  `encendida` tinyint(1) NOT NULL,
  `velocidad` int NOT NULL,
  `autonomia` decimal(4,1) NOT NULL,
  `aceleracion` int NOT NULL,
  `velocidad_maxima` int NOT NULL,
  `fabricante_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fabricante_id` (`fabricante_id`),
  CONSTRAINT `segway_ibfk_1` FOREIGN KEY (`fabricante_id`) REFERENCES `fabricante` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `segway`
--

LOCK TABLES `segway` WRITE;
/*!40000 ALTER TABLE `segway` DISABLE KEYS */;
INSERT INTO `segway` VALUES (1,'Segway Modelo A',1,10,6.4,10,40,1),(2,'Segway Modelo B',1,20,6.3,10,40,2),(3,'Segway Modelo C',1,30,6.2,10,40,3),(4,'Segway Modelo D',1,40,6.1,10,40,1),(5,'Segway Modelo E',0,0,6.0,10,40,2),(6,'Segway Modelo F',1,10,6.4,10,40,3),(7,'Segway Modelo G',1,20,6.3,10,40,1),(8,'Segway Modelo H',1,30,6.2,10,40,2),(9,'Segway Modelo I',1,40,6.1,10,40,3),(10,'Segway Modelo J',0,0,6.0,10,40,1);
/*!40000 ALTER TABLE `segway` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-08 14:35:32
