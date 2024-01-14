
-- Host: localhost    Database: qlkscnpm

/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;



--
-- Dumping data for table `bangsdt`
--

LOCK TABLES `bangsdt` WRITE;
/*!40000 ALTER TABLE `bangsdt` DISABLE KEYS */;
INSERT INTO `bangsdt` VALUES (1,1),(1,2);
/*!40000 ALTER TABLE `bangsdt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `bangsdtnhanvien`
--

LOCK TABLES `bangsdtnhanvien` WRITE;
/*!40000 ALTER TABLE `bangsdtnhanvien` DISABLE KEYS */;
/*!40000 ALTER TABLE `bangsdtnhanvien` ENABLE KEYS */;
UNLOCK TABLES;


--
-- Dumping data for table `chi_tiet_thue`
--

LOCK TABLES `chi_tiet_thue` WRITE;
/*!40000 ALTER TABLE `chi_tiet_thue` DISABLE KEYS */;
INSERT INTO `chi_tiet_thue` VALUES (1,101,1,'2023-11-20 00:00:00',10, 2),(2,102,1,'2023-11-20 00:00:00',5, 2),(3,103,1,'2023-11-20 00:00:00',1, 2);
/*!40000 ALTER TABLE `chi_tiet_thue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `danh_gia_cua_khach`
--

LOCK TABLES `danh_gia_cua_khach` WRITE;
/*!40000 ALTER TABLE `danh_gia_cua_khach` DISABLE KEYS */;
/*!40000 ALTER TABLE `danh_gia_cua_khach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `hoa_don`
--

LOCK TABLES `hoa_don` WRITE;
/*!40000 ALTER TABLE `hoa_don` DISABLE KEYS */;
INSERT INTO `hoa_don` VALUES (3,'2023-11-25 00:00:00',1000);
/*!40000 ALTER TABLE `hoa_don` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `khach`
--

LOCK TABLES `khach` WRITE;
/*!40000 ALTER TABLE `khach` DISABLE KEYS */;
INSERT INTO `khach` VALUES (1,1,'1','1','2003-01-01 00:00:00');
/*!40000 ALTER TABLE `khach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `loai_khach`
--

LOCK TABLES `loai_khach` WRITE;
/*!40000 ALTER TABLE `loai_khach` DISABLE KEYS */;
INSERT INTO `loai_khach` VALUES (1,'NoiDia'),(2,'NuocNgoai');
/*!40000 ALTER TABLE `loai_khach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `loai_phong`
--

LOCK TABLES `loai_phong` WRITE;
/*!40000 ALTER TABLE `loai_phong` DISABLE KEYS */;
INSERT INTO `loai_phong` VALUES (1,'A',150),(2,'B',170),(3,'C',200);
/*!40000 ALTER TABLE `loai_phong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `phong`
--

LOCK TABLES `phong` WRITE;
/*!40000 ALTER TABLE `phong` DISABLE KEYS */;
INSERT INTO `phong` VALUES (101,1,NULL,'IU',NULL),(102,1,NULL,'IU',NULL),(103,3,NULL,'FR',NULL);
/*!40000 ALTER TABLE `phong` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `sdt`
--

LOCK TABLES `sdt` WRITE;
/*!40000 ALTER TABLE `sdt` DISABLE KEYS */;
INSERT INTO `sdt` VALUES (1,'Riêng','0823582541'),(2,'Công ty','0823658741');
/*!40000 ALTER TABLE `sdt` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `tai_khoan_admin`
--

LOCK TABLES `tai_khoan_admin` WRITE;
/*!40000 ALTER TABLE `tai_khoan_admin` DISABLE KEYS */;
INSERT INTO `tai_khoan_admin` VALUES (1,1);
/*!40000 ALTER TABLE `tai_khoan_admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `tai_khoan_khach`
--

LOCK TABLES `tai_khoan_khach` WRITE;
/*!40000 ALTER TABLE `tai_khoan_khach` DISABLE KEYS */;
INSERT INTO `tai_khoan_khach` VALUES (1,'khach','b\' ,\\xb9b\\xacY\\x07[\\x96K\\x07\\x15-#Kp\'');
/*!40000 ALTER TABLE `tai_khoan_khach` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `tai_khoan_nhan_vien`
--

LOCK TABLES `tai_khoan_nhan_vien` WRITE;
/*!40000 ALTER TABLE `tai_khoan_nhan_vien` DISABLE KEYS */;
INSERT INTO `tai_khoan_nhan_vien` VALUES (1,'admin','admin','b\' ,\\xb9b\\xacY\\x07[\\x96K\\x07\\x15-#Kp\'',1),(2,'nhanvien','nhanvien','b\' ,\\xb9b\\xacY\\x07[\\x96K\\x07\\x15-#Kp\'',1);
/*!40000 ALTER TABLE `tai_khoan_nhan_vien` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `thong_so_quy_dinh`
--

LOCK TABLES `thong_so_quy_dinh` WRITE;
/*!40000 ALTER TABLE `thong_so_quy_dinh` DISABLE KEYS */;
INSERT INTO `thong_so_quy_dinh` VALUES (1, 3, 150, 3, 0.25, 1), (2,3,170,3,0.25,2), (3,3,200,3,0.25,3);
/*!40000 ALTER TABLE `thong_so_quy_dinh` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

