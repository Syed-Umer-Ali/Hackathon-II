# Feature Specification: Phase I In-Memory Todo CLI

**Feature Branch**: `1-phase1-cli-todo`  
**Created**: 2025-12-04  
**Status**: Draft  
**Input**: User description: "Implement Phase I In-Memory Todo App with CLI using Typer and Rich"

## User Scenarios & Testing

### User Story 1 - Interactive Session (Priority: P1)

As a user, I want to start an interactive session so that my tasks persist while I am using the application.

**Why this priority**: Since data is in-memory, a single-command CLI would lose data immediately. An interactive loop is essential for the app to be usable.

**Independent Test**: Launch the app; verify it enters a command loop and doesn't exit immediately.

**Acceptance Scenarios**:
1. **Given** the application is installed, **When** I run `python main.py`, **Then** I see a welcome message and a prompt waiting for input.
2. **Given** I am in the session, **When** I type `exit`, **Then** the application terminates.

---

### User Story 2 - Add Task (Priority: P1)

As a user, I want to add a new task with a title and description so I can track my work.

**Why this priority**: Core functionality of a Todo app.

**Independent Test**: In the app loop, add a task and verify it appears in the list.

**Acceptance Scenarios**:
1. **Given** I am in the app loop, **When** I run `add "Buy Milk" "Groceries"`, **Then** the system confirms "Task 'Buy Milk' added" and assigns a unique ID.
2. **Given** I am in the app loop, **When** I run `add` without arguments, **Then** the system prompts me for the title and description.

---

### User Story 3 - List Tasks (Priority: P1)

As a user, I want to view all my tasks in a formatted table so I can see what needs to be done.

**Why this priority**: Essential to verify additions and updates.

**Independent Test**: Add multiple tasks, then run `list` and check output format.

**Acceptance Scenarios**:
1. **Given** I have added tasks, **When** I run `list`, **Then** I see a table with columns: ID, Title, Description, Status, Created At.
2. **Given** the list is empty, **When** I run `list`, **Then** I see a friendly message "No tasks found".

---

### User Story 4 - Update Task (Priority: P2)

As a user, I want to modify a task's title or description so I can correct mistakes or add details.

**Why this priority**: Data accuracy.

**Independent Test**: Create a task, update it, and verify the change in the list.

**Acceptance Scenarios**:
1. **Given** a task with ID 1 exists, **When** I run `update 1 --title "Buy Almond Milk"`, **Then** the task title changes to "Buy Almond Milk".
2. **Given** a non-existent ID, **When** I run `update 999`, **Then** I see an error "Task not found".

---

### User Story 5 - Mark Complete (Priority: P2)

As a user, I want to mark a task as done so I can track my progress.

**Why this priority**: Core Todo lifecycle.

**Independent Test**: Create a task, mark it complete, verify status is "Completed".

**Acceptance Scenarios**:
1. **Given** a "Pending" task, **When** I run `complete <ID>`, **Then** its status changes to "Completed" and the row color in `list` changes (e.g., green).
2. **Given** a task is already completed, **When** I run `complete <ID>`, **Then** the system informs me it's already done.

---

### User Story 6 - Delete Task (Priority: P3)

As a user, I want to remove a task permanently so I can declutter my list.

**Why this priority**: Cleanup functionality.

**Independent Test**: Create a task, delete it, verify it's gone from the list.

**Acceptance Scenarios**:
1. **Given** a task exists, **When** I run `delete <ID>`, **Then** the system asks for confirmation (Y/n).
2. **Given** I confirm with 'Y', **Then** the task is removed and "Task deleted" is displayed.

### Edge Cases

- **Empty Input**: What happens if I try to add a task with an empty title? (Should be rejected).
- **Invalid IDs**: Commands receiving non-UUID or non-existent IDs should fail gracefully.
- **App Exit**: Data is intentionally lost when the session ends (In-Memory constraint).

## Requirements

### Functional Requirements

- **FR-001**: System MUST provide an interactive REPL (Read-Eval-Print Loop) mode.
- **FR-002**: System MUST store tasks in volatile memory (RAM) using a Python list/dictionary.
- **FR-003**: System MUST use **Typer** to handle command parsing within the loop.
- **FR-004**: System MUST use **Rich** to render tables (for `list`) and colored feedback messages (green for success, red for errors).
- **FR-005**: System MUST validate Task data (Title required) using **Pydantic** models.
- **FR-006**: Task entities MUST have auto-generated unique IDs (UUID4) and timestamps.

### Key Entities

- **Task**:
    - `id`: UUID (auto-generated)
    - `title`: String (required)
    - `description`: String (optional)
    - `status`: Enum (Pending, Completed)
    - `created_at`: Datetime

## Success Criteria

### Measurable Outcomes

- **SC-001**: User can perform the full CRUD lifecycle (Add -> List -> Update -> Complete -> Delete) in a single session without errors.
- **SC-002**: `list` command renders a properly aligned table for up to 50 tasks in under 100ms.
- **SC-003**: Application handles invalid inputs (e.g., wrong ID format) without crashing, displaying a red error message instead.
- **SC-004**: Codebase passes `mypy` strict type checking and `pylint` analysis (adhering to Constitution).
