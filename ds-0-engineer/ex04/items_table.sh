export $(grep -v '^#' .env | xargs)

for file in "$GOINFRE_PATH/raw_data/item"/*.csv; do
    if [[ -f "$file" ]]; then
        table_name=$(basename "$file" .csv)

		create_table_query="DROP TABLE IF EXISTS $table_name ;"
        create_table_query+="CREATE TABLE IF NOT EXISTS $table_name (product_id INT, category_id BIGINT, category_code TEXT, brand TEXT);"

        PGPASSWORD=$POSTGRES_PASSWORD psql -h localhost -U $POSTGRES_USER -d $POSTGRES_DB -p $POSTGRES_PORT -c "$create_table_query"

		insert_query="COPY $table_name (product_id, category_id, category_code, brand) "
		insert_query+="FROM '"
		insert_query+=$POSTGRES_PATH
		insert_query+="/raw_data/item/"
		insert_query+="$table_name.csv' DELIMITER ',' CSV HEADER;"

		PGPASSWORD=$POSTGRES_PASSWORD psql -h localhost -U $POSTGRES_USER -d $POSTGRES_DB -p $POSTGRES_PORT -c "$insert_query"
    fi
done
