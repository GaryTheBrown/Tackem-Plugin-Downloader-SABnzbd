'''WEBUI FOR PLUGIN'''
import cherrypy
from libs.html_template import HTMLTEMPLATE

LAYOUT = {}
def mounts(key, systems, plugins, config, auth):
    '''where the system creates the cherrypy mounts'''
    cherrypy.tree.mount(Root("Sabnzbd", key, systems, plugins, config, auth),
                        config.get("webui", {}).get("baseurl", "/") + key.replace(" ", "/") + "/",
                        cfg(config))

def cfg(config):
    '''generate the cherrypy conf'''
    return {}

class Root(HTMLTEMPLATE):
    '''ROOT OF PLUGINS WEBUI HERE'''
    @cherrypy.expose
    def index(self):
        '''index of plugin'''
        self._auth.check_auth()
        index_page = self._name + " ROOT"
        return self._template(index_page)
