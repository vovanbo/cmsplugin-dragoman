from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from dragoman_blog.models import EntryTranslation, TranslationTagged
from django.utils.translation import get_language


class BlogEntriesMenu(CMSAttachMenu):
    name = _("Blog Entries Menu")

    def get_nodes(self, request):
        nodes = []
        posts = EntryTranslation.objects.filter(
            is_published=True, language_code=get_language())
        tags = TranslationTagged.objects.none()
        for post in posts:
            tags = tags | TranslationTagged.tags_for(EntryTranslation, post).order_by("name")
        for tag in tags:
            node = NavigationNode(
                tag.name,
                reverse(
                    'dragoman_blog_list_by_tag', kwargs={'tag': tag.slug}),
                tag.pk
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(BlogEntriesMenu)
