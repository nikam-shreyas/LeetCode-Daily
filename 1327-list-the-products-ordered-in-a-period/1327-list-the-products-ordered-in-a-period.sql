# Write your MySQL query statement below
select pr.product_name, sum(o.unit) as unit from
products pr join orders o
on pr.product_id = o.product_id
where Month(o.order_date)=2 and Year(o.order_date)=2020 
group by pr.product_id 
having sum(unit)>=100