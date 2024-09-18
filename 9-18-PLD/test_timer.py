#!/usr/bin/python3
import time
from contextlib import contextmanager
import unittest

@contextmanager
def timer(name):
    start_time = time.time()
    yield
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"{name} took {elapsed_time:.4f} seconds")

class TestTimer(unittest.TestCase):

    def test_short_operation(self):
        with timer("Short Operation"):
            time.sleep(0.1)  # Sleep for 100 milliseconds
        self.assertLessEqual(time.time() - time.perf_counter(), 0.15, "Short operation took too long")

    def test_medium_operation(self):
        with timer("Medium Operation"):
            time.sleep(1)  # Sleep for 1 second
        self.assertLessEqual(time.time() - time.perf_counter(), 1.05, "Medium operation took too long")

    def test_long_operation(self):
        with timer("Long Operation"):
            time.sleep(5)  # Sleep for 5 seconds
        self.assertLessEqual(time.time() - time.perf_counter(), 5.05, "Long operation took too long")

    def test_multiple_operations(self):
        total_time = 0
        with timer("Multiple Operations"):
            time.sleep(1)  # First operation
            total_time += 1
            time.sleep(2)  # Second operation
            total_time += 2
            time.sleep(3)  # Third operation
            total_time += 3
        self.assertAlmostEqual(total_time, 6, places=2, msg="Total time calculation incorrect")

    def test_nested_timers(self):
        with timer("Outer Timer"):
            with timer("Inner Timer"):
                time.sleep(0.5)  # Sleep for 500 milliseconds
            time.sleep(0.5)  # Additional wait outside inner timer
        self.assertGreaterEqual(time.time() - time.perf_counter(), 1.5, "Nested timers didn't add up correctly")

if __name__ == '__main__':
    unittest.main()
