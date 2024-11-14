-- Temporary Table은 Autovacuum 대상이 아니다.
-- Temporary Table은 임시 테이블을 생성한 Connection에서만 조회할 수 있기 때문에 Autovacuum 데몬은 Temporary Table을 볼 수 없다.
-- Temporary Table이 사용중인 공간은 Connection이 닫히면 저절로 회수된다.

CREATE TEMPORARY TABLE temp_customers AS SELECT DISTINCT * FROM customers;
TRUNCATE customers;
INSERT INTO customers SELECT * FROM temp_customers;

WITH ranked_events AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY event_type, product_id ORDER BY event_time) AS row_num,
           LAG(event_time) OVER (PARTITION BY event_type, product_id ORDER BY event_time) AS prev_event_time
    FROM customers
)
DELETE FROM customers
USING ranked_events
WHERE ranked_events.row_num > 1
  AND EXTRACT(EPOCH FROM (ranked_events.event_time - ranked_events.prev_event_time)) <= 1
  AND customers.event_time = ranked_events.event_time
  AND customers.event_type = ranked_events.event_type
  AND customers.product_id = ranked_events.product_id;