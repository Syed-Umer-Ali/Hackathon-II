# Research: Phase I In-Memory Todo CLI

**Feature**: Phase I In-Memory Todo CLI
**Status**: Complete

## Decision 1: REPL vs. Single Command
- **Decision**: Implement an interactive REPL (Read-Eval-Print Loop).
- **Rationale**: The requirement is "In-Memory" storage. If we used a standard CLI (e.g., `python app.py add "Task"`), the process would exit immediately after the command, wiping the memory. An interactive loop (`while True: input()`) is the only way to keep the process alive and persist state across multiple commands without external storage (file/db).
- **Alternatives Considered**:
    - *File-based persistence (JSON/SQLite)*: Rejected because the spec explicitly demands "In-Memory" for Phase I.
    - *Daemon process*: Too complex for Phase I.

## Decision 2: Typer in REPL
- **Decision**: Use Typer for command parsing even within the REPL loop.
- **Rationale**: While Typer is designed for system argv parsing, we can manually invoke it or use a library like `typer-cli` or just standard input parsing mapped to functions. However, to stick to the "User-Centric CLI" principle and prepare for future phases where this MIGHT become a standard CLI, we will structure commands as Typer commands but invoke them via a custom loop or look into `typer`'s interactive capabilities if available, or simply simulate it by parsing the input string and calling the relevant function.
- **Refinement**: We will use a simple `cmd` module or a custom `while` loop that parses input and calls service functions, potentially using `typer` just for the initial entry point or help generation, OR use a library like `cmd2` or `questionary` for the REPL if Typer proves too rigid for a loop.
- **Final Choice**: Custom `while` loop using `rich.prompt` for input and parsing arguments manually or using `shlex` to pass to Typer-like functions. *Correction*: To strictly use Typer as requested, we might build the app such that `python main.py` enters the loop, and inside the loop, we parse commands. Actually, `typer` is best for non-interactive CLIs. For interactive REPLs, `prompt_toolkit` or `cmd` is standard.
- **Hybrid Approach**: We will use `typer` for the main entry point. One command will be `interactive` (default). Inside `interactive`, we will use a loop. The specific commands (add, list) can be defined as functions that *could* be Typer commands later, but for now, they will be Python functions called by the loop to ensure state persistence.

## Decision 3: Rich for UI
- **Decision**: Use `rich.console.Console` and `rich.table.Table`.
- **Rationale**: Meets the "User-Centric" constitution principle. Provides instant visual feedback.

## Decision 4: Project Structure
- **Decision**: `src/` with `models`, `repositories`, `services`, `cli`.
- **Rationale**: Clean Architecture (Constitution Principle IV). Even for a simple app, this separates concerns and makes Phase II (Persistence) a matter of swapping the Repository.
