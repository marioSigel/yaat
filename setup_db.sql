
# Setup database:

create database `yaat`;
create user 'yaat_user'@'localhost' identified by 'secret_string';
grant all on `yaat`.* to 'yaat_user'@'localhost';

CREATE TABLE `results` (
  `user` varchar(200) NOT NULL,
  `name` varchar(200) NOT NULL,
  `discarded` tinyint(4) NOT NULL,
  `x1` int(11) DEFAULT NULL,
  `y1` int(11) DEFAULT NULL,
  `x2` int(11) DEFAULT NULL,
  `y2` int(11) DEFAULT NULL,
  PRIMARY KEY (`user`,`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
