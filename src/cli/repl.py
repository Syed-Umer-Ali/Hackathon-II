from typing import Optional
import shlex

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

from src.cli.commands import TodoCommands
from src.services.todo_service import TodoService


class REPL:
    def __init__(self, service: TodoService, console: Optional[Console] = None):
        self.service = service
        self.console = console or Console()
        self.commands = TodoCommands(service, self.console)

    def display_menu(self):
        menu_text = """[bold cyan]Available Commands:[/bold cyan]
1. [bold green]Add Task[/bold green]      (type '1' or 'add')
2. [bold yellow]List Tasks[/bold yellow]    (type '2' or 'list')
3. [bold blue]Update Task[/bold blue]   (type '3' or 'update')
4. [bold magenta]Complete Task[/bold magenta] (type '4' or 'complete')
5. [bold red]Delete Task[/bold red]   (type '5' or 'delete')
6. [bold white]Exit[/bold white]          (type '6' or 'exit')
"""
        self.console.print(Panel(menu_text, title="Todo App Menu", border_style="blue"))

    def run(self):
        self.console.print(
            "[bold green]Welcome to the Interactive Todo App![/bold green]"
        )
        
        while True:
            try:
                self.display_menu()
                choice = Prompt.ask("[bold blue]Select an option[/bold blue]", choices=["1", "2", "3", "4", "5", "6", "add", "list", "update", "complete", "delete", "exit", "quit"], default="list")
                
                if choice in ("6", "exit", "quit"):
                    self.console.print("[yellow]Goodbye![/yellow]")
                    break

                self.handle_choice(choice)
                self.console.print("") # Add spacing
                
            except KeyboardInterrupt:
                self.console.print("\n[yellow]Goodbye![/yellow]")
                break
            except Exception as e:
                self.console.print(f"[bold red]Error:[/bold red] {e}")

    def handle_choice(self, choice: str):
        # Normalize choice
        if choice == "1": choice = "add"
        if choice == "2": choice = "list"
        if choice == "3": choice = "update"
        if choice == "4": choice = "complete"
        if choice == "5": choice = "delete"

        if choice == "add":
            title = Prompt.ask("Enter Task Title")
            desc = Prompt.ask("Enter Description", default="")
            # Simulate CLI args for existing command logic
            self.commands.add_task([title, desc])
            
        elif choice == "list":
            self.commands.list_tasks()
            
        elif choice == "update":
            self.commands.list_tasks() # Show list first to see IDs
            task_id = Prompt.ask("Enter Task ID to update")
            title = Prompt.ask("New Title (leave empty to keep current)", default=None)
            desc = Prompt.ask("New Description (leave empty to keep current)", default=None)
            
            args = [task_id]
            if title:
                args.extend(["--title", title])
            if desc:
                args.extend(["--desc", desc])
            self.commands.update_task(args)
            
        elif choice == "complete":
            self.commands.list_tasks()
            task_id = Prompt.ask("Enter Task ID to complete")
            self.commands.complete_task([task_id])
            
        elif choice == "delete":
            self.commands.list_tasks()
            task_id = Prompt.ask("Enter Task ID to delete")
            self.commands.delete_task([task_id])