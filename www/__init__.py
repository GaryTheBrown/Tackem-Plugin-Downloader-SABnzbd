'''WEBUI FOR PLUGIN'''
import cherrypy
from libs.html_template import HTMLTEMPLATE
from system.plugin import TackemSystemPlugin

LAYOUT = {}
def mounts(key, instance_name=None):
    '''where the system creates the cherrypy mounts'''
    tackem_system = TackemSystemPlugin("downloader", "sabnzbd", instance_name)
    cherrypy.tree.mount(Root("SABnzbd Downloader", key, tackem_system),
                        tackem_system.baseurl + key.replace(" ", "/") + "/",
                        cfg(tackem_system.config()))

def cfg(config):
    '''generate the cherrypy conf'''
    return {}

class Root(HTMLTEMPLATE):
    '''ROOT OF PLUGINS WEBUI HERE'''
    @cherrypy.expose
    def index(self):
        '''index of plugin'''
        self._tackem_system.auth.check_auth()
        index_page = self._name.replace("_", " ").title() + " ROOT"
        return self._template(index_page)
