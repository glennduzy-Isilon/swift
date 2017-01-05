import logging
import pprint
import swiftclient

from swiftclient.service import SwiftService

from sys import argv

logging.basicConfig(level=logging.ERROR)
logging.getLogger("requests").setLevel(logging.CRITICAL)
logging.getLogger("swiftclient").setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)

user = "swiftacct:root"
key = "a"
conn = swiftclient.Connection(
    user=user,
    key=key,
    authurl='http://10.111.158.211:28080/auth/v1.0',
)

print "List out swift capabilities"
data = conn.get_capabilities()['swift']
for caps in data:
    print caps+'='+str(data[caps])
print 

print "-------------- Container Contents ------------------"
for container in conn.get_account()[1]:
    print "Container = "+container['name']
    for data in conn.get_container(container['name'])[1]:
        print '{0}\t{1}\t{2}'.format(data['name'], data['bytes'], data['last_modified'])
        obj_tuple = conn.get_object(container['name'], data['name'])
        #print obj_tuple
        print obj_tuple[1]
        print
    print
