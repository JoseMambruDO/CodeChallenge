/*
You are given three tables: Students, Friends and Packages. Students contains two 
columns: ID and Name. Friends contains two columns: ID and Friend_ID (ID of the ONLY 
best friend). Packages contains two columns: ID and Salary (offered salary in $ 
thousands per month).

Write a query to output the names of those students whose best friends got offered a 
higher salary than them. Names must be ordered by the salary amount offered to the best 
friends. It is guaranteed that no two students got same salary offer.
*/


select ms.name
from (select s.id, s.name, p.salary
from students as s inner join
packages as p on s.id = p.id) as ms 

inner join

(select f.id, friend_id, pf.salary, sf.name
from  friends as f 
inner join packages as pf on f.friend_id = pf.id
inner join students as sf on f.friend_id = sf.id)  as ss

on ms.id = ss.id

where ss.salary > ms.salary

order by ss.salary asc
