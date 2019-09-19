select *
from "stock-price-db"."raw"
where symbol = 'GOOG' and date(date) > date('2019-07-20')