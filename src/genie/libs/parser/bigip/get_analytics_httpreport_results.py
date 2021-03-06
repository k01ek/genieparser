# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/http/report-results' resources
# =============================================


class AnalyticsHttpReportresultsSchema(MetaParser):

    schema = {}


class AnalyticsHttpReportresults(AnalyticsHttpReportresultsSchema):
    """ To F5 resource for /mgmt/tm/analytics/http/report-results
    """

    cli_command = "/mgmt/tm/analytics/http/report-results"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
