from ftw.upgrade import UpgradeStep


class RemoveUnnecessaryCssFilesFromCollectiveQuickupload(UpgradeStep):
    """Remove unnecessary css files from collective.quickupload.
    """

    def __call__(self):
        self.install_upgrade_profile()
