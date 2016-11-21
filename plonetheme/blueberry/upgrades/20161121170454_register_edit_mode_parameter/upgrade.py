from ftw.upgrade import UpgradeStep


class RegisterEditModeParameter(UpgradeStep):
    """Register edit mode parameter.
    """

    def __call__(self):
        self.install_upgrade_profile()
