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
-- Table structure for table `apps_JobInfo`
--

DROP TABLE IF EXISTS `apps_JobInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `apps_JobInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `createUser` varchar(32) DEFAULT NULL,
  `updateUser` varchar(32) DEFAULT NULL,
  `createTime` datetime(6) DEFAULT NULL,
  `updateTime` datetime(6) DEFAULT NULL,
  `status` varchar(16) DEFAULT NULL,
  `isDelete` tinyint(1) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `property` varchar(32) DEFAULT NULL,
  `rank` varchar(32) DEFAULT NULL,
  `description` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apps_JobInfo`
--

LOCK TABLES `apps_JobInfo` WRITE;
/*!40000 ALTER TABLE `apps_JobInfo` DISABLE KEYS */;
INSERT INTO `apps_JobInfo` VALUES (3,'2','1','2018-09-03 08:51:45.160004','2018-09-06 08:24:14.896224','0',0,'the fish in the house','4','3','fdsfdsfds'),(4,'1','1','2018-09-03 09:46:20.666451','2018-09-03 09:46:18.072386','0',0,'cat dash on the table','2','2','fdsfsdfds dsfdsf'),(5,'1','1','2018-09-03 09:57:09.123731','2018-09-03 09:56:27.232510','0',0,'the  bull run the sky','4','3','fdsfdsfds'),(6,'2','1','2018-09-03 08:51:45.160004','2018-09-06 08:23:54.237571','0',0,'tttssss','4','4','gfdgfddddgfdg'),(7,'2','1','2018-09-03 08:51:45.160004','2018-09-06 08:24:01.694616','0',0,'tttt7777','3','3','fdsfds'),(8,'2','1','2018-09-03 08:51:45.160004','2018-09-06 08:24:14.651605','0',0,'the fish in the house','2','3','fdsfds'),(9,'2','1','2018-09-03 08:51:45.160004','2018-09-06 08:24:06.254145','0',0,'the fish in the house','2','3','fdsfds'),(10,'2','1','2018-09-03 08:51:45.160004','2018-09-06 08:24:09.147163','0',0,'aa','4','3','fdsfds'),(11,'1','1','2018-09-05 01:12:36.908763','2018-09-05 01:17:29.039358','0',0,'ttt','2','3','vvc'),(12,'1','1','2018-09-06 01:14:39.143051','2018-09-06 08:23:58.340200','0',0,'new job!','5','2','this is a new job!'),(13,'1','1','2018-09-06 01:14:39.143051','2018-09-06 08:23:58.487670','0',0,'New Job !!','4','1','job job jump jump !!!');
/*!40000 ALTER TABLE `apps_JobInfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-06 17:04:07
