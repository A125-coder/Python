-- Task 1.

-- 1. Выберите из таблицы заказов (orders) номера всех заказов, их суммы и даты.
SELECT `onum`, `amt`, `odate` FROM `orders`;

-- 2. Составьте запрос, который выберет строки из таблицы клиентов (customers), номер продавца которых равен 1001.
SELECT * FROM `customers` where `snum`=1001;
 
-- 3. Выберите имена клиентов города San Jose и их рейтинг из таблицы клиентов (customers).
SELECT `cname`, `rating` FROM `customers` where `city` = "San Jose"; 

-- 4. Выберите идентификаторы продавцов из таблицы заказов (orders), при этом исключите повторы.
SELECT DISTINCT `snum` FROM `orders`;

-- 5. Получите все ряды из таблицы заказов (orders), где сумма заказа больше 1000.
SELECT * FROM `orders` WHERE `amt` > 1000;
 
-- 6. Выберите название города и имена продавцов в Лондоне с размером комиссионных выше 0.11 из таблицы продавцов (salers).
SELECT `city`, `sname` FROM `salers` WHERE `comm`>0.11;

-- 7. Выберите всех клиентов из таблицы клиентов (customers), у которых рейтинг меньше или равен 100 и они при этом не из Рима. В запросе должен использоваться оператор NOT.
SELECT * FROM `customers` WHERE `rating`<=100 AND NOT `city`="Rome";

-- 8. Упростите запрос: "SELECT * FROM salers WHERE comm < 0.12 OR comm = 0.12;".
SELECT * FROM `salers` WHERE `comm` <= 0.12;






--  Task 2.

-- 1. Напишите запрос, который выберет все ряды из таблицы заказов (orders) за март-апрель
SELECT * FROM orders WHERE odate BETWEEN "1990-03-00" AND "1990-05-00";

-- 2. Выберите всех клиентов (таблица customers) продавцов Peel и Motika.
select * from customers where snum in (1001, 1004);

-- 3. Составьте запрос, который выведет всех клиентов, чьи имена находятся в диапазоне A-G включительно.
select * from customers WHERE cname BETWEEN "A" AND "H";

-- 4. Выберите всех представителей, чьи имена начинаются с латинской литеры "C".
SELECT * FROM `customers` WHERE cname like "C%";

-- 5. Выберите всех представителей, чьи имена начинаются на латинскую литеру "D" и при этом заканчиваются на латинскую литеру "n". 
-- Выборка проведите 2-мя различными способами (2 различных запроса, дающих одинаковый результат).
SELECT * FROM salers WHERE sname like "D%" and sname like "%n";
SELECT * FROM salers WHERE sname like "D%n";

-- 6. Выберите всех представителей, чьи имена заканчиваются на латинскую литеру "n", но при этом не начинаются на латинскую литеру "D".
SELECT * FROM customers WHERE cname like "%n" and not cname like "D%";

-- 7. Выберите все ряды с NULL-значениями из таблицы продавцов
SELECT * FROM salers where sname is NULL;







-- Task 3.

-- 1. Получите среднее значение поля amt (таблица orders), не используя при этом функцию AVG(). 
-- Результат должен быть получен одним запросом. Подсказка: используйте вложенный запрос.
SELECT (sum(amt)/count(amt)) as average from orders;
SELECT ((SELECT SUM(amt) FROM orders) / (SELECT COUNT(amt) FROM orders)) AS result;

-- 2. Получите сумму всех продаж продавца с идентификатором 1007. 
-- Попробуйте составить 2 запроса, получающих одинаковый результат.
SELECT SUM(amt) FROM orders WHERE snum = 1007;
SELECT SUM(amt) FROM orders GROUP BY snum HAVING snum = 1007;

-- 3. Получите список городов (без повторов) и максимальный рейтинг для каждого из них из таблицы customers.
SELECT city, max(rating) from customers group by city;

-- 4. Получите список городов (без повторов) и минимальный размер комиссионных для каждого из них из таблицы salers.
SELECT city, min(comm) FROM salers GROUP BY city;