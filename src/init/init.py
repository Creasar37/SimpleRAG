from fastapi import FastAPI
import os
import sqlite3

app = FastAPI()

if not os.path.exists("database"):
    os.mkdir("database")

conn = sqlite3.connect("database/sqlite.db")