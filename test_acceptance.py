"""My own acceptance tests. The AI may not modify this file."""

import os
import tempfile

import task_tracker as tt


def test_add_rejects_empty_title():
    tasks = []
    for bad in ["", "   ", "\t\n"]:
        try:
            tt.add_task(tasks, bad)
        except ValueError:
            pass
        else:
            raise AssertionError(f"expected ValueError for title {bad!r}")
    assert tasks == []


def test_load_tasks_corrupted_file_raises_taskerror():
    fd, path = tempfile.mkstemp(suffix=".json")
    os.close(fd)
    with open(path, "w") as f:
        f.write("{not valid json")

    original = tt.DATA_FILE
    tt.DATA_FILE = path
    try:
        try:
            tt.load_tasks()
        except tt.TaskTrackerError:
            pass
        else:
            raise AssertionError("expected TaskTrackerError for corrupted tasks.json")
    finally:
        tt.DATA_FILE = original
        os.remove(path)
