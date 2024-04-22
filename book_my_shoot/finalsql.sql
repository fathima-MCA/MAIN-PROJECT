/*
SQLyog Community
MySQL - 10.4.25-MariaDB : Database - djnago_book_my_shoot
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`djnago_book_my_shoot` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `djnago_book_my_shoot`;

/*Table structure for table `app5_article` */

DROP TABLE IF EXISTS `app5_article`;

CREATE TABLE `app5_article` (
  `artice_id` int(11) NOT NULL AUTO_INCREMENT,
  `article` varchar(255) NOT NULL,
  `details` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  `photographers_id` int(11) NOT NULL,
  PRIMARY KEY (`artice_id`),
  KEY `app5_article_photographers_id_2fb743ba_fk_app5_phot` (`photographers_id`),
  CONSTRAINT `app5_article_photographers_id_2fb743ba_fk_app5_phot` FOREIGN KEY (`photographers_id`) REFERENCES `app5_photographer` (`photographer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `app5_article` */

/*Table structure for table `app5_assignphoto` */

DROP TABLE IF EXISTS `app5_assignphoto`;

CREATE TABLE `app5_assignphoto` (
  `assignphoto_id` int(11) NOT NULL AUTO_INCREMENT,
  `bookings_id` int(11) NOT NULL,
  `photographers_id` int(11) NOT NULL,
  PRIMARY KEY (`assignphoto_id`),
  KEY `app5_assignphoto_bookings_id_d90ec62a_fk_app5_booking_booking_id` (`bookings_id`),
  KEY `app5_assignphoto_photographers_id_c8cf99c7_fk_app5_phot` (`photographers_id`),
  CONSTRAINT `app5_assignphoto_bookings_id_d90ec62a_fk_app5_booking_booking_id` FOREIGN KEY (`bookings_id`) REFERENCES `app5_booking` (`booking_id`),
  CONSTRAINT `app5_assignphoto_photographers_id_c8cf99c7_fk_app5_phot` FOREIGN KEY (`photographers_id`) REFERENCES `app5_photographer` (`photographer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `app5_assignphoto` */

insert  into `app5_assignphoto`(`assignphoto_id`,`bookings_id`,`photographers_id`) values 
(1,1,1),
(2,4,1),
(3,4,1);

/*Table structure for table `app5_booking` */

DROP TABLE IF EXISTS `app5_booking`;

CREATE TABLE `app5_booking` (
  `booking_id` int(11) NOT NULL AUTO_INCREMENT,
  `venue` varchar(225) NOT NULL,
  `place` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  `bookingfordate` varchar(225) NOT NULL,
  `time` varchar(225) NOT NULL,
  `amounts` varchar(225) NOT NULL,
  `status` varchar(225) NOT NULL,
  `pref` varchar(225) NOT NULL,
  `services_id` int(11) NOT NULL,
  `users_id` int(11) NOT NULL,
  `photographers_id` int(11) NOT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `app5_booking_services_id_60651926_fk_app5_service_service_id` (`services_id`),
  KEY `app5_booking_users_id_f6d01026_fk_app5_user_user_id` (`users_id`),
  KEY `app5_booking_photographers_id_f6a1dee4_fk_app5_phot` (`photographers_id`),
  CONSTRAINT `app5_booking_photographers_id_f6a1dee4_fk_app5_phot` FOREIGN KEY (`photographers_id`) REFERENCES `app5_photographer` (`photographer_id`),
  CONSTRAINT `app5_booking_services_id_60651926_fk_app5_service_service_id` FOREIGN KEY (`services_id`) REFERENCES `app5_service` (`service_id`),
  CONSTRAINT `app5_booking_users_id_f6d01026_fk_app5_user_user_id` FOREIGN KEY (`users_id`) REFERENCES `app5_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `app5_booking` */

insert  into `app5_booking`(`booking_id`,`venue`,`place`,`date`,`bookingfordate`,`time`,`amounts`,`status`,`pref`,`services_id`,`users_id`,`photographers_id`) values 
(1,'kollam','kochi','2023-08-04','2023-08-19','14:36','1500','accepted','1',1,1,1),
(4,'zxjnxjcn','mjnvfjkvn','2023-08-04','2023-08-22','16:17','1500','accepted','2',1,2,2);

/*Table structure for table `app5_camera` */

DROP TABLE IF EXISTS `app5_camera`;

CREATE TABLE `app5_camera` (
  `camera_id` int(11) NOT NULL AUTO_INCREMENT,
  `camera` varchar(255) NOT NULL,
  `resolution` varchar(255) NOT NULL,
  `sensortypeandsize` varchar(255) NOT NULL,
  `lensetype` varchar(255) NOT NULL,
  `connectiontype` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `amountperday` varchar(255) NOT NULL,
  `studios_id` int(11) NOT NULL,
  `cam_img` varchar(255) NOT NULL,
  PRIMARY KEY (`camera_id`),
  KEY `app5_camera_studios_id_2871fb24_fk_app5_studio_studio_id` (`studios_id`),
  CONSTRAINT `app5_camera_studios_id_2871fb24_fk_app5_studio_studio_id` FOREIGN KEY (`studios_id`) REFERENCES `app5_studio` (`studio_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `app5_camera` */

insert  into `app5_camera`(`camera_id`,`camera`,`resolution`,`sensortypeandsize`,`lensetype`,`connectiontype`,`status`,`amountperday`,`studios_id`,`cam_img`) values 
(1,'camara1','1500','15','10','conncet','Not Available','500',1,'Screenshot (34).png'),
(4,'cam2','500','asxsax','sxsbx','xcnbdch','Available','1000',1,'Screenshot (38).png');

/*Table structure for table `app5_category` */

DROP TABLE IF EXISTS `app5_category`;

CREATE TABLE `app5_category` (
  `category_id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(225) NOT NULL,
  `image` varchar(225) NOT NULL,
  PRIMARY KEY (`category_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `app5_category` */

insert  into `app5_category`(`category_id`,`category`,`image`) values 
(1,'category1','Screenshot (43).png'),
(2,'cate2','Screenshot (52).png');

/*Table structure for table `app5_chat` */

DROP TABLE IF EXISTS `app5_chat`;

CREATE TABLE `app5_chat` (
  `artice_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) NOT NULL,
  `receiver_id` int(11) NOT NULL,
  `message` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  PRIMARY KEY (`artice_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `app5_chat` */

insert  into `app5_chat`(`artice_id`,`sender_id`,`receiver_id`,`message`,`date`) values 
(1,1,6,'haloo','2023-08-04');

/*Table structure for table `app5_complaints` */

DROP TABLE IF EXISTS `app5_complaints`;

CREATE TABLE `app5_complaints` (
  `complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `complaints` varchar(255) NOT NULL,
  `reply` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`complaint_id`),
  KEY `app5_complaints_users_id_957ac9a0_fk_app5_user_user_id` (`users_id`),
  CONSTRAINT `app5_complaints_users_id_957ac9a0_fk_app5_user_user_id` FOREIGN KEY (`users_id`) REFERENCES `app5_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `app5_complaints` */

/*Table structure for table `app5_feedback` */

DROP TABLE IF EXISTS `app5_feedback`;

CREATE TABLE `app5_feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`feedback_id`),
  KEY `app5_feedback_users_id_d5cb23f7_fk_app5_user_user_id` (`users_id`),
  CONSTRAINT `app5_feedback_users_id_d5cb23f7_fk_app5_user_user_id` FOREIGN KEY (`users_id`) REFERENCES `app5_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `app5_feedback` */

/*Table structure for table `app5_login` */

DROP TABLE IF EXISTS `app5_login`;

CREATE TABLE `app5_login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(225) NOT NULL,
  `password` varchar(225) NOT NULL,
  `usertype` varchar(225) NOT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `app5_login` */

insert  into `app5_login`(`login_id`,`username`,`password`,`usertype`) values 
(1,'sh','sh','user'),
(2,'st','st','studio'),
(3,'st1','st1','studio'),
(4,'u','u','user'),
(5,'admin','admin','admin'),
(6,'ph','ph','photographer'),
(7,'ph1','ph1','photographer');

/*Table structure for table `app5_mywork` */

DROP TABLE IF EXISTS `app5_mywork`;

CREATE TABLE `app5_mywork` (
  `mywork_id` int(11) NOT NULL AUTO_INCREMENT,
  `works` varchar(255) NOT NULL,
  `files` varchar(100) NOT NULL,
  `type` varchar(255) NOT NULL,
  `category_id` int(11) NOT NULL,
  `studios_id` int(11) NOT NULL,
  PRIMARY KEY (`mywork_id`),
  KEY `app5_mywork_category_id_13509ad1_fk_app5_category_category_id` (`category_id`),
  KEY `app5_mywork_studios_id_ce40c59a_fk_app5_studio_studio_id` (`studios_id`),
  CONSTRAINT `app5_mywork_category_id_13509ad1_fk_app5_category_category_id` FOREIGN KEY (`category_id`) REFERENCES `app5_category` (`category_id`),
  CONSTRAINT `app5_mywork_studios_id_ce40c59a_fk_app5_studio_studio_id` FOREIGN KEY (`studios_id`) REFERENCES `app5_studio` (`studio_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `app5_mywork` */

insert  into `app5_mywork`(`mywork_id`,`works`,`files`,`type`,`category_id`,`studios_id`) values 
(1,'ZBXsghavahcb','Screenshot (62).png','image/png',1,1),
(2,'<HJBavxhsxn','Screenshot (68).png','image/png',2,1);

/*Table structure for table `app5_payment` */

DROP TABLE IF EXISTS `app5_payment`;

CREATE TABLE `app5_payment` (
  `payment_id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` varchar(225) NOT NULL,
  `date` varchar(225) NOT NULL,
  `bookings_id` int(11) NOT NULL,
  PRIMARY KEY (`payment_id`),
  KEY `app5_payment_bookings_id_4c73f59e_fk_app5_booking_booking_id` (`bookings_id`),
  CONSTRAINT `app5_payment_bookings_id_4c73f59e_fk_app5_booking_booking_id` FOREIGN KEY (`bookings_id`) REFERENCES `app5_booking` (`booking_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `app5_payment` */

insert  into `app5_payment`(`payment_id`,`amount`,`date`,`bookings_id`) values 
(1,'200','2023-08-04',4);

/*Table structure for table `app5_photographer` */

DROP TABLE IF EXISTS `app5_photographer`;

CREATE TABLE `app5_photographer` (
  `photographer_id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(225) NOT NULL,
  `lname` varchar(225) NOT NULL,
  `place` varchar(225) NOT NULL,
  `pincode` varchar(7) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `email` varchar(254) NOT NULL,
  `logins_id` int(11) NOT NULL,
  `studios_id` int(11) NOT NULL,
  PRIMARY KEY (`photographer_id`),
  KEY `app5_photographer_studios_id_b94a295a_fk_app5_studio_studio_id` (`studios_id`),
  KEY `app5_photographer_logins_id_cd104aef_fk_app5_login_login_id` (`logins_id`),
  CONSTRAINT `app5_photographer_logins_id_cd104aef_fk_app5_login_login_id` FOREIGN KEY (`logins_id`) REFERENCES `app5_login` (`login_id`),
  CONSTRAINT `app5_photographer_studios_id_b94a295a_fk_app5_studio_studio_id` FOREIGN KEY (`studios_id`) REFERENCES `app5_studio` (`studio_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `app5_photographer` */

insert  into `app5_photographer`(`photographer_id`,`fname`,`lname`,`place`,`pincode`,`phone`,`email`,`logins_id`,`studios_id`) values 
(1,'photographer','graph','kollam','697111','9874561230','sh@gmail.com',6,1),
(2,'photograpph','phoy','kochi','789456','7412369875','xs@gmail.com',7,1);

/*Table structure for table `app5_protfolio` */

DROP TABLE IF EXISTS `app5_protfolio`;

CREATE TABLE `app5_protfolio` (
  `protfolio_id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `files` varchar(100) NOT NULL,
  `type` varchar(255) NOT NULL,
  `photographers_id` int(11) NOT NULL,
  PRIMARY KEY (`protfolio_id`),
  KEY `app5_protfolio_photographers_id_ee329f57_fk_app5_phot` (`photographers_id`),
  CONSTRAINT `app5_protfolio_photographers_id_ee329f57_fk_app5_phot` FOREIGN KEY (`photographers_id`) REFERENCES `app5_photographer` (`photographer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `app5_protfolio` */

/*Table structure for table `app5_requests` */

DROP TABLE IF EXISTS `app5_requests`;

CREATE TABLE `app5_requests` (
  `request_id` int(11) NOT NULL AUTO_INCREMENT,
  `date` varchar(255) NOT NULL,
  `requestedfor` varchar(255) NOT NULL,
  `status` varchar(255) NOT NULL,
  `cameras_id` int(11) NOT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`request_id`),
  KEY `app5_requests_cameras_id_60895ca2_fk_app5_camera_camera_id` (`cameras_id`),
  KEY `app5_requests_users_id_12a80eb8_fk_app5_user_user_id` (`users_id`),
  CONSTRAINT `app5_requests_cameras_id_60895ca2_fk_app5_camera_camera_id` FOREIGN KEY (`cameras_id`) REFERENCES `app5_camera` (`camera_id`),
  CONSTRAINT `app5_requests_users_id_12a80eb8_fk_app5_user_user_id` FOREIGN KEY (`users_id`) REFERENCES `app5_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `app5_requests` */

insert  into `app5_requests`(`request_id`,`date`,`requestedfor`,`status`,`cameras_id`,`users_id`) values 
(1,'2023-08-04','','Accept',1,2),
(2,'2023-08-04','','pending',4,2);

/*Table structure for table `app5_review` */

DROP TABLE IF EXISTS `app5_review`;

CREATE TABLE `app5_review` (
  `review_id` int(11) NOT NULL AUTO_INCREMENT,
  `rate` varchar(255) NOT NULL,
  `review` varchar(255) NOT NULL,
  `date` varchar(255) NOT NULL,
  `photographers_id` int(11) NOT NULL,
  `users_id` int(11) NOT NULL,
  PRIMARY KEY (`review_id`),
  KEY `app5_review_photographers_id_493fb0ea_fk_app5_phot` (`photographers_id`),
  KEY `app5_review_users_id_c0d35632_fk_app5_user_user_id` (`users_id`),
  CONSTRAINT `app5_review_photographers_id_493fb0ea_fk_app5_phot` FOREIGN KEY (`photographers_id`) REFERENCES `app5_photographer` (`photographer_id`),
  CONSTRAINT `app5_review_users_id_c0d35632_fk_app5_user_user_id` FOREIGN KEY (`users_id`) REFERENCES `app5_user` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `app5_review` */

/*Table structure for table `app5_service` */

DROP TABLE IF EXISTS `app5_service`;

CREATE TABLE `app5_service` (
  `service_id` int(11) NOT NULL AUTO_INCREMENT,
  `service` varchar(225) NOT NULL,
  `amount` varchar(225) NOT NULL,
  `details` varchar(225) NOT NULL,
  `image` varchar(1000) NOT NULL,
  `categorys_id` int(11) NOT NULL,
  `studios_id` int(11) NOT NULL,
  PRIMARY KEY (`service_id`),
  KEY `app5_service_categorys_id_6ebb2499_fk_app5_category_category_id` (`categorys_id`),
  KEY `app5_service_studios_id_ec6f6bb6_fk_app5_studio_studio_id` (`studios_id`),
  CONSTRAINT `app5_service_categorys_id_6ebb2499_fk_app5_category_category_id` FOREIGN KEY (`categorys_id`) REFERENCES `app5_category` (`category_id`),
  CONSTRAINT `app5_service_studios_id_ec6f6bb6_fk_app5_studio_studio_id` FOREIGN KEY (`studios_id`) REFERENCES `app5_studio` (`studio_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `app5_service` */

insert  into `app5_service`(`service_id`,`service`,`amount`,`details`,`image`,`categorys_id`,`studios_id`) values 
(1,'service1','1500','detailsssssss','Screenshot (63).png',1,1),
(2,'service2','50000','mhbcsdcvdgc','Screenshot (69).png',2,1);

/*Table structure for table `app5_studio` */

DROP TABLE IF EXISTS `app5_studio`;

CREATE TABLE `app5_studio` (
  `studio_id` int(11) NOT NULL AUTO_INCREMENT,
  `studioname` varchar(225) NOT NULL,
  `place` varchar(225) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `email` varchar(225) NOT NULL,
  `since` varchar(225) NOT NULL,
  `licence` varchar(225) NOT NULL,
  `logins_id` int(11) NOT NULL,
  PRIMARY KEY (`studio_id`),
  KEY `app5_studio_logins_id_d1ef3d41_fk_app5_login_login_id` (`logins_id`),
  CONSTRAINT `app5_studio_logins_id_d1ef3d41_fk_app5_login_login_id` FOREIGN KEY (`logins_id`) REFERENCES `app5_login` (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `app5_studio` */

insert  into `app5_studio`(`studio_id`,`studioname`,`place`,`phone`,`email`,`since`,`licence`,`logins_id`) values 
(1,'studio1','asmxcdnc','7894561230','ss@gmail.com','2022','x2454864',2),
(2,'studio2','kochi','1234567895','st@gmail.com','20233','scdas51547',3);

/*Table structure for table `app5_uploads` */

DROP TABLE IF EXISTS `app5_uploads`;

CREATE TABLE `app5_uploads` (
  `upload_id` int(11) NOT NULL AUTO_INCREMENT,
  `file` varchar(100) NOT NULL,
  `type` varchar(255) NOT NULL,
  `link` varchar(255) NOT NULL,
  `bookingss_id` int(11) NOT NULL,
  PRIMARY KEY (`upload_id`),
  KEY `app5_uploads_bookingss_id_09f4c804_fk_app5_booking_booking_id` (`bookingss_id`),
  CONSTRAINT `app5_uploads_bookingss_id_09f4c804_fk_app5_booking_booking_id` FOREIGN KEY (`bookingss_id`) REFERENCES `app5_booking` (`booking_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `app5_uploads` */

/*Table structure for table `app5_user` */

DROP TABLE IF EXISTS `app5_user`;

CREATE TABLE `app5_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(225) NOT NULL,
  `lname` varchar(225) NOT NULL,
  `place` varchar(225) NOT NULL,
  `phone` varchar(225) NOT NULL,
  `email` varchar(254) NOT NULL,
  `logins_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`),
  KEY `app5_user_logins_id_383290ec_fk_app5_login_login_id` (`logins_id`),
  CONSTRAINT `app5_user_logins_id_383290ec_fk_app5_login_login_id` FOREIGN KEY (`logins_id`) REFERENCES `app5_login` (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `app5_user` */

insert  into `app5_user`(`user_id`,`fname`,`lname`,`place`,`phone`,`email`,`logins_id`) values 
(1,'shemme','asxsx','xmbsccb','9874561230','scs@gmail.com',1),
(2,'user','user','kollam','7894561203','u@gmail.com',4);

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=latin1;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add booking',7,'add_booking'),
(26,'Can change booking',7,'change_booking'),
(27,'Can delete booking',7,'delete_booking'),
(28,'Can view booking',7,'view_booking'),
(29,'Can add camera',8,'add_camera'),
(30,'Can change camera',8,'change_camera'),
(31,'Can delete camera',8,'delete_camera'),
(32,'Can view camera',8,'view_camera'),
(33,'Can add category',9,'add_category'),
(34,'Can change category',9,'change_category'),
(35,'Can delete category',9,'delete_category'),
(36,'Can view category',9,'view_category'),
(37,'Can add chat',10,'add_chat'),
(38,'Can change chat',10,'change_chat'),
(39,'Can delete chat',10,'delete_chat'),
(40,'Can view chat',10,'view_chat'),
(41,'Can add login',11,'add_login'),
(42,'Can change login',11,'change_login'),
(43,'Can delete login',11,'delete_login'),
(44,'Can view login',11,'view_login'),
(45,'Can add photographer',12,'add_photographer'),
(46,'Can change photographer',12,'change_photographer'),
(47,'Can delete photographer',12,'delete_photographer'),
(48,'Can view photographer',12,'view_photographer'),
(49,'Can add user',13,'add_user'),
(50,'Can change user',13,'change_user'),
(51,'Can delete user',13,'delete_user'),
(52,'Can view user',13,'view_user'),
(53,'Can add uploads',14,'add_uploads'),
(54,'Can change uploads',14,'change_uploads'),
(55,'Can delete uploads',14,'delete_uploads'),
(56,'Can view uploads',14,'view_uploads'),
(57,'Can add studio',15,'add_studio'),
(58,'Can change studio',15,'change_studio'),
(59,'Can delete studio',15,'delete_studio'),
(60,'Can view studio',15,'view_studio'),
(61,'Can add service',16,'add_service'),
(62,'Can change service',16,'change_service'),
(63,'Can delete service',16,'delete_service'),
(64,'Can view service',16,'view_service'),
(65,'Can add review',17,'add_review'),
(66,'Can change review',17,'change_review'),
(67,'Can delete review',17,'delete_review'),
(68,'Can view review',17,'view_review'),
(69,'Can add requests',18,'add_requests'),
(70,'Can change requests',18,'change_requests'),
(71,'Can delete requests',18,'delete_requests'),
(72,'Can view requests',18,'view_requests'),
(73,'Can add payment',19,'add_payment'),
(74,'Can change payment',19,'change_payment'),
(75,'Can delete payment',19,'delete_payment'),
(76,'Can view payment',19,'view_payment'),
(77,'Can add mywork',20,'add_mywork'),
(78,'Can change mywork',20,'change_mywork'),
(79,'Can delete mywork',20,'delete_mywork'),
(80,'Can view mywork',20,'view_mywork'),
(81,'Can add protfolio',21,'add_protfolio'),
(82,'Can change protfolio',21,'change_protfolio'),
(83,'Can delete protfolio',21,'delete_protfolio'),
(84,'Can view protfolio',21,'view_protfolio'),
(85,'Can add feedback',22,'add_feedback'),
(86,'Can change feedback',22,'change_feedback'),
(87,'Can delete feedback',22,'delete_feedback'),
(88,'Can view feedback',22,'view_feedback'),
(89,'Can add complaints',23,'add_complaints'),
(90,'Can change complaints',23,'change_complaints'),
(91,'Can delete complaints',23,'delete_complaints'),
(92,'Can view complaints',23,'view_complaints'),
(93,'Can add assignphoto',24,'add_assignphoto'),
(94,'Can change assignphoto',24,'change_assignphoto'),
(95,'Can delete assignphoto',24,'delete_assignphoto'),
(96,'Can view assignphoto',24,'view_assignphoto'),
(97,'Can add article',25,'add_article'),
(98,'Can change article',25,'change_article'),
(99,'Can delete article',25,'delete_article'),
(100,'Can view article',25,'view_article');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user` */

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(25,'app5','article'),
(24,'app5','assignphoto'),
(7,'app5','booking'),
(8,'app5','camera'),
(9,'app5','category'),
(10,'app5','chat'),
(23,'app5','complaints'),
(22,'app5','feedback'),
(11,'app5','login'),
(20,'app5','mywork'),
(19,'app5','payment'),
(12,'app5','photographer'),
(21,'app5','protfolio'),
(18,'app5','requests'),
(17,'app5','review'),
(16,'app5','service'),
(15,'app5','studio'),
(14,'app5','uploads'),
(13,'app5','user'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(5,'contenttypes','contenttype'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=latin1;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-08-04 05:43:29.839083'),
(2,'auth','0001_initial','2023-08-04 05:43:30.460501'),
(3,'admin','0001_initial','2023-08-04 05:43:30.621354'),
(4,'admin','0002_logentry_remove_auto_add','2023-08-04 05:43:30.655076'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-08-04 05:43:30.733395'),
(6,'app5','0001_initial','2023-08-04 05:43:33.270155'),
(7,'app5','0002_booking_photographers','2023-08-04 05:43:33.373114'),
(8,'contenttypes','0002_remove_content_type_name','2023-08-04 05:43:33.504502'),
(9,'auth','0002_alter_permission_name_max_length','2023-08-04 05:43:33.543084'),
(10,'auth','0003_alter_user_email_max_length','2023-08-04 05:43:33.583061'),
(11,'auth','0004_alter_user_username_opts','2023-08-04 05:43:33.601051'),
(12,'auth','0005_alter_user_last_login_null','2023-08-04 05:43:33.682003'),
(13,'auth','0006_require_contenttypes_0002','2023-08-04 05:43:33.688000'),
(14,'auth','0007_alter_validators_add_error_messages','2023-08-04 05:43:33.716984'),
(15,'auth','0008_alter_user_username_max_length','2023-08-04 05:43:33.754962'),
(16,'auth','0009_alter_user_last_name_max_length','2023-08-04 05:43:33.796938'),
(17,'auth','0010_alter_group_name_max_length','2023-08-04 05:43:33.828920'),
(18,'auth','0011_update_proxy_permissions','2023-08-04 05:43:33.877893'),
(19,'auth','0012_alter_user_first_name_max_length','2023-08-04 05:43:33.907876'),
(20,'sessions','0001_initial','2023-08-04 05:43:33.986830'),
(21,'app5','0003_camera_cam_img','2023-08-04 06:41:43.353774');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('tzpe35a9lmem5aidopu3t3rjz7vce4ul','eyJsb2dpbl9pZCI6NSwidXNlcm5hbWUiOiJzdHVkaW8xIiwidXNlcl9pZCI6MX0:1qRsuA:Jz0Rw5QDyYYv9lRAH_T4tnZob-KmtT24LniZ_3_23cI','2023-08-18 11:23:38.810364');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
