# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/daemon-log-settings/csyncd' resources
# =============================================


class SysDaemonlogsettingsCsyncdSchema(MetaParser):

    schema = {}


class SysDaemonlogsettingsCsyncd(SysDaemonlogsettingsCsyncdSchema):
    """ To F5 resource for /mgmt/tm/sys/daemon-log-settings/csyncd
    """

    cli_command = "/mgmt/tm/sys/daemon-log-settings/csyncd"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
