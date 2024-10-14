-- Run this block if you already have a database and need to re-create it
DELETE FROM Metals;
DELETE FROM Sizes;
DELETE FROM Styles;
DELETE FROM "Orders";

DROP TABLE IF EXISTS Metals;
DROP TABLE IF EXISTS Sizes;
DROP TABLE IF EXISTS Styles;
DROP TABLE IF EXISTS "Orders";
-- End block

CREATE TABLE `Metals`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(7,2) NOT NULL
);

CREATE TABLE `Sizes`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `size` NUMERIC(5, 2) NOT NULL,
    `price` NUMERIC(7,2) NOT NULL
);

CREATE TABLE `Styles`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(7,2) NOT NULL
);

CREATE TABLE `Orders`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    [metal_id] INTEGER NOT NULL,
    [size_id] INTEGER NOT NULL,
    [style_id] INTEGER NOT NULL,
    FOREIGN KEY('metal_id') REFERENCES `Metals`(`id`),
    FOREIGN KEY('size_id') REFERENCES `Sizes`(`id`),
    FOREIGN KEY('style_id') REFERENCES `Styles`(`id`)
);

INSERT INTO `Metals` (metal, price) VALUES ("Sterling Silver", 409.95);
INSERT INTO `Metals` (metal, price) VALUES ("14K Gold", 909.95);
INSERT INTO `Metals` (metal, price) VALUES ("24K Gold", 1009.95);
INSERT INTO `Metals` (metal, price) VALUES ("Platinum", 2009.95);
INSERT INTO `Metals` (metal, price) VALUES ("Palladium", 3009.95);

INSERT INTO `Sizes` (size, price) VALUES (0.5, 409.95);
INSERT INTO `Sizes` (size, price) VALUES (0.75, 909.95);
INSERT INTO `Sizes` (size, price) VALUES (1, 1009.95);
INSERT INTO `Sizes` (size, price) VALUES (1.5, 2009.95);
INSERT INTO `Sizes` (size, price) VALUES (2, 3009.95);

INSERT INTO `Styles` (style, price) VALUES ("Sterling Silver", 409.95);
INSERT INTO `Styles` (style, price) VALUES ("14K Gold", 909.95);
INSERT INTO `Styles` (style, price) VALUES ("24K Gold", 1009.95);

INSERT INTO `Orders` (metal_id, size_id, style_id) VALUES (1, 5, 3);
INSERT INTO `Orders` (metal_id, size_id, style_id) VALUES (2, 5, 2);
INSERT INTO `Orders` (metal_id, size_id, style_id) VALUES (3, 4, 1);
INSERT INTO `Orders` (metal_id, size_id, style_id) VALUES (4, 2, 2);
INSERT INTO `Orders` (metal_id, size_id, style_id) VALUES (5, 3, 3);