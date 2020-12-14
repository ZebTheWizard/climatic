import numpy as np
import sqlite3
from autoload import load_submodules
import app.migrations
import time
import sqlite3

class model():
    table = None
    _query = ""
    _params = []
    _insert_columns = {}
    def __init__(self):
        self.table = getattr(self, 'table', self.__class__.__name__.lower())

    def __setattr__(self, name, value):
        if name not in dir(self):
            self._insert_columns[name] = value
        else:
            self.__dict__[name] = value

    def query(self, query, params=[]):
        self._query = query
        self._params = params
        return self

    def remove(self):
        query = "DELETE FROM %s %s" % (self.table, self._query)
        code = 500
        msg = "success"
        with sqlite3.connect("database.db") as con:
            try:
                cur = con.cursor()
                cur.execute(query, list(self._params))
                code = 200
            except Exception as e:
                msg = str(e)
                con.rollback()
            return msg, code

    def get(self, select="*"):
        query = "SELECT %s FROM %s %s" % (select, self.table, self._query)
        code = 500
        msg = "success"
        with sqlite3.connect("database.db") as con:
            try:
                cur = con.cursor()
                cur.execute(query, list(self._params))
                res = cur.fetchall()
                columns = next(zip(*cur.description))
                msg = []
                for m in res:
                    msg.append(dict(zip(columns, m)))
                code = 200
            except Exception as e:
                msg = str(e)
                con.rollback()
            return msg, code

    def insert(self):
        columns = self._insert_columns.keys()
        qmarks = list("?" * len(columns))
        query = "INSERT INTO %s (%s) VALUES (%s)" % (self.table, ",".join(columns), ",".join(qmarks))
        
        code = 500
        msg = "success"
        with sqlite3.connect("database.db") as con:
            try:
                cur = con.cursor()
                cur.execute(query, list(self._insert_columns.values()))
                con.commit()
                code = 200
            except Exception as e:
                msg = str(e)
                con.rollback()
            return msg, code

def _create_migrations(force=False):
    with sqlite3.connect("database.db") as con:
        try:
            cur = con.cursor()
            if force:
                cur.execute("DROP TABLE IF EXISTS migrations")
            cur.execute(("""
            CREATE TABLE IF NOT EXISTS migrations (
                name TEXT UNIQUE,
                migration INT
            )
            """))
            con.commit()
        except Exception as err:
            print(err)
        
def _last_migration():
    with sqlite3.connect("database.db") as con:
        try:
            cur = con.cursor()
            cur.execute("SELECT MAX(migration) FROM migrations")
        except Exception as err:
            print(err)

def _insert_migration(name, num):
    with sqlite3.connect("database.db") as con:
        try:
            cur = con.cursor()
            cur.execute("INSERT INTO migrations (name, migration) VALUES (?,?)", (name, num))
            return True
        except Exception as err:
            return False

def _get_rollback(num):
    with sqlite3.connect("database.db") as con:
        try:
            cur = con.cursor()
            cur.execute("SELECT * FROM migrations WHERE migration = ?", [num])
            return cur.fetchall()
        except Exception as err:
            print(err)
            return []

def _rollback(num):
    with sqlite3.connect("database.db") as con:
        try:
            cur = con.cursor()
            cur.execute("DELETE FROM migrations WHERE migration = ?", [num])
        except Exception as err:
            print(err)

def run_migrations_up():
    time.sleep(0.5)
    _create_migrations(True)
    last = _last_migration() or 1
    migrations = load_submodules(app.migrations)
    for key in sorted(migrations.keys()):
        migration = migrations[key]
        if _insert_migration(key, last):
            with sqlite3.connect("database.db") as con:
                try:
                    cur = con.cursor()
                    query = migration.up()
                    if query:
                        if isinstance(query, str):
                            cur.execute(query)
                        else:
                            for q in query:
                                cur.execute(q)
                except Exception as err:
                    print(key ,err)
    


def run_migrations_down():
    last = _last_migration() or 1
    migrations = load_submodules(app.migrations)
    rollbacks = _get_rollback(last)
    for rollback in rollbacks:
        module_key = rollback[0]
        migration = migrations[module_key]
        with sqlite3.connect("database.db") as con:
            try:
                cur = con.cursor()
                query = migration.down()
                if query:
                    if isinstance(query, str):
                        cur.execute(query)
                    else:
                        for q in query:
                            cur.execute(q)
            except Exception as err:
                print(err)
    _rollback(last)