-- MySQL Script generated by MySQL Workbench
-- Wed Feb 19 20:07:39 2020
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema tg_rl_openai_atari
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `tg_rl_openai_atari` ;

-- -----------------------------------------------------
-- Schema tg_rl_openai_atari
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `tg_rl_openai_atari` DEFAULT CHARACTER SET utf8 ;
USE `tg_rl_openai_atari` ;

-- -----------------------------------------------------
-- Table `tg_rl_openai_atari`.`AlgorithmParams`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tg_rl_openai_atari`.`AlgorithmParams` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `neural_network_params` JSON NOT NULL,
  `rl_params` JSON NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tg_rl_openai_atari`.`Game`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tg_rl_openai_atari`.`Game` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NOT NULL,
  `gym_name` VARCHAR(45) NOT NULL,
  `action_space` INT NOT NULL DEFAULT 9,
  `state_size` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `tg_rl_openai_atari`.`TrainingResults`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `tg_rl_openai_atari`.`TrainingResults` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `avg_score` DOUBLE NOT NULL,
  `num_of_episodes` INT NOT NULL,
  `training_start` DATETIME NOT NULL,
  `training_end` DATETIME NOT NULL,
  `avg_game_time_seconds` INT NOT NULL,
  `id_algorithm_params` INT NOT NULL,
  `id_game` INT NOT NULL,
  INDEX `fk_Results_AlgorithmParams_idx` (`id_algorithm_params` ASC) VISIBLE,
  PRIMARY KEY (`id`),
  INDEX `fk_Results_Game1_idx` (`id_game` ASC) VISIBLE,
  CONSTRAINT `fk_Results_AlgorithmParams`
    FOREIGN KEY (`id_algorithm_params`)
    REFERENCES `tg_rl_openai_atari`.`AlgorithmParams` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Results_Game1`
    FOREIGN KEY (`id_game`)
    REFERENCES `tg_rl_openai_atari`.`Game` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;