-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server version:               10.4.22-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Version:             11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Dumping database structure for hasiltest
CREATE DATABASE IF NOT EXISTS `hasiltest` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `hasiltest`;

-- Dumping structure for table hasiltest.depresi
CREATE TABLE IF NOT EXISTS `depresi` (
  `IP` text DEFAULT NULL,
  `Score_Depresi` varchar(50) DEFAULT NULL,
  `Score_Anxiety` varchar(50) DEFAULT NULL,
  `Score_Stress` varchar(50) DEFAULT NULL,
  `TK_Depresi` varchar(50) DEFAULT NULL,
  `TK_Anxiety` varchar(50) DEFAULT NULL,
  `TK_Stress` varchar(50) DEFAULT NULL,
  `Prediksi` varchar(50) DEFAULT NULL,
  `Penjelasan` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table hasiltest.depresi: ~0 rows (approximately)
/*!40000 ALTER TABLE `depresi` DISABLE KEYS */;
/*!40000 ALTER TABLE `depresi` ENABLE KEYS */;

-- Dumping structure for table hasiltest.user
CREATE TABLE IF NOT EXISTS `user` (
  `IP` text DEFAULT NULL,
  `Total_Jawaban` int(255) DEFAULT 0,
  `Quest_num` int(255) DEFAULT 0,
  `D_Score` int(255) DEFAULT 0,
  `A_Score` int(255) DEFAULT 0,
  `S_Score` int(255) DEFAULT 0,
  `Hasil` int(255) DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Dumping data for table hasiltest.user: ~0 rows (approximately)
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
/*!40000 ALTER TABLE `user` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
