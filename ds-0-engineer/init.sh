docker compose up --wait
psql "postgresql://sunpark:mysecretpassword@localhost/piscineds" -f ./ex02/table.sql
cd ex03 && source ./automatic_table.sh
cd ../ex04 && source ./items_table.sh
