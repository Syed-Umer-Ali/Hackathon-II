# Command Interface Contract

Since this is a CLI app, the "API" is the set of text commands accepted by the REPL.

## Commands

### ADD
- **Syntax**: `add "<title>" "<description>"`
- **Arguments**:
    - `title` (String, Required): Quote if contains spaces.
    - `description` (String, Optional): Quote if contains spaces.
- **Example**: `add "Buy Milk" "From the corner store"`
- **Output (Success)**: `[green]Task 'Buy Milk' added (ID: <uuid>)[/green]`
- **Output (Error)**: `[red]Error: Title cannot be empty[/red]`

### LIST
- **Syntax**: `list`
- **Arguments**: None
- **Output**: Rich Table with columns: `ID`, `Title`, `Description`, `Status`, `Created`

### UPDATE
- **Syntax**: `update <id> --title "<new_title>" --desc "<new_desc>"`
- **Arguments**:
    - `id` (UUID/String, Required): The task ID.
    - `--title` (String, Optional)
    - `--desc` (String, Optional)
- **Example**: `update 1234-5678 --title "Buy Soy Milk"`
- **Output**: `[green]Task updated successfully[/green]`

### COMPLETE
- **Syntax**: `complete <id>`
- **Arguments**:
    - `id` (UUID/String, Required)
- **Output**: `[green]Task marked as Completed[/green]`

### DELETE
- **Syntax**: `delete <id>`
- **Arguments**:
    - `id` (UUID/String, Required)
- **Output**: `[green]Task deleted[/green]`
