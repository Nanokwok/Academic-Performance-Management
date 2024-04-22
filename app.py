import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
import statistics

class AcademicPerformanceManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Academic Performance Management")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        self.data_frame = ttk.Frame(self)
        self.data_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.create_student_data_table()
        self.create_buttons()

        self.bind("<Configure>", self.resize)

    def create_student_data_table(self):
        self.canvas = tk.Canvas(self.data_frame)
        self.canvas.grid(row=0, column=0, sticky="nsew")

        self.frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor="nw")

        self.tree = ttk.Treeview(self.frame,
                                 columns=["ID", "Test 1", "Test 2", "Test 3", "Test 4", "Test 5", "Test 6", "Test 7",
                                          "Test 8", "Test 9", "Test 10", "Test 11", "Test 12"])

        self.tree.heading("#0", text="Student ID")
        for i in range(1, 13):
            self.tree.heading(f"#{i}", text=f"Test {i}")
        self.tree.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.vsb = ttk.Scrollbar(self.data_frame, orient="vertical", command=self.canvas.yview)
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.canvas.configure(yscrollcommand=self.vsb.set)

        self.hsb = ttk.Scrollbar(self.data_frame, orient="horizontal", command=self.canvas.xview)
        self.hsb.grid(row=1, column=0, sticky="ew")
        self.canvas.configure(xscrollcommand=self.hsb.set)

        self.frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

        self.canvas.bind("<Configure>", self.resize_canvas)

    def create_buttons(self):
        self.import_button = ttk.Button(self.button_frame, text="Import Data", command=self.import_data)
        self.import_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.create_add_del_buttons()
        self.create_group_buttons()
        self.create_graph_buttons()
        self.create_stats_buttons()

    def create_add_del_buttons(self):
        self.add_del_frame = ttk.LabelFrame(self.button_frame, text="Add/Del student")
        self.add_del_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.input_box = ttk.Entry(self.add_del_frame)
        self.input_box.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        # self.add_button = ttk.Button(self.add_del_frame, text="Add Student", command=self.add_student)
        # self.add_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.delete_button = ttk.Button(self.add_del_frame, text="Delete Student", command=self.delete_student)
        self.delete_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    def create_group_buttons(self):
        self.group_frame = ttk.LabelFrame(self.button_frame, text="Grouping student")
        self.group_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.group_input_box = ttk.Entry(self.group_frame)
        self.group_input_box.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.similar_button = ttk.Button(self.group_frame, text="Similar score together", command=self.group_students)
        self.similar_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.every_group_button = ttk.Button(self.group_frame, text="Every group same performance",
                                             command=self.group_students)
        self.every_group_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    def create_graph_buttons(self):
        self.graph_frame = ttk.LabelFrame(self.button_frame, text="Generate Graphs")
        self.graph_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        self.one_student_button = ttk.Button(self.graph_frame, text="1 student", command=self.generate_graphs)
        self.one_student_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.two_or_more_button = ttk.Button(self.graph_frame, text="2 or more students", command=self.generate_graphs)
        self.two_or_more_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.all_students_button = ttk.Button(self.graph_frame, text="All students", command=self.generate_graphs)
        self.all_students_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    def create_stats_buttons(self):
        self.stats_frame = ttk.LabelFrame(self.button_frame, text="Show Statistics")
        self.stats_frame.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        self.individual_button = ttk.Button(self.stats_frame, text="Individual", command=self.show_individual_statistics)
        self.individual_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.multiple_button = ttk.Button(self.stats_frame, text="Multiple", command=self.show_multiple_statistics)
        self.multiple_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

    def add_student(self):
        pass

    def delete_student(self):
        selected_item = self.tree.focus()
        if selected_item:
            self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Warning", "Please select a student to delete.")

    def group_students(self):
        pass

    def generate_graphs(self):
        pass

    def show_individual_statistics(self):
        selected_id = self.tree.focus()
        if selected_id:
            student_id = self.tree.item(selected_id, "text")
            scores_str = self.tree.item(selected_id, "values")[1:]

            scores = []
            for score in scores_str:
                if score:
                    scores.append(int(score))

            maxx = max(scores)
            minn = min(scores)
            avg = statistics.mean(scores)
            stdev = statistics.stdev(scores)

            statistics_func = tk.Toplevel(self)
            statistics_func.title(f"Statistics for Student ID {student_id}")

            tk.Label(statistics_func, text="Statistics:").pack()
            tk.Label(statistics_func, text=f"Student ID: {student_id}").pack()
            tk.Label(statistics_func, text=f"Max Score: {maxx}").pack()
            tk.Label(statistics_func, text=f"Min Score: {minn}").pack()
            tk.Label(statistics_func, text=f"Avg Score: {avg}").pack()
            tk.Label(statistics_func, text=f"Standard Deviation: {stdev}").pack()
        else:
            messagebox.showwarning("Warning", "Please select a student to view statistics.")

    def show_multiple_statistics(self):
        pass

    def import_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv"), ("All files", "*.*")])
        if file_path:
            for child in self.tree.get_children():
                self.tree.delete(child)
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    self.tree.insert("", "end", text=row[0], values=row[1:])

    def resize(self, event):
        self.button_frame.grid_configure(sticky="nsew")
        self.data_frame.grid_configure(sticky="nsew")
        self.canvas.config(width=self.data_frame.winfo_width(), height=self.data_frame.winfo_height())
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
        self.vsb.config(command=self.canvas.yview)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

    def resize_canvas(self, event):
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
