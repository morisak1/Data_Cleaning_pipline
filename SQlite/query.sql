-- view table
SELECT * FROM user_profiles;



-- query 1: select names and salary with age greater than 30 and country USA
SELECT name,Salary_USD FROM user_profiles
WHERE age > 30 AND Country = 'USA';

-- query 2: select names and age of users from USA
SELECT name,age FROM user_profiles
WHERE country = 'USA';

-- query 3: select names and country of users with age between 30 and 35
SELECT name,country FROM user_profiles
WHERE age BETWEEN 30 AND 35;