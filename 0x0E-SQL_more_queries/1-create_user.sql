-- Creates user `user_0d_1`.
CREATE USER
       IF NOT EXISTS 'user_0d_1'@'localhost'
       IDENTIFIED WITH 'user_0d_1_pwd';

-- Grant all privileges
GRANT ALL PRIVILEGES
      ON *.*
      TO 'user_0d_1'@'localhost';
