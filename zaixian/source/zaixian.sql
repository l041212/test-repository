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

--
-- Table structure for table `apps_JobModule`
--

DROP TABLE IF EXISTS `apps_JobModule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `apps_JobModule` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `text` varchar(1024) DEFAULT NULL,
  `attachment` varchar(100) DEFAULT NULL,
  `jobInfo_id` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apps_JobModule`
--

LOCK TABLES `apps_JobModule` WRITE;
/*!40000 ALTER TABLE `apps_JobModule` DISABLE KEYS */;
/*!40000 ALTER TABLE `apps_JobModule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `apps_JobRequirement`
--

DROP TABLE IF EXISTS `apps_JobRequirement`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `apps_JobRequirement` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `createUser` varchar(32) DEFAULT NULL,
  `updateUser` varchar(32) DEFAULT NULL,
  `createTime` datetime(6) DEFAULT NULL,
  `updateTime` datetime(6) DEFAULT NULL,
  `status` varchar(16) DEFAULT NULL,
  `isDelete` tinyint(1) DEFAULT NULL,
  `education` varchar(20) DEFAULT NULL,
  `experience` varchar(256) DEFAULT NULL,
  `passTime` varchar(32) DEFAULT NULL,
  `certificate` varchar(128) DEFAULT NULL,
  `major` varchar(64) DEFAULT NULL,
  `skill` varchar(128) DEFAULT NULL,
  `jobInfo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `apps_JobRequirement_jobInfo_id_70fa2362_uniq` (`jobInfo_id`),
  CONSTRAINT `apps_JobRequirement_jobInfo_id_70fa2362_fk_apps_JobInfo_id` FOREIGN KEY (`jobInfo_id`) REFERENCES `apps_JobInfo` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apps_JobRequirement`
--

LOCK TABLES `apps_JobRequirement` WRITE;
/*!40000 ALTER TABLE `apps_JobRequirement` DISABLE KEYS */;
/*!40000 ALTER TABLE `apps_JobRequirement` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `apps_TestReport`
--

DROP TABLE IF EXISTS `apps_TestReport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `apps_TestReport` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `createUser` varchar(32) DEFAULT NULL,
  `updateUser` varchar(32) DEFAULT NULL,
  `createTime` datetime(6) DEFAULT NULL,
  `updateTime` datetime(6) DEFAULT NULL,
  `status` varchar(16) DEFAULT NULL,
  `isDelete` tinyint(1) DEFAULT NULL,
  `name` varchar(32) DEFAULT NULL,
  `match` decimal(5,2) DEFAULT NULL,
  `text` varchar(1024) DEFAULT NULL,
  `attachment` varchar(100) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `jobInfo_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `apps_TestReport_jobInfo_id_a302f2ac_fk_apps_JobInfo_id` (`jobInfo_id`),
  CONSTRAINT `apps_TestReport_jobInfo_id_a302f2ac_fk_apps_JobInfo_id` FOREIGN KEY (`jobInfo_id`) REFERENCES `apps_JobInfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `apps_TestReport`
--

LOCK TABLES `apps_TestReport` WRITE;
/*!40000 ALTER TABLE `apps_TestReport` DISABLE KEYS */;
INSERT INTO `apps_TestReport` VALUES (1,'1','1','2018-09-04 01:41:27.479000','2018-09-04 01:41:35.245000','0',0,NULL,0.00,NULL,NULL,2,4),(2,'1','1','2018-09-04 01:41:56.561000','2018-09-04 01:42:02.652000','1',0,NULL,10.10,NULL,NULL,3,4),(3,'1','1','2018-09-04 01:42:07.579000','2018-09-04 01:42:10.546000','1',0,NULL,30.25,NULL,NULL,4,4),(4,'1','1','2018-09-04 01:42:15.181000','2018-09-04 01:42:19.585000','2',0,NULL,50.34,NULL,NULL,5,4),(5,'1','1','2018-09-04 01:42:24.298000','2018-09-04 01:42:27.051000','2',0,NULL,70.75,NULL,NULL,6,4),(6,'1','1','2018-09-04 01:42:32.491000','2018-09-04 01:42:35.738000','0',0,NULL,0.00,NULL,NULL,7,4),(7,'1','1','2018-09-04 01:42:42.479000','2018-09-04 01:42:45.645000','0',0,NULL,0.00,NULL,NULL,8,4),(8,'1','1','2018-09-04 01:43:32.218000','2018-09-04 01:43:37.918000','0',0,NULL,0.00,NULL,NULL,9,5),(9,'1','1','2018-09-04 01:43:40.875000','2018-09-04 01:43:42.896000','0',0,NULL,0.00,NULL,NULL,10,5),(10,'1','1','2018-09-04 01:43:49.309000','2018-09-05 01:43:52.501000','0',0,NULL,0.00,NULL,NULL,11,5);
/*!40000 ALTER TABLE `apps_TestReport` ENABLE KEYS */;
UNLOCK TABLES;

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

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add user',7,'add_user'),(26,'Can change user',7,'change_user'),(27,'Can delete user',7,'delete_user'),(28,'Can view user',7,'view_user'),(29,'Can add job info',8,'add_jobinfo'),(30,'Can change job info',8,'change_jobinfo'),(31,'Can delete job info',8,'delete_jobinfo'),(32,'Can view job info',8,'view_jobinfo'),(33,'Can add job requirement',9,'add_jobrequirement'),(34,'Can change job requirement',9,'change_jobrequirement'),(35,'Can delete job requirement',9,'delete_jobrequirement'),(36,'Can view job requirement',9,'view_jobrequirement'),(37,'Can add job module',10,'add_jobmodule'),(38,'Can change job module',10,'change_jobmodule'),(39,'Can delete job module',10,'delete_jobmodule'),(40,'Can view job module',10,'view_jobmodule'),(41,'Can add test report',11,'add_testreport'),(42,'Can change test report',11,'change_testreport'),(43,'Can delete test report',11,'delete_testreport'),(44,'Can view test report',11,'view_testreport');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(8,'jobInfo','jobinfo'),(10,'jobModule','jobmodule'),(9,'jobRequirement','jobrequirement'),(7,'login','user'),(6,'sessions','session'),(11,'testReport','testreport');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2018-09-03 02:47:22.632032'),(2,'auth','0001_initial','2018-09-03 02:47:40.804783'),(3,'admin','0001_initial','2018-09-03 02:47:44.863369'),(4,'admin','0002_logentry_remove_auto_add','2018-09-03 02:47:44.968557'),(5,'admin','0003_logentry_add_action_flag_choices','2018-09-03 02:47:45.089976'),(6,'contenttypes','0002_remove_content_type_name','2018-09-03 02:47:47.482043'),(7,'auth','0002_alter_permission_name_max_length','2018-09-03 02:47:48.920372'),(8,'auth','0003_alter_user_email_max_length','2018-09-03 02:47:50.435506'),(9,'auth','0004_alter_user_username_opts','2018-09-03 02:47:50.533904'),(10,'auth','0005_alter_user_last_login_null','2018-09-03 02:47:52.026273'),(11,'auth','0006_require_contenttypes_0002','2018-09-03 02:47:52.232600'),(12,'auth','0007_alter_validators_add_error_messages','2018-09-03 02:47:52.331638'),(13,'auth','0008_alter_user_username_max_length','2018-09-03 02:47:54.391751'),(14,'auth','0009_alter_user_last_name_max_length','2018-09-03 02:47:56.348713'),(15,'jobInfo','0001_initial','2018-09-03 02:47:57.058415'),(16,'jobModule','0001_initial','2018-09-03 02:47:58.313802'),(17,'jobRequirement','0001_initial','2018-09-03 02:48:00.752383'),(18,'login','0001_initial','2018-09-03 02:48:01.515433'),(19,'sessions','0001_initial','2018-09-03 02:48:02.884369'),(20,'testReport','0001_initial','2018-09-03 02:48:05.464149'),(21,'jobInfo','0002_auto_20180903_1103','2018-09-03 11:04:57.719470'),(22,'jobRequirement','0002_auto_20180903_1103','2018-09-03 11:04:58.106803'),(23,'login','0002_auto_20180903_1103','2018-09-03 11:04:58.252518'),(24,'testReport','0002_auto_20180903_1103','2018-09-03 11:04:58.436739'),(25,'testReport','0002_auto_20180904_0157','2018-09-04 01:57:45.025326'),(26,'testReport','0003_auto_20180904_0159','2018-09-04 01:59:05.271038'),(27,'jobRequirement','0002_auto_20180904_0408','2018-09-04 04:08:43.129128');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('1em0fr5yxvggrn1h8xfe97c9m0vdzfic','YjM1MjZhOTkzOWFjY2Y2NGE3ZTE5NDg1YTFkYWE1YTczYjdiZGY1NTp7InVzZXJfaWQiOjF9','2018-09-17 10:28:31.974364'),('ink3ooeby2oas50nu98i2im8fs5rhyi8','YjM1MjZhOTkzOWFjY2Y2NGE3ZTE5NDg1YTFkYWE1YTczYjdiZGY1NTp7InVzZXJfaWQiOjF9','2018-09-20 08:35:58.353551'),('n25g0aczghssqinyzr4p7l83gc8dfyv7','NzY3YzZmMzI4NmU4YzdiNjZjZTQ0MzlkMGJhNzFiZTVmZDBhNzFhNDp7InVzZXIiOjEsInVzZXJfaWQiOjF9','2018-09-17 09:56:43.949926');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-09-06 17:00:32
