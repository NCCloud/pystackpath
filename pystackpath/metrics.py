from .util import BaseObject, PageInfo, pagination_query, api_time_format
from datetime import datetime as dt
from datetime import timedelta


class Metrics(BaseObject):

    def get(self, granularity="P1D", start_datetime_object=None, end_datetime_object=None, platforms=["CDE"]):
        available_granularity_options = ["PT5M", "PT1H", "P1D", "P1M"]
        if not granularity in available_granularity_options:
            raise ValueError(f"{granularity} is not a valid granularity setting: {available_granularity_options}")

        if not end_datetime_object:
            end_datetime_object = dt.today()

        if not start_datetime_object:
            start_datetime_object = end_datetime_object - timedelta(days=1)

        start_date_iso = api_time_format(start_datetime_object)
        end_date_iso = api_time_format(end_datetime_object)

        if start_datetime_object > end_datetime_object:
            raise ValueError(f"Search start date, \"{start_date_iso}\", is later than end date, \"{end_date_iso}\"!")

        platforms_string = ','.join(platforms)
        response = self._client.get(f"/cdn/v1/stacks/{self._parent_id}/metrics?start_date={start_date_iso}&end_date={end_date_iso}&platforms={platforms_string}&granularity={granularity}")
        response.raise_for_status()

        return self.loaddict(response.json())
