from django.db import models
from django.utils import timezone


class PostQuerySet(models.QuerySet):

    def with_related_data(self):
        return self.select_related(
            'author',
            'category',
            'location',
        )

    def only_published(self):
        return self.filter(
            is_published=True,
            category__is_published=True,
            pub_date__lte=timezone.now()
        )


class PublishedPostManager(models.Manager):

    def get_queryset(self):
        return (
            PostQuerySet(self.model)
            .with_related_data()
            .only_published()
        )
