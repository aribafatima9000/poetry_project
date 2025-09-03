class Library:
    def __init__(self):
        self.books = {}
        self.issued_books = {}

    def add_book(self, book_id, title):
        self.books[book_id] = title
        print(f"Book '{title}' added successfully.")

    def remove_book(self, book_id):
        if book_id in self.books:
            removed = self.books.pop(book_id)
            print(f"Book '{removed}' removed successfully.")
        else:
            print("Book not found!")

    def issue_book(self, book_id, student):
        if book_id in self.books:
            self.issued_books[book_id] = student
            print(f"Book '{self.books[book_id]}' issued to {student}.")
            del self.books[book_id]
        else:
            print("Book not available!")

    def return_book(self, book_id):
        if book_id in self.issued_books:
            student = self.issued_books.pop(book_id)
            print(f"Book ID {book_id} returned by {student}.")
        else:
            print("No record found!")

# ----------- Test Code -----------
lib = Library()
lib.add_book(1, "Python Basics")
lib.add_book(2, "Data Science with Python")
lib.issue_book(1, "Ali")
lib.return_book(1)
lib.remove_book(2)






class Hospital:
    def __init__(self):
        self.patients = {}
        self.appointments = {}

    def register_patient(self, patient_id, name, age):
        self.patients[patient_id] = {"Name": name, "Age": age}
        print(f"Patient {name} registered successfully.")

    def book_appointment(self, patient_id, doctor, date):
        if patient_id in self.patients:
            self.appointments[patient_id] = {"Doctor": doctor, "Date": date}
            print(f"Appointment booked for {self.patients[patient_id]['Name']} with Dr.{doctor} on {date}.")
        else:
            print("Patient not found!")

    def view_records(self, patient_id):
        if patient_id in self.patients:
            print("Patient Record:", self.patients[patient_id])
            if patient_id in self.appointments:
                print("Appointment:", self.appointments[patient_id])
        else:
            print("Patient not found!")

# ----------- Test Code -----------
hosp = Hospital()
hosp.register_patient(101, "Fatima", 25)
hosp.book_appointment(101, "Dr. Khan", "2025-09-05")
hosp.view_records(101)
