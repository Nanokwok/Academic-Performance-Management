import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv
import statistics
import matplotlib.pyplot as plt
from matplotlib.backends._backend_tk import NavigationToolbar2Tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class AcademicPerformanceManagementApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Academic Performance Management")
        width = self.winfo_screenwidth()
        hight = self.winfo_screenheight()

        self.geometry(f"{width}x{hight}")
        # self.configure(width=self.winfo_width())
        # print(width, hight)

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

        self.import_data()

    def create_student_data_table(self):
        self.data_frame.grid_rowconfigure(0, weight=1)
        self.data_frame.grid_columnconfigure(0, weight=1)

        self.tree = ttk.Treeview(self.data_frame,
                                 columns=["ID", "Test 1", "Test 2", "Test 3", "Test 4", "Test 5", "Test 6", "Test 7",
                                          "Test 8", "Test 9", "Test 10", "Test 11", "Test 12"], show="headings")

        self.tree.heading("ID", text="Student ID", anchor="center")

        for i in range(1, 13):
            self.tree.heading(f"Test {i}", text=f"Test {i}")

        self.tree.grid(row=0, column=0, sticky="nsew")

        self.vsb = ttk.Scrollbar(self.data_frame, orient="vertical", command=self.tree.yview)
        self.vsb.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=self.vsb.set)

        self.hsb = ttk.Scrollbar(self.data_frame, orient="horizontal", command=self.tree.xview)
        self.hsb.grid(row=1, column=0, sticky="ew")
        self.tree.configure(xscrollcommand=self.hsb.set)

    def create_buttons(self):
        # self.import_button = ttk.Button(self.button_frame, text="Import Data", command=self.import_data)
        # self.import_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.create_add_del_buttons()
        self.create_group_buttons()
        self.create_graph_buttons()
        self.create_stats_buttons()

    def create_add_del_buttons(self):
        self.add_del_frame = ttk.LabelFrame(self.button_frame, text="Add/Del student")
        self.add_del_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # self.input_box = ttk.Entry(self.add_del_frame)
        # self.input_box.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.import_button = ttk.Button(self.add_del_frame, text="Import Data", command=self.import_data)
        self.import_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

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

        # self.individual_button = ttk.Button(self.stats_frame, text="Individual",
        # command=self.show_individual_statistics)
        # self.individual_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.selected_button = ttk.Button(self.stats_frame, text="Selected Student",
                                          command=self.show_selected_statistics)
        self.selected_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.allstu_button = ttk.Button(self.stats_frame, text="All Student", command=self.show_all_statistics)
        self.allstu_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.disable_all_students_button()

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
        graph_window = tk.Toplevel(self)
        graph_window.title("Generate Graph")

        graph_type_label = ttk.Label(graph_window, text="Select Graph Type:")
        graph_type_label.grid(row=0, column=0, padx=5, pady=5)

        graph_type_var = tk.StringVar()
        graph_type_combobox = ttk.Combobox(graph_window, textvariable=graph_type_var, state="readonly",
                                           values=["Bar Chart", "Histogram", "Scatterplot"])
        graph_type_combobox.current(0)
        graph_type_combobox.grid(row=0, column=1, padx=5, pady=5)

        def generate_graph():
            selected_graph_type = graph_type_var.get()
            selected_items = self.tree.selection()
            if not selected_items:
                messagebox.showwarning("Warning", "Please select one or more students to generate the graph.")
                return

            scores_dict = {}
            for selected_item in selected_items:
                student_id = self.tree.item(selected_item, "text")
                scores_str = self.tree.item(selected_item, "values")[1:]
                scores = [int(score) for score in scores_str]
                scores_dict[student_id] = scores

            fig, ax = plt.subplots()
            if selected_graph_type == "Bar Chart":
                # Generate Bar Chart
                for student_id, scores in scores_dict.items():
                    ax.bar(range(1, len(scores) + 1), scores, label=student_id)
                ax.set_xlabel("Test")
                ax.set_ylabel("Score")
                ax.set_title("Bar Chart")
                # ax.legend()

                bar_graph_window = tk.Toplevel(self)
                bar_graph_window.title("Bar Graph")

                canvas = FigureCanvasTkAgg(fig, master=bar_graph_window)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

                toolbar = NavigationToolbar2Tk(canvas, bar_graph_window)
                toolbar.update()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            elif selected_graph_type == "Histogram":
                for student_id, scores in scores_dict.items():
                    ax.hist(scores, bins=10, alpha=0.5, label=student_id)
                ax.set_xlabel("Score")
                ax.set_ylabel("Frequency")
                ax.set_title("Histogram")
                # ax.legend()

                histogram_window = tk.Toplevel(self)
                histogram_window.title("Histogram")

                canvas = FigureCanvasTkAgg(fig, master=histogram_window)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

                toolbar = NavigationToolbar2Tk(canvas, histogram_window)
                toolbar.update()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            elif selected_graph_type == "Scatterplot":
                for student_id, scores in scores_dict.items():
                    plt.scatter(range(1, len(scores) + 1), scores, label=student_id)
                plt.xlabel("Test")
                plt.ylabel("Score")
                plt.title("Scatterplot")
                # plt.legend()
                plt.show()

                scatterplot_window = tk.Toplevel(self)
                scatterplot_window.title("Scatterplot")

                canvas = FigureCanvasTkAgg(fig, master=scatterplot_window)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

                toolbar = NavigationToolbar2Tk(canvas, scatterplot_window)
                toolbar.update()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            else:
                messagebox.showerror("Error", "Invalid graph type selected.")

        generate_button = ttk.Button(graph_window, text="Generate Graph", command=generate_graph)
        generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    # def show_individual_statistics(self):
    #     selected_id = self.tree.focus()
    #     if selected_id:
    #         student_id = self.tree.item(selected_id, "text")
    #         scores_str = self.tree.item(selected_id, "values")[1:]
    #
    #         scores = []
    #         for score in scores_str:
    #             if score:
    #                 scores.append(int(score))
    #
    #         maxx = max(scores)
    #         minn = min(scores)
    #         avg = statistics.mean(scores)
    #         stdev = statistics.stdev(scores)
    #
    #         statistics_func = tk.Toplevel(self)
    #         statistics_func.title(f"Statistics for Student ID {student_id}")
    #
    #         tk.Label(statistics_func, text="Statistics:").pack()
    #         tk.Label(statistics_func, text=f"Student ID: {student_id}").pack()
    #         tk.Label(statistics_func, text=f"Max Score: {maxx}").pack()
    #         tk.Label(statistics_func, text=f"Min Score: {minn}").pack()
    #         tk.Label(statistics_func, text=f"Avg Score: {avg}").pack()
    #         tk.Label(statistics_func, text=f"Standard Deviation: {stdev}").pack()
    #     else:
    #         messagebox.showwarning("Warning", "Please select a student to view statistics.")

    def show_selected_statistics(self):
        selected_items = self.tree.selection()
        if selected_items:
            statistics_window = tk.Toplevel(self)
            statistics_window.title("Statistics for Selected Students")

            statistics_tree = ttk.Treeview(statistics_window,
                                           columns=["Max Score", "Min Score", "Avg Score", "Median Score",
                                                    "Stdev Score"])
            statistics_tree.heading("#0", text="Student ID")
            statistics_tree.heading("#1", text="Max Score")
            statistics_tree.heading("#2", text="Min Score")
            statistics_tree.heading("#3", text="Avg Score")
            statistics_tree.heading("#4", text="Median Score")
            statistics_tree.heading("#5", text="Stdev Score")

            for selected_item in selected_items:
                student_id = self.tree.item(selected_item, "text")
                scores_str = self.tree.item(selected_item, "values")[1:]
                scores = [int(score) for score in scores_str]

                max_score = max(scores)
                min_score = min(scores)
                avg_score = statistics.mean(scores)
                median_score = statistics.median(scores)
                stdev_score = statistics.stdev(scores)

                statistics_tree.insert("", "end", text=student_id,
                                       values=(max_score, min_score, avg_score, median_score, stdev_score))

            statistics_tree.pack(expand=True, fill="both")
        else:
            messagebox.showwarning("Warning", "Please select one or more students to view statistics.")

    def show_all_statistics(self):
        if not self.tree.get_children():
            messagebox.showwarning("Warning", "No data available. Please import data first.")
            return

        statistics_window = tk.Toplevel(self)
        statistics_window.title("Statistics for All Students")

        statistics_tree = ttk.Treeview(statistics_window,
                                       columns=["Max Score", "Min Score", "Avg Score", "Median Score", "Stdev Score"])
        statistics_tree.heading("#0", text="Student ID")
        statistics_tree.heading("#1", text="Max Score")
        statistics_tree.heading("#2", text="Min Score")
        statistics_tree.heading("#3", text="Avg Score")
        statistics_tree.heading("#4", text="Median Score")
        statistics_tree.heading("#5", text="Stdev Score")

        for child in self.tree.get_children():
            student_id = self.tree.item(child, "text")
            scores_str = self.tree.item(child, "values")[1:]
            scores = [int(score) for score in scores_str]

            max_score = max(scores)
            min_score = min(scores)
            avg_score = statistics.mean(scores)
            median_score = statistics.median(scores)
            stdev_score = statistics.stdev(scores)

            statistics_tree.insert("", "end", text=student_id,
                                   values=(max_score, min_score, avg_score, median_score, stdev_score))

        statistics_tree.pack(expand=True, fill="both")

    def enable_all_students_button(self):
        self.allstu_button["state"] = "normal"

    def disable_all_students_button(self):
        self.allstu_button["state"] = "disabled"

    def import_data(self):
        file_path = "student_marks.csv"
        if file_path:
            for child in self.tree.get_children():
                self.tree.delete(child)
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                header = next(reader)
                for row in reader:
                    student_id = row[0]
                    scores = row[1:]
                    self.tree.insert("", "end", text=student_id, values=scores)

            self.tree.column("#0", width=100, anchor="center")

            self.enable_all_students_button()

    def resize(self, event):
        self.button_frame.grid_configure(sticky="nsew")
        self.data_frame.grid_configure(sticky="nsew")
        # self.canvas.config(width=self.data_frame.winfo_width(), height=self.data_frame.winfo_height())
        # self.canvas.config(scrollregion=self.canvas.bbox("all"))
        # self.vsb.config(command=self.canvas.yview)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

    def resize_canvas(self, event):
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

