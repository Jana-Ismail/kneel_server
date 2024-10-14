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
                o.style_id,
                m.metal,
                m.price metal_price,
                s.size,
                s.price size_price,
                st.style,
                st.price style_price
            FROM `Orders` o
            JOIN Metals m ON o.metal_id = m.id
            JOIN Sizes s ON o.size_id = s.id
            JOIN Styles st ON o.style_id = st.id
        """
        )
        query_results = db_cursor.fetchall()

        orders = []
        for row in query_results:
            metal = {
                'metal': row['metal'],
                'price': row['metal_price']
            }
            size = {
                'size': row['size'],
                'price': row['size_price']
            }
            style = {
                'style': row['style'],
                'price': row['style_price']
            }
            order = {
                'metal_id': row['metal_id'],
                'metal': metal,
                'size_id': row['size_id'],
                'size': size,
                'style_id': row['style_id'],
                'style': style
            }
            orders.append(order)
        
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
            o.style_id,
            m.metal,
            m.price metal_price,
            s.size,
            s.price size_price,
            st.style,
            st.price style_price                                         
        FROM `Orders` o
        JOIN Metals m ON o.metal_id = m.id
        JOIN Sizes s ON o.size_id = s.id
        JOIN Styles st ON o.style_id = st.id                                   
        WHERE o.id = ?  
        """, (pk,))
        
        query_result = db_cursor.fetchone()

        if query_result is None:
            return None

        metal = {
            'metal': query_result['metal'],
            'price': query_result['metal_price']
        }
        size = {
            'size': query_result['size'],
            'price': query_result['size_price']
        }
        style = {
            'style': query_result['style'],
            'price': query_result['style_price']
        }
        order = {
            'metal_id': query_result['metal_id'],
            'metal': metal,
            'size_id': query_result['size_id'],
            'size': size,
            'style_id': query_result['style_id'],
            'style': style
        }
        
        serialized_order = json.dumps(order)

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