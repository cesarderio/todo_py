import unittest
import os
from backend import TodoAppBackend

class TodoAppBackendTests(unittest.TestCase):
    def setUp(self):
        self.file_path = 'test_tasks.txt'
        self.backend = TodoAppBackend(self.file_path)

    def tearDown(self):
        # Clean up the test file
        if self.file_path:
            try:
                os.remove(self.file_path)
            except OSError:
                pass

    def test_add_task(self):
        self.backend.add_task("Task 1")
        self.assertEqual(len(self.backend.get_tasks()), 1)

    def test_add_duplicate_task(self):
        self.backend.add_task("Task 1")
        self.backend.add_task("Task 1")
        self.assertEqual(len(self.backend.get_tasks()), 1)

    def test_mark_task_complete_valid_index(self):
        self.backend.add_task("Task 1")
        self.backend.mark_task_complete(1)
        self.assertEqual(len(self.backend.get_tasks()), 0)

    def test_mark_task_complete_invalid_index(self):
        self.backend.add_task("Task 1")
        self.backend.mark_task_complete(2)
        self.assertEqual(len(self.backend.get_tasks()), 1)

    def test_delete_task_valid_index(self):
        self.backend.add_task("Task 1")
        self.backend.delete_task(1)
        self.assertEqual(len(self.backend.get_tasks()), 0)

    def test_delete_task_invalid_index(self):
        self.backend.add_task("Task 1")
        self.backend.delete_task(2)
        self.assertEqual(len(self.backend.get_tasks()), 1)

if __name__ == '__main__':
    unittest.main()
