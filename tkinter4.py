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
input_frame.pack(pady=5)

# Definisi field input yang diminta
fields = ["Nama Siswa", "Nilai Biologi", "Nilai Fisika", "Nilai Inggris"]
entries = {}

for i, field in enumerate(fields):
  lbl = tk.Label(input_frame, text=field + ":", font=("Helvetica", 11), bg="#dcdcdc")
  lbl.grid(row=i, column=0, sticky="w", pady=5, padx=10)

  entry = tk.Entry(input_frame, width=25, font=("Helvetica", 11))
  entry.grid(row=i, column=1, pady=5)
  entries[field] = entry


# --- 3. LOGIKA PREDIKSI & SUBMIT ---
def read_form():