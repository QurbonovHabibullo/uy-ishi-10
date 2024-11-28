select country from customers
union 
select country from employees;

select country from customers
union all
select country from employees;

-- ---------------------------------
select country from customers
intersect 
select country from employees;

select country from customers
intersect all
select country from employees;

select country from customers
except
select country from employees;

-- ====================================

-- select car_count count(*) from models natural join brands 
-- group by brand_name
-- having count(*) >=4;
-- ==============================
select distinct country from customers;


select count(distinct country) from customers;






