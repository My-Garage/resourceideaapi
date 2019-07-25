import enum


class OrganizationStatus(enum.Enum):
    """Organization status enumeration."""
    ACTIVE = 'active'
    DISABLED = 'disabled'
    ARCHIVED = 'archived'
