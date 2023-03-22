SQL - more quiries
-- check if user in sql is created or not 
SELECT User FROM mysql.user WHERE User = 'user_0d_1';
-- show grants of user 
SHOW GRANTS FOR 'user_0d_2'@'localhost';

** sudo service mysql start 
sudo mysql 
use (name of database)
-- check properties of tables 
SHOW COLUMNS FROM (name of table);
__ downnoload file in my current direct
wget https://s3.eu-west-3.amazonaws.com/hbtn.intranet.project.files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql
