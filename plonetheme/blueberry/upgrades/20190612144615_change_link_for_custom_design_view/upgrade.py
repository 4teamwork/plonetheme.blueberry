from ftw.upgrade import UpgradeStep


class ChangeLinkForCustomDesignView(UpgradeStep):
    """Change link for custom design view.
    """

    def __call__(self):
        self.install_upgrade_profile()
