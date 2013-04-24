-- MySQL dump 10.13  Distrib 5.5.29, for osx10.6 (i386)
--
-- Host: localhost    Database: praylist
-- ------------------------------------------------------
-- Server version	5.5.29

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
-- Table structure for table `PrayList_groups`
--

DROP TABLE IF EXISTS `PrayList_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PrayList_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `groupname` varchar(30) NOT NULL,
  `privacy` tinyint(1) NOT NULL,
  `prayer_count` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PrayList_groups`
--

LOCK TABLES `PrayList_groups` WRITE;
/*!40000 ALTER TABLE `PrayList_groups` DISABLE KEYS */;
INSERT INTO `PrayList_groups` VALUES (8,'Animals',1,2),(9,'Cancer',1,2),(10,'Family',1,2),(11,'Austin Covenant Church',1,3),(12,'TheVaticanOfficial',1,1),(13,'parenting',1,2);
/*!40000 ALTER TABLE `PrayList_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PrayList_groups_users_favorited`
--

DROP TABLE IF EXISTS `PrayList_groups_users_favorited`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PrayList_groups_users_favorited` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `groups_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `groups_id` (`groups_id`,`user_id`),
  KEY `user_id_refs_id_995c6764` (`user_id`),
  CONSTRAINT `groups_id_refs_id_69028265` FOREIGN KEY (`groups_id`) REFERENCES `PrayList_groups` (`id`),
  CONSTRAINT `user_id_refs_id_995c6764` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PrayList_groups_users_favorited`
--

LOCK TABLES `PrayList_groups_users_favorited` WRITE;
/*!40000 ALTER TABLE `PrayList_groups_users_favorited` DISABLE KEYS */;
INSERT INTO `PrayList_groups_users_favorited` VALUES (3,8,20),(35,9,1),(1,9,20),(6,10,20),(36,11,1),(2,11,20),(5,12,20),(4,13,20);
/*!40000 ALTER TABLE `PrayList_groups_users_favorited` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `PrayList_prayer_prayed_users`
--

DROP TABLE IF EXISTS `PrayList_prayer_prayed_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `PrayList_prayer_prayed_users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `prayer_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `prayer_id` (`prayer_id`,`user_id`),
  KEY `user_id_refs_id_9dc6e0eb` (`user_id`),
  CONSTRAINT `prayer_id_refs_id_fa19c10f` FOREIGN KEY (`prayer_id`) REFERENCES `PrayList_prayer` (`id`),
  CONSTRAINT `user_id_refs_id_9dc6e0eb` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=98 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `PrayList_prayer_prayed_users`
--

LOCK TABLES `PrayList_prayer_prayed_users` WRITE;
/*!40000 ALTER TABLE `PrayList_prayer_prayed_users` DISABLE KEYS */;
INSERT INTO `PrayList_prayer_prayed_users` VALUES (21,5,1),(3,5,2),(73,5,3),(48,5,4),(57,5,5),(30,5,6),(35,5,10),(90,5,19),(25,6,1),(4,6,2),(69,6,3),(44,6,4),(60,6,5),(27,6,6),(39,6,10),(83,6,11),(11,7,1),(5,7,2),(55,7,5),(15,7,6),(33,7,10),(82,7,11),(86,7,19),(9,8,1),(72,8,3),(45,8,4),(61,8,5),(41,8,10),(81,8,11),(94,8,19),(12,9,1),(42,9,2),(71,9,3),(49,9,4),(63,9,5),(32,9,6),(40,9,10),(80,9,11),(93,9,19),(20,10,1),(6,10,2),(68,10,3),(47,10,4),(59,10,5),(28,10,6),(79,10,11),(91,10,19),(96,10,20),(10,11,1),(7,11,2),(67,11,3),(51,11,4),(17,11,6),(18,11,10),(92,11,19),(23,12,1),(65,12,3),(46,12,4),(58,12,5),(29,12,6),(36,12,10),(78,12,11),(95,12,19),(13,13,1),(70,13,3),(50,13,4),(54,13,5),(31,13,6),(34,13,10),(77,13,11),(89,13,19),(22,14,1),(8,14,2),(66,14,3),(53,14,5),(84,14,6),(38,14,10),(85,14,19),(97,14,20),(14,15,1),(74,15,3),(52,15,4),(62,15,5),(16,15,6),(19,15,10),(76,15,11),(87,15,19),(24,16,1),(64,16,3),(43,16,4),(56,16,5),(26,16,6),(37,16,10),(75,16,11),(88,16,19);
/*!40000 ALTER TABLE `PrayList_prayer_prayed_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add prayer',1,'add_prayer'),(2,'Can change prayer',1,'change_prayer'),(3,'Can delete prayer',1,'delete_prayer'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add site',7,'add_site'),(20,'Can change site',7,'change_site'),(21,'Can delete site',7,'delete_site'),(22,'Can add log entry',8,'add_logentry'),(23,'Can change log entry',8,'change_logentry'),(24,'Can delete log entry',8,'delete_logentry'),(25,'Can add tag',9,'add_tag'),(26,'Can change tag',9,'change_tag'),(27,'Can delete tag',9,'delete_tag'),(28,'Can add tagged item',10,'add_taggeditem'),(29,'Can change tagged item',10,'change_taggeditem'),(30,'Can delete tagged item',10,'delete_taggeditem');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'thebirdthebear','','','brcdrums@gmail.com','pbkdf2_sha256$10000$FvuAtkBkg3iq$U77mMmHzQSLSuRltqTxxUWM9p9vlsqcgUnBv6uj/07g=',1,1,1,'2013-04-23 02:11:05','2013-02-20 07:53:55'),(2,'booty','','','','pbkdf2_sha256$10000$He7uGnSZKQuf$rnPIp6JpI3C0o635JfVvxTNzEM9PMx2Deud6OGKC4K0=',0,1,0,'2013-04-15 08:12:59','2013-02-25 07:00:18'),(3,'fuckface','','','','pbkdf2_sha256$10000$zHxlkJjXhXGa$dJsD2Nb3YxohROihPxRSkxhJGxv7JSWiU7JBMOVwz7k=',0,1,0,'2013-04-15 22:47:40','2013-02-25 07:01:17'),(4,'testuser','','','','pbkdf2_sha256$10000$hU3Ns0ZZOFnn$DyWHw8Tw+402l9z7GAP2OYGmBpzeQaggjjqXNVbzwY0=',0,1,0,'2013-04-15 22:46:59','2013-02-25 07:08:07'),(5,'testuser2','','','','pbkdf2_sha256$10000$nCE94tWtLeul$KfV5FKLd77+gG8SQWpCZr1fE0WiwO6DpJHf5qNtiN8Y=',0,1,0,'2013-04-15 08:36:14','2013-02-25 07:08:39'),(6,'testaccount3','','','','pbkdf2_sha256$10000$jQKrvImn4ipU$26HSb8f2lvzXgWInbSptSskLDPKwnEi5Ot/bgX2KGQk=',0,1,0,'2013-04-16 04:23:26','2013-02-25 07:10:32'),(7,'testaccount4','','','','pbkdf2_sha256$10000$8IQYknbuklkc$GbXRbUbGXqRXgXZtme6skk9EkoOFW4wcsWPSgfDP0Jw=',0,1,0,'2013-02-25 07:12:24','2013-02-25 07:12:24'),(8,'testaccount5','','','','pbkdf2_sha256$10000$eu6hYNtICHk9$7GT03sJ1Bjro2pMtMZpPlDO8Nt2RN+2SrqzubjF93j0=',0,1,0,'2013-02-25 07:16:28','2013-02-25 07:16:28'),(9,'testaccount8','','','','pbkdf2_sha256$10000$rho3LxjpKzHJ$1jBkdbNY3Fp4NSNFr463846nOQtZTrgzS/UsSDhJcqY=',0,1,0,'2013-02-25 07:21:32','2013-02-25 07:21:32'),(10,'testaccount0','','','','pbkdf2_sha256$10000$oNqi0SoJBOug$Yg1rulgPJUqGwRWgrMBZqfzvrvLiQGvNL+FzygpJVw4=',0,1,0,'2013-04-15 07:03:22','2013-02-25 07:25:05'),(11,'testaccount100','','','','pbkdf2_sha256$10000$QbiPwLQI7yUy$rcRB/Eo6AYJI6xUe3ctpkpiLvhFtS9zindCOKNorMLM=',0,1,0,'2013-04-15 23:05:26','2013-02-25 07:26:32'),(12,'testaccount3934','','','','pbkdf2_sha256$10000$M7zbGAIOIDZW$RBaBawRVY59HFmJufh/w5QFm2BrBtnESvzcfOye5RuE=',0,1,0,'2013-02-25 07:28:04','2013-02-25 07:28:04'),(13,'testaccount3935','','','','pbkdf2_sha256$10000$q3b256YfE6sT$GJl6f4Jn7sML/EFwbb6+h/ylu24e511cq93+GMg8lOs=',0,1,0,'2013-02-25 07:29:01','2013-02-25 07:29:01'),(14,'testaccount3939','','','','pbkdf2_sha256$10000$1cYOPpA4d8eJ$mzAM4lLosGadB9ZIuzVzgJh8yesImZtg2EbQZITUclY=',0,1,0,'2013-02-25 07:31:06','2013-02-25 07:31:05'),(15,'totallynew','','','','pbkdf2_sha256$10000$AUv29VeY9ReV$a4hBTK3vMBum8cRp7voi+sbb8lMYaVXNEd3fdA1acvA=',0,1,0,'2013-02-26 02:46:13','2013-02-26 02:46:12'),(16,'bitches','','','','pbkdf2_sha256$10000$ydFrRQwkukGI$0onnaq7xJXaGzn9vw1bMSBuiK1u6dDNgjIM5gC3OpMI=',0,1,0,'2013-04-16 23:01:11','2013-04-16 23:01:11'),(17,'fuckandblah','','','','pbkdf2_sha256$10000$JRbhNRTfP3Zl$bLJtB1jwzcZfZhlA5ZkpbTwtcC1xPe7sDPRfg/+ErDo=',0,1,0,'2013-04-16 23:02:11','2013-04-16 23:02:11'),(18,'motherfuckerandbitch','','','','pbkdf2_sha256$10000$gTcn7QAPNZqX$oIjqPMrYGsYZEHDiLDaDk9OPXhqxnE1mqMgnnAFneH4=',0,1,0,'2013-04-16 23:04:45','2013-04-16 23:04:18'),(19,'blahblahblah','','','','pbkdf2_sha256$10000$CXCSqd78Y75O$o0y46jLWwxgzUbrxdjCH0itH4mEtsYSTi5lmf+1G+/M=',0,1,0,'2013-04-17 00:30:17','2013-04-17 00:30:17'),(20,'waffles','','','','pbkdf2_sha256$10000$0RM6CuMYbze0$euafpZlJR8BSVjHU4tYSECM3i0/Tp+wHKhk070it/LI=',0,1,0,'2013-04-23 01:45:49','2013-04-23 00:34:58');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`),
  CONSTRAINT `group_id_refs_id_f0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
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
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2013-02-22 01:10:01',1,1,'14','Prayer object',3,''),(2,'2013-02-22 01:14:33',1,1,'16','Prayer object',3,'');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'prayer','PrayList','prayer'),(2,'permission','auth','permission'),(3,'group','auth','group'),(4,'user','auth','user'),(5,'content type','contenttypes','contenttype'),(6,'session','sessions','session'),(7,'site','sites','site'),(8,'log entry','admin','logentry'),(9,'tag','tagging','tag'),(10,'tagged item','tagging','taggeditem');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('327672e9b79c216609dfc31ad6a0482b','ZDg2MTYxOThmMTdlYmFmMDVhMjkxOGQ2NWU1MGRkZWFlNDIwYzQ2YzqAAn1xAShVCnRlc3Rjb29r\naWVxAlUGd29ya2VkcQNVDV9hdXRoX3VzZXJfaWSKAQFVEl9hdXRoX3VzZXJfYmFja2VuZFUpZGph\nbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmR1Lg==\n','2013-03-09 06:28:15'),('6ce1577bc6f7dce7a1b37b66e9210ffa','NWFlODUwMThkYzc5YjU4ZWE3NjM2MGUxZjg4ZjlhMmU5ZWIwM2E4NDqAAn1xAVUKdGVzdGNvb2tp\nZVUGd29ya2VkcQJzLg==\n','2013-03-09 06:07:33'),('9da6dc0793a5522ccac0500961b1fba3','Zjk4NGY2ZTNiYThmNmNhYzI1NmQ5Y2MxYWRlOGQ5ZmY2ZmFmMzE5MTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2013-05-07 02:11:05'),('c391fa557baaf7a7e228e1defa9bc647','ZDg2MTYxOThmMTdlYmFmMDVhMjkxOGQ2NWU1MGRkZWFlNDIwYzQ2YzqAAn1xAShVCnRlc3Rjb29r\naWVxAlUGd29ya2VkcQNVDV9hdXRoX3VzZXJfaWSKAQFVEl9hdXRoX3VzZXJfYmFja2VuZFUpZGph\nbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmR1Lg==\n','2013-03-09 05:57:51'),('cfaf92eb5f976f377d0086b952a234ed','Zjk4NGY2ZTNiYThmNmNhYzI1NmQ5Y2MxYWRlOGQ5ZmY2ZmFmMzE5MTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKAQF1Lg==\n','2013-03-10 07:04:36'),('e7f9b717056fdf39153cebad6ead1e47','YTNiNzAwZDI3ZTQ1MDM2ZjRkYjljYzUyNTkyMDdjNzI3NDFiNTY1ZDqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHED\nVQ1fYXV0aF91c2VyX2lkcQSKARR1Lg==\n','2013-05-07 01:45:49'),('ea5345821cc11211efc7ccc72499544f','M2UxMDgwNTgwMzc0MTk4NjY3ZDBjYjI0YTAxY2ExMjExMzlmOWI1OTqAAn1xAShVEl9hdXRoX3Vz\nZXJfYmFja2VuZFUpZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmRxAlUN\nX2F1dGhfdXNlcl9pZIoBAXUu\n','2013-03-09 06:18:49'),('ebb1c5bdeedede98d9d02b3a86114614','NWFlODUwMThkYzc5YjU4ZWE3NjM2MGUxZjg4ZjlhMmU5ZWIwM2E4NDqAAn1xAVUKdGVzdGNvb2tp\nZVUGd29ya2VkcQJzLg==\n','2013-03-09 06:13:59');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `praylist_prayer`
--

DROP TABLE IF EXISTS `praylist_prayer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `praylist_prayer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `poster` varchar(30) NOT NULL,
  `timestamp` datetime NOT NULL,
  `subject` varchar(100) NOT NULL,
  `prayer` varchar(2000) NOT NULL,
  `prayerscore` int(11) NOT NULL,
  `hotness` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `PrayList_prayer_bda51c3c` (`group_id`),
  CONSTRAINT `group_id_refs_id_484c6d7e` FOREIGN KEY (`group_id`) REFERENCES `PrayList_groups` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `praylist_prayer`
--

LOCK TABLES `praylist_prayer` WRITE;
/*!40000 ALTER TABLE `praylist_prayer` DISABLE KEYS */;
INSERT INTO `praylist_prayer` VALUES (5,'','2013-04-09 04:48:09','Pray for Cheerio','Cheerio is my dog.  She is sooo sleepy.  She sleeps all day.  And only wakes up to attack waffles.  PRAY FOR CHEEEERIO',8,5143,8),(6,'','2013-04-09 04:55:36','My Cousin has surgery tomorrow','My cousin was diagnosed with prostate cancer.  She was given a 50/50 chance to survive this surgery, it\'s really experimental and he really needs prayers.  Thanks to all ',10,5144,9),(7,'','2013-04-09 04:57:04','Pray for my dog Waffles...','Waffles has so much fur.  She gets hot at night, and her fur is overflowing.  Sometimes it covers her eyes.  pray for her, and maybe the fur will cut itself.  ',7,5143,8),(8,'','2013-04-09 05:01:01','I just was diagnosed with skin cancer','I just was diagnosed with melanoma.  Awaiting lymph node biopsy to determine if it\'s spread.  Its a little scary, and pray that my lymph node biopsy comes back negative. Thanks everyone.',7,5143,9),(9,'','2013-04-09 05:03:13','My son listens to satanic music','My son is starting to rebel.  He is 14 and he is already listening to maryln manson and tool and other bands that worship the devil.  It\'s depressing to me and I don\'t know how to deal with it.  Pray for his soul, and that he snaps out of this phase!',9,5144,10),(10,'','2013-04-09 05:33:09','my teenage daughter is pregnant','Today, I heard my teenage daughter is pregnant.  I can\'t believe it.  She\'s only 15.  I\'m embarrassed, but thought she could use some prayers.  Pray that she makes it through the pregnancy and can continue her school work.  She\'s so afraid, please pray for her. ',9,5144,10),(11,'','2013-04-09 06:19:05','I have a job interview tomorrow!','Pray for me yall. I have a job interview tomorrow at Facebook!  I\'m very nervous and could use the support and prayers.  Thanks!',7,5144,11),(12,'','2013-04-09 06:37:28','My grandma just died','Hey everyone.  My grandma just died.  She was an amazing person.  Pray that she\'s in heaven surrounded by her family and friends who have passed.',8,5144,11),(13,'','2013-04-09 06:57:17','I have tryouts for football and hope I make the team','Pray for me.  I really want to play football, but I\'m only 5\'4, 125lbs.  I\'m trying out for running back, since I\'m very fast.  Pray for me to make the team!',11,5144,11),(14,'','2013-04-09 07:06:50','il papa','il papa es el nuevo papa.  praya for him',8,5144,12),(15,'','2013-04-09 16:53:56','My infant son needs surgery on ear','My son is only 10 months old and has to go get tubes put in his ears.  He has bad sleep apnea, and its a big procedure.  Pray that he comes out ok!',8,5144,13),(16,'','2013-04-09 21:19:45','My two year old swallowed a penny','I took him to the hospital, and now they are checking him out, but I just need some prayers to make sure he\'s ok!   Thank you!',8,5145,13);
/*!40000 ALTER TABLE `praylist_prayer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2013-04-23 20:24:47
