# PyStackpath - StackPath Python Library
[![Actions Status](https://github.com/NCCloud/pystackpath/workflows/Upload%20Python%20Package/badge.svg)](https://github.com/NCCloud/pystackpath/actions)
[![Python Version](https://img.shields.io/pypi/pyversions/pystackpath)](https://pypi.org/project/pystackpath/)
[![Pypi license](https://img.shields.io/pypi/l/pystackpath)](https://pypi.org/project/pystackpath/)
[![GitHub stars](https://img.shields.io/badge/contributions-welcome-orange.svg)](https://github.com/NCCloud/pystackpath/blob/master/CONTRIBUTING.md)

Python library interact with StackPath API (https://stackpath.dev/reference)

It uses a custom OAuth2 requests.session

## Install

```bash
pip install pystackpath
```

## Examples

### Set up a new Stackpath instance
```python
from pystackpath import Stackpath

sp = Stackpath(
    os.getenv("STACKPATH_CLIENTID"),
    os.getenv("STACKPATH_APISECRET")
)
```

###  Search for stacks
```python
stacks = sp.stacks().index(filter="name='my-awesome-stack' and status='ACTIVE'")
print(stacks)
```

### Get one stack
```python
stackid = "afcdaf14-47cb-40dd-9c13-3b20e6caf74a
onestack = sp.stacks().get(stackid)
```

### Create a new stack
```python
accountid = "081af5ee-38f8-44e9-b08a-881ea5de66f9"
newstack = sp.stacks().create(accountid, "my-second-stack")
```

### Create a cdn site
```python
stackid = "afcdaf14-47cb-40dd-9c13-3b20e6caf74a
cdnsite = sp.stacks().get(stackid).cdnsites().create(
    domain="cdn.johndoe.com",
    origin={"hostname": "www.johndoe.com"},
    type="CDN"
)
```

### Search for cdn sites
```python
cdnsite = sp.stacks().get(stackid).cdnsites().index(
    filter="label='www.johndoe.com' and status='ACTIVE'"
)
```

### Delete a cdn site
```python
cdnsiteid = "19e1a7b2-068f-491c-a95f-b64eae66dd34"
cdnsite = sp.stacks().get(stackid).cdnsites().get(cdnsiteid).delete()
```

### Disable and enable a cdn site
```python
cdnsiteid = "19e1a7b2-068f-491c-a95f-b64eae66dd34"
cdnsite = sp.stacks().get(stackid).cdnsites().get(cdnsiteid).enable()
cdnsite = cdnsite.disable()
```

### Purge a cdn resource and check the purge status.
```python
purge_request_id = sp.stacks().get(stackid).purge(
    [
        {
            "url": "https://example.com/resource/", # required
            "recursive": True,
            "invalidateOnly": False,
            "purgeAllDynamic": False,
            "headers": [],
            "purgeSelector": [],
        }
    ]
)

## purge_status can be used to check the status of the requested purge.
## Progress is represented as a decimal between 0 and 1, correlating to a
## percentage.

progress = sp.stacks().get(stackid).purge_status(purge_request_id)
print(progress)
##>> 1
```

## Get metrics for a stack:
```python
metrics_response1 = sp.stacks().get(stackid).metrics().get()

## Python datetime objects can be used to specify a date range, and the call
## allows a granularity to be specified. If no values are provided, the search range
## defaults to the last 24 hours, with 1 day granularity. See API doc for options.
## https://developer.stackpath.com/en/api/cdn/#operation/GetMetrics
## There is also a "platforms" argument which takes an array of "platform" codes.
## However the dev guide linked below only lists "CDE" which tracks egress traffic, which is
## how Stackpath bills for CDN usage, and "CDO" which is ingest traffic from the
## origin host, but is not billed. Since "CDE" tracks billable usage, it is the
## default.
## https://developer.stackpath.com/docs/en/cdn/getting-stack-metrics/
from datetime import datetime, timedelta
end = datetime.today()
start = end - timedelta(days=7)
metrics_response2 = sp.stacks().get(stackid).metrics().get(granularity="PT1H",\
  platforms = ["CDO", "CDE"], start_datetime_object = start, end_datetime_object = end)
```

## Retrieve all certificates from a stack:
```python
certificate_response = sp.stacks().get(stackid).certificates()

 ##The object returned will have a 'results' attribute containing
 ##an array of the available certificates:
 first_certificate = certificate_response['results'][0]
 second_certificate = certificate_response['results'][1]
```

## Add, update and delete a certificate for a stack:
```python
##The cert and key are required, CA bundle is optional.
new_cert_response = sp.stacks().get(stackid).certificates().add(\
SERVER_CERTIFICATE_STRING, PRIVATE_KEY_STRING, CA_BUNDLE_STRING)
##The new cert ID can be retrieved from the returned object:
cert_id = new_cert_response.id

##To update a cert:
sp.stacks().get(stackid).certificates().update(cert_id, UPDATED_CERT_STRING, UPDATED_KEY_STRING)

##To delete a cert:
delete_cert_response = sp.stacks().get(stackid).certificates().delete(cert_id)
```
