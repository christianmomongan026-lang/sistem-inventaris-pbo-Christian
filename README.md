# Tugas Praktikum Mandiri
**Mata Kuliah:** Pemrograman Berorientasi Objek

## Identitas
- **Nama:** Christian Daniel Zefanya Momongan
- **NIM:** 250211060128
- **Kelas:** E
- **Mata Kuliah:** Pemrograman Berorientasi Objek (PBO)
- **Dosen Pengampu:** Rendy Syahputra, S.Kom., M.Kom
- **Universitas:** Universitas Sam Ratulangi, Program Studi Teknik Informatika

## Deskripsi
Program ini adalah Sistem Inventaris & Payroll sederhana yang saya buat berdasarkan materi Live Code hari itu tentang Property Visibility, Name Mangling, dan @property. Fokus utamanya adalah menerapkan enkapsulasi supaya data penting di dalam program (seperti saldo, harga, dan gaji karyawan) tidak bisa diubah sembarangan dari luar class.

## Struktur File
```
sistem_inventaris.py
semua class dan demo dalam satu file
README.md
```

## Fitur Wajib (Class Company)
1. **Class `Company`** dengan enkapsulasi array data karyawan lewat `self.__employees = []`.
2. **Private method** `__calculate_payroll()`. Method ini hanya bisa dipanggil dari dalam class itu sendiri, memanfaatkan name mangling Python, sama seperti contoh `self.__version` di materi.
3. **Validasi `isinstance()`** pada method `add_employee()`. Sebelum sebuah objek dimasukkan ke dalam list karyawan, program mengecek dulu apakah objek tersebut benar-benar instance dari class `Employee`.

```python
def add_employee(self, employee):
    if not isinstance(employee, Employee):
        raise TypeError("Objek yang ditambahkan harus instance dari Employee!")
    self.__employees.append(employee)

def __calculate_payroll(self):   # private
    return sum(emp.salary for emp in self.__employees)

def process_payroll(self):       # pintu resmi (public) ke private method
    return self.__calculate_payroll()
```

## Fitur Tambahan (Product & Account)
- `Product.__price` dan `Employee.__salary` dibuat private, dan hanya bisa diubah lewat setter `@property` yang menolak nilai negatif.
- `Account.__balance` juga private, jadi saldo tidak bisa diset menjadi angka minus.
- `Account.purchase_product()` selalu mengecek dulu apakah saldo dan stok cukup sebelum benar-benar mengubah data apa pun.

## Cara Menjalankan
```bash
python3 sistem_inventaris.py
```

Program akan menjalankan demo lengkap, termasuk beberapa percobaan yang memang sengaja dibuat gagal untuk membuktikan validasinya benar-benar bekerja:
- Menambahkan objek yang bukan `Employee` akan menghasilkan `TypeError`.
- Memanggil `company.__calculate_payroll()` langsung dari luar class akan menghasilkan `AttributeError`, karena name mangling.
- Membeli produk melebihi stok atau saldo akan menghasilkan `ValueError`.
- Mengubah harga produk menjadi negatif juga akan menghasilkan `ValueError`.

## Kesimpulan
Enkapsulasi bukan hanya sekadar aturan formal yang harus diikuti, tapi lebih ke cara berpikir untuk menjaga data tetap konsisten dan aman. Dengan menyembunyikan atribut penting di balik double underscore,Python memakai name mangling bukan untuk benar-benar mengunci variabel dari niat jahat, tapi untuk mencegah kesalahan tidak sengaja, seperti typo atau modifikasi langsung dari modul lain yang bisa membuat data jadi tidak valid.

Yang paling disadari lewat contoh saldo dan harga adalah bagaimana satu baris kode yang mengubah nilai secara langsung, tanpa lewat validasi, bisa memicu efek berantai yang merusak keseluruhan sistem, seperti kasus "side-effect cascade" yang dibahas di kelas. Di sinilah `@property` jadi solusi yang elegan, karena tampilannya tetap seperti atribut biasa, tapi di baliknya tetap ada logika validasi yang berjalan otomatis setiap kali nilainya diubah.

Penggunaan `isinstance()` pada `add_employee()` juga adalah untuk memvalidasi tipe data sebelum data itu masuk ke dalam struktur yang lebih besar, supaya sistem tidak menyimpan objek yang salah tanpa disadari. Secara keseluruhan, tugas ini tujannya untuk melihat enkapsulasi bukan hanya sebagai konsep abstrak di slide, tapi sebagai kebiasaan menulis kode yang lebih hati-hati dan dapat diandalkan.

