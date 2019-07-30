import enum


class Status(enum.Enum):
    """Status enumeration."""
    ACTIVE = 'active'
    DISABLED = 'disabled'
    ARCHIVED = 'archived'


class ProgressStatus(enum.Enum):
    """Progress status enumeration."""

    NOT_STARTED = 'not started',
    RUNNING = 'running'
    IN_REVIEW = 'in review'
    REVIEWED = 'reviewed'
    CLOSED = 'closed'
