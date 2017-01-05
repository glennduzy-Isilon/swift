import logging
import pprint
import swiftclient

from swiftclient.service import SwiftService

from sys import argv

logging.basicConfig(level=logging.ERROR)
logging.getLogger("requests").setLevel(logging.CRITICAL)
logging.getLogger("swiftclient").setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)

user = "root"
key = "a"
conn = swiftclient.Connection(
    user=user,
    key=key,
    authurl='http://10.111.158.211:28080/v1/AUTH_swiftacct',
    auth_version="1",
    tenant_name="swiftacct",
)
print conn

mylist = SwiftService.list
print mylist

_opts = {}
with SwiftService(options=_opts) as swift:
    container = argv[1]
    objects = argv[2:]
    header_data = {}
    stats_it = swift.stat(container=container, objects=objects)
    pprint.pprint(stats_it)

    for stat_res in stats_it:
        if stat_res['success']:
            header_data[stat_res['object']] = stat_res['headers']
        else:
            logger.error(
                'Failed to retrieve stats for %s' % stat_res['object']
            )
    pprint.pprint(header_data)
