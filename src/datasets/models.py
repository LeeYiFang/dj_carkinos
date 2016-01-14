from django.db import models
from django.conf import settings


class DataSet(models.Model):
    name = models.CharField(
        max_length=1024,
        primary_key=True,
    )
    data_path = models.FilePathField(
        path=settings.DATA_ROOT,
        max_length=512,
        blank=True,
    )

    def __str__(self):
        return self.name


class CellLine(models.Model):

    name = models.CharField(
        max_length=1024,
    )
    primary_site = models.CharField(
        max_length=1024,
    )
    primary_histology = models.CharField(
        max_length=1024,
    )

    class Meta:
        unique_together = (
            ("name", "primary_site", "primary_histology"),
        )

    def __str__(self):
        return self.name


class GeneralPlatform(models.Model):

    name = models.CharField(
        max_length=1024,
        primary_key=True
    )
    description = models.TextField()

    def __str__(self):
        return self.name


class MicroarrayPlatform(GeneralPlatform):

    manufacturer = models.CharField(
        max_length=256,
    )


class Sample(models.Model):

    name = models.CharField(
        max_length=1024,
    )

    cell_line = models.ForeignKey(
        'CellLine',
        related_name='samples',
        blank=True, null=True,
        on_delete=models.CASCADE,
    )

    dataset = models.ForeignKey(
        'DataSet',
        related_name='samples',
        on_delete=models.CASCADE,
    )
    dataset_order = models.IntegerField()

    platform = models.ForeignKey(
        'GeneralPlatform',
        related_name='samples',
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = (
            ("dataset", "name"),
            ("dataset", "dataset_order"),
        )

    def __str__(self):
        return "{0.name} {0.cell_line} from {0.dataset}".format(self)


class Gene(models.Model):

    entrez_id = models.IntegerField(
        unique=True,
    )

    symbol = models.CharField(
        max_length=256,
        blank=True,
    )

    name = models.TextField(
        blank=True,
    )


class ProbeInfo(models.Model):

    identifier = models.CharField(
        max_length=256,
    )

    platform = models.ForeignKey(
        'MicroarrayPlatform',
        on_delete=models.CASCADE,
        related_name='probes',
    )

    platform_order = models.IntegerField()

    genes = models.ManyToManyField(
        "Gene",
        related_name="probes",
    )

    class Meta:
        unique_together = (
            ("platform", "identifier"),
            ("platform", "platform_order"),
        )

    def __str__(self):
        return '{0.identifier} of {0.platform}'.format(self)


