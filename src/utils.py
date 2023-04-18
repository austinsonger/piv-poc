import uuid

from django.db import models


class BaseModel(models.Model):
    """
    Abstract base model

    provides:

    @id = UUID4
    @date_created = DateTimeField
    @last_updated = DateTimeField
    """

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

