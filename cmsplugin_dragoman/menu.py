from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language
from dragoman_blog.models import Entry, EntryTranslation
from django.conf import settings

CMSPLUGIN_DRAGOMAN_MENU_ITEMS_LIMIT = getattr(
    settings, 'CMSPLUGIN_DRAGOMAN_MENU_ITEMS_LIMIT', 5)


class BlogEntriesMenu(CMSAttachMenu):
    name = _("Blog Entries Menu")

    def get_nodes(self, request):
        nodes = []
        for entry in EntryTranslation.objects.filter(is_published=True, language_code=get_language()).order_by('-pub_date')[:CMSPLUGIN_DRAGOMAN_MENU_ITEMS_LIMIT]:
            node = NavigationNode(
                entry.title,
                reverse('dragoman_blog_detail',
                        kwargs={
                        'year': entry.pub_date.strftime("%Y"),
                        'month': entry.pub_date.strftime("%m"),
                        'day': entry.pub_date.strftime("%d"),
                        'slug': entry.slug
                        }),
                entry.pk
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(BlogEntriesMenu)
