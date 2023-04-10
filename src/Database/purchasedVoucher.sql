SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";



CREATE DATABASE IF NOT EXISTS `purchasedVoucher` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `purchasedVoucher`;

DROP TABLE IF EXISTS `purchasedVoucher`;
CREATE TABLE IF NOT EXISTS `purchasedVoucher` (
  `VID` int NOT NULL AUTO_INCREMENT,
  `UID` int NOT NULL,
  `PlatformName` varchar(50) NOT NULL,
    `DiscountAmt` int NOT NULL,
  `DDRequired` int NOT NULL,
  `PurchasedDate` timestamp NULL DEFAULT NULL,
  `RedeemedDate` timestamp NULL DEFAULT NULL,
  `ExpiryDate` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`VID`,`UID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;


INSERT INTO `purchasedVoucher` (`VID`, `UID`, `PlatformName`, `DiscountAmt`, `DDRequired`, `PurchasedDate`, `RedeemedDate`, `ExpiryDate`) VALUES
(1, 11, 'ASOS', 5, 20,  '2023-03-18 07:22:12', '2023-03-17 23:37:41', '2023-03-17 23:22:12'),
(2, 11, 'ASOS',5, 20,  '2023-03-18 07:23:06', NULL, '2023-03-17 23:23:06'),
(3, 11, 'ASOS',5, 20,  '2023-03-18 07:25:28', NULL, '2023-03-17 23:25:28');
COMMIT;