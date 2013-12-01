from django.utils.translation import ugettext as _
from dragoman_blog.model_bases import BaseEntry
from cms.models.fields import PlaceholderField
from django.db.models.signals import post_save
from django.dispatch import receiver
from menus.menu_pool import menu_pool


class Entry(BaseEntry):

    placeholder = PlaceholderField('dragoman_placeholder')

    class Meta:
        verbose_name = _('Entry')
        verbose_name_plural = _('Entrys')
        abstract = False
        app_label = 'cmsplugin_dragoman'


@receiver(post_save, sender=Entry)
def clear_menu_pool_cache(sender, **kwargs):
    menu_pool.clear()
