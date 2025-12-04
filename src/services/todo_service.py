from typing import List, Optional
from uuid import UUID

from src.models.task import Task, TaskStatus
from src.repositories.todo_repository import TodoRepository


class TodoService:
    def __init__(self, repository: TodoRepository):
        self.repository = repository

    def create_task(self, title: str, description: str = "") -> Task:
        task = Task(title=title, description=description)
        return self.repository.add(task)

    def get_all_tasks(self) -> List[Task]:
        return self.repository.list()

    def get_task(self, task_id: UUID) -> Optional[Task]:
        return self.repository.get_by_id(task_id)

    def update_task(
        self,
        task_id: UUID,
        title: Optional[str] = None,
        description: Optional[str] = None,
    ) -> Optional[Task]:
        task = self.repository.get_by_id(task_id)
        if not task:
            return None

        if title is not None:
            task.title = title
        if description is not None:
            task.description = description

        return self.repository.update(task)

    def complete_task(self, task_id: UUID) -> Optional[Task]:
        task = self.repository.get_by_id(task_id)
        if not task:
            return None

        task.status = TaskStatus.COMPLETED
        return self.repository.update(task)

    def delete_task(self, task_id: UUID) -> bool:
        return self.repository.delete(task_id)
