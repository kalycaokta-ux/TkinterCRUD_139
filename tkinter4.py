import sqlite3
import tkinter as tk
from tkinter import messagebox, ttk

DB_NAME = "school.db"


def run_query(sql, params=()):
  conn = sqlite3.connect(DB_NAME)
  try:
    with conn:
      return conn.execute(sql, params).fetchall()
  finally:
    conn.close()


def init_db():
  run_query("""CREATE TABLE IF NOT EXISTS nilai_siswa (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          nama_siswa TEXT NOT NULL,
          biologi INTEGER,
          fisika INTEGER,
          inggris INTEGER,
          prediksi_fakultas TEXT
      )""")
  
  
  def add_student(nama, biologi, fisika, inggris, prediksi):