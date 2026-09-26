# Tugas Praktikum Mandiri 
**Mata Kuliah:** Pemrograman Berorientasi Objek

## Identitas
- **Nama:** Christian Daniel Zefanya Momongan
- **NIM:** 250211060128
- **Kelas:** E
- **Mata Kuliah:** Pemrograman Berorientasi Objek (PBO)
- **Dosen Pengampu:** Rendy Syahputra, S.Kom., M.Kom
- **Universitas:** Universitas Sam Ratulangi Program Studi Teknik Informatika

## Deskripsi
Sistem Inventaris & Payroll sederhana yang dikembangkan dari materi Live Code Property Visibility, Name Mangling, dan @property. Program ini
menunjukkan penerapan **enkapsulasi** untuk melindungi data dari mutasi ilegal.

## Struktur File
```
sistem_inventaris.py   # semua class + demo dalam satu file
README.md
```

## Fitur Wajib/company
1. **Class `Company`** dengan enkapsulasi array data karyawan:
   `self.__employees = []`
2. **Private method** `__calculate_payroll()` — hanya bisa dipanggil dari
   dalam class itu sendiri (memanfaatkan *name mangling* Python, sama seperti
   contoh `self.__version` di materi).
3. **Validasi `isinstance()`**: method `add_employee()` memvalidasi bahwa
   objek yang dimasukkan adalah instance dari `Employee` sebelum di-*append*
   ke list, sesuai petunjuk teknis tugas.

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

## Fitur Tambahan dari Live Code, Product & Account
- `Product.__price` dan `Employee.__salary` bersifat private, hanya bisa
  diubah lewat setter `@property` yang menolak nilai negatif.
- `Account.__balance` bersifat private. Tidak bisa diset menjadi negatif.
- `Account.purchase_product()` memvalidasi kecukupan saldo **dan** stok
  produk sebelum memodifikasi data apa pun.

## Cara Menjalankan
```bash
python3 sistem_inventaris.py
```

Program akan menjalankan demo lengkap, termasuk kasus-kasus yang **sengaja
gagal** untuk membuktikan validasi bekerja:
- Menambahkan objek yang bukan `Employee` → `TypeError`
- Memanggil `company.__calculate_payroll()` langsung dari luar class →
  `AttributeError` (karena name mangling)
- Membeli produk melebihi stok/saldo → `ValueError`
- Mengubah harga produk menjadi negatif → `ValueError`

## Kesimpulan
Enkapsulasi (`__attribute`, name mangling) mencegah mutasi data ilegal dari
luar class, sementara `@property` memberi antarmuka publik yang tetap
"terlihat publik, berjalan internal" — validasi tetap berjalan otomatis
setiap kali atribut diubah.

## Pengumpulan
Push file ini (`sistem_inventaris.py` + `README.md`) ke repository GitHub
masing-masing.
