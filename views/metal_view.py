import sqlite3
import json

def get_all_metals():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
        """ 
            SELECT
                m.id,
                m.metal,
                m.price
            FROM Metals m
        """
        )
        query_results = db_cursor.fetchall()

        metals = []
        for row in query_results:
            metals.append(dict(row))
        
        serialized_metals = json.dumps(metals)

        return serialized_metals

def get_single_metal(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            m.id,
            m.metal,
            m.price
        FROM Metals m
        WHERE m.id = ?  
        """, (pk,))
        
        query_results = db_cursor.fetchone()

        dictionary_version_of_object = dict(query_results)
        serialized_metal = json.dumps(dictionary_version_of_object)

    return serialized_metal

def create_metal(metal_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO `metals` (metal, price)
            VALUES (?, ?)

            """, 
            (metal_data["metal"], metal_data["price"])
        )

        rows_affected = db_cursor.rowcount

        return True if rows_affected > 0 else False
    
def delete_metal(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
    
        db_cursor.execute(
            """
            DELETE FROM `metals` 
            WHERE id = ?
            """, (pk,))
        
        num_rows_deleted = db_cursor.rowcount

        return True if num_rows_deleted > 0 else False