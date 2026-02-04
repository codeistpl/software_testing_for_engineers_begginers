import pytest
from app.model import TaskManager


def test_add_and_toggle(tmp_path):
    p = tmp_path / "tasks.json"
    mgr = TaskManager(str(p))
    t = mgr.add_task("Test")
    assert t.id == 1
    assert not t.done
    mgr.toggle_done(1)
    assert mgr.find(1).done is True


def test_save_load(tmp_path):
    p = tmp_path / "tasks.json"
    mgr = TaskManager(str(p))
    mgr.add_task("A")
    mgr.add_task("B")
    mgr.save()
    mgr2 = TaskManager(str(p))
    tasks = mgr2.get_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "A"
