from django.db import models
from spiff.membership.models import Member

class Resource(models.Model):
  name = models.TextField()
  trainable = models.BooleanField(default=True)
  users = models.ManyToManyField(Member, through='TrainingLevel',
      limit_choices_to={'is_active': True})

  @models.permalink
  def get_absolute_url(self):
    return ('inventory:view', [], {'id':self.id})

  def serialize(self):
    return {
      'name': self.name,
      'trainable': self.trainable,
      'trainings': self.trainings,
      'metadata': self.metadata,
      'changelog': self.changelog,
      'id': self.id,
    }
  
  def __unicode__(self):
    return self.name

  def logChange(self, member, trained_member=None, property=None, old=None, new=None):
    Change.objects.create(
        resource=self,
        member=member,
        old=old,
        new=new,
        property=property,
        trained_member=trained_member)

META_TYPES = (
  (0, 'string'),
  (1, 'url'),
  (2, 'image'),
)

class Metadata(models.Model):
  name = models.TextField()
  type = models.IntegerField(choices=META_TYPES)
  value = models.TextField()
  resource = models.ForeignKey(Resource, related_name='metadata')

  def serialize(self):
    return {
      'name': self.name,
      'type': self.type,
      'value': self.value,
    }

  def __unicode__(self):
    return self.value

class TrainingLevel(models.Model):
  member = models.ForeignKey(Member, related_name='trainings')
  resource = models.ForeignKey(Resource, related_name='trainings')
  rank = models.IntegerField()

  class Meta:
    ordering = ['-rank']

  def __unicode__(self):
    return "%s: level %d %s user"%(self.member.fullName, self.rank, self.resource.name)

class Change(models.Model):
  resource = models.ForeignKey(Resource, related_name='changelog')
  member = models.ForeignKey(Member, related_name='changes')
  trained_member = models.ForeignKey(Member, related_name='training_changes',
      null=True, blank=True)
  old = models.TextField(null=True, blank=True)
  new = models.TextField(null=True, blank=True)
  property = models.TextField(null=True, blank=True)
  stamp = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-stamp']

  def __unicode__(self):
    if self.trained_member:
      name = "%s's training on %s"%(self.trained_member, self.resource)
    if self.property:
      name = "%s:%s"%(self.resource, self.property)
    return "%s: %s -> %s"%(name, self.old, self.new)
