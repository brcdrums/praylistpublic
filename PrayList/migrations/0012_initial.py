# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Groups'
        db.create_table('PrayList_groups', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('groupname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('privacy', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('prayer_count', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('total_hotness', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('PrayList', ['Groups'])

        # Adding M2M table for field users_favorited on 'Groups'
        db.create_table('PrayList_groups_users_favorited', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('groups', models.ForeignKey(orm['PrayList.groups'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('PrayList_groups_users_favorited', ['groups_id', 'user_id'])

        # Adding model 'Prayer'
        db.create_table('PrayList_prayer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('poster', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('subject', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('prayer', self.gf('django.db.models.fields.CharField')(max_length=2000)),
            ('prayerscore', self.gf('django.db.models.fields.IntegerField')()),
            ('hotness', self.gf('django.db.models.fields.IntegerField')()),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PrayList.Groups'])),
        ))
        db.send_create_signal('PrayList', ['Prayer'])

        # Adding M2M table for field prayed_users on 'Prayer'
        db.create_table('PrayList_prayer_prayed_users', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('prayer', models.ForeignKey(orm['PrayList.prayer'], null=False)),
            ('user', models.ForeignKey(orm['auth.user'], null=False))
        ))
        db.create_unique('PrayList_prayer_prayed_users', ['prayer_id', 'user_id'])

        # Adding model 'SavedPrayerCustom'
        db.create_table('PrayList_savedprayercustom', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('custom_prayer', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('prayed_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
        ))
        db.send_create_signal('PrayList', ['SavedPrayerCustom'])

        # Adding model 'DailyPrayer'
        db.create_table('PrayList_dailyprayer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('prayed_user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('prayer_id', self.gf('django.db.models.fields.related.ForeignKey')(default='null', to=orm['PrayList.Prayer'], null=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('saved_prayer_custom', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['PrayList.SavedPrayerCustom'], null=True)),
        ))
        db.send_create_signal('PrayList', ['DailyPrayer'])

        # Adding model 'UserProfile'
        db.create_table('PrayList_userprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['auth.User'], unique=True)),
        ))
        db.send_create_signal('PrayList', ['UserProfile'])

        # Adding M2M table for field saved_prayer on 'UserProfile'
        db.create_table('PrayList_userprofile_saved_prayer', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['PrayList.userprofile'], null=False)),
            ('prayer', models.ForeignKey(orm['PrayList.prayer'], null=False))
        ))
        db.create_unique('PrayList_userprofile_saved_prayer', ['userprofile_id', 'prayer_id'])


    def backwards(self, orm):
        # Deleting model 'Groups'
        db.delete_table('PrayList_groups')

        # Removing M2M table for field users_favorited on 'Groups'
        db.delete_table('PrayList_groups_users_favorited')

        # Deleting model 'Prayer'
        db.delete_table('PrayList_prayer')

        # Removing M2M table for field prayed_users on 'Prayer'
        db.delete_table('PrayList_prayer_prayed_users')

        # Deleting model 'SavedPrayerCustom'
        db.delete_table('PrayList_savedprayercustom')

        # Deleting model 'DailyPrayer'
        db.delete_table('PrayList_dailyprayer')

        # Deleting model 'UserProfile'
        db.delete_table('PrayList_userprofile')

        # Removing M2M table for field saved_prayer on 'UserProfile'
        db.delete_table('PrayList_userprofile_saved_prayer')


    models = {
        'PrayList.dailyprayer': {
            'Meta': {'object_name': 'DailyPrayer'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'prayed_user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'prayer_id': ('django.db.models.fields.related.ForeignKey', [], {'default': "'null'", 'to': "orm['PrayList.Prayer']", 'null': 'True'}),
            'saved_prayer_custom': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['PrayList.SavedPrayerCustom']", 'null': 'True'}),
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