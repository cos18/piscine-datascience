#!/bin/bash

export $(grep -v '^#' .env | xargs)

for file in "$GOINFRE_PATH$CUSTOMER_RAW_DATA_PATH"/*.csv; do
    if [[ -f "$file" ]]; then
        table_name=$(basename "$file" .csv)

        insert_query="COPY $table_name (event_time, event_type, product_id, price, user_id, user_session) "
		insert_query+="FROM '"
		insert_query+=$POSTGRES_PATH$CUSTOMER_RAW_DATA_PATH
		insert_query+="/"
		insert_query+="$table_name.csv' DELIMITER ',' CSV HEADER;"

        PGPASSWORD=$POSTGRES_PASSWORD psql -h localhost -U $POSTGRES_USER -d $POSTGRES_DB -p $POSTGRES_PORT -c "$insert_query"
    fi
done