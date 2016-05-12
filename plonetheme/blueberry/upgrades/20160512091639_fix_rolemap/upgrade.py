from ftw.upgrade import UpgradeStep


class FixRolemap(UpgradeStep):
    """Fix rolemap.
    """

    def __call__(self):
        self.install_upgrade_profile()
