#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Kendell Fabricius
# Copyright (c) 2014 Kendell Fabricius
#
# License: MIT
#

"""This module exports the G++ plugin class."""

from SublimeLinter.lint import Linter, util
import sublime


class GPP(Linter):

    """Provides an interface to g++."""

    """
        g++:
            trial.cpp: In function ‘int main()’:
            trial.cpp:21:5: error: expected ‘;’ before ‘light’
                light.turnLightOff();q

        clang:
            <stdin>:1:10: fatal error: 'iostream' file not found
     """

    syntax = 'c++'
    # cmd = 'g++'
    executable = 'g++'
    regex = (
        r':(?P<line>\d+):(?P<col>\d+): (?:(?P<error>(error|fatal error))|(?P<warning>warning)): (?P<message>.+)'
    )
    multiline = True
    line_col_base = (1, 1)
    tempfile_suffix = ""
    error_stream = util.STREAM_BOTH
    selectors = {}
    word_re = None
    defaults = {}
    inline_settings = None
    inline_overrides = None
    comment_re = None

    def cmd(self):
        print("Running g++")
        window = sublime.active_window()
        view = window.active_view()
        print(view.file_name())
        return "g++ -fsyntax-only -Wall -x c++ -"