-- MySQL dump 10.13  Distrib 5.7.12, for osx10.9 (x86_64)
--
-- Host: 192.168.120.232    Database: gramium
-- ------------------------------------------------------
-- Server version	5.7.16-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `core_member`
--

DROP TABLE IF EXISTS `core_member`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_member` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `phone` varchar(20) NOT NULL,
  `door_no` varchar(10) DEFAULT NULL,
  `street_name` varchar(50) DEFAULT NULL,
  `village` varchar(50) DEFAULT NULL,
  `district` varchar(30) DEFAULT NULL,
  `pincode` varchar(10) DEFAULT NULL,
  `is_incharge` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_member_group_id_9fc5e816_fk_core_group_id` (`group_id`),
  KEY `core_member_b068931c` (`name`),
  CONSTRAINT `core_member_group_id_9fc5e816_fk_core_group_id` FOREIGN KEY (`group_id`) REFERENCES `core_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_member`
--

LOCK TABLES `core_member` WRITE;
/*!40000 ALTER TABLE `core_member` DISABLE KEYS */;
INSERT INTO `core_member` VALUES (1,'Jayanthi','8220150482','2-13','Test Street','Test','Test','629851',1,1,1),(2,'Test','9445636004','Test','Test','Test','Chennai','1234567',0,1,2),(3,'test user 2','8056903214','21','11 Test Street, Puthukula Street, 1122','12','Test','10019',0,1,1),(4,'Madhu','9445636004','Test','Test','Test','Test','600089',0,1,3);
/*!40000 ALTER TABLE `core_member` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-13 14:28:54
