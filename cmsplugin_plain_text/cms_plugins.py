from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Plaintext


class PlaintextPlugin(CMSPluginBase):
    model = Plaintext
    render_template = 'cms/plugins/plaintext.html'

    def render(self, context, instance, placeholder):
        context['body'] = instance.body
        return context

plugin_pool.register_plugin(PlaintextPlugin)
