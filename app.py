""" import importable modules """
from model import Model
from view import View


class AcademicPerformanceManagementApp:
    def __init__(self):
        """ Initialize the application."""
        self.model = Model("student_marks.csv")
        self.view = View(self.model.get_function_import_new_data())

        self.import_data()

    def get_allstu_button(self):
        return self.view.get_allstu_button()

    def get_tree(self):
        return self.view.get_tree()

    def get_messagebox(self):
        return self.view.get_messagebox()

    def get_function_import_data(self):
        return self.model.get_function_import_data()

    def get_function_delete_student(self):
        return self.model.get_function_delete_students()

    def import_data(self):
        self.model.import_data(
            tree=self.get_tree(),
            messagebox=self.get_messagebox()
        )
        self.enable_all_students_button()

    def enable_all_students_button(self):
        self.view.enable_all_students_button()

    def get_function_import_new_data(self):
        return self.model.get_function_import_new_data()

