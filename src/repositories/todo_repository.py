from typing import List, Optional, Protocol
from uuid import UUID

from src.models.task import Task


class TodoRepository(Protocol):
    def add(self, task: Task) -> Task: ...

    def list(self) -> List[Task]: ...

    def get_by_id(self, task_id: UUID) -> Optional[Task]: ...

    def update(self, task: Task) -> Task: ...

    def delete(self, task_id: UUID) -> bool: ...


class InMemoryTodoRepository:
    def __init__(self):
        self._tasks: List[Task] = []

    def add(self, task: Task) -> Task:
        self._tasks.append(task)
        return task

    def list(self) -> List[Task]:
        return list(self._tasks)

    def get_by_id(self, task_id: UUID) -> Optional[Task]:
        for task in self._tasks:
            if task.id == task_id:
                return task
        return None

    def update(self, task: Task) -> Task:
        # Since it's in-memory and objects are mutable references (mostly),
        # or we replace the object in the list.
        # To be safe and consistent with a DB approach, we find and replace.
        for i, t in enumerate(self._tasks):
            if t.id == task.id:
                self._tasks[i] = task
                return task
        raise ValueError(f"Task with ID {task.id} not found")

    def delete(self, task_id: UUID) -> bool:
        initial_len = len(self._tasks)
        self._tasks = [t for t in self._tasks if t.id != task_id]
        return len(self._tasks) < initial_len
