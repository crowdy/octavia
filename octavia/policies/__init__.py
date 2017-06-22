#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


import itertools

from octavia.policies import base
from octavia.policies import listener
from octavia.policies import loadbalancer
from octavia.policies import pool


def list_rules():
    return itertools.chain(
        base.list_rules(),
        loadbalancer.list_rules(),
        listener.list_rules(),
        pool.list_rules(),
    )
