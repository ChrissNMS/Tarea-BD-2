-- MySQL dump 10.13  Distrib 8.0.42, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: library_db
-- ------------------------------------------------------
-- Server version	9.3.0

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
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL,
  PRIMARY KEY (`version_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('d3eac9ff46c7');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book_categories`
--

DROP TABLE IF EXISTS `book_categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book_categories` (
  `book_id` int NOT NULL,
  `category_id` int NOT NULL,
  PRIMARY KEY (`book_id`,`category_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `book_categories_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`),
  CONSTRAINT `book_categories_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book_categories`
--

LOCK TABLES `book_categories` WRITE;
/*!40000 ALTER TABLE `book_categories` DISABLE KEYS */;
INSERT INTO `book_categories` VALUES (3,1),(4,1),(2,2),(5,2),(6,2),(7,3),(9,3),(10,4),(1,5),(8,5);
/*!40000 ALTER TABLE `book_categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `books` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `author_id` int NOT NULL,
  `stock` int NOT NULL,
  `description` text,
  `language` varchar(2) NOT NULL,
  `publisher` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `books`
--

LOCK TABLES `books` WRITE;
/*!40000 ALTER TABLE `books` DISABLE KEYS */;
INSERT INTO `books` VALUES (1,'Libro Ejemplo 1',1,5,NULL,'es','Editorial UMAG'),(2,'Libro Ejemplo 2',1,5,NULL,'es','Editorial UMAG'),(3,'Libro Ejemplo 3',1,5,NULL,'es','Editorial UMAG'),(4,'Libro Ejemplo 4',1,5,NULL,'es','Editorial UMAG'),(5,'Libro Ejemplo 5',1,5,NULL,'es','Editorial UMAG'),(6,'Libro Ejemplo 6',1,5,NULL,'es','Editorial UMAG'),(7,'Libro Ejemplo 7',1,5,NULL,'es','Editorial UMAG'),(8,'Libro Ejemplo 8',1,5,NULL,'es','Editorial UMAG'),(9,'Libro Ejemplo 9',1,5,NULL,'es','Editorial UMAG'),(10,'Libro Ejemplo 10',1,5,NULL,'es','Editorial UMAG');
/*!40000 ALTER TABLE `books` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `description` text,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'Ficción','Libros de Ficción'),(2,'No Ficción','Libros de No Ficción'),(3,'Ciencia','Libros de Ciencia'),(4,'Historia','Libros de Historia'),(5,'Fantasía','Libros de Fantasía');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `loans`
--

DROP TABLE IF EXISTS `loans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `loans` (
  `id` int NOT NULL AUTO_INCREMENT,
  `loan_date` date NOT NULL,
  `return_date` date DEFAULT NULL,
  `due_date` date NOT NULL,
  `fine_amount` decimal(10,2) DEFAULT NULL,
  `status` enum('ACTIVE','RETURNED','OVERDUE') NOT NULL,
  `user_id` int NOT NULL,
  `book_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `book_id` (`book_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `loans_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`),
  CONSTRAINT `loans_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `loans`
--

LOCK TABLES `loans` WRITE;
/*!40000 ALTER TABLE `loans` DISABLE KEYS */;
INSERT INTO `loans` VALUES (1,'2025-11-22',NULL,'2025-12-06',0.00,'ACTIVE',5,5),(2,'2025-11-09','2025-12-05','2025-11-23',0.00,'RETURNED',1,6),(3,'2025-12-03',NULL,'2025-12-17',0.00,'OVERDUE',4,10),(4,'2025-12-04',NULL,'2025-12-18',0.00,'ACTIVE',2,8),(5,'2025-11-11','2025-12-05','2025-11-25',0.00,'RETURNED',2,9),(6,'2025-11-28',NULL,'2025-12-12',0.00,'OVERDUE',3,5),(7,'2025-11-28',NULL,'2025-12-12',0.00,'ACTIVE',1,8),(8,'2025-12-01','2025-12-05','2025-12-15',0.00,'RETURNED',2,1);
/*!40000 ALTER TABLE `loans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` int NOT NULL AUTO_INCREMENT,
  `rating` int NOT NULL,
  `comment` text NOT NULL,
  `review_date` date NOT NULL,
  `user_id` int NOT NULL,
  `book_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `book_id` (`book_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`book_id`) REFERENCES `books` (`id`),
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,2,'Excelente libro muy recomendado.','2025-12-05',4,9),(2,4,'Excelente libro muy recomendado.','2025-12-05',4,5),(3,3,'Excelente libro muy recomendado.','2025-12-05',4,5),(4,3,'Excelente libro muy recomendado.','2025-12-05',2,9),(5,3,'Excelente libro muy recomendado.','2025-12-05',5,6),(6,4,'Excelente libro muy recomendado.','2025-12-05',5,1),(7,2,'Excelente libro muy recomendado.','2025-12-05',2,9),(8,1,'Excelente libro muy recomendado.','2025-12-05',4,5),(9,5,'Excelente libro muy recomendado.','2025-12-05',3,1),(10,4,'Excelente libro muy recomendado.','2025-12-05',5,8),(11,3,'Excelente libro muy recomendado.','2025-12-05',1,9),(12,1,'Excelente libro muy recomendado.','2025-12-05',1,2),(13,4,'Excelente libro muy recomendado.','2025-12-05',2,1),(14,5,'Excelente libro muy recomendado.','2025-12-05',5,8),(15,1,'Excelente libro muy recomendado.','2025-12-05',5,3);
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Juan Perez','$argon2id$v=19$m=65536,t=3,p=4$JHLZusxre94BejlWNdN2Kw$HDABgMy0CPsnU2JafAtLGlHRRptWoUMu9PFdMiA+Bvw','juan@example.com',NULL,NULL,1),(2,'Maria Lopez','$argon2id$v=19$m=65536,t=3,p=4$JHLZusxre94BejlWNdN2Kw$HDABgMy0CPsnU2JafAtLGlHRRptWoUMu9PFdMiA+Bvw','maria@example.com',NULL,NULL,1),(3,'Carlos Ruiz','$argon2id$v=19$m=65536,t=3,p=4$JHLZusxre94BejlWNdN2Kw$HDABgMy0CPsnU2JafAtLGlHRRptWoUMu9PFdMiA+Bvw','carlos@example.com',NULL,NULL,1),(4,'Ana Diaz','$argon2id$v=19$m=65536,t=3,p=4$JHLZusxre94BejlWNdN2Kw$HDABgMy0CPsnU2JafAtLGlHRRptWoUMu9PFdMiA+Bvw','ana@example.com',NULL,NULL,1),(5,'Pedro Pascal','$argon2id$v=19$m=65536,t=3,p=4$JHLZusxre94BejlWNdN2Kw$HDABgMy0CPsnU2JafAtLGlHRRptWoUMu9PFdMiA+Bvw','pedro@example.com',NULL,NULL,1);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-05  3:19:03
