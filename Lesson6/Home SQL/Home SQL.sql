-- 1 Выберите все заказы за 1990-03-10 из таблицы orders, упорядочив их по сумме в порядке возрастания

SELECT * FROM orders WHERE odate='1990-03-10' GROUP BY amt;
SELECT * FROM orders WHERE odate='1990-03-10' ORDER BY amt;
SELECT * FROM orders WHERE odate='1990-03-10' ORDER BY amt ASC;


-- 2 Выберите 2 последних заказа из таблицы orders

SELECT * FROM orders LIMIT 8, 9;
SELECT * FROM orders ORDER BY onum DESC LIMIT 2;


-- 3 Получите имена клиентов, рейтинг которых больше 200, город их проживания, а также имена продавцов, к которым относятся указанные клиенты. Используйте псевдонимы таблиц

SELECT customers.cname, customers.city, customers.rating, salers.sname FROM `customers`, `salers` WHERE customers.rating>200 AND customers.snum = salers.snum;



-- 4 Выберите данные о максимальной сумме заказа таблицы orders

SELECT *, MAX(amt)FROM `orders`;
SELECT * FROM orders ORDER BY amt DESC LIMIT 1;



-- 5 Выберите имена продавцов (таблица salers), сумму каждой продажи продавцов (таблица orders) и подсчитанную сумму комиссионных с каждой конкретной продажи. Вывод сопроводите пояснениями, чтобы каждый ряд таблицы имел следующий вид: Продавец: | Rifkin | Сумма продажи: | 18.69 | Размер комиссионных: | 2.8035

SELECT DISTINCT salers.sname AS "Продавец", orders.amt AS "Cумма продажи", salers.comm*orders.amt AS "Размер комиссионных" FROM `customers`, `salers`, `orders` WHERE salers.snum = orders.snum;

SELECT DISTINCT "Продавец:" AS "Продавец", salers.sname AS "Saler", "Сумма продажи:" AS "Cумма продажи", orders.amt AS "Amount", "Размер комиссионных:" AS "Размер комиссионных", salers.comm*orders.amt AS "Comm" FROM `customers`, `salers`, `orders` WHERE salers.snum = orders.snum ORDER BY salers.sname;
