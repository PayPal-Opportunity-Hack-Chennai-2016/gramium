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
-- Table structure for table `core_loan`
--

DROP TABLE IF EXISTS `core_loan`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_loan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `principal` decimal(8,2) NOT NULL,
  `rate_of_interest` decimal(8,2) NOT NULL,
  `number_of_installments` decimal(8,2) NOT NULL,
  `monthly_installment` decimal(8,2) NOT NULL,
  `remaining_amount` decimal(8,2) NOT NULL,
  `remaining_installments` int(11) NOT NULL,
  `due_date` date NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_loan_group_id_d4e7d470_fk_core_group_id` (`group_id`),
  CONSTRAINT `core_loan_group_id_d4e7d470_fk_core_group_id` FOREIGN KEY (`group_id`) REFERENCES `core_group` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_loan`
--

LOCK TABLES `core_loan` WRITE;
/*!40000 ALTER TABLE `core_loan` DISABLE KEYS */;
INSERT INTO `core_loan` VALUES (1,'2016-10-03',10000.00,10.00,10.00,1100.00,8900.00,8,'2016-11-05',1,2),(2,'2016-06-22',12000.00,10.00,10.00,1300.00,10700.00,5,'2016-07-15',1,1),(3,'2016-10-05',5000.00,10.00,5.00,1100.00,5000.00,5,'2016-10-05',1,3);
/*!40000 ALTER TABLE `core_loan` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-11-13 14:28:52
