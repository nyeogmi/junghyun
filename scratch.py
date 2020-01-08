"""
from read import read_game
from solve import possible_solves

examine = lambda i: print(list(possible_solves(read_game(i))))

examine("B<8 B<4 B>5")
"""
from pluginbase import PluginBase
plugin_base = PluginBase(package="players")
plugin_source = plugin_base.make_plugin_source(searchpath=["./players/awful", "./players/heuristic"])

print(plugin_source.list_plugins())

from basics.game import play
print(play(
    plugin_source.load_plugin("random"),
    plugin_source.load_plugin("maxinfo"),
    loud=True,
))

