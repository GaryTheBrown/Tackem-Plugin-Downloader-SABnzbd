'''sabnzbd controller init'''
from glob import glob
import sys
from configobj import ConfigObj
from validate import Validator
from libs.plugin_base import PluginBaseClass, load_plugin_settings
from libs.config.list import ConfigList
from libs.config.obj.boolean import ConfigObjBoolean
from libs.config.obj.string import ConfigObjString
from libs.config.obj.integer_number import ConfigObjIntegerNumber
from libs.config.obj.data.input_attributes import InputAttributes
from libs.startup_arguments import PLUGINFOLDERLOCATION
from . import www

SETTINGS = load_plugin_settings(PLUGINFOLDERLOCATION + "downloader/sabnzbd/settings.json")

CONFIG = ConfigList(
    "sabnzbd",
    "SABnzbd",
    ConfigObjBoolean(
        "enabled",
        False,
        "Enabled",
        ""
    ),
    ConfigObjString(
        "downloadlocation",
        "downloads/",
        "Download Location",
        "Where is the completed download location?"
    ),

    ConfigObjSting(
        "host",
        "localhost",
        "Host Location",
        "Where is the sabnzbd website?"
    ),
    ConfigObjIntegerNumber(
        "port",
        8080,
        "Host Port",
        "The Port where the host is located"),
        input_attributes=InputAttributes(
            min=1001,
            max=65535
        )
    )
)


class Plugin(PluginBaseClass):
    '''Main Class to create an instance of the plugin'''

    def startup(self):
        '''Startup Script'''
        self._running = True
        return True, ""

    def shutdown(self):
        '''stop the plugin'''
        self._running = False
