import sqlite3
database_name = "app.db"
def get_connection():
    conn = sqlite3.connect(database_name)
    conn.row_factory = sqlite3.Row
    return conn
def init_db():
    conn = get_connection()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed BOOLEAN DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()
def create_task(title):
    conn = get_connection()
    cursor = conn.execute(
    "INSERT INTO tasks(title)" \
    "VALUES(?)",
    (title,)
        )
    conn.commit()
    task_id = cursor.lastrowid
    row = conn.execute(
    "SELECT*FROM tasks WHERE id=?",
    (task_id,)
    ).fetchone()
    conn.close()
def get_all_tasks():
    conn = get_connection()
    rows = conn.execute(
    "SELECT*FROM tasks"
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]
def get_task_by_id(task_id):
    with get_connection() as conn:
        row = conn.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()
        return dict(row) if row else None
def update_task(task_id, title, status):
    with get_connection() as conn:
        conn.execute("""
            UPDATE tasks
            SET title = ?, completed = ?
            WHERE id = ? """,
            (title, status, task_id)
        )
        conn.commit()
        row = conn.execute(
            "SELECT * FROM tasks WHERE id = ?",
            (task_id,)
        ).fetchone()
        return dict(row) if row else None
def delete_task(task_id):
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )
        conn.commit()
        return cursor.rowcount > 0