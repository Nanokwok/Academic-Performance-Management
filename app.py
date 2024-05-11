""" import importable modules """
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

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

        self.data_frame = ttk.Frame(self)
        self.data_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.create_student_data_table()
        self.create_buttons()
        story_telling = ttk.Button(self.button_frame, text="Story Telling", command=self.story_telling_page)
        story_telling.grid(row=5, column=0, padx=10, pady=10, sticky="nsew")

        menu = tk.Menu(self)
        self.config(menu=menu)

        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Exit", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.quit)

        self.bind("<Configure>", self.resize)

        self.import_data()

    def create_student_data_table(self):
        """ Create a Treeview widget to display student data."""
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
        """ Create buttons."""
        self.create_add_del_buttons()
        self.create_group_buttons()
        self.create_graph_buttons()
        self.create_stats_buttons()

    def create_add_del_buttons(self):
        """ Create Add/Del student buttons."""
        self.add_del_frame = ttk.LabelFrame(self.button_frame, text="Add/Del student")
        self.add_del_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.import_button = ttk.Button(self.add_del_frame, text="Import Data", command=self.import_data)
        self.import_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.delete_button = ttk.Button(self.add_del_frame, text="Delete Student", command=self.delete_student)
        self.delete_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    def create_group_buttons(self):
        """ Create Group student buttons."""
        self.group_frame = ttk.LabelFrame(self.button_frame, text="Grouping student")
        self.group_frame.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.group_input_box = ttk.Entry(self.group_frame)
        self.group_input_box.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.similar_button = ttk.Button(self.group_frame, text="Similar score together",
                                         command=self.group_students_sim)
        self.similar_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.every_group_button = ttk.Button(self.group_frame, text="Different score together",
                                             command=self.group_students_dif)
        self.every_group_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    def create_graph_buttons(self):
        """ Create Generate Graph buttons."""
        self.graph_frame = ttk.LabelFrame(self.button_frame, text="Generate Graphs")
        self.graph_frame.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

        self.one_student_button = ttk.Button(self.graph_frame, text="1 student", command=self.one_student_graphs)
        self.one_student_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.two_or_more_button = ttk.Button(self.graph_frame, text="2 or more students",
                                             command=self.more_student_graphs)
        self.two_or_more_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.all_students_button = ttk.Button(self.graph_frame, text="All students", command=self.all_student_graphs)
        self.all_students_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

    def create_stats_buttons(self):
        """ Create Show Statistics buttons."""
        self.stats_frame = ttk.LabelFrame(self.button_frame, text="Show Statistics")
        self.stats_frame.grid(row=4, column=0, padx=10, pady=10, sticky="nsew")

        self.selected_button = ttk.Button(self.stats_frame, text="Selected Student",
                                          command=self.show_selected_statistics)
        self.selected_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.allstu_button = ttk.Button(self.stats_frame, text="All Student", command=self.show_all_statistics)
        self.allstu_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.disable_all_students_button()

    def delete_student(self):
        """ Delete a student from the Treeview."""
        selected_item = self.tree.focus()
        if selected_item:
            self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Warning", "Please select a student to delete.")

    def group_students_sim(self):
        """ Group students with similar scores together."""
        total_students = self.tree.get_children()
        if not total_students:
            messagebox.showwarning("Warning", "No students found in the Treeview.")
            return

        total_group = self.group_input_box.get()
        if not total_group:
            messagebox.showwarning("Warning", "Please enter total group number.")
            return

        if total_group == 0:
            messagebox.showwarning("Warning", "Please enter total group number > 0.")

        num_groups = int(total_group)
        num_students = len(total_students)

        student_scores = []
        for item in total_students:
            student_id = self.tree.item(item, "text")
            scores_str = self.tree.item(item, "values")[1:]

            scores = []
            for score_str in scores_str:
                scores.append(int(score_str))

            mid_score = statistics.median(scores)
            student_scores.append((student_id, mid_score))

        student_scores.sort(key=lambda x: x[1], reverse=True)

        groups = []

        for _ in range(num_groups):
            groups.append([])

        group_size = num_students // num_groups
        remainder = num_students % num_groups

        for i, student in enumerate(student_scores):
            group_index = i // group_size if remainder == 0 else i // (group_size + 1)
            groups[group_index].append(student[0])

        group_window = tk.Toplevel(self)
        group_window.title("Student Groups")

        columns = tuple([f"Group {i + 1}" for i in range(num_groups)])
        tree = ttk.Treeview(group_window, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)

        for i in range(max(len(group) for group in groups)):
            values = [group[i] if i < len(group) else "" for group in groups]
            tree.insert("", "end", values=values)

        tree.pack(expand=True, fill="both")

    def group_students_dif(self):
        """ Group students with different scores together."""
        total_students = self.tree.get_children()
        if not total_students:
            messagebox.showwarning("Warning", "No students found in the Treeview.")
            return

        total_group = self.group_input_box.get()
        if not total_group:
            messagebox.showwarning("Warning", "Please enter total group number.")
            return

        if total_group == 0:
            messagebox.showwarning("Warning", "Please enter total group number > 0.")

        num_groups = int(total_group)
        num_students = len(total_students)

        student_scores = []
        for item in total_students:
            student_id = self.tree.item(item, "text")
            scores_str = self.tree.item(item, "values")[1:]

            scores = []
            for score_str in scores_str:
                scores.append(int(score_str))

            mid_score = statistics.median(scores)
            student_scores.append((student_id, mid_score))

        student_scores.sort(key=lambda x: x[1])

        groups = []

        for _ in range(num_groups):
            groups.append([])

        group_size = num_students // num_groups
        remainder = num_students % num_groups

        for i, student in enumerate(student_scores):
            group_index = i // group_size if remainder == 0 else i // (group_size + 1)
            groups[group_index].append(student[0])

        group_window = tk.Toplevel(self)
        group_window.title("Student Groups")

        columns = tuple([f"Group {i + 1}" for i in range(num_groups)])
        tree = ttk.Treeview(group_window, columns=columns, show="headings")

        for col in columns:
            tree.heading(col, text=col)

        for i in range(max(len(group) for group in groups)):
            values = [group[i] if i < len(group) else "" for group in groups]
            tree.insert("", "end", values=values)

        tree.pack(expand=True, fill="both")

    def one_student_graphs(self):
        """ Generate graphs for one student."""
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Warning", "Please select a student to generate the graph.")
            return
        elif len(selected_item) > 1:
            messagebox.showwarning("Warning", "Please select only one student to generate the graph.")
            return
        else:
            graph_window = tk.Toplevel(self)
            graph_window.title("Generate Graph")

            graph_type_label = ttk.Label(graph_window, text="Select Graph Type:")
            graph_type_label.grid(row=0, column=0, padx=5, pady=5)

            graph_type_var = tk.StringVar()
            graph_type_combobox = ttk.Combobox(graph_window, textvariable=graph_type_var, state="readonly",
                                               values=["Bar Chart", "Histogram"])
            graph_type_combobox.current(0)
            graph_type_combobox.grid(row=0, column=1, padx=5, pady=5)

            def generate_graph():
                selected_graph_type = graph_type_var.get()
                selected_items = self.tree.selection()
                if not selected_items:
                    messagebox.showwarning("Warning", "Please select one or more students to "
                                                      "generate the graph.")
                    return

                scores_dict = {}
                for selected_item in selected_items:
                    student_id = self.tree.item(selected_item, "text")
                    scores_str = self.tree.item(selected_item, "values")[1:]
                    scores = [int(score) for score in scores_str]
                    scores_dict[student_id] = scores

                test_names = self.tree["columns"][1:]

                fig, ax = plt.subplots()
                if selected_graph_type == "Bar Chart":
                    for student_id, scores in scores_dict.items():
                        ax.bar(range(1, len(scores) + 1), scores, label=student_id)

                    ax.set_xticks(range(1, len(test_names) + 1))
                    ax.set_xticklabels(test_names, rotation=45, ha='right')
                    ax.set_xlabel("Test")
                    ax.set_ylabel("Score")
                    ax.set_title("Bar Chart")

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

                    histogram_window = tk.Toplevel(self)
                    histogram_window.title("Histogram")

                    canvas = FigureCanvasTkAgg(fig, master=histogram_window)
                    canvas.draw()
                    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

                    toolbar = NavigationToolbar2Tk(canvas, histogram_window)
                    toolbar.update()
                    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            generate_button = ttk.Button(graph_window, text="Generate Graph", command=generate_graph)
            generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def more_student_graphs(self):
        """ Generate graphs for two or more students."""
        selected_items = self.tree.selection()
        if not selected_items:
            messagebox.showwarning("Warning", "Please select a student to generate the graph.")
            return
        elif len(selected_items) == 1:
            messagebox.showwarning("Warning", "Please select more than one student to generate the graph.")
            return
        else:
            graph_window = tk.Toplevel(self)
            graph_window.title("Generate Graph")

            graph_type_label = ttk.Label(graph_window, text="Select Graph Type:")
            graph_type_label.grid(row=0, column=0, padx=5, pady=5)

            graph_type_var = tk.StringVar()
            graph_type_combobox = ttk.Combobox(graph_window, textvariable=graph_type_var, state="readonly",
                                               values=["Boxplot", "Histogram", "Scatterplot"])
            graph_type_combobox.current(0)
            graph_type_combobox.grid(row=0, column=1, padx=5, pady=5)

            def generate_graph():
                selected_graph_type = graph_type_var.get()

                scores_dict = {}
                for selected_item in selected_items:
                    student_id = self.tree.item(selected_item, "text")
                    scores_str = self.tree.item(selected_item, "values")[1:]
                    scores = [int(score) for score in scores_str]
                    scores_dict[student_id] = scores

                fig, ax = plt.subplots()
                if selected_graph_type == "Boxplot":
                    test_names = self.tree["columns"][1:]
                    all_scores = [[] for _ in range(len(test_names))]

                    for student_scores in scores_dict.values():
                        for i, test_score in enumerate(student_scores):
                            all_scores[i].append(test_score)

                    fig, ax = plt.subplots()
                    ax.boxplot(all_scores)

                    ax.set_xlabel("Test Name")
                    ax.set_ylabel("Test Score")
                    ax.set_title("Boxplot")

                    ax.set_xticklabels(test_names, rotation=45, ha='right')

                    boxplot_window = tk.Toplevel(self)
                    boxplot_window.title("Boxplot")

                    canvas = FigureCanvasTkAgg(fig, master=boxplot_window)
                    canvas.draw()

                    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

                    toolbar = NavigationToolbar2Tk(canvas, boxplot_window)
                    toolbar.update()

                    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

                elif selected_graph_type == "Histogram":
                    scores = []
                    for student_id, student_scores in scores_dict.items():
                        scores.append(statistics.median(student_scores))
                    ax.hist(scores, bins=10, alpha=0.5)
                    ax.set_xlabel("Test Score")
                    ax.set_ylabel("Frequency")
                    ax.set_title("Histogram")

                    histogram_window = tk.Toplevel(self)
                    histogram_window.title("Histogram")

                    canvas = FigureCanvasTkAgg(fig, master=histogram_window)
                    canvas.draw()
                    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

                    toolbar = NavigationToolbar2Tk(canvas, histogram_window)
                    toolbar.update()
                    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

                elif selected_graph_type == "Scatterplot":
                    scatter_window = tk.Toplevel(self)

                    scatter_window.title("Select Students and Tests")
                    student_ids = [self.tree.item(item)["values"][0] for item in selected_items]
                    test_names = self.tree["columns"][1:]

                    test1_label = tk.Label(scatter_window, text="Test 1:")
                    test1_label.pack()
                    test1_combo = ttk.Combobox(scatter_window, values=test_names)
                    test1_combo.pack()

                    test2_label = tk.Label(scatter_window, text="Test 2:")
                    test2_label.pack()
                    test2_combo = ttk.Combobox(scatter_window, values=test_names)
                    test2_combo.pack()

                    def generate_scatter_graph():
                        test1_name = test1_combo.get()
                        test2_name = test2_combo.get()

                        scatter_plot_window = tk.Toplevel(self)
                        scatter_plot_window.title("Scatter Plot")

                        fig, ax = plt.subplots()

                        for student_id in student_ids:
                            student_scores = []
                            for selected_item in selected_items:
                                if self.tree.item(selected_item)["values"][0] == student_id:
                                    student_scores = self.tree.item(selected_item)["values"][1:]
                                    break

                            test1_scores = student_scores[test_names.index(test1_name)]
                            test2_scores = student_scores[test_names.index(test2_name)]

                            ax.scatter(test1_scores, test2_scores, label=f"Student {student_id}")

                        ax.set_xlabel(test1_name)
                        ax.set_ylabel(test2_name)
                        ax.set_title("Scatter Plot")

                        canvas = FigureCanvasTkAgg(fig, master=scatter_plot_window)
                        canvas.draw()
                        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                        toolbar = NavigationToolbar2Tk(canvas, scatter_plot_window)
                        toolbar.update()

                    generate_button = tk.Button(scatter_window, text="Generate Graph", command=generate_scatter_graph)
                    generate_button.pack()
                else:
                    messagebox.showerror("Error", "Invalid graph type selected.")

            generate_button = ttk.Button(graph_window, text="Generate Graph", command=generate_graph)
            generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def all_student_graphs(self):
        """ Generate graphs for all students."""
        selected_items = self.tree.get_children()

        graph_window = tk.Toplevel(self)
        graph_window.title("Generate Graph")

        graph_type_label = ttk.Label(graph_window, text="Select Graph Type:")
        graph_type_label.grid(row=0, column=0, padx=5, pady=5)

        graph_type_var = tk.StringVar()
        graph_type_combobox = ttk.Combobox(graph_window, textvariable=graph_type_var, state="readonly",
                                           values=["Boxplot", "Histogram", "Scatterplot"])
        graph_type_combobox.current(0)
        graph_type_combobox.grid(row=0, column=1, padx=5, pady=5)

        def generate_graph():
            selected_graph_type = graph_type_var.get()

            scores_dict = {}
            for selected_item in selected_items:
                student_id = self.tree.item(selected_item, "text")
                scores_str = self.tree.item(selected_item, "values")[1:]
                scores = [int(score) for score in scores_str]
                scores_dict[student_id] = scores

            fig, ax = plt.subplots()
            if selected_graph_type == "Boxplot":
                test_names = self.tree["columns"][1:]
                all_scores = [[] for _ in range(len(test_names))]

                for student_scores in scores_dict.values():
                    for i, test_score in enumerate(student_scores):
                        all_scores[i].append(test_score)

                fig, ax = plt.subplots()
                ax.boxplot(all_scores)

                ax.set_xlabel("Test Name")
                ax.set_ylabel("Test Score")
                ax.set_title("Boxplot")

                ax.set_xticklabels(test_names, rotation=45, ha='right')

                boxplot_window = tk.Toplevel(self)
                boxplot_window.title("Boxplot")

                canvas = FigureCanvasTkAgg(fig, master=boxplot_window)
                canvas.draw()

                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

                toolbar = NavigationToolbar2Tk(canvas, boxplot_window)
                toolbar.update()

                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            elif selected_graph_type == "Histogram":
                scores = []
                for student_id, student_scores in scores_dict.items():
                    scores.append(statistics.median(student_scores))
                ax.hist(scores, bins=10, alpha=0.5)
                ax.set_xlabel("Test Score")
                ax.set_ylabel("Frequency")
                ax.set_title("Histogram")

                histogram_window = tk.Toplevel(self)
                histogram_window.title("Histogram")

                canvas = FigureCanvasTkAgg(fig, master=histogram_window)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

                toolbar = NavigationToolbar2Tk(canvas, histogram_window)
                toolbar.update()
                canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

            elif selected_graph_type == "Scatterplot":
                scatter_window = tk.Toplevel(self)

                scatter_window.title("Select Students and Tests")
                student_ids = [self.tree.item(item)["values"][0] for item in selected_items]
                test_names = self.tree["columns"][1:]

                test1_label = tk.Label(scatter_window, text="Test 1:")
                test1_label.pack()
                test1_combo = ttk.Combobox(scatter_window, values=test_names)
                test1_combo.pack()

                test2_label = tk.Label(scatter_window, text="Test 2:")
                test2_label.pack()
                test2_combo = ttk.Combobox(scatter_window, values=test_names)
                test2_combo.pack()

                def generate_scatter_graph():
                    test1_name = test1_combo.get()
                    test2_name = test2_combo.get()

                    scatter_plot_window = tk.Toplevel(self)
                    scatter_plot_window.title("Scatter Plot")

                    fig, ax = plt.subplots()

                    for student_id in student_ids:
                        student_scores = []
                        for selected_item in selected_items:
                            if self.tree.item(selected_item)["values"][0] == student_id:
                                student_scores = self.tree.item(selected_item)["values"][1:]
                                break

                        test1_scores = student_scores[test_names.index(test1_name)]
                        test2_scores = student_scores[test_names.index(test2_name)]

                        ax.scatter(test1_scores, test2_scores, label=f"Student {student_id}")

                    ax.set_xlabel(test1_name)
                    ax.set_ylabel(test2_name)
                    ax.set_title("Scatter Plot")

                    canvas = FigureCanvasTkAgg(fig, master=scatter_plot_window)
                    canvas.draw()
                    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
                    toolbar = NavigationToolbar2Tk(canvas, scatter_plot_window)
                    toolbar.update()

                generate_button = tk.Button(scatter_window, text="Generate Graph", command=generate_scatter_graph)
                generate_button.pack()
            else:
                messagebox.showerror("Error", "Invalid graph type selected.")

        generate_button = ttk.Button(graph_window, text="Generate Graph", command=generate_graph)
        generate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def show_selected_statistics(self):
        """ Show statistics for selected students."""
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
        """ Show statistics for all students."""
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
        """ Enable the All Students button."""
        self.allstu_button["state"] = "normal"

    def disable_all_students_button(self):
        """ Disable the All Students button."""
        self.allstu_button["state"] = "disabled"

    def import_data(self):
        """ Import data from a CSV file."""
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

    def story_telling_page(self):
        """ Create a new window for Story Telling page."""
        story_window = tk.Toplevel(self)
        story_window.title("Story Telling")

        story_label = ttk.Label(story_window, text="This is a story telling page.")
        story_label.pack()


    def resize(self, event):
        """ Resize the widgets."""
        self.button_frame.grid_configure(sticky="nsew")
        self.data_frame.grid_configure(sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)

    def resize_canvas(self, event):
        """ Resize the canvas."""
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
