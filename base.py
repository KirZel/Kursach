import sqlite3

connection = sqlite3.connect('my_database.db')
cursor = connection.cursor()

# Создаем таблицу Users
cursor.execute('''
CREATE TABLE IF NOT EXISTS `Жанры` (
  `id_Жанра` INT NOT NULL,
  `Название` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_Жанра`));


CREATE TABLE IF NOT EXISTS `Инструменты` (
  `id_Инструмента` INT NOT NULL,
  `Название` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`id_Инструмента`));


CREATE TABLE IF NOT EXISTS `Название характеристики инструментов` (
  `id_ХИ` INT NOT NULL,
  `Название` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`id_ХИ`));

               
CREATE TABLE IF NOT EXISTS `Инструменты жанра` (
  `id_Жанра` INT NOT NULL,
  `id_Инструмента` INT NOT NULL,
  PRIMARY KEY (`id_Жанра`, `id_Инструмента`),
  CONSTRAINT `fk_Жанры_has_Инструменты_Жанры`
    FOREIGN KEY (`id_Жанра`)
    REFERENCES `Жанры` (`id_Жанра`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Жанры_has_Инструменты_Инструмент1`
    FOREIGN KEY (`id_Инструмента`)
    REFERENCES `Инструменты` (`id_Инструмента`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

               
CREATE TABLE IF NOT EXISTS `Характеристики инструментов` (
  `id_Инструмента` INT NOT NULL,
  `id_ХИ` INT NOT NULL,
  PRIMARY KEY (`id_Инструмента`, `id_ХИ`),
  CONSTRAINT `fk_Инструменты_has_Характеристики и1`
    FOREIGN KEY (`id_Инструмента`)
    REFERENCES `Инструменты` (`id_Инструмента`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Инструменты_has_Характеристики и2`
    FOREIGN KEY (`id_ХИ`)
    REFERENCES `Название характеристики инструментов` (`id_ХИ`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);

               
CREATE TABLE IF NOT EXISTS `Возможные значения характеристки` (
  `id_ВЗХ` INT NOT NULL,
  `id_ХИ` INT NOT NULL,
  `dataType` VARCHAR(5) NOT NULL,
  `Значение` VARCHAR(90) NOT NULL,
  PRIMARY KEY (`id_ВЗХ`, `id_ХИ`),
  CONSTRAINT `fk_Возможные значения характерист1`
    FOREIGN KEY (`id_ХИ`)
    REFERENCES `Название характеристики инструментов` (`id_ХИ`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);


CREATE TABLE IF NOT EXISTS `Значения для характеристик инструмента для жанра` (
  `id_Жанра` INT NOT NULL,
  `id_Инструмента` INT NOT NULL,
  `id_ХИ` INT NOT NULL,
  `id_Возможные значения характеристки` INT NOT NULL,
  PRIMARY KEY (`id_Жанра`, `id_Инструмента`, `id_ХИ`, `id_Возможные значения характеристки`),
  CONSTRAINT `fk_Инструменты жанра_has_Характерис3`
    FOREIGN KEY (`id_Возможные значения характеристки` , `id_ХИ`)
    REFERENCES `Возможные значения характеристки` (`id_ВЗХ` , `id_ХИ`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Инструменты жанра_has_Характерис4`
    FOREIGN KEY (`id_Инструмента`)
    REFERENCES `Характеристики инструментов` (`id_Инструмента`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Инструменты жанра_has_Характерис5`
    FOREIGN KEY (`id_Жанра`)
    REFERENCES `Инструменты жанра` (`id_Жанра`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Инструменты жанра_has_Характерис1`
    FOREIGN KEY (`id_Инструмента`)
    REFERENCES `Инструменты жанра` (`id_Инструмента`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_Инструменты жанра_has_Характерис2`
    FOREIGN KEY (`id_ХИ`)
    REFERENCES `Характеристики инструментов` (`id_ХИ`)
    ON DELETE CASCADE
    ON UPDATE CASCADE);
''')

# Сохраняем изменения и закрываем соединение
connection.commit()
connection.close()