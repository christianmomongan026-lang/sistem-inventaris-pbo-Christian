"""
Tugas Praktikum Mandiri - Minggu Ke-5
Pemrograman Berorientasi Objek
Property Visibility & Enkapsulasi (Python 3.12)

Sistem Inventaris & Payroll sederhana yang menerapkan:
- Enkapsulasi (private attribute pakai __)
- @property untuk getter/setter dengan validasi
- isinstance() untuk memvalidasi objek sebelum masuk ke list
- Private method yang hanya bisa dipanggil dari dalam class
"""


class Product:
    """__price bersifat private, hanya bisa diubah lewat setter @property
    yang menolak nilai negatif."""

    def __init__(self, name: str, price: float, stock: int = 0):
        self.name = name
        self.__price = 0
        self.price = price  
        self.stock = stock

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Harga produk tidak boleh negatif!")
        self.__price = value

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.__price}, stock={self.stock})"


class Employee:
    """__salary bersifat private, divalidasi lewat setter @property."""

    def __init__(self, name: str, salary: float):
        self.name = name
        self.__salary = 0
        self.salary = salary  

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Gaji tidak boleh negatif!")
        self.__salary = value

    def __repr__(self):
        return f"Employee(name={self.name!r}, salary={self.__salary})"


class Account:
    """__balance bersifat private. purchase_product() memvalidasi
    kecukupan saldo & stok SEBELUM memodifikasi data apa pun."""

    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.__balance = 0
        self.balance = balance  

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Saldo tidak boleh negatif!")
        self.__balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Jumlah deposit harus positif!")
        self.balance = self.__balance + amount
        return f"Deposit berhasil. Saldo sekarang: {self.__balance}"

    def purchase_product(self, product: Product, quantity: int = 1):
        if not isinstance(product, Product):
            raise TypeError("Objek yang dibeli harus instance dari Product!")
        if quantity <= 0:
            raise ValueError("Jumlah pembelian harus lebih dari 0!")
        if quantity > product.stock:
            raise ValueError(f"Stok {product.name} tidak cukup! Sisa stok: {product.stock}")

        total_harga = product.price * quantity
        if total_harga > self.__balance:
            raise ValueError("Saldo tidak cukup untuk melakukan pembelian!")

        self.balance = self.__balance - total_harga
        product.stock -= quantity
        return (f"Pembelian berhasil: {quantity}x {product.name} "
                f"seharga {total_harga}. Sisa saldo: {self.__balance}")

    def __repr__(self):
        return f"Account(owner={self.owner!r}, balance={self.__balance})"


class Company:
    """FITUR WAJIB TUGAS:
    1. Enkapsulasi array data karyawan: self.__employees = []
    2. Private method __calculate_payroll() - hanya bisa dipanggil
       dari dalam class ini (name mangling).
    3. isinstance() untuk validasi objek sebelum masuk ke list.
    """

    def __init__(self, name: str):
        self.name = name
        self.__employees = []  

    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError(
                f"Objek yang ditambahkan harus instance dari Employee, "
                f"bukan {type(employee).__name__}!"
            )
        self.__employees.append(employee)
        return f"{employee.name} berhasil ditambahkan ke {self.name}."

    def __calculate_payroll(self):
        """Private method: hanya bisa dipanggil dari dalam class ini."""
        return sum(emp.salary for emp in self.__employees)

    def process_payroll(self):
        """Method publik (pintu resmi) yang memanggil method private."""
        total = self.__calculate_payroll()
        print(f"=== Laporan Payroll: {self.name} ===")
        for emp in self.__employees:
            print(f"  - {emp.name}: {emp.salary}")
        print(f"Total payroll: {total}")
        return total

    def list_employees(self):
        return [emp.name for emp in self.__employees]

    def __repr__(self):
        return f"Company(name={self.name!r}, jumlah_karyawan={len(self.__employees)})"


def main():
    print("\n--- 1. Demo Company: Encapsulation + Private Method ---")
    company = Company("PT Maju Jaya")

    e1 = Employee("Christian", 5_000_000)
    e2 = Employee("Jeremy", 4_500_000)
    e3 = Employee("Miracle", 4_800_000)

    print(company.add_employee(e1))
    print(company.add_employee(e2))
    print(company.add_employee(e3))
    print("Daftar karyawan:", company.list_employees())

    company.process_payroll()

    print("\n--- 2. Uji isinstance(): menolak object yang salah tipe ---")
    try:
        company.add_employee("Bukan objek Employee")
    except TypeError as e:
        print(f"Gagal (sesuai harapan): {e}")

    print("\n--- 3. Uji akses langsung ke private method dari luar class ---")
    try:
        company.__calculate_payroll()  
    except AttributeError as e:
        print(f"Gagal (sesuai harapan): {e}")

    print("\n--- 4. Demo Product & Account: @property + validasi saldo ---")
    laptop = Product("Laptop", price=7_000_000, stock=3)
    account = Account("jj", balance=10_000_000)
    print(account)
    print(laptop)

    print(account.purchase_product(laptop, quantity=1))
    print("Sisa stok laptop:", laptop.stock)

    print("\n--- 5. Uji validasi saldo/stok tidak cukup ---")
    try:
        account.purchase_product(laptop, quantity=5)
    except ValueError as e:
        print(f"Gagal (sesuai harapan): {e}")

    print("\n--- 6. Uji harga produk tidak boleh negatif ---")
    try:
        laptop.price = -1000
    except ValueError as e:
        print(f"Gagal (sesuai harapan): {e}")


if __name__ == "__main__":
    main()
