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

from typing import List  # noqa: F401

from libqtile import qtile, bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

import os
import subprocess

mod = "mod4"
# terminal = guess_terminal()
terminal = "alacritty"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "c", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),

    # Sound 
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -c 0 sset Master 1- unmute")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -c 0 sset Master 1+ unmute")),

    # Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),

    # Applications
    Key([mod], "d", lazy.spawn("/usr/bin/dmenu_run -fn 'Droid Sans Mono-14'"), desc="Launch Dmenu"),
    Key([mod], "w", lazy.spawn("google-chrome-stable"), desc="Launch Chrome"),
    Key([mod, "shift"], "w", lazy.spawn("firefox"), desc="Launch Firefox"),
    Key([mod], "v", lazy.spawn("vivaldi-stable"), desc="Launch Vivaldi"),
    Key([mod], "t", lazy.spawn("subl "), desc="Launch Sublime Text"),
    Key([mod], "f", lazy.spawn("nautilus"), desc="Launch File Manager"),
    Key([mod], "m", lazy.spawn("lollypop"), desc="Launch Lollypop"),
    Key([mod], 'space', lazy.spawn('rofi -combi-modi drun,window -show combi -icon-theme "Papirus" -show-icons'), desc="Launch Rofi"),
    Key([mod], "r", lazy.spawn("rstudio-bin"), desc="Launch RStudio"),
    # Key([mod], "z", lazy.spawn("zettlr"), desc="Launch Zettlr"),
    Key([mod, "shift"], "t", lazy.spawn("marktext"), desc="Launch Mark Text"),
  ]

# groups = [Group(i) for i in "123456789"]
#
# for i in groups:
#    keys.extend([
#       # mod1 + number of group = switch to group
#        Key([mod], i.name, lazy.group[i.name].toscreen(),
#            desc="Switch to group {}".format(i.name)),
#
#        # mod1 + shift + number of group = switch to & move focused window to group
#        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#            desc="Switch to & move focused window to group {}".format(i.name)),
#        # Or, use below if you prefer not to switch to that group.
#        # # mod1 + shift + number of group = move focused window to group
#        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#        #     desc="move focused window to group {}".format(i.name)),
#    ])


#groups = [Group(i) for i in [
#    "1:", "2:", "3:", "4:", "5:", "6:", "7:", "8:"
#]]Key([mod, "shift"], "w", lazy.spawn("firefox"), desc="Launch Firefox"),


#for i, group in enumerate(groups):
#    actual_key = str(i + 1)
#    keys.extend([
#        # Switch to workspace N
#        Key([mod], actual_key, lazy.group[group.name].toscreen()),
#        # Send window to workspace N
#        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
#    ])


### Workspaces
groups = [
    Group(name="1", label="  ", layout="monadtall",
        matches=[
            Match(wm_class="tilix"),
            Match(wm_class="Alacritty"),
            Match(wm_class="Termite"),
            Match(wm_class="Xfce4-terminal"),
        ]),
    Group(name="2", label="  ", layout="monadtall",
        matches=[
            Match(wm_class="google-chrome-stable"),
            Match(wm_class="firefox"),
            Match(wm_class="Vivaldi-stable"),
        ]),
    Group(name="3", label="  ", layout="monadtall",
        matches=[
            Match(wm_class="Org.gnome.Nautilus"),
        ]),
    Group(name="4", label="  ", layout="monadtall",
        matches=[
            Match(wm_class="Lollypop"),
            Match(wm_class="Audacious"),
            Match(wm_class="Io.github.celluloid_player.Celluloid"),
        ]),
    Group(name="5", label="  ", layout="monadtall",
        matches=[
            Match(wm_class="Sublime_text"), 
        ]),
    Group(name="6", label="  ", layout="monadtall",
        matches=[
            Match(wm_class="RStudio"),
        ]),
    Group(name="7", label="  ", layout="monadtall",
        matches=[
            Match(wm_class="Typora"),
            Match(wm_class="zettlr"),
            Match(wm_class="marktext"),
        ]),
    Group(name="8", label="  ", layout="monadtall",
        matches=[
            Match(wm_class="Lxappearance"),
        ]),
]

for group in groups:
    keys.extend([
        # Switch to workspace
        Key([mod], group.name, lazy.group[group.name].toscreen(),
            desc="Switch to workspace '{}'".format(group.name)),
        # Switch to and move focused window to workspace
        Key([mod, "shift"], group.name,
            lazy.window.togroup(group.name, switch_group=True),
            desc="Move window to workspace {}".format(group.name)),
    ])


layouts = [
    layout.Bsp(margin=3, border_width=3, border_focus='#B31B32'),
    layout.MonadTall(margin=3, border_width=3, border_focus='#B31B32'),
    layout.Columns(margin=3, border_width=3, border_focus='#B31B32'),
    layout.Max(),
    layout.RatioTile(margin=3, border_width=3, border_focus='#B31B32'),
    layout.Floating(margin=3, border_width=3, border_focus='#B31B32'),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(margin=3, num_stacks=2),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    #font='Droid Sans Mono for powerline',
    #font='Ubuntu Mono',
    #font='MesloLGS NF',
    #font='Iosevka Nerd Font Regular',
    font='font awesome',
    fontsize=14,
    padding=5,
)
extension_defaults = widget_defaults.copy()

colors = [["#000000", "#000000"], # colors[0] Black
          ["#FFFFFF", "#FFFFFF"], # colors[1] White
          ["#e64344", "#e64344"], # colors[2] Imperial Red
          ["#225f4d", "#225f4d"], # colors[3] Castleton Green
          ["#64734c", "#64734c"], # colors[4] Dark Olive Green
          ["#b6d369", "#b6d369"], # colors[5] June Bud
          ["#93c48b", "#93c48b"], # colors[6] Dark Sea Green
          ["#59406B", "#59406B"], # colors[7] Violet
          ["#6B9D34", "#6B9D34"], # colors[8] Green
          ["#C8632F", "#C8632F"], # colors[9] Orange
          ["#B31B32", "#B31B32"], # colors[10] Red
          ["#E3D637", "#E3D637"], # colors[11] Yellow
          ["#6CA3BC", "#6CA3BC"], # colors[12] Light Blue
          ["#1184E8", "#1184E8"]] # colors[13] Sky Blue

screens = [
    Screen(
        top=bar.Bar(
            [
                # widget.QuickExit(
                #    default_text='  ',
                #    countdown_format=' {} b',
                #    background=colors[10],
                # ),

                widget.TextBox(
                    text="  ",
                    background=colors[10],
                    padding=5,
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("./.config/rofi/qtilepowermenu.sh")},
                ),

                widget.TextBox(
                    text="\uE0BC",
                    fonts="droid sans mono for powerline",
                    foreground=colors[10],
                    background=colors[9],
                    padding=0,
                    fontsize=24
                ),

                widget.GroupBox(
                    padding=2,
                    this_current_screen_border="#FFFFFF",
                    borderwidth=2,
                    rounded=False,
                    background=colors[9]
                ),

                widget.TextBox(
                    text="\uE0BC",
                    fonts="droid sans mono for powerline",
                    foreground=colors[9],
                    background=colors[3],
                    padding=0,
                    fontsize=24
                ),

                widget.Prompt(background=colors[3]),

                # widget.TaskList(
                #    background=colors[4],
                #    rounded=False,
                #),

                widget.WindowName(
                    padding=5,
                    background=colors[3]
                ),

                # widget.Chord(
                #    chords_colors={
                #        'launch': ("#ff0000", "#ffffff"),
                #    },
                #    name_transform=lambda name: name.upper(),
                #),

                widget.TextBox(
                    text="\uE0BC",
                    fonts="droid sans mono for powerline",
                    foreground=colors[3],
                    background=colors[8],
                    padding=0,
                    fontsize=24
                ),

                widget.CurrentLayoutIcon(
                    padding=0,
                    background=colors[8],
                    scale=0.6
                ),

                widget.CurrentLayout(
                    padding=5,
                    background=colors[8]
                ),

                widget.TextBox(
                    text="\uE0BC",
                    fonts="droid sans mono for powerline",
                    foreground=colors[8],
                    background=colors[12],
                    padding=0,
                    fontsize=24
                ),

                widget.TextBox(
                    " Man Cave",
                    padding=5,
                    name="default",
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e bashtop')},
                    background=colors[12]
                ),

               # widget.Net(interface="wlan0", format = '{down} ↓↑ {up}', padding=5, background=colors[2]),
               # widget.CPU(format='CPU {freq_current} GHz  {load_percent}%', padding=5, background=colors[2]),

               widget.TextBox(
                    text="\uE0BC",
                    fonts="droid sans mono for powerline",
                    foreground=colors[12],
                    background=colors[11],
                    padding=0,
                    fontsize=24
                ),

                widget.Volume(
                    fmt=" {}",
                    padding=5,
                    background=colors[11]
                ),

               # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d76f7d"),

               widget.TextBox(
                    text="\uE0BC",
                    fonts="droid sans mono for powerline",
                    foreground=colors[11],
                    background=colors[13],
                    padding=0,
                    fontsize=24
                ),

                widget.Wttr(
                    location={'Melbourne': 'Melbourne'},
                    format='%m %c %t',
                    units='m',
                    update_interval=300,
                    #json=False,
                    padding=5,
                    background=colors[13],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e curl wttr.in')},
                ),

                widget.TextBox(
                    text="\uE0BC",
                    fonts="droid sans mono for powerline",
                    foreground=colors[13],
                    background=colors[7],
                    padding=0,
                    fontsize=24
                ),

                widget.Clock(
                    format=' %a %d %b %Y',
                    padding=5,
                    background=colors[7],
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e cal -y')},
                ),

                widget.TextBox(
                    text="\uE0BC",
                    fonts="droid sans mono for powerline",
                    foreground=colors[7],
                    background=colors[9],
                    padding=0,
                    fontsize=24
                ),

                widget.Clock(
                    format=' %H:%M',
                    padding=5,
                    background=colors[9],
                ),

                # widget.Wlan(format='{percent:2.0%}'),

                widget.TextBox(
                    text="\uE0BC",
                    fonts="droid sans mono for powerline",
                    foreground=colors[9],
                    background=colors[10],
                    padding=0,
                    fontsize=24
                ),

                widget.CheckUpdates(
                    distro='Arch_checkupdates',
                    display_format=' {updates}',
                    no_update_string='',
                    mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' --hold -e yay -Syu')},
                    padding=5,
                    background=colors[10]
                ),

                widget.Systray(
                    background=colors[10],
                    padding=5
                ),

                widget.TextBox(
                    text=" ",
                    background=colors[10],
                    padding=0,
                ),
            ],
            24, margin=[3, 3, 0, 3],  # [top, right, bottom, left]
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='Io.github.celluloid_player.Celluloid'), #Celluloid music player
    Match(wm_class='feh'), #feh image viewer
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "focus"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh') # path to my script, under my user directory
    subprocess.call([home])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
# wmname = "LG3D"
wmname = "Qtile"
