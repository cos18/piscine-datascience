docker compose up --wait

export $(grep -v '^#' .env | xargs)

for file in "$GOINFRE_PATH$CUSTOMER_RAW_DATA_PATH"/*.csv; do
    if [[ -f "$file" ]]; then
        table_name=$(basename "$file" .csv)

		create_table_query="DROP TABLE IF EXISTS $table_name ;"
        create_table_query+="CREATE TABLE IF NOT EXISTS $table_name (event_time TIMESTAMP with time zone, event_type VARCHAR(128), product_id INT, price NUMERIC, user_id BIGINT, user_session UUID);"

        PGPASSWORD=$POSTGRES_PASSWORD psql -h localhost -U $POSTGRES_USER -d $POSTGRES_DB -p $POSTGRES_PORT -c "$create_table_query"

		insert_query+="COPY $table_name (event_time, event_type, product_id, price, user_id, user_session) "
		insert_query+="FROM '"
		insert_query+=$POSTGRES_PATH$CUSTOMER_RAW_DATA_PATH
		insert_query+="/"
		insert_query+="$table_name.csv' DELIMITER ',' CSV HEADER;"

		PGPASSWORD=$POSTGRES_PASSWORD psql -h localhost -U $POSTGRES_USER -d $POSTGRES_DB -p $POSTGRES_PORT -c "$insert_query"
    fi
done

source ex04/items_table.sh
