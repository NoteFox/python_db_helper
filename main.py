import psycopg2

PG_HOST = "db.f4.htw-berlin.de"
PG_DATABASE = "_s0569194__htw_db_service"
PG_USER = "s0569194"
PG_PASSWORD = "P3a_-S2l"

if __name__ == '__main__':

    #create_schemas = open("Uni-DB_Schema").read()
    #import_data = open("Uni-DB_Daten").read()

    conn = psycopg2.connect(
        host=PG_HOST,
        database=PG_DATABASE,
        user=PG_USER,
        password=PG_PASSWORD
    )

    cursor = conn.cursor()

    schema_list = cursor.execute("SELECT schema_name FROM information_schema.schemata")

    #cursor.execute(create_schemas)
    #return_value = cursor.fetchone()
    #print(return_value)

    #cursor.execute(import_data)
    #return_value = cursor.fetchone()
    #print(return_value)

    cursor.close()