-- MySQL Script generated by MySQL Workbench
-- Thu Jan 17 20:08:39 2019
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema magacin2
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema magacin2
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `magacin2` DEFAULT CHARACTER SET utf8 ;
USE `magacin2` ;

-- -----------------------------------------------------
-- Table `magacin2`.`korisnici`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `magacin2`.`korisnici` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(32) NOT NULL,
  `lozinka` VARCHAR(32) NOT NULL,
  `ime` TEXT NOT NULL,
  `prezime` TEXT NOT NULL,
  `uloga` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `magacin2`.`stavke`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `magacin2`.`stavke` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `naziv` TEXT NOT NULL,
  `kolicina` INT NOT NULL,
  `opis` LONGTEXT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `magacin2`.`trebovanja`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `magacin2`.`trebovanja` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `datum` DATETIME NOT NULL,
  `kolicina` INT NOT NULL,
  `korisnici_id` INT NOT NULL,
  `stavke_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_trebovanja_korisnici_idx` (`korisnici_id` ASC) VISIBLE,
  INDEX `fk_trebovanja_stavke1_idx` (`stavke_id` ASC) VISIBLE,
  CONSTRAINT `fk_trebovanja_korisnici`
    FOREIGN KEY (`korisnici_id`)
    REFERENCES `magacin2`.`korisnici` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_trebovanja_stavke1`
    FOREIGN KEY (`stavke_id`)
    REFERENCES `magacin2`.`stavke` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `magacin2`.`korisnici`
-- -----------------------------------------------------
START TRANSACTION;
USE `magacin2`;
INSERT INTO `magacin2`.`korisnici` (`id`, `username`, `lozinka`, `ime`, `prezime`, `uloga`) VALUES (1, 'toma', '1234', 'Nemanja', 'Tomanic', 'admin');
INSERT INTO `magacin2`.`korisnici` (`id`, `username`, `lozinka`, `ime`, `prezime`, `uloga`) VALUES (2, 'jovo', '123', 'Jovan', 'Pejanovic', 'user');
INSERT INTO `magacin2`.`korisnici` (`id`, `username`, `lozinka`, `ime`, `prezime`, `uloga`) VALUES (3, 'vjeko', '1234', 'Vjekoslav', 'Rakanovic', 'user');

COMMIT;


-- -----------------------------------------------------
-- Data for table `magacin2`.`stavke`
-- -----------------------------------------------------
START TRANSACTION;
USE `magacin2`;
INSERT INTO `magacin2`.`stavke` (`id`, `naziv`, `kolicina`, `opis`) VALUES (1, 'Monitor', 10, 'LCD Monitor');
INSERT INTO `magacin2`.`stavke` (`id`, `naziv`, `kolicina`, `opis`) VALUES (2, 'Tastatura', 5, 'Mehanicka RAZER GT520');
INSERT INTO `magacin2`.`stavke` (`id`, `naziv`, `kolicina`, `opis`) VALUES (3, 'Mis', 20, 'Bezicni MS 450');

COMMIT;


-- -----------------------------------------------------
-- Data for table `magacin2`.`trebovanja`
-- -----------------------------------------------------
START TRANSACTION;
USE `magacin2`;
INSERT INTO `magacin2`.`trebovanja` (`id`, `datum`, `kolicina`, `korisnici_id`, `stavke_id`) VALUES (1, '2018-12-12', 3, 2, 1);

COMMIT;

