from ftw.upgrade import UpgradeStep


class RenameCustomizationForm(UpgradeStep):
    """Rename customization form.
    """

    def __call__(self):
        self.install_upgrade_profile()
