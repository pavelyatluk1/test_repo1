-- Pavlo Yatluk
-- dz_16
-- #1. Написати запит, щоб отримати всі відомості про співробітників із таблиці employees упорядковано
-- за іменами за зростанням.

use pds;
SELECT * FROM employees ORDER BY FIRST_NAME;

-- #2. Написати запит, щоб отримати імена, ЗП та податки усії співробітників.

use pds;
alter table pds.employees
Add taxes float;
SELECT FIRST_NAME, LAST_NAME, SALARY, taxes FROM employees;

-- #3. Написати запит, щоб отримати загальну суму ЗП всіх співробітників.

use pds;
SELECT SUM(SALARY) FROM employees;

-- #4. Написати запит, щоб отримати max та min ЗП працівників.

use pds;
SELECT max(SALARY), min(SALARY) FROM employees;

-- #5. Написати запит, щоб отримати середню ЗП та кількість працівників.

 use pds;
SELECT avg(SALARY), COUNT(*) FROM employees;