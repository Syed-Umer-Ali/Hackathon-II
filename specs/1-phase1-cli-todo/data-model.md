# Data Model: Phase I In-Memory Todo CLI

## Entities

### Task
Represents a single unit of work to be tracked.

| Field | Type | Required | Description | Constraints |
|-------|------|----------|-------------|-------------|
| `id` | UUID | Yes | Unique identifier | Auto-generated (UUID4) |
| `title` | String | Yes | Short summary of the task | Min len 1, Max len 100 |
| `description` | String | No | Detailed explanation | Max len 500, Default "" |
| `status` | Enum | Yes | Current state | `Pending` or `Completed` |
| `created_at` | DateTime | Yes | Timestamp of creation | Auto-generated (UTC) |

## Relationships

- None (Single Entity for Phase I).

## Validation Rules

1. **Title**: Must not be empty or whitespace only.
2. **Status**: Must be a valid enum value.
3. **Immutability**: `id` and `created_at` should not change after creation.
