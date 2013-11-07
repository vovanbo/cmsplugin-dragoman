from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from dragoman_blog.models import EntryTranslation


class BlogEntriesMenu(CMSAttachMenu):
    name = _("Blog Entries Menu")

    def get_nodes(self, request):
        nodes = []
        for tag in EntryTranslation.tags.all():
            node = NavigationNode(
                tag.name,
                reverse(
                    'dragoman_blog_list_by_tag', kwargs={'tag': tag.name}),
                tag.pk
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(BlogEntriesMenu)
