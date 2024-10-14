import sqlite3
import json

def get_all_orders():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
        """ 
            SELECT
                o.id,
                o.metal_id,
                o.size_id,
                o.style_id
            FROM `Orders` o
        """
        )
        query_results = db_cursor.fetchall()

        orders = []
        for row in query_results:
            orders.append(dict(row))
        
        serialized_orders = json.dumps(orders)

        return serialized_orders

def get_single_order(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            o.id,
            o.metal_id,
            o.size_id,
            o.style_id
        FROM `Orders` o
        WHERE o.id = ?  
        """, (pk,))
        
        query_results = db_cursor.fetchone()

        if query_results is None:
            return None

        dictionary_version_of_object = dict(query_results)
        serialized_order = json.dumps(dictionary_version_of_object)

    return serialized_order

def create_order(order_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO `Orders` (metal_id, size_id, style_id)
            VALUES (?, ?, ?)

            """, 
            (order_data["metal_id"], order_data["size_id"], order_data["style_id"],)
        )

        rows_affected = db_cursor.rowcount

        return True if rows_affected > 0 else False
    
def delete_order(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
    
        db_cursor.execute(
            """
            DELETE FROM `Orders` 
            WHERE id = ?
            """, (pk,))
        
        num_rows_deleted = db_cursor.rowcount

        return True if num_rows_deleted > 0 else False