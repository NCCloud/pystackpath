# PyStackpath

Python library interact with StackPath API (https://developer.stackpath.com/en/)

It uses a custom OAuth2 requests.session

#Example
```python
from pystackpack import Stackpath
 
sp = Stackpath(
    os.getenv("STACKPATH_CLIENTID"),
    os.getenv("STACKPATH_APISECRET")
)

# search stacks
stacks = sp.stacks().index(filter="name='my-awesome-stack' and status='ACTIVE'")
print(stacks)

# get one stack
stackid = "afcdaf14-47cb-40dd-9c13-3b20e6caf74a
onestack = sd.stacks().get(stackid)

# create a new stack
accountid = "081af5ee-38f8-44e9-b08a-881ea5de66f9"
newstack = sp.stacks().create(accountid, "my-second-stack")

# create a cdn site
stackid = "afcdaf14-47cb-40dd-9c13-3b20e6caf74a
cdnsite = sd.stacks().get(stackid).cdnsites().create("cdn.johndoe.com", "www.johndoe.com")

# search for cdn sites
cdnsite = sd.stacks().get(stackid).cdnsites().index(filter="label='www.johndoe.com' and status='ACTIVE'")

# delete a cdn site
cdnsiteid = "19e1a7b2-068f-491c-a95f-b64eae66dd34"
cdnsite = sd.stacks().get(stackid).cdnsites().get(cdnsiteid).delete()
```