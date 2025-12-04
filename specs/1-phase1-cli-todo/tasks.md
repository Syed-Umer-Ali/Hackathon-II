---
description: "Task list for Phase I In-Memory Todo CLI"
---

# Tasks: Phase I In-Memory Todo CLI

**Input**: Design documents from `/specs/1-phase1-cli-todo/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/
**Tests**: Included as per Spec-Driven Development principle (Constitution).

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure (src/models, src/repositories, src/services, src/cli)
- [x] T002 Initialize Python project with `pyproject.toml` (dependencies: typer, rich, pydantic, pytest)
- [x] T003 [P] Configure linting (ruff/pylint) and formatting (black/isort) tools

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core entities and repository structure needed for all stories.

- [x] T004 [P] Create Task model with Pydantic in `src/models/task.py`
- [x] T005 Create TodoRepository interface (Protocol) and InMemory implementation in `src/repositories/todo_repository.py`
- [x] T006 [P] Create TodoService class in `src/services/todo_service.py`
- [x] T007 Create basic Typer app entry point in `src/main.py`

**Checkpoint**: Foundation ready - Core data structures and architecture in place.

## Phase 3: User Story 1 - Interactive Session (Priority: P1) 🎯 MVP

**Goal**: Establish the REPL loop to maintain application state.

**Independent Test**: Run `python src/main.py` -> Should enter loop -> Type `exit` -> Should terminate.

### Tests
- [x] T008 [P] [US1] Unit test for REPL exit command in `tests/unit/test_repl.py`

### Implementation
- [x] T009 [US1] Implement `interactive` command with `while` loop in `src/main.py`
- [x] T010 [US1] Implement input parsing and command routing logic in `src/main.py`
- [x] T011 [US1] Integrate Rich for welcome/exit messages in `src/main.py`

## Phase 4: User Story 2 - Add Task (Priority: P1)

**Goal**: Ability to add new tasks.

**Independent Test**: Run app -> `add "Test" "Desc"` -> Output should confirm addition.

### Tests
- [x] T012 [P] [US2] Unit test for `TodoRepository.add` in `tests/unit/test_repository.py`
- [x] T013 [P] [US2] Unit test for `TodoService.create_task` in `tests/unit/test_service.py`

### Implementation
- [x] T014 [US2] Implement `add` method in `TodoRepository` (src/repositories/todo_repository.py)
- [x] T015 [US2] Implement `create_task` logic in `TodoService` (src/services/todo_service.py)
- [x] T016 [US2] Implement `add` CLI command logic and routing in `src/cli/commands.py` (or `src/main.py`)

## Phase 5: User Story 3 - List Tasks (Priority: P1)

**Goal**: View all tasks in a table.

**Independent Test**: Add tasks -> `list` -> See Rich table.

### Tests
- [x] T017 [P] [US3] Unit test for `TodoRepository.list` in `tests/unit/test_repository.py`

### Implementation
- [x] T018 [US3] Implement `list` method in `TodoRepository` (src/repositories/todo_repository.py)
- [x] T019 [US3] Implement `get_all_tasks` in `TodoService` (src/services/todo_service.py)
- [x] T020 [US3] Implement `list` CLI command using `rich.table.Table` in `src/cli/commands.py`

## Phase 6: User Story 4 - Update Task (Priority: P2)

**Goal**: Modify existing tasks.

**Independent Test**: Update a task -> `list` -> Verify changes.

### Tests
- [x] T021 [P] [US4] Unit test for `TodoRepository.update` in `tests/unit/test_repository.py`

### Implementation
- [x] T022 [US4] Implement `update` method in `TodoRepository` (src/repositories/todo_repository.py)
- [x] T023 [US4] Implement `update_task` in `TodoService` (src/services/todo_service.py)
- [x] T024 [US4] Implement `update` CLI command logic in `src/cli/commands.py`

## Phase 7: User Story 5 - Mark Complete (Priority: P2)

**Goal**: Toggle task status.

**Independent Test**: `complete <id>` -> `list` -> Status is 'Completed'.

### Tests
- [x] T025 [P] [US5] Unit test for `TodoService.complete_task` in `tests/unit/test_service.py`

### Implementation
- [x] T026 [US5] Implement `complete_task` convenience method in `TodoService` (src/services/todo_service.py)
- [x] T027 [US5] Implement `complete` CLI command logic in `src/cli/commands.py`

## Phase 8: User Story 6 - Delete Task (Priority: P3)

**Goal**: Remove tasks.

**Independent Test**: `delete <id>` -> `list` -> Task gone.

### Tests
- [x] T028 [P] [US6] Unit test for `TodoRepository.delete` in `tests/unit/test_repository.py`

### Implementation
- [x] T029 [US6] Implement `delete` method in `TodoRepository` (src/repositories/todo_repository.py)
- [x] T030 [US6] Implement `delete_task` in `TodoService` (src/services/todo_service.py)
- [x] T031 [US6] Implement `delete` CLI command with confirmation prompt in `src/cli/commands.py`

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements and cleanup.

- [x] T032 [P] Review code against Constitution (Types, Docs)
- [x] T033 Run `mypy` and fix type errors
- [x] T034 Run `pylint`/`ruff` and fix linter errors
- [x] T035 Verify all Quickstart scenarios

---

## Dependencies & Execution Order

1. **Setup & Foundational (Phase 1 & 2)**: Must be done first. Blocks everything.
2. **User Story 1 (REPL)**: Blocks testing of other commands interactively, but logic can be tested via unit tests.
3. **User Story 2 & 3 (Add/List)**: Core CRUD, should be done early.
4. **User Story 4, 5, 6**: Can be done in parallel or sequence after US 2 & 3.

## Implementation Strategy

### MVP First
1. Complete Setup & Foundation.
2. Implement REPL (US1).
3. Implement Add (US2) & List (US3).
4. **Release MVP**.

### Full Feature Set
5. Iterate to add Update (US4), Complete (US5), Delete (US6).
6. Polish and Finalize.
