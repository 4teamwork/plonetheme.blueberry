from ftw.upgrade import UpgradeStep


class Fix_customizeDesign_actionPermissionCheck(UpgradeStep):
    """Fix "customize design" action permission check.
    """

    def __call__(self):
        self.install_upgrade_profile()
