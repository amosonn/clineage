from django.contrib.auth.models import User
from django.db import models
from lib_prep.workflows.models import Library, BarcodedContent
from primers.parts.models import IlluminaReadingAdaptor1, \
    IlluminaReadingAdaptor2

class MachineType(models.Model):
    company = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    read_length = models.IntegerField(null=True)

    def __unicode__(self):
        return self.company + '_' + self.model


class Machine(models.Model):
    machineid = models.CharField(max_length=50)
    name = models.CharField(max_length=100, null=True, blank=True)
    type = models.ForeignKey(MachineType)

    def __unicode__(self):
        return self.type.__unicode__() + '_' + self.machineid


class NGSKit(models.Model):
    reading_adaptor1 = models.ForeignKey(IlluminaReadingAdaptor1)
    reading_adaptor2 = models.ForeignKey(IlluminaReadingAdaptor2)

    @property
    def adapter(self):
        """
        Return the value for the Adapter field in the SampleSheet.
        """
        return reading_adaptor2.sequence[1:].rev_comp()

    @property
    def adapterread2(self):
        """
        Return the value for the AdapterRead2 field in the SampleSheet.
        """
        return reading_adaptor1.sequence.rev_comp()


class NGSRun(models.Model):
    libraries = models.ManyToManyField(Library)
    bcl_directory = models.FilePathField(allow_files=False, allow_folders=True, null=True)
    name = models.CharField(max_length=100, unique=True)
    machine = models.ForeignKey(Machine)
    kit = models.ForeignKey(NGSKit, null=True)
    user = models.ForeignKey(User)
    date = models.DateField()
