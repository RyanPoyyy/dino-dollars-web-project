SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone="+08:00";

CREATE DATABASE IF NOT EXISTS `user` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `user`;

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user`(
    `UID` int(4) NOT NULL AUTO_INCREMENT,
    `Name` varchar(64) NOT NULL,
    `Email` varchar(64) NOT NULL,
    `Points` int(10) DEFAULT 0,
    `Password` varchar(64) NOT NULL,
    PRIMARY KEY (`UID`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `ACCOUNTS`;
CREATE TABLE IF NOT EXISTS `ACCOUNTS`(
    `UID` int(4) NOT NULL,
    `Name` varchar(64) NOT NULL,
    PRIMARY KEY (`UID`, `Name`),
    KEY `FK_UID` (`UID`)

) ENGINE=InnoDB DEFAULT CHARSET=utf8;

INSERT INTO `user` (`UID`, `Name`, `Email`, `Points`, `Password`) VALUES
(1, 'Ding', 'gerald.ding.2021@scis.smu.edu.sg', 0, 'password'),
(2, 'Poy', 'ryanpoy.2021@scis.smu.edu.sg', 0, 'password');
COMMIT;

-- INSERT INTO `ACCOUNTS` (`UID`, `Name`) VALUES
-- (1, 'Facebook'),
-- (1, 'Google'),
-- (2, 'Facebook'),
-- (2, 'Google');
-- COMMIT;

ALTER TABLE `ACCOUNTS` ADD CONSTRAINT `FK_UID` FOREIGN KEY (`UID`) REFERENCES `user` (`UID`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;