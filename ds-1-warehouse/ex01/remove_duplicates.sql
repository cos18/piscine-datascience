DELETE FROM customers C1
      USING customers C2
WHERE C1.ctid         > C2.ctid
  AND C1.event_type   = C2.event_type
  AND C1.product_id   = C2.product_id
  AND C1.user_id      = C2.user_id;

SELECT t.*, CTID
                  FROM public.customers t
                  where user_id = 561162056
order by event_time;

SELECT min(user_id), max(user_id) FROM public.customers t;

-- 39cf2227-03ed-421e-9615-7814b9b3c5e6
-- 2022-12-01 00:03:13.000000 +00:00,remove_from_cart,5830501,3.67,561162056,39cf2227-03ed-421e-9615-7814b9b3c5e6