import enum


class Status(enum.Enum):
    """Status enumeration."""
    ACTIVE = 'active'
    DISABLED = 'disabled'
    ARCHIVED = 'archived'
