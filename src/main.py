import typer
from rich.console import Console

from src.cli.repl import REPL
from src.repositories.todo_repository import InMemoryTodoRepository
from src.services.todo_service import TodoService

app = typer.Typer()
console = Console()


def start_interactive():
    """
    Start the interactive Todo REPL session.
    """
    repo = InMemoryTodoRepository()
    service = TodoService(repo)
    repl = REPL(service, console)
    repl.run()


@app.command()
def interactive():
    """
    Start the interactive Todo REPL session explicitly.
    """
    start_interactive()


@app.callback(invoke_without_command=True)
def main(ctx: typer.Context):
    """
    Phase I In-Memory Todo CLI.
    """
    if ctx.invoked_subcommand is None:
        start_interactive()


if __name__ == "__main__":
    app()