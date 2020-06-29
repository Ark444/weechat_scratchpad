#!/usr/bin/env python
# -*- coding: utf-8 -*-

SCRIPT_NAME    = "scratchpad"
SCRIPT_AUTHOR  = "eq"
SCRIPT_VERSION = "0.0.1"
SCRIPT_LICENSE = "MIT"
SCRIPT_DESC    = "opens a scratchpad buffer"
SCRIPT_COMMAND = "scratchpad"

try:
    import weechat
except:
    print("This script must be run under WeeChat.")
    print("Get WeeChat now at: http://www.weechat.org/")
    quit()

weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, "", "")

is_scratchpad_open = False

def scratchpad_input_cb(data, buff, args):
    weechat.prnt(buff, args)
    return weechat.WEECHAT_RC_OK

def scratchpad_close_cb(data, buff):
    global is_scratchpad_open
    try:
        weechat.buffer_close("scratchpad")
    except:
        weechat.prnt("", "Error: can not close scratchpad")
    is_scratchpad_open = False
    return weechat.WEECHAT_RC_OK

def scratchpad_open():
    global is_scratchpad_open

    if not is_scratchpad_open:
        try:
            scratchpad = weechat.buffer_new("scratchpad", "scratchpad_input_cb", "", "scratchpad_close_cb", "")
            weechat.buffer_set(scratchpad, "title", "Scratchpad buffer.")
        except:
            weechat.prnt("", "Error: can not open scratchpad")
            return weechat.WEECHAT_RC_ERROR
        is_scratchpad_open = True
    weechat.command("", "/buffer scratchpad")
    return weechat.WEECHAT_RC_OK

def scratchpad_cb(data, buff, args):
    return scratchpad_open()

hook = weechat.hook_command("scratchpad",
        "A buffer where you can write what you like, so you don't forget about it.",
        "", "", "", "scratchpad_cb", "")

