# Write your MySQL query statement below
#sort descending
# select turn use two tables
# calculate rolling weight
select k.person_name from (select person_name, sum(weight) over (order by turn) as cum_sum from queue) k where k.cum_sum<=1000
order by k.cum_sum desc
limit 1
