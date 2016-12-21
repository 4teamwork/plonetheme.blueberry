from ftw.upgrade import UpgradeStep


class RemoveDefaultDatagridStyling(UpgradeStep):
    """Remove default datagrid styling.
    """

    def __call__(self):
        self.install_upgrade_profile()
