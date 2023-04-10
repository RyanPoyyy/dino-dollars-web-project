SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";



CREATE DATABASE IF NOT EXISTS `availableVoucher` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `availableVoucher`;


DROP TABLE IF EXISTS `availableVoucher`;
CREATE TABLE IF NOT EXISTS `availableVoucher` (
  `PlatformName` varchar(50) NOT NULL,
  `DiscountAmt` int NOT NULL,
  `DDRequired` int NOT NULL,
  PRIMARY KEY (`PlatformName`,`DiscountAmt`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;


INSERT INTO `availablevoucher` (`PlatformName`, `DiscountAmt`, `DDRequired`) VALUES
('ASOS', 10, 40),
('ASOS', 5, 20);

