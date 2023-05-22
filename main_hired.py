import streamlit as st
import sqlite3

# Membuat koneksi ke database
conn = sqlite3.connect('payroll.db')

# Membuat kursor
cursor = conn.cursor()

# Membuat tabel jika belum ada
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        position TEXT NOT NULL,
        salary INTEGER NOT NULL
    )
''')

# Fungsi untuk menambahkan data pegawai
def add_employee(name, position, salary):
    cursor.execute("INSERT INTO employees (name, position, salary) VALUES (?, ?, ?)", (name, position, salary))
    conn.commit()

# Fungsi untuk mengambil data pegawai
def get_employees():
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    return rows

# Fungsi untuk menghitung total gaji
def calculate_total_salary():
    cursor.execute("SELECT SUM(salary) FROM employees")
    total_salary = cursor.fetchone()[0]
    return total_salary

# Tampilan aplikasi dengan Streamlit
def main():
    st.title("Aplikasi Penggajian")

    # Menambahkan data pegawai
    st.header("Tambah Pegawai")
    emp_name = st.text_input("Nama Pegawai")
    emp_position = st.text_input("Posisi Pegawai")
    emp_salary = st.number_input("Gaji Pegawai", min_value=0)
    if st.button("Tambah"):
        add_employee(emp_name, emp_position, emp_salary)
        st.success("Pegawai ditambahkan!")

    # Menampilkan data pegawai
    st.header("Data Pegawai")
    employees = get_employees()
    for emp in employees:
        st.write(f"Nama: {emp[1]}")
        st.write(f"Posisi: {emp[2]}")
        st.write(f"Gaji: {emp[3]}")
        st.write("---")

    # Menampilkan total gaji
    total_salary = calculate_total_salary()
    st.header("Total Gaji")
    st.write(f"Total: {total_salary}")

if __name__ == "__main__":
    main()

# Menutup koneksi
conn.close()
