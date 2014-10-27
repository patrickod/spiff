# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UserResetToken'
        db.create_table(u'identity_userresettoken', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='resetTokens', to=orm['auth.User'])),
            ('token', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'identity', ['UserResetToken'])

        # Adding model 'Identity'
        db.create_table(u'identity_identity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tagline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(related_name='member', unique=True, to=orm['auth.User'])),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('lastSeen', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('hidden', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('displayName', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'identity', ['Identity'])

        # Adding model 'Rank'
        db.create_table(u'identity_rank', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('monthlyDues', self.gf('django.db.models.fields.FloatField')(default=0)),
            ('group', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.Group'], unique=True)),
            ('isActiveMembership', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('isKeyholder', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'identity', ['Rank'])

        # Adding model 'Field'
        db.create_table(u'identity_field', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('required', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('public', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('protected', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'identity', ['Field'])

        # Adding model 'FieldValue'
        db.create_table(u'identity_fieldvalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('field', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['identity.Field'])),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(related_name='attributes', to=orm['identity.Identity'])),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'identity', ['FieldValue'])

        # Adding model 'RankSubscriptionPlan'
        db.create_table(u'identity_ranksubscriptionplan', (
            (u'subscriptionplan_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['subscription.SubscriptionPlan'], unique=True, primary_key=True)),
            ('rank', self.gf('django.db.models.fields.related.ForeignKey')(related_name='subscriptions', to=orm['identity.Rank'])),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='rankSubscriptions', null=True, to=orm['identity.Identity'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=1)),
        ))
        db.send_create_signal(u'identity', ['RankSubscriptionPlan'])

        # Adding model 'RankLineItem'
        db.create_table(u'identity_ranklineitem', (
            (u'lineitem_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['payment.LineItem'], unique=True, primary_key=True)),
            ('rank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['identity.Rank'])),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(related_name='rankLineItems', to=orm['identity.Identity'])),
            ('activeFromDate', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 10, 13, 0, 0))),
            ('activeToDate', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 10, 13, 0, 0))),
        ))
        db.send_create_signal(u'identity', ['RankLineItem'])

        # Adding model 'MembershipPeriod'
        db.create_table(u'identity_membershipperiod', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rank', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['identity.Rank'])),
            ('member', self.gf('django.db.models.fields.related.ForeignKey')(related_name='membershipPeriods', to=orm['identity.Identity'])),
            ('activeFromDate', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 10, 13, 0, 0))),
            ('activeToDate', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 10, 13, 0, 0))),
            ('lineItem', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['identity.RankLineItem'], null=True, blank=True)),
        ))
        db.send_create_signal(u'identity', ['MembershipPeriod'])

        # Adding index on 'MembershipPeriod', fields ['activeFromDate', 'activeToDate']
        db.create_index(u'identity_membershipperiod', ['activeFromDate', 'activeToDate'])


    def backwards(self, orm):
        # Removing index on 'MembershipPeriod', fields ['activeFromDate', 'activeToDate']
        db.delete_index(u'identity_membershipperiod', ['activeFromDate', 'activeToDate'])

        # Deleting model 'UserResetToken'
        db.delete_table(u'identity_userresettoken')

        # Deleting model 'Identity'
        db.delete_table(u'identity_identity')

        # Deleting model 'Rank'
        db.delete_table(u'identity_rank')

        # Deleting model 'Field'
        db.delete_table(u'identity_field')

        # Deleting model 'FieldValue'
        db.delete_table(u'identity_fieldvalue')

        # Deleting model 'RankSubscriptionPlan'
        db.delete_table(u'identity_ranksubscriptionplan')

        # Deleting model 'RankLineItem'
        db.delete_table(u'identity_ranklineitem')

        # Deleting model 'MembershipPeriod'
        db.delete_table(u'identity_membershipperiod')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'identity.field': {
            'Meta': {'object_name': 'Field'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'protected': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'public': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'required': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'identity.fieldvalue': {
            'Meta': {'object_name': 'FieldValue'},
            'field': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['identity.Field']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'attributes'", 'to': u"orm['identity.Identity']"}),
            'value': ('django.db.models.fields.TextField', [], {})
        },
        u'identity.identity': {
            'Meta': {'object_name': 'Identity'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'displayName': ('django.db.models.fields.TextField', [], {}),
            'fields': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['identity.Field']", 'through': u"orm['identity.FieldValue']", 'symmetrical': 'False'}),
            'hidden': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lastSeen': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'tagline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'member'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'identity.membershipperiod': {
            'Meta': {'object_name': 'MembershipPeriod', 'index_together': "[['activeFromDate', 'activeToDate']]"},
            'activeFromDate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 13, 0, 0)'}),
            'activeToDate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 13, 0, 0)'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lineItem': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['identity.RankLineItem']", 'null': 'True', 'blank': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'membershipPeriods'", 'to': u"orm['identity.Identity']"}),
            'rank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['identity.Rank']"})
        },
        u'identity.rank': {
            'Meta': {'object_name': 'Rank'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'group': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.Group']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isActiveMembership': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'isKeyholder': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'monthlyDues': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'identity.ranklineitem': {
            'Meta': {'object_name': 'RankLineItem', '_ormbases': [u'payment.LineItem']},
            'activeFromDate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 13, 0, 0)'}),
            'activeToDate': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 10, 13, 0, 0)'}),
            u'lineitem_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['payment.LineItem']", 'unique': 'True', 'primary_key': 'True'}),
            'member': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'rankLineItems'", 'to': u"orm['identity.Identity']"}),
            'rank': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['identity.Rank']"})
        },
        u'identity.ranksubscriptionplan': {
            'Meta': {'object_name': 'RankSubscriptionPlan', '_ormbases': [u'subscription.SubscriptionPlan']},
            'member': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'rankSubscriptions'", 'null': 'True', 'to': u"orm['identity.Identity']"}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'rank': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'subscriptions'", 'to': u"orm['identity.Rank']"}),
            u'subscriptionplan_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['subscription.SubscriptionPlan']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'identity.userresettoken': {
            'Meta': {'object_name': 'UserResetToken'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'resetTokens'", 'to': u"orm['auth.User']"})
        },
        u'payment.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'draft': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'dueDate': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'open': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'invoices'", 'to': u"orm['auth.User']"})
        },
        u'payment.lineitem': {
            'Meta': {'object_name': 'LineItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['payment.Invoice']"}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'quantity': ('django.db.models.fields.FloatField', [], {'default': '1'}),
            'unitPrice': ('django.db.models.fields.FloatField', [], {'default': '0'})
        },
        u'subscription.subscriptionperiod': {
            'Meta': {'object_name': 'SubscriptionPeriod'},
            'dayOfMonth': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monthOfYear': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'subscription.subscriptionplan': {
            'Meta': {'object_name': 'SubscriptionPlan'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'period': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['subscription.SubscriptionPeriod']"})
        }
    }

    complete_apps = ['identity']