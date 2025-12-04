from src.cli.repl import REPL
from src.repositories.todo_repository import InMemoryTodoRepository
from src.services.todo_service import TodoService


def test_repl_should_exit():
    repo = InMemoryTodoRepository()
    service = TodoService(repo)
    repl = REPL(service)

    assert repl.should_exit("exit") is True
    assert repl.should_exit("quit") is True
    assert repl.should_exit("add task") is False
