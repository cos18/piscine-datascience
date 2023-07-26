docker compose up --wait
psql "postgresql://sunpark:mysecretpassword@localhost/piscineds" -f ./ex02/table.sql
cd ex04 && source ./items_table.sh
