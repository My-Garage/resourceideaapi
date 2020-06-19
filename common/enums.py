import enum


class Status(enum.Enum):
    """Status enumeration."""
    ACTIVE = 'active'
    DISABLED = 'disabled'
    ARCHIVED = 'archived'
    DELETED = 'deleted'


class ProgressStatus(enum.Enum):
    """Enumeration indicates the different
    stages of the progress made on an engagement,
    job or task."""

    NOT_STARTED = 'not started'
    RUNNING = 'running'
    IN_REVIEW = 'in review'
    REVIEWED = 'reviewed'
    CLOSED = 'closed'
