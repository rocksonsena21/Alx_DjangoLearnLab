from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Set up default groups and assign permissions'

    def handle(self, *args, **kwargs):
        content_type = ContentType.objects.get_for_model(Book)

        # Create permissions
        perms = {
            'can_view': Permission.objects.get(codename='can_view', content_type=content_type),
            'can_create': Permission.objects.get(codename='can_create', content_type=content_type),
            'can_edit': Permission.objects.get(codename='can_edit', content_type=content_type),
            'can_delete': Permission.objects.get(codename='can_delete', content_type=content_type),
        }

        # Create groups
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        editors, _ = Group.objects.get_or_create(name='Editors')
        admins, _ = Group.objects.get_or_create(name='Admins')

        # Assign permissions to groups
        viewers.permissions.set([perms['can_view']])
        editors.permissions.set([perms['can_create'], perms['can_edit']])
        admins.permissions.set([perms['can_view'], perms['can_create'], perms['can_edit'], perms['can_delete']])

        self.stdout.write(self.style.SUCCESS('Groups and permissions created successfully.'))
