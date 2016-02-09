from ftw.upgrade import UpgradeStep


class ExcludeAutocompleteIfThemeIsActive(UpgradeStep):
    """Exclude autocomplete if theme is active.
    """

    def __call__(self):
        self.install_upgrade_profile()
