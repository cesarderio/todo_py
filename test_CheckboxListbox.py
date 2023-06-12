import unittest
from frontend import CheckboxListbox

class CheckboxListboxTests(unittest.TestCase):
    def setUp(self):
        self.checkbox_listbox = CheckboxListbox(None)

    def test_add_task(self):
        self.checkbox_listbox.add_task("Task 1")
        self.assertEqual(len(self.checkbox_listbox.tasks), 1)
        self.assertEqual(len(self.checkbox_listbox.checkboxes), 1)

    def test_delete_valid_task(self):
        self.checkbox_listbox.add_task("Task 1")
        self.checkbox_listbox.delete(0)
        self.assertEqual(len(self.checkbox_listbox.tasks), 0)
        self.assertEqual(len(self.checkbox_listbox.checkboxes), 0)

    def test_delete_invalid_task(self):
        self.checkbox_listbox.add_task("Task 1")
        self.checkbox_listbox.delete(1)
        self.assertEqual(len(self.checkbox_listbox.tasks), 1)
        self.assertEqual(len(self.checkbox_listbox.checkboxes), 1)

    def test_get_checked_indices(self):
        self.checkbox_listbox.add_task("Task 1")
        self.checkbox_listbox.add_task("Task 2")
        self.checkbox_listbox.add_task("Task 3")
        self.checkbox_listbox.checkboxes[0][1].set(True)
        self.checkbox_listbox.checkboxes[2][1].set(True)
        checked_indices = self.checkbox_listbox.get_checked_indices()
        self.assertEqual(checked_indices, [0, 2])

    def test_get_task(self):
        self.checkbox_listbox.add_task("Task 1")
        self.assertEqual(self.checkbox_listbox.get_task(0), "Task 1")

if __name__ == '__main__':
    unittest.main()
