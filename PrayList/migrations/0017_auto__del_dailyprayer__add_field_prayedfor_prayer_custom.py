# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'DailyPrayer'
        db.delete_table(u'PrayList_dailyprayer')

        # Adding field 'PrayedFor.prayer_custom'
        db.add_column(u'PrayList_prayedfor', 'prayer_custom',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PrayList.SavedPrayerCustom'], null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'DailyPrayer'
        db.create_table(u'PrayList_dailyprayer', (
            ('prayed_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('prayer_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PrayList.Prayer'], null=True)),
            ('saved_prayer_custom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PrayList.SavedPrayerCustom'], null=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'PrayList', ['DailyPrayer'])

        # Deleting field 'PrayedFor.prayer_custom'
        db.delete_column(u'PrayList_prayedfor', 'prayer_custom_id')


    models = {
        u'PrayList.groups': {
            'Meta': {'object_name': 'Groups'},
            'groupname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prayer_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'privacy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'total_hotness': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'users_favorited': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'favorited'", 'symmetrical': 'False', 'to': u"orm['auth.User']"})
        },
        u'PrayList.prayedfor': {
            'Meta': {'object_name': 'PrayedFor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prayed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True'}),
            'prayer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PrayList.Prayer']", 'null': 'True'}),
            'prayer_custom': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PrayList.SavedPrayerCustom']", 'null': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'PrayList.prayer': {
            'Meta': {'object_name': 'Prayer'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['PrayList.Groups']"}),
            'hotness': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'prayed_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.User']", 'symmetrical': 'False'}),
            'prayer': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'prayerscore': ('django.db.models.fields.IntegerField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'PrayList.savedprayercustom': {
            'Meta': {'object_name': 'SavedPrayerCustom'},
            'custom_prayer': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prayed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'PrayList.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'saved_prayer': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['PrayList.Prayer']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        },
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
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['PrayList']