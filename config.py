# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import os
import subprocess
import re
import socket
from libqtile import qtile
from libqtile import hook
from libqtile import bar, layout, widget
from libqtile.command import lazy
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from typing import List
from libqtile.utils import guess_terminal
mod = "mod4"
terminal = guess_terminal()
colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]
barSize=24
fuente= "Ubuntu Mono Nerd Font"
tamanoFuente = 16
barColor = colors[0]
myTerm = "alacritty" 
color_light = "#ff8855"

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Volume and Backlight keys
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+ unmute")),
    Key([], "XF86AudioMute", lazy.spawn("amixer set Master togglemute")),
    Key([], "XF86AudioMicMute", lazy.spawn("amixer set Capture togglemute")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("xbacklight -5")),
    Key([], "XF86MonBrightnessUp", lazy.spawn("xbacklight +5")),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),
    #Tecla para menu rofi
    Key([mod],"m", lazy.spawn("rofi -show drun"),desc="Launch menu"),
    #abrir navegador
    Key([mod],"f", lazy.spawn("brave"),desc="open brave"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]



groups = [Group("  ", layout='monadtall'),
          Group("  ", layout='monadtall'),
          Group("  ", layout='monadtall'),
          Group("  ", layout='monadtall'),
          Group("  ", layout='monadtall'),
          Group("  ", layout='monadtall'),
          Group("  ", layout='monadtall'),
          Group("  ", layout='monadtall'),
          ]


for i, group in enumerate(groups):
    numeroEscritorio=str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                numeroEscritorio,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                numeroEscritorio,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )



layouts = [
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        border_normal="#222222",
        border_focus="#4a66c2",
        border_width=3,
        single_border_width=0,
        margin=9,
        single_margin=0,
        ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font=fuente,
    fontsize=tamanoFuente,
    padding=3,
)
extension_defaults = widget_defaults.copy()

#CALLBACKS
def open_pavu(qtile):
    qtile.cmd_spawn("pavucontrol")

def open_calendar(qtile):  # spawn calendar widget
    qtile.cmd_spawn('gsimplecal')

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Sep(
                       linewidth = 0,
                       padding = 6,
                       foreground = colors[2],
                       background = colors[0]
                       ),

                widget.GroupBox(
                       font = "Ubuntu Bold",
                       fontsize = 37,
                       margin_y = 3,
                       margin_x = 0,
                       padding_y = 5,
                       padding_x = 3,
                       borderwidth = 3,
                       active = colors[2],
                       inactive = "#1597ed",
                       rounded = False,
                       highlight_color = colors[1],
                       highlight_method = "line",
                       this_current_screen_border = colors[6],
                       this_screen_border = colors [4],
                       other_current_screen_border = colors[6],
                       other_screen_border = colors[4],
                       foreground = colors[2],
                       background = colors[0]
                       ),
                widget.Prompt(),
                widget.WindowName(foreground="#1597ed"),
                
                
                
                widget.Memory(
                    background = "#56bff0",
                    foreground = "#0a0500",
                    fmt = '{}',
                    mouse_callbacks={'Button1': open_pavu}               
                    ),
                widget.Sep(
                    linewidth = 6,
                    foreground = barColor
                ),
                widget.CPU(
                    background = "#ed9c4a",
                    foreground = "#000000",
                    padding = 5,
                    fmt = '{},',
                ),
                
                widget.ThermalSensor(
                    background = "#ed9c4a",
                    foreground = "#000000",
                    fmt = ': {}'
                ),
                widget.Sep(
                    linewidth = 6,
                    foreground = barColor
                ),
                widget.Clock(
                    format=' %Y-%m-%d %a,  %I:%M %p', 
                    padding=10,
                    background = colors[4],
                    foreground = "#0a0500",
                    mouse_callbacks={'Button1': open_calendar}
                ),
                widget.Sep(
                    linewidth = 6,
                    foreground = barColor
                ),
                widget.Systray(
                    background = "#b364e8",
                    icon_size = 20,
                ),
               
                widget.Volume(
                   foreground = "#000000",
                   background = "#b364e8", 
                   fmt = '墳 :{}'
                ),
                widget.Sep(
                    linewidth = 6,
                    foreground = barColor
                ),
                widget.QuickExit(
                    default_text="Salir",
                    foreground=color_light,
                    countdown_format="[ {} ]"
                ),
                

            ],
            barSize,
            background=colors[0],

        ),
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
        home = os.path.expanduser('~')
        subprocess.Popen([home + '/.config/qtile/autostart.sh'])
