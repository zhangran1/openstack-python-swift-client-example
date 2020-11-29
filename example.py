from keystoneauth1 import session
from keystoneauth1.identity import v3
import swiftclient.client

_auth_url = 'openstack_v3_auth_url'
_user = 'change_it'
_key = 'change_it'

# for je tpo trial project
# PROJECT_NAME = 'Testing'
# OS_PROJECT_NAME = "Testing"
# OS_USER_DOMAIN_NAME = "trial"

PROJECT_NAME = 'change_it'
OS_PROJECT_NAME = "change_it"
OS_USER_DOMAIN_NAME = "change_it"

auth = v3.Password(auth_url=_auth_url,
                   username=_user,
                   password=_key,
                   user_domain_name=OS_USER_DOMAIN_NAME,
                   project_name=PROJECT_NAME,
                   project_domain_name=OS_USER_DOMAIN_NAME)

keystone_session = session.Session(auth=auth)

# establish connection
swift_conn = swiftclient.Connection(session=keystone_session)

# create new container
container = 'new-container'
swift_conn.put_container(container)

resp_headers, containers = swift_conn.get_account()

for container in containers:
    print container
