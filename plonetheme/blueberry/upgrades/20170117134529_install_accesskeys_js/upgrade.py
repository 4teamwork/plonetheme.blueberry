from ftw.upgrade import UpgradeStep


class InstallAccesskeysJs(UpgradeStep):
    """Install accesskeys js.
    """

    def __call__(self):
        self.install_upgrade_profile()
