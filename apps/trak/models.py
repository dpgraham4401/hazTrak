import datetime

from django.db import models

from apps.sites.models import EpaSite
from lib.rcrainfo import lookups as ri


class Manifest(models.Model):
    manifestTrackingNumber = models.CharField(max_length=15)
    createdDate = models.DateTimeField(null=True)
    updatedDate = models.DateTimeField(default=datetime.datetime.now())
    status = models.CharField(max_length=25,
                              choices=ri.STATUS,
                              default='notAssigned')
    submissionType = models.CharField(max_length=25,
                                      choices=ri.SUB_TYPE,
                                      default='FullElectronic')
    originType = models.CharField(max_length=25,
                                  choices=ri.ORIGIN_TYPE,
                                  default='Service')
    shippedDate = models.DateTimeField('Shipped date', null=True)
    receivedDate = models.DateTimeField('Received date', null=True)
    transporters = models.JSONField()
    generator = models.ForeignKey('Handler', on_delete=models.PROTECT)
    broker = models.JSONField(null=True)
    designatedFacility = models.JSONField()
    wastes = models.JSONField()
    additionalInfo = models.JSONField(null=True)
    printedDocument = models.JSONField(null=True)
    rejection = models.BooleanField(null=True)
    residue = models.BooleanField(null=True)
    importFlag = models.BooleanField(null=True)
    containsPreviousRejectOrResidue = models.BooleanField(null=True)
    formDocument = models.JSONField(null=True)
    newResidueManifestTrackingNumbers = models.JSONField(null=True)
    rejectionInfo = models.JSONField(null=True)
    importInfo = models.JSONField(null=True)
    correctionInfo = models.JSONField(null=True)
    ppcInfo = models.JSONField(null=True)
    transferRequested = models.BooleanField(null=True)
    transferStatus = models.CharField(max_length=200, null=True)
    originalSubmissionType = models.CharField(max_length=25,
                                              choices=ri.SUB_TYPE,
                                              null=True)
    potentialShipDate = models.DateTimeField('Potential Ship Date', null=True)
    reTransferCount = models.IntegerField(null=True)
    nextTransferTime = models.DateTimeField('Next Transfer Time', null=True)
    locked = models.BooleanField(null=True)
    lockReason = models.CharField(max_length=25, null=True)
    certifiedDate = models.DateTimeField('Certified date', null=True)
    certifiedBy = models.JSONField(null=True)

    def __str__(self):
        return self.manifestTrackingNumber


class Handler(models.Model):
    epaSiteId = models.CharField(max_length=25)
    name = models.CharField(max_length=200)
    registered = models.BooleanField()
    mailingAddress = models.JSONField()
    siteAddress = models.JSONField()
    contact = models.JSONField()
    emergencyPhone = models.JSONField()
    canEsign = models.BooleanField()
    hasRegisteredEmanifestUser = models.BooleanField()

    def __str__(self):
        return self.epaSiteId


class ElectronicSignature(models.Model):
    signer_first_name = models.CharField(max_length=200)
    signer_last_name = models.CharField(max_length=200)
    signer_user_id = models.CharField(max_length=200)
    signature_date = models.DateTimeField('signature_date')

    def __str__(self):
        return f'{self.signature_date} by {self.signer_user_id}'
