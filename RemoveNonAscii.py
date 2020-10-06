import sublime
import sublime_plugin
import unicodedata


class RemoveNonAsciiCharsFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        entire_view = sublime.Region(0, self.view.size())
        s = self.view.substr(entire_view)
        # Convert Vietnamese chars
        s = s.replace('đ', 'd').replace('Đ', 'D')
        # Remove non-ascii chars
        ascii_only = unicodedata.normalize(
            'NFKD', s).encode('ascii', 'ignore').decode('utf-8')
        self.view.replace(edit, entire_view, ascii_only)


class RemoveNonAsciiCharsSelecCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel_view = self.view.sel()
        for region in sel_view:
            if not region.empty():
                # Get the selected text
                s = self.view.substr(region)
                # Convert Vietnamese chars
                s = s.replace('đ', 'd').replace('Đ', 'D')
                # Remove non-ascii chars
                ascii_only = unicodedata.normalize(
                    'NFKD', s).encode('ascii', 'ignore').decode('utf-8')
                self.view.replace(edit, region, ascii_only)
