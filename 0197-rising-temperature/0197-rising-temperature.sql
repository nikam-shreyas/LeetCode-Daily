select a.id
from weather a, weather b
where a.temperature > b.temperature and DateDiff(a.recordDate,b.recordDate)=1;