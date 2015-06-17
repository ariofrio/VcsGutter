import sublime, sublime_plugin

# TODO: Make this more general and/or configurable.

class CycleVcsOrders(sublime_plugin.WindowCommand):
    def run(self):
        setts = sublime.load_settings('VcsGutter.sublime-settings')
        vcs_order = setts.get('vcs_order')
        vcs_orders = (["git", "svn"], ["svn", "git"])

        if vcs_order == vcs_orders[0]:
            vcs_order = vcs_orders[1]
        else:
            vcs_order = vcs_orders[0]

        setts.set('vcs_order', vcs_order)
        sublime.save_settings('VcsGutter.sublime-settings')

        self.window.run_command("vcs_gutter_reload")
