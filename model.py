import csv


class Model:
    def __init__(self, file_path):
        self.file_path = file_path

    def import_data(self, tree, messagebox):
        """ Import data from a CSV file."""
        if self.file_path:
            for child in tree.get_children():
                tree.delete(child)
            with open(self.file_path, "r") as file:
                reader = csv.reader(file)
                headers = next(reader, None)

                if headers is None:
                    messagebox.showerror("Error", "The CSV file is empty.")
                    return

                tree["columns"] = ["ID"] + headers[1:]
                tree.heading("#0", text="ID")
                for col_index, col in enumerate(tree["columns"], start=1):
                    tree.heading(col, text=headers[col_index - 1])

                for row in reader:
                    student_id = row[0]
                    scores = row[1:]
                    tree.insert("", "end", text=student_id, values=[student_id] + scores)

            tree.column("#0", width=100, anchor="center")
            for col in tree["columns"]:
                tree.column(col, width=100, anchor="center")

    def import_new_data(self, tree, allstu_button, messagebox, filedialog):
        """ Import new data from a CSV file."""
        try:
            self.file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            return
        if self.file_path == "":
            return
        self.delete_data(tree)

        if self.file_path:
            with open(self.file_path, "r") as file:
                reader = csv.reader(file)
                headers = next(reader, None)

                if headers is None:
                    messagebox.showerror("Error", "The CSV file is empty.")
                    return

                tree["columns"] = ["ID"] + headers[1:]
                tree.heading("#0", text="ID")
                for col_index, col in enumerate(tree["columns"], start=1):
                    tree.heading(col, text=headers[col_index - 1])

                for row in reader:
                    student_id = row[0]
                    scores = row[1:]
                    tree.insert("", "end", text=student_id, values=[student_id] + scores)

            tree.column("#0", width=100, anchor="center")
            for col in tree["columns"]:
                tree.column(col, width=100, anchor="center")

            # self.enable_all_students_button(allstu_button)

    def delete_data(self, tree):
        """ Delete all data from the Treeview."""
        tree.delete(*tree.get_children())
        # self.disable_all_students_button(allstu_button)

    def get_function_import_data(self):
        return self.import_data

    def get_function_delete_students(self):
        return self.delete_data

    def get_function_import_new_data(self):
        return self.import_new_data

