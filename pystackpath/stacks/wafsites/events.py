import json
from pystackpath.util import BaseObject, api_time_format
from datetime import datetime as dt
from datetime import timedelta


ACCEPTED_ACTIONS = (
    'ANY_ACTION', 'ALLOW_ACTION', 
    'BLOCK_ACTION', 'CAPTCHA_ACTION', 
    'HANDSHAKE_ACTION', 'MONITOR_ACTION'
)
ACCEPTED_RESULTS = ('ANY_RESULT', 'BLOCKED_RESULT')
ACCEPTED_SORT_BY = ('TIMESTAMP', 'COUNTRY', 'RULE_NAME')
ACCEPTED_SORT_ORDER = ('ASCENDING', 'DESCENDING')
DEFAULT_DELTA_TIME = 1  # day


class Events(BaseObject):

    def get(self, event_id):
        """
        Get an Event by its ID
        """
        response = self._client.get(f"{self._base_api}/events/{event_id}")
        return self.loaddict(response.json())

    def index(
        self,
        page_request_first=None,
        page_request_after=None,
        page_request_filter=None,
        page_request_sort_by=None,
        start_date=None,
        end_date=None,
        filter_action_value=ACCEPTED_ACTIONS[0],
        filter_result_value=ACCEPTED_RESULTS[0],
        filter_client_ip=None,
        filter_reference_id=None,
        sort_by=ACCEPTED_SORT_BY[0],
        sort_order=ACCEPTED_SORT_ORDER[0]
    ):
        """
        Get all the Events.
        You can use the parameters to add options to your request.
        """

        params = Events._common_params(start_date, end_date, filter_action_value, \
            filter_result_value, filter_client_ip, filter_reference_id)

        if page_request_first:
            params['page_request.first'] = page_request_first

        if page_request_after:
            params['page_request.after'] = page_request_after

        if page_request_filter:
            params['page_request.filter'] = page_request_filter

        if page_request_sort_by:
            params['page_request.sort_by'] = page_request_sort_by

        if sort_by not in ACCEPTED_SORT_BY:
            raise ValueError(f"{sort_by} is not a valid sort type: {ACCEPTED_SORT_BY}") 
        params['sort_by'] = sort_by            

        if sort_order not in ACCEPTED_SORT_ORDER:
            raise ValueError(f"{sort_order} is not a valid sort type: {ACCEPTED_SORT_ORDER}") 
        params['sort_order'] = sort_order 
        
        response = self._client.get(f"{self._base_api}/events", params=params)
        return self.loaddict(response.json())      


    def get_event_statistics(
        self, 
        start_date=None, 
        end_date=None,
        filter_action_value=ACCEPTED_ACTIONS[0],
        filter_result_value=ACCEPTED_RESULTS[0],
        filter_client_ip=None,
        filter_reference_id=None
    ):
        """
        Get WAF Event statistics
        You can use the parameters to add options to your request.
        """          
        params = Events._common_params(start_date, end_date, filter_action_value, \
            filter_result_value, filter_client_ip, filter_reference_id)
        response = self._client.get(f"{self._base_api}/event_stats", params=params)
        return self.loaddict(response.json())


    @staticmethod
    def _common_params(
        start_date, 
        end_date,
        filter_action_value,
        filter_result_value,
        filter_client_ip,
        filter_reference_id
    ):
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

        if filter_action_value not in ACCEPTED_ACTIONS:
            raise ValueError(f"{filter_action_value} is not a valid action filter: {ACCEPTED_ACTIONS}") 
        params['filter.action_value'] = filter_action_value

        if filter_result_value not in ACCEPTED_RESULTS:
            raise ValueError(f"{filter_result_value} is not a valid action filter: {ACCEPTED_RESULTS}") 
        params['filter.result_value'] = filter_result_value    

        if filter_client_ip:
            params['filter.client_ip'] = filter_client_ip

        if filter_reference_id:
            params['filter.reference_id'] = filter_reference_id

        return params