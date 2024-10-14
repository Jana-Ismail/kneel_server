import sqlite3
import json

def get_all_sizes():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
        """ 
            SELECT
                s.id,
                s.size,
                s.price
            FROM Sizes s
        """
        )
        query_results = db_cursor.fetchall()

        sizes = []
        for row in query_results:
            sizes.append(dict(row))
        
        serialized_sizes = json.dumps(sizes)

        return serialized_sizes

def get_single_size(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            s.id,
            s.size,
            s.price
        FROM sizes s
        WHERE s.id = ?  
        """, (pk,))
        
        query_result = db_cursor.fetchone()

        if query_result is None:
            return None
        
        dictionary_version_of_object = dict(query_result)
        serialized_size = json.dumps(dictionary_version_of_object)

    return serialized_size

def create_size(size_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO `sizes` (size, price)
            VALUES (?, ?)

            """, 
            (size_data["size"], size_data["price"])
        )

        rows_affected = db_cursor.rowcount

        return True if rows_affected > 0 else False
    
def delete_size(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
    
        db_cursor.execute(
            """
            DELETE FROM Sizes 
            WHERE id = ?
            """, (pk,))
        
        num_rows_deleted = db_cursor.rowcount

        return True if num_rows_deleted > 0 else None
    
def update_size(pk, size_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(""" 
            UPDATE Sizes  
                SET 
                    size = ?,
                    price = ?
            WHERE id = ?
        """,
        (size_data['size'], size_data['price'], pk,)
        )

        rows_affected = db_cursor.rowcount

        return True if rows_affected > 0 else False