from src.repositories.todo_repository import InMemoryTodoRepository
from src.services.todo_service import TodoService


def test_service_create_task():
    repo = InMemoryTodoRepository()
    service = TodoService(repo)

    task = service.create_task(title="Service Task", description="Service Desc")

    assert task.title == "Service Task"
    assert task.description == "Service Desc"
    assert len(repo.list()) == 1


def test_service_complete_task():
    repo = InMemoryTodoRepository()
    service = TodoService(repo)
    task = service.create_task(title="Task to Complete")

    completed_task = service.complete_task(task.id)

    assert completed_task.status == "Completed"
    assert repo.get_by_id(task.id).status == "Completed"
