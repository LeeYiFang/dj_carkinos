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
    probe_list = models.TextField()


class Sample(models.Model):

    name = models.CharField(
        max_length=1024,
    )
    filename = models.CharField(
        max_length=512,
        blank=True
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
    platform = models.ForeignKey(
        'GeneralPlatform',
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = (
            ("name", "dataset"),
        )

    def __str__(self):
        return "{0.name} {0.cell_line} from {0.dataset}".format(self)


class ProbeInfo(models.Model):

    identifier = models.CharField(
        max_length=256,
    )
    platform = models.ForeignKey(
        'MicroarrayPlatform',
        related_name='probes',
    )
    gene_symbol = models.CharField(
        max_length=256,
        blank=True,
    )
    gene_name = models.TextField(
        blank=True,
    )
    entrez_id = models.IntegerField(
        null=True, blank=True,
    )

    class Meta:
        unique_together = (
            ("platform", "identifier", "gene_symbol",),
        )

    def __str__(self):
        return '{0.identifier} of {0.platform}'.format(self)


class ProbeValue(models.Model):

    sample = models.ForeignKey(
        'Sample',
        related_name='probe_values',
        on_delete=models.CASCADE,
    )
    probe_id = models.CharField(
        max_length=256,
    )
    value = models.FloatField(blank=True)

    class Meta:
        unique_together = (
            ('sample', 'probe_id'),
        )

    def __str__(self):
        return '{0.probe_id}={0.value:.2f}'.format(self)
