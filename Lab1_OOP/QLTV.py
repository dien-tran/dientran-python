from abc import ABC, abstractmethod

# ======= Lớp cha (Book) =======
class Book(ABC):
    def __init__(self, title, author, price, quantity):
        self.__title = title
        self.__author = author
        self.__price = price
        self.__quantity = quantity

    # Getter & Setter
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        self.__price = new_price

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, new_quantity):
        self.__quantity = new_quantity

    def total_value(self):
        return self.__price * self.__quantity

    @abstractmethod
    def display_info(self):
        pass


# ======= Lớp con (TextBook) =======
class TextBook(Book):
    def __init__(self, title, author, price, quantity, subject):
        super().__init__(title, author, price, quantity)
        self.__subject = subject

    def display_info(self):
        return f"[TextBook] {self.get_title()} - {self.get_author()} | Subject: {self.__subject} | Giá: {self.get_price()} | SL: {self.get_quantity()}"


# ======= Lớp con (Novel) =======
class Novel(Book):
    def __init__(self, title, author, price, quantity, genre):
        super().__init__(title, author, price, quantity)
        self.__genre = genre

    def display_info(self):
        return f"[Novel] {self.get_title()} - {self.get_author()} | Thể loại: {self.__genre} | Giá: {self.get_price()} | SL: {self.get_quantity()}"


# ======= Lớp quản lý BookStore =======
class BookStore:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def list_books(self):
        if not self.books:
            print("Chưa có sách nào trong cửa hàng!")
        else:
            for i, book in enumerate(self.books, start=1):
                print(f"{i}. {book.display_info()}")

    def total_inventory_value(self):
        return sum(book.total_value() for book in self.books)

    def statistic_by_type(self):
        stats = {}
        for book in self.books:
            key = type(book).__name__
            stats[key] = stats.get(key, 0) + book.get_quantity()
        return stats

    def find_book(self, title):
        results = [book for book in self.books if title.lower() in book.get_title().lower()]
        return results

    def remove_book(self, title):
        before = len(self.books)
        self.books = [book for book in self.books if title.lower() not in book.get_title().lower()]
        return before - len(self.books)  # số lượng sách đã xóa


# ======= Menu CLI =======
def menu():
    store = BookStore()

    while True:
        print("\n===== MENU QUẢN LÝ BÁN SÁCH =====")
        print("1. Thêm sách giáo trình (TextBook)")
        print("2. Thêm tiểu thuyết (Novel)")
        print("3. Xem danh sách sách")
        print("4. Tính tổng giá trị tồn kho")
        print("5. Thống kê số lượng theo loại sách")
        print("6. Tìm sách theo tên")
        print("7. Xóa sách theo tên")
        print("0. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == "1":
            title = input("Nhập tên sách: ")
            author = input("Nhập tác giả: ")
            price = int(input("Nhập giá: "))
            quantity = int(input("Nhập số lượng: "))
            subject = input("Nhập môn học: ")
            store.add_book(TextBook(title, author, price, quantity, subject))
            print("Đã thêm sách giáo trình!")

        elif choice == "2":
            title = input("Nhập tên sách: ")
            author = input("Nhập tác giả: ")
            price = int(input("Nhập giá: "))
            quantity = int(input("Nhập số lượng: "))
            genre = input("Nhập thể loại: ")
            store.add_book(Novel(title, author, price, quantity, genre))
            print("Đã thêm tiểu thuyết!")

        elif choice == "3":
            print("\n===== DANH SÁCH SÁCH =====")
            store.list_books()

        elif choice == "4":
            print(f"Tổng giá trị tồn kho: {store.total_inventory_value()} VND")

        elif choice == "5":
            stats = store.statistic_by_type()
            print("\n===== THỐNG KÊ THEO LOẠI =====")
            for k, v in stats.items():
                print(f"{k}: {v} quyển")

        elif choice == "6":
            keyword = input("Nhập tên (hoặc từ khóa) cần tìm: ")
            results = store.find_book(keyword)
            if results:
                print("\n===== KẾT QUẢ TÌM KIẾM =====")
                for book in results:
                    print(book.display_info())
            else:
                print("Không tìm thấy sách nào!")

        elif choice == "7":
            keyword = input("Nhập tên (hoặc từ khóa) sách cần xóa: ")
            removed = store.remove_book(keyword)
            if removed > 0:
                print(f"Đã xóa {removed} sách có chứa từ khóa '{keyword}'")
            else:
                print("Không tìm thấy sách để xóa!")

        elif choice == "0":
            print("Thoát chương trình. Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ, vui lòng thử lại!")


# ======= Chạy chương trình =======
if __name__ == "__main__":
    menu()
