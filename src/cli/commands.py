from typing import List, Optional
from uuid import UUID

from rich.console import Console
from rich.prompt import Confirm
from rich.table import Table

from src.services.todo_service import TodoService
from src.models.task import Task


class TodoCommands:
    def __init__(self, service: TodoService, console: Console):
        self.service = service
        self.console = console
        self.last_listed_tasks: List[Task] = []

    def _resolve_id(self, id_str: str) -> Optional[UUID]:
        """
        Resolves an ID string which can be either a UUID or a temporary List Index (1, 2, 3).
        Returns the UUID if found, or None/Raises ValueError.
        """
        # Try as Index first (if list was shown)
        if id_str.isdigit() and self.last_listed_tasks:
            idx = int(id_str) - 1
            if 0 <= idx < len(self.last_listed_tasks):
                return self.last_listed_tasks[idx].id
            
        # Try as UUID
        try:
            return UUID(id_str)
        except ValueError:
            return None

    def delete_task(self, args: List[str]):
        if not args:
            self.console.print("[red]Error: Task # required. Usage: delete <#>[/red]")
            return

        task_id = self._resolve_id(args[0])
        if not task_id:
            self.console.print(f"[red]Error: Invalid Task ID or Index '{args[0]}'. Try running 'list' first.[/red]")
            return

        # Check if task exists before confirming
        task = self.service.get_task(task_id)
        if not task:
            self.console.print(f"[red]Error: Task not found[/red]")
            return

        if Confirm.ask(f"Are you sure you want to delete task '{task.title}'?"):
            if self.service.delete_task(task_id):
                self.console.print("[green]Task deleted[/green]")
                # Refresh list cache implicitly or clear it? 
                # Better to keep it stale but valid until next list, or clear it.
                # Let's refresh it from service to keep indices somewhat valid if we were to re-list,
                # but indices shift on delete. Safest to just let next 'list' fix it.
            else:
                self.console.print("[red]Error: Failed to delete task[/red]")

    def update_task(self, args: List[str]):
        if not args:
            self.console.print(
                '[red]Error: Task # required. Usage: update <#> --title "..."[/red]'
            )
            return

        task_id = self._resolve_id(args[0])
        if not task_id:
            self.console.print(f"[red]Error: Invalid Task ID or Index '{args[0]}'. Try running 'list' first.[/red]")
            return

        title = None
        description = None

        # Simple flag parsing
        i = 1
        while i < len(args):
            if args[i] == "--title" and i + 1 < len(args):
                title = args[i + 1]
                i += 2
            elif args[i] == "--desc" and i + 1 < len(args):
                description = args[i + 1]
                i += 2
            else:
                i += 1

        if title is None and description is None:
            self.console.print(
                "[yellow]Warning: No changes specified. Use --title or --desc.[/yellow]"
            )
            return

        try:
            task = self.service.update_task(task_id, title, description)
            if task:
                self.console.print(
                    f"[green]Task '{task.title}' updated successfully[/green]"
                )
            else:
                self.console.print(
                    f"[red]Error: Task not found[/red]"
                )
        except ValueError as e:
            self.console.print(f"[red]Error: {e}[/red]")

    def complete_task(self, args: List[str]):
        if not args:
            self.console.print(
                "[red]Error: Task # required. Usage: complete <#>[/red]"
            )
            return

        task_id = self._resolve_id(args[0])
        if not task_id:
            self.console.print(f"[red]Error: Invalid Task ID or Index '{args[0]}'. Try running 'list' first.[/red]")
            return

        try:
            task = self.service.complete_task(task_id)
            if task:
                self.console.print(
                    f"[green]Task '{task.title}' marked as Completed[/green]"
                )
            else:
                self.console.print(
                    f"[red]Error: Task not found[/red]"
                )
        except ValueError as e:
            self.console.print(f"[red]Error: {e}[/red]")

    def add_task(self, args: List[str]):
        if not args:
            self.console.print(
                '[red]Error: Title required. Usage: add "Title" "Description"[/red]'
            )
            return

        title = args[0]
        description = args[1] if len(args) > 1 else ""

        try:
            task = self.service.create_task(title, description)
            self.console.print(
                f"[green]Task '{task.title}' added![/green]"
            )
            # We intentionally don't show UUID here anymore to keep it clean.
        except ValueError as e:
            self.console.print(f"[red]Error: {e}[/red]")

    def list_tasks(self):
        tasks = self.service.get_all_tasks()
        self.last_listed_tasks = tasks  # Cache for index resolution

        if not tasks:
            self.console.print("[yellow]No tasks found.[/yellow]")
            return

        table = Table(title="Todo List")
        table.add_column("#", style="cyan", no_wrap=True) # Short Index
        table.add_column("Title", style="magenta")
        table.add_column("Description", style="white")
        table.add_column("Status", style="green")
        table.add_column("Created At", style="dim")

        for idx, task in enumerate(tasks, 1): # Start from 1
            status_style = "green" if task.status == "Completed" else "yellow"
            table.add_row(
                str(idx),
                task.title,
                task.description,
                f"[{status_style}]{task.status.value}[/{status_style}]",
                task.created_at.strftime("%Y-%m-%d %H:%M"),
            )

        self.console.print(table)