import sublime
import sublime_plugin


class fecsCheckCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filepath = self.view.file_name()
        packages = sublime.packages_path()
        args = {
            "cmd": [
                "fecs",
                filepath,
                "--reporter=baidu",
                "--rule"
            ],
            "file_regex": r"fecs: (.+)\]",
            "line_regex": r"(\d+),(\d+): (.*)$"
        }

        if sublime.platform() == "windows":
            args['cmd'][0] += ".cmd"
        elif sublime.platform() == "osx":
            args['path'] = "/usr/local/share/npm/bin:/usr/local/bin:/opt/local/bin"

        self.view.window().run_command('exec', args)


class fecsFormatCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filepath = self.view.file_name()
        packages = sublime.packages_path()
        args = {
            "cmd": [
                "fecs",
                "format",
                filepath,
                "--replace"
            ],
            "file_regex": r"fecs: (.+)\]",
            "line_regex": r"(\d+),(\d+): (.*)$"
        }

        if sublime.platform() == "windows":
            args['cmd'][0] += ".cmd"
        elif sublime.platform() == "osx":
            args['path'] = "/usr/local/share/npm/bin:/usr/local/bin:/opt/local/bin"

        self.view.window().run_command('exec', args)
