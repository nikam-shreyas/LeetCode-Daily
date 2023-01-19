/* Write your PL/SQL query statement below */

select 
    a.id,
    case
        when a.p_id is null then 'Root'
        when a.id in (select p_id from tree where p_id is not null) then 'Inner'
        else 'Leaf'
    end as Type
from 
    tree a