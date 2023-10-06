(select name as results from users join movierating using(user_id)
group by user_id 
order by count(rating) desc, name asc
limit 1)
union all
(select title as results from movies join movieRating using(movie_id)
where Year(created_at)=2020 and Month(created_at)=2
group by movie_id
order by avg(rating) desc, title asc
limit 1
)