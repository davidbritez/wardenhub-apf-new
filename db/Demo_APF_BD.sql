-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema wardenhubapf
-- -----------------------------------------------------

CREATE SCHEMA IF NOT EXISTS `wardenhubapf` DEFAULT CHARACTER SET latin1 ;
USE `wardenhubapf` ;

-- -----------------------------------------------------
-- Table `wardenhubapf`.`Usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `wardenhubapf`.`Usuarios` (
  `id` INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `nombre` VARCHAR(50) NOT NULL DEFAULT '',
  `email` VARCHAR(50) NOT NULL DEFAULT '',
  `Rostro` TEXT NOT NULL
  )
ENGINE = InnoDB
DEFAULT CHARACTER SET = latin1;



SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
