import sqlite3
import json

def get_all_styles():
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(
        """ 
            SELECT
                s.id,
                s.style,
                s.price
            FROM Styles s
        """
        )
        query_results = db_cursor.fetchall()

        styles = []
        for row in query_results:
            styles.append(dict(row))
        
        serialized_styles = json.dumps(styles)

        return serialized_styles

def get_single_style(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            s.id,
            s.style,
            s.price
        FROM styles s
        WHERE s.id = ?  
        """, (pk,))
        
        query_result = db_cursor.fetchone()

        if query_result is None:
            return None
        
        dictionary_version_of_object = dict(query_result)
        serialized_style = json.dumps(dictionary_version_of_object)

    return serialized_style

def create_style(style_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute(
            """
            INSERT INTO Styles (style, price)
            VALUES (?, ?)

            """, 
            (style_data["style"], style_data["price"])
        )

        rows_affected = db_cursor.rowcount

        return True if rows_affected > 0 else False
    
def delete_style(pk):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
    
        db_cursor.execute(
            """
            DELETE FROM Styles 
            WHERE id = ?
            """, (pk,))
        
        num_rows_deleted = db_cursor.rowcount

        return True if num_rows_deleted > 0 else None
    
def update_style(pk, style_data):
    with sqlite3.connect("./kneeldiamonds.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute(""" 
            UPDATE Styles  
                SET 
                    style = ?,
                    price = ?
            WHERE id = ?
        """,
        (style_data['style'], style_data['price'], pk,)
        )

        rows_affected = db_cursor.rowcount

        return True if rows_affected > 0 else False