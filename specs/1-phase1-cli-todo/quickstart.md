# Quickstart: Phase I Todo App

## Prerequisites
- Python 3.13+
- `uv` (Universal Virtualenv Manager)

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repo-url>
   cd todo-evolution
   ```

2. **Install dependencies**:
   ```bash
   uv sync
   ```

## Running the App

To start the interactive session:

```bash
uv run python src/main.py
```

## Usage Guide

Once inside the app, use the following commands:

- **Add a task**: `add "Task Title" "Description"`
- **List tasks**: `list`
- **Update a task**: `update <ID> --title "New Title"`
- **Complete a task**: `complete <ID>`
- **Delete a task**: `delete <ID>`
- **Exit**: `exit`

## Development

Run tests:
```bash
uv run pytest
```
