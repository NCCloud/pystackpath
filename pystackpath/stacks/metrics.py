from pystackpath.util import BaseObject, api_time_format
from datetime import datetime as dt
from datetime import timedelta


class Metrics(BaseObject):

    def get(self, start_date: dt = None, end_date: dt = None, granularity="AUTO",
            platforms=["CDE"], pops=[], billing_regions=[], sites=[], group_by="NONE", site_type_filter="ALL"):

        available_granularity_options = ["AUTO", "PT5M", "PT1H", "P1D", "P1M"]
        if granularity not in available_granularity_options:
            raise ValueError(f"{granularity} is not a valid granularity setting: {available_granularity_options}")

        if end_date is None:
            end_date = dt.today()
        if start_date is None:
            start_date = end_date - timedelta(days=1)

        start_date_iso = api_time_format(start_date)
        end_date_iso = api_time_format(end_date)

        if start_date > end_date:
            raise ValueError(f"Search start date, \"{start_date_iso}\", is later than end date, \"{end_date_iso}\"!")

        response = self._client.get(
            f"{self._base_api}/metrics",
            params={
                "start_date": start_date_iso,
                "end_date": end_date_iso,
                "granularity": granularity,
                "platforms": ','.join(platforms),
                "pops": ','.join(pops),
                "billing_regions": ','.join(billing_regions),
                "sites": ','.join(sites),
                "group_by": group_by,
                "site_type_filter": site_type_filter
            }
        )
        response.raise_for_status()

        return self.loaddict(response.json())
