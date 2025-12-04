# Hackathon II: The Evolution of Todo (Phase I)

A modern, interactive, **In-Memory CLI Todo Application** built with **Python 3.14**, **Typer**, and **Rich**.
This project represents the first phase of an evolutionary architecture journey, focusing on Clean Architecture and User Experience (UX) before introducing persistence.

![Todo CLI](https://img.shields.io/badge/Built%20With-Python%203.14-blue.svg)
![Typer](https://img.shields.io/badge/CLI-Typer-white.svg)
![Rich](https://img.shields.io/badge/UI-Rich-red.svg)

## 🚀 Features

- **Interactive REPL:** A persistent session loop that keeps your data alive in RAM.
- **Smart Menu:** Easy navigation using numbers (`1`, `2`, `3`) or text commands.
- **Beautiful UI:** Rich tables, colored status indicators, and confirmation prompts.
- **Clean Architecture:** Separation of concerns (Models, Repositories, Services, CLI).
- **Strict Quality:** Fully typed (Mypy) and linted (Ruff).

## 🛠️ Prerequisites

- **Python 3.14+**
- **uv** (An extremely fast Python package manager)

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Syed-Umer-Ali/Hackathon-II.git
   cd Hackathon-II
   ```

2. **Install dependencies:**
   ```bash
   uv sync
   ```
   *(This will automatically create a virtual environment and install Typer, Rich, Pydantic, etc.)*

## 🎮 How to Run

To start the interactive session, run:

```bash
uv run python -m src.main
```

## 📖 Usage Guide

Once the app starts, you will see a menu. You can interact in two ways:

1.  **Menu Selection:** Type `1`, `2`, `3`... to select an option.
2.  **Direct Commands:** Type `add`, `list`, `delete` directly.

### Available Commands

| Option | Command | Description |
| :--- | :--- | :--- |
| **1** | `add` | Add a new task (Prompts for Title & Description) |
| **2** | `list` | View all tasks in a formatted table |
| **3** | `update` | Edit a task's title or description |
| **4** | `complete` | Mark a task as "Completed" |
| **5** | `delete` | Permanently remove a task |
| **6** | `exit` | Close the application (Data will be lost!) |

### 💡 Pro Tip
When using `update`, `complete`, or `delete`, you can provide the **Task #** (Index) shown in the list instead of the long ID.
*Example:* If "Buy Milk" is #1 in the list, just type `1` when asked for ID.

## 🧪 Development

Run the test suite to verify logic:
```bash
uv run pytest
```

Check code quality:
```bash
uv run ruff check .
uv run mypy .
```

## 📂 Project Structure

```text
src/
├── models/          # Pydantic Data Models (Task)
├── repositories/    # Data Access Layer (In-Memory Storage)
├── services/        # Business Logic
├── cli/             # UI & Command Handling (Typer + Rich)
└── main.py          # Entry Point
```
