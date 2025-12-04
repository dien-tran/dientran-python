# ============================================
# CHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN - OOP PYTHON
# Có: Trừu tượng, Kế thừa, Đa hình, Đóng gói
# CRUD: Thêm – Sửa – Xóa – Tìm kiếm
# Menu chạy trong 1 cell duy nhất
# ============================================

from abc import ABC, abstractmethod   # Dùng để tạo lớp trừu tượng

# -----------------------------
# LỚP TRỪU TƯỢNG PERSON
# -----------------------------
class Person(ABC):  # ABC = Abstract Base Class
    def __init__(self, student_id, name, age):
        self.student_id = student_id  # Thuộc tính chung
        self.name = name
        self.age = age

    @abstractmethod
    def show_info(self):
        """Phương thức trừu tượng → subclass phải override"""
        pass


# -----------------------------
# LỚP STUDENT KẾ THỪA PERSON
# -----------------------------
class Student(Person):
    def __init__(self, student_id, name, age, gpa):
        super().__init__(student_id, name, age)  # Gọi constructor của Person
        self.gpa = gpa  # Thuộc tính riêng của Student

    # Ghi đè (đa hình) phương thức trừu tượng
    def show_info(self):
        print(f"ID: {self.student_id} | Tên: {self.name} | Tuổi: {self.age} | GPA: {self.gpa}")


# -----------------------------
# LỚP QUẢN LÝ DANH SÁCH SINH VIÊN
# -----------------------------
class StudentManager:
    def __init__(self):
        self.students = []  # Danh sách lưu trữ sinh viên

    # Thêm sinh viên
    def add_student(self):
        print("\n--- Thêm sinh viên ---")
        sid = input("Nhập ID: ")
        name = input("Nhập tên: ")
        age = int(input("Nhập tuổi: "))
        gpa = float(input("Nhập GPA: "))
        self.students.append(Student(sid, name, age, gpa))
        print("Thêm thành công!")

    # Hiển thị toàn bộ sinh viên
    def show_all(self):
        print("\n--- Danh sách sinh viên ---")
        if not self.students:
            print("Danh sách rỗng!")
            return
        for s in self.students:
            s.show_info()

    # Tìm sinh viên theo ID
    def find_by_id(self, sid):
        for s in self.students:
            if s.student_id == sid:
                return s
        return None

    # Sửa sinh viên
    def update_student(self):
        print("\n--- Sửa thông tin sinh viên ---")
        sid = input("Nhập ID cần sửa: ")

        student = self.find_by_id(sid)
        if student is None:
            print("Không tìm thấy sinh viên!")
            return

        student.name = input("Tên mới: ")
        student.age = int(input("Tuổi mới: "))
        student.gpa = float(input("GPA mới: "))
        print("Sửa thành công!")

    # Xóa sinh viên
    def delete_student(self):
        print("\n--- Xóa sinh viên ---")
        sid = input("Nhập ID cần xóa: ")

        student = self.find_by_id(sid)
        if student is None:
            print("Không tìm thấy sinh viên!")
            return

        self.students.remove(student)
        print("Xóa thành công!")

    # Tìm kiếm hiển thị
    def search_student(self):
        print("\n--- Tìm kiếm sinh viên ---")
        sid = input("Nhập ID: ")

        student = self.find_by_id(sid)
        if student:
            student.show_info()
        else:
            print("Không tìm thấy sinh viên!")


# -----------------------------
# MENU CHÍNH
# -----------------------------
def main():
    manager = StudentManager()

    while True:
        print("\n===== MENU QUẢN LÝ SINH VIÊN =====")
        print("1. Thêm sinh viên")
        print("2. Hiển thị danh sách")
        print("3. Sửa thông tin sinh viên")
        print("4. Xóa sinh viên")
        print("5. Tìm sinh viên theo ID")
        print("0. Thoát")
        choice = input("Chọn chức năng: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.show_all()
        elif choice == "3":
            manager.update_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            manager.search_student()
        elif choice == "0":
            print("Thoát chương trình...")
            break
        else:
            print("Lựa chọn không hợp lệ!")


# Chạy chương trình
main()
