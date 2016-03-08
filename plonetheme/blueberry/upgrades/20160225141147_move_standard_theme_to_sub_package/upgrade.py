from ftw.upgrade import UpgradeStep


class MoveStandardThemeToSubPackage(UpgradeStep):
    """Move standard theme to sub package.
    """

    def __call__(self):
        self.install_upgrade_profile()
        self.setup_install_profile('profile-plonetheme.blueberry.standard:default')
