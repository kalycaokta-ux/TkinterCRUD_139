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
  run_query(
      "INSERT INTO nilai_siswa (nama_siswa, biologi, fisika, inggris,"
      " prediksi_fakultas) VALUES (?, ?, ?, ?, ?)",
      (nama, biologi, fisika, inggris, prediksi),
  )


def get_students():
  return run_query(
      "SELECT id, nama_siswa, biologi, fisika, inggris, prediksi_fakultas FROM"
      " nilai_siswa ORDER BY nama_siswa"
  )


init_db()

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("600x650")
root.configure(bg="#f4f6f8")

judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Helvetica", 16, "bold"),
    bg="#F37AF3",
    fg="#333",
)
judul.pack(pady=15)

input_frame = tk.Frame(root, bg="#fffbfe")