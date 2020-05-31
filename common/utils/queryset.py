from typing import TypeVar, Generic

from django.db.models import QuerySet

from client.models import Client
from client_industry.models import ClientIndustry

T = TypeVar('T', Client, ClientIndustry)


def filter_organization_active_clients(model: Generic[T], organization_id: str) -> QuerySet:
    """
    Filters the active clients that belong to an organization.

    Args:
        model (Generic[T]): Model that is going to be queried.
        organization_id (str): ID of the organization whose clients are to filtered.

    Returns:
        QuerySet of the active clients of the organization whose ID has been supplied.
    """
    queryset = model.objects.filter(organization_id=organization_id, is_deleted=False, deleted_at__isnull=True)
    return queryset