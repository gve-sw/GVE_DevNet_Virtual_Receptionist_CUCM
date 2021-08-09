# Copyright (c) 2020 Cisco and/or its affiliates.
#
# This software is licensed to you under the terms of the Cisco Sample
# Code License, Version 1.1 (the "License"). You may obtain a copy of the
# License at
#
#                https://developer.cisco.com/docs/licenses
#
# All use of the material herein must be in accordance with the terms of
# the License. All rights not expressly granted by the License are
# reserved. Unless required by applicable law or agreed to separately in
# writing, software distributed under the License is distributed on an "AS
# IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied.


import json


# Read guest list Json with list of invitations
def read_list():
    with open("guest_list.json", "r") as data:
        json_guest_list = json.loads(data.read())
    #print(json_guest_list)
    return json_guest_list


# Prepare a list of ONLY the invitation numbers:
def list_of_invitation_numbers(json_guest_list):
    list_of_invitations = []
    for guest in json_guest_list:
        # print(guest['invitation_id'])
        list_of_invitations.append(guest['invitation_id'])
    #print(f'This is the list on invitations: {list_of_invitations}')
    return list_of_invitations

print(read_list())
print(list_of_invitation_numbers(read_list()))

invitation='1111'
invitation='2222'
invitation='3333'
index = list_of_invitation_numbers(read_list()).index(invitation)
print(index)
