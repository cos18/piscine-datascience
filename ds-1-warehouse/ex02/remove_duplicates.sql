-- Temporary Table은 Autovacuum 대상이 아니다.
-- Temporary Table은 임시 테이블을 생성한 Connection에서만 조회할 수 있기 때문에 Autovacuum 데몬은 Temporary Table을 볼 수 없다.
-- Temporary Table이 사용중인 공간은 Connection이 닫히면 저절로 회수된다.

CREATE TEMPORARY TABLE temp_customers AS SELECT DISTINCT * FROM customers;
TRUNCATE customers;
INSERT INTO customers SELECT * FROM temp_customers;