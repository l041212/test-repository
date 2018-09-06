-- MySQL dump 10.13  Distrib 8.0.12, for linux-glibc2.12 (x86_64)
--
-- Host: localhost    Database: zaixian
-- ------------------------------------------------------
-- Server version	8.0.12

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8mb4 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `apps_User`
--

DROP TABLE IF EXISTS `apps_User`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `apps_User` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `createUser` varchar(32) DEFAULT NULL,
  `updateUser` varchar(32) DEFAULT NULL,
  `createTime` datetime(6) DEFAULT NULL,
  `updateTime` datetime(6) DEFAULT NULL,
  `status` varchar(16) DEFAULT NULL,
  `isDelete` tinyint(1) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `code` varchar(32) DEFAULT NULL,
  `role` varchar(16) DEFAULT NULL,
  `email` varchar(64) DEFAULT NULL,
  `password` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apps_User`
--

LOCK TABLES `apps_User` WRITE;
/*!40000 ALTER TABLE `apps_User` DISABLE KEYS */;
INSERT INTO `apps_User` VALUES (1,NULL,NULL,NULL,NULL,NULL,0,'Tom','tomt','admin',NULL,NULL),(2,NULL,NULL,NULL,NULL,'',0,'test1','test1','test',NULL,NULL),(3,NULL,NULL,NULL,NULL,'',0,'test2','test2','test',NULL,NULL),(4,NULL,NULL,NULL,NULL,'',0,'test3','test3','test',NULL,NULL),(5,NULL,NULL,NULL,NULL,'',0,'test4','test4','test',NULL,NULL),(6,'2','1','2018-09-03 08:51:45.160004','2018-09-06 08:11:07.261749','',0,'test5','test5','test',NULL,NULL),(7,NULL,NULL,NULL,NULL,'',0,'test6','test6','test',NULL,NULL),(8,NULL,NULL,NULL,NULL,'',0,'test7','test7','test',NULL,NULL),(9,NULL,NULL,NULL,NULL,'',0,'test8','test8','test',NULL,NULL),(10,NULL,NULL,NULL,NULL,'',0,'test9','test9','test',NULL,NULL),(11,NULL,NULL,NULL,NULL,'',0,'testA','testA','test',NULL,NULL),(12,'1','1','2018-09-06 01:14:39.143051','2018-09-06 08:11:04.504667',NULL,0,'Alice','alicea','hr',NULL,NULL),(13,NULL,NULL,NULL,NULL,NULL,0,'John','johnn','psychologist',NULL,NULL);
/*!40000 ALTER TABLE `apps_User` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-06 17:05:16
