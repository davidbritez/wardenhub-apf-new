create user 'wardenhub-apf'@'localhost' identified by 'password';
create database wardenhubapf;
grant all privileges on wardenhubapf.* to 'wardenhub-apf'@'localhost' ;
flush privileges;
