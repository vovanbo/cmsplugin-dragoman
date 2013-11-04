from cms.menu_bases import CMSAttachMenu
from menus.base import Menu, NavigationNode
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from dragoman_blog.models import Entry, EntryTranslation


class BlogEntriesMenu(CMSAttachMenu):
    name = _("Blog Entries Menu")

    def get_nodes(self, request):
        nodes = []
        for entry in EntryTranslation.objects.filter(is_published=True):
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
