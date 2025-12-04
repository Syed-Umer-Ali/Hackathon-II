from src.models.task import Task
from src.repositories.todo_repository import InMemoryTodoRepository


def test_repository_add():
    repo = InMemoryTodoRepository()
    task = Task(title="Test Task")
    saved_task = repo.add(task)

    assert saved_task.id == task.id
    assert len(repo.list()) == 1
    assert repo.list()[0].title == "Test Task"


def test_repository_list():
    repo = InMemoryTodoRepository()
    repo.add(Task(title="Task 1"))
    repo.add(Task(title="Task 2"))

    tasks = repo.list()
    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"


def test_repository_update():
    repo = InMemoryTodoRepository()
    task = repo.add(Task(title="Original Title"))

    task.title = "Updated Title"
    updated_task = repo.update(task)

    assert updated_task.title == "Updated Title"
    assert repo.get_by_id(task.id).title == "Updated Title"


def test_repository_delete():
    repo = InMemoryTodoRepository()
    task = repo.add(Task(title="Task to Delete"))

    assert len(repo.list()) == 1
    assert repo.delete(task.id) is True
    assert len(repo.list()) == 0
    assert repo.delete(task.id) is False  # Already deleted
