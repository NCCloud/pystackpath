import json
from pystackpath.util import BaseObject, api_time_format
from datetime import datetime as dt
from datetime import timedelta


ACCEPTED_GRANULARITY = ('AUTO', 'PT5M', 'PT1H', 'P1D', 'P1M')
ACCEPTED_GROUP_BY = (
    'NONE', 'SITE', 'PLATFORM', 'POP',
    'REGION', 'STATUS', 'STATUS_CATEGORY'
)
ACCEPTED_METRIC_TYPE = ('TRANSFER', 'STATUS_CODE')
DEFAULT_DELTA_TIME = 1  # day


class Metrics(BaseObject):

    def index(
        self,
        start_date=None,
        end_date=None,
        granularity=ACCEPTED_GRANULARITY[0],
        group_by=ACCEPTED_GROUP_BY[0],
        status_category=[],
        status_code=[],
        sites=[],
        billing_regions=[],
        pops=[],
        platforms=[],
        site_type_filter=[],
        metric_type=ACCEPTED_METRIC_TYPE[0]
    ):
        """
        Get all the Metrics.
        You can use the parameters to add options to your request.
        """

        params = dict()

        if end_date is None:
            end_date = dt.today()
        if start_date is None:
            start_date = end_date - timedelta(days=DEFAULT_DELTA_TIME)

        end_date_iso = api_time_format(end_date)
        start_date_iso = api_time_format(start_date)

        if start_date_iso > end_date_iso:
            raise ValueError(f"Search start date, \"{start_date_iso}\", is later than end date, \"{end_date_iso}\"!")        

        params['start_date'] = start_date_iso
        params['end_date'] = end_date_iso    

        if granularity not in ACCEPTED_GRANULARITY:
            raise ValueError(f"{granularity} is not a valid granularity value: {ACCEPTED_GRANULARITY}") 
        params['granularity'] = granularity

        if group_by not in ACCEPTED_GROUP_BY:
            raise ValueError(f"{group_by} is not a valid group_by value: {ACCEPTED_GROUP_BY}") 
        params['group_by'] = group_by

        if metric_type not in ACCEPTED_METRIC_TYPE:
            raise ValueError(f"{metric_type} is not a valid metric type: {ACCEPTED_METRIC_TYPE}") 
        params['metric_type'] = metric_type

        if status_category:
            params['status_category'] = Metrics._list_to_string(status_category)

        if status_code:
            params['status_code'] = Metrics._list_to_string(status_code)

        if sites:
            params['sites'] = Metrics._list_to_string(sites)

        if billing_regions:
            params['billing_regions'] = Metrics._list_to_string(billing_regions)

        if pops:
            params['pops'] = Metrics._list_to_string(pops)

        if platforms:
            params['platforms'] = Metrics._list_to_string(platforms)

        if site_type_filter:
            params['site_type_filter'] = Metrics._list_to_string(site_type_filter)              
        
        response = self._client.get(f"{self._base_api}/metrics", params=params)
        return self.loaddict(response.json())         


    @staticmethod
    def _list_to_string(items, separator=','):
        if not isinstance(items, list):
            raise ValueError(f"{items} is not a list")

        try:
            return separator.join(items)
        except Exception as e:
            raise ValueError(f"{items} is not valid data: {e}")