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
-- Table structure for table `core_repayment`
--

DROP TABLE IF EXISTS `core_repayment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `core_repayment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `amount_paid` decimal(8,2) NOT NULL,
  `installment_number` int(11) NOT NULL,
  `number_of_installments_paid` int(11) NOT NULL,
  `date_paid` date NOT NULL,
  `loan_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `core_repayment_loan_id_ee7eb1c4_fk_core_loan_id` (`loan_id`),
  CONSTRAINT `core_repayment_loan_id_ee7eb1c4_fk_core_loan_id` FOREIGN KEY (`loan_id`) REFERENCES `core_loan` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `core_repayment`
--

LOCK TABLES `core_repayment` WRITE;
/*!40000 ALTER TABLE `core_repayment` DISABLE KEYS */;
INSERT INTO `core_repayment` VALUES (1,1100.00,12345,2,'2016-11-02',1),(2,1300.00,1222,5,'2016-11-02',2),(3,11000.00,665765,2,'2016-11-06',3);
/*!40000 ALTER TABLE `core_repayment` ENABLE KEYS */;
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
