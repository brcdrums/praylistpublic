# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field saved_prayer_custom on 'UserProfile'
        db.create_table('PrayList_userprofile_saved_prayer_custom', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['PrayList.userprofile'], null=False)),
            ('savedprayercustom', models.ForeignKey(orm['PrayList.savedprayercustom'], null=False))
        ))
        db.create_unique('PrayList_userprofile_saved_prayer_custom', ['userprofile_id', 'savedprayercustom_id'])

        # Adding M2M table for field saved_prayer_custom on 'DailyPrayer'
        db.create_table('PrayList_dailyprayer_saved_prayer_custom', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dailyprayer', models.ForeignKey(orm['PrayList.dailyprayer'], null=False)),
            ('savedprayercustom', models.ForeignKey(orm['PrayList.savedprayercustom'], null=False))
        ))
        db.create_unique('PrayList_dailyprayer_saved_prayer_custom', ['dailyprayer_id', 'savedprayercustom_id'])


    def backwards(self, orm):
        # Removing M2M table for field saved_prayer_custom on 'UserProfile'
        db.delete_table('PrayList_userprofile_saved_prayer_custom')

        # Removing M2M table for field saved_prayer_custom on 'DailyPrayer'
        db.delete_table('PrayList_dailyprayer_saved_prayer_custom')


    models = {
        'PrayList.dailyprayer': {
            'Meta': {'object_name': 'DailyPrayer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prayed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'prayer_id': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['PrayList.Prayer']"}),
            'saved_prayer_custom': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['PrayList.SavedPrayerCustom']", 'null': 'True', 'symmetrical': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        'PrayList.groups': {
            'Meta': {'object_name': 'Groups'},
            'groupname': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prayer_count': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'privacy': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'total_hotness': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'users_favorited': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'favorited'", 'symmetrical': 'False', 'to': "orm['auth.User']"})
        },
        'PrayList.prayer': {
            'Meta': {'object_name': 'Prayer'},
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['PrayList.Groups']"}),
            'hotness': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poster': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'prayed_users': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.User']", 'symmetrical': 'False'}),
            'prayer': ('django.db.models.fields.CharField', [], {'max_length': '2000'}),
            'prayerscore': ('django.db.models.fields.IntegerField', [], {}),
            'subject': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        'PrayList.savedprayercustom': {
            'Meta': {'object_name': 'SavedPrayerCustom'},
            'custom_prayer': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prayed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        'PrayList.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'saved_prayer': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['PrayList.Prayer']", 'symmetrical': 'False'}),
            'saved_prayer_custom': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['PrayList.SavedPrayerCustom']", 'symmetrical': 'False'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        },
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['PrayList']