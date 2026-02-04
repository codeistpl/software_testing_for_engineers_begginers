from dataclasses import dataclass, asdict
from typing import List, Optional
import json
from pathlib import Path


@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    priority: int = 3
    due: Optional[str] = None
    done: bool = False


class TaskManager:
    def __init__(self, storage_path: str = "tasks.json"):
        self.storage_path = Path(storage_path)
        self._tasks: List[Task] = []
        self._next_id = 1
        self.load()

    def add_task(
        self,
        title: str,
        description: str = "",
        priority: int = 3,
        due: Optional[str] = None,
    ) -> Task:
        t = Task(self._next_id, title, description, priority, due, False)
        self._tasks.append(t)
        self._next_id += 1
        return t

    def get_tasks(self) -> List[Task]:
        return list(self._tasks)

    def find(self, task_id: int) -> Optional[Task]:
        for t in self._tasks:
            if t.id == task_id:
                return t
        return None

    def toggle_done(self, task_id: int) -> Optional[Task]:
        t = self.find(task_id)
        if t:
            t.done = not t.done
            return t
        return None

    def remove(self, task_id: int) -> bool:
        t = self.find(task_id)
        if t:
            self._tasks.remove(t)
            return True
        return False

    def save(self) -> None:
        data = {"next_id": self._next_id, "tasks": [asdict(t) for t in self._tasks]}
        self.storage_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    def load(self) -> None:
        if not self.storage_path.exists():
            return
        data = json.loads(self.storage_path.read_text(encoding="utf-8"))
        self._next_id = data.get("next_id", 1)
        self._tasks = [Task(**t) for t in data.get("tasks", [])]
