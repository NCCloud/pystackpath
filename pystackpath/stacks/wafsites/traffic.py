import json
from pystackpath.util import BaseObject, api_time_format
from datetime import datetime as dt
from datetime import timedelta


ACCEPTED_RESOLUTIONS = ('HOURLY', 'MINUTELY')
DEFAULT_DELTA_TIME = 1  # day


class Traffic(BaseObject):

    def get(
        self,
        site_id=None,
        start_date=None,
        end_date=None,
        resolution=ACCEPTED_RESOLUTIONS[0]
    ):
        """
        Get Waf Traffic
        """

        params = dict()

        if site_id is None:
            params['site_id'] = site_id

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

        if resolution not in ACCEPTED_RESOLUTIONS:
            raise ValueError(f"{resolution} is not a valid resolution: {ACCEPTED_RESOLUTIONS}") 
        params['resolution'] = resolution          
        
        response = self._client.get(f"{self._base_api}/traffic", params=params)
        return self.loaddict(response.json())
