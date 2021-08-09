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

from flask import Flask, render_template, request, session, redirect, url_for, jsonify, make_response, flash
import json


app = Flask(__name__)
app.config['SECRET_KEY'] = 'flash_message'

# Script started
print('APPLICATION START - VIRTUAL RECEPTIONIST')


# Read JSON Guest list (guest_list.json) and return the JSON information as a python dictionary
def read_list():
    with open("guest_list.json", "r") as data:
        json_guest_list = json.loads(data.read())
    # print(json_guest_list)
    return json_guest_list


# Prepare a list of ONLY the invitation numbers:
def list_of_invitation_numbers(json_guest_list):
    list_of_invitations = []
    for guest in json_guest_list:
        # print(guest['invitation_id'])
        list_of_invitations.append(guest['invitation_id'])
    print(f'This is the list on invitations: {list_of_invitations}')
    return list_of_invitations


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        # Gets the invitation number from the form (ex: 1111)
        invitation = request.form.get('invitation_id')
        print(f'This is the invitation number obtained from the FORM (input from guest): {invitation}')
        try:
            # STEP 1:
            # Get the list of INVITATION Numbers ONLY to determine the index (position of the invitation in the dict)
            list_of_invitations = list_of_invitation_numbers(read_list())
            print(f'This is the current list of invitations: {list_of_invitations}')

            # STEP 2:
            # Get the index of the invitation obtained from the FORM to search the json list of invitations
            # in order to get name, host and extension to dial
            index = list_of_invitation_numbers(read_list()).index(invitation)
            print(f'This is the index of the invitation obtained from the form: INDEX = {index}')

            # STEP 3:
            # Get the whole list of invitations from the json file:
            json_guest_list_int = read_list()
            print(f'There are {len(json_guest_list_int)} invitations in total.')
            print(f'This the the FULL List of invitations: \n {json_guest_list_int}')

            # STEP 4
            # With index, parse the list of invitations to get the corresponding name, visiting and number values
            invitation_id = json_guest_list_int[index]['invitation_id']  # NOT USED
            name = json_guest_list_int[index]['name']
            host = json_guest_list_int[index]['host']
            extension_to_dial = json_guest_list_int[index]['extension_to_dial']
            # Make sure the information parsed is correct - and pass name and host to print route:
            print(f'The obtained information is: Name:{name}, Host:{host}, Extension:{extension_to_dial}')
            session['name'] = name
            session['host'] = host

            # STEP 5:
            # If the invitation is in the list, the guest can proceed to dial - RENDERS THE DIAL TEMPLATE with values
            if invitation in list_of_invitations:
                return render_template('dial.html', name=name, host=host, extension_to_dial=extension_to_dial)
            else:
                print('HELLO THERE')
                return render_template('guest_not_found.html')
                # return redirect(url_for(guest_not_found))
        # If the invitation is not in the list, catch the Value Error, alert and redirect to page
        except ValueError:
            print("Guest not found - RETURNING VALUE ERROR")
            return render_template('guest_not_found.html')
    else:
        return render_template('login.html')


@app.route('/admin', methods=["GET", "POST"])
def admin():
    if request.method == "POST":
        # Get information of the new invitation from the web form
        invitation_id = request.form.get('invitation_id')
        name = request.form.get('name')
        host = request.form.get('host')
        extension_to_dial = int(request.form.get('extension_to_dial'))
        # Validate if invitation is in list of invitations - THIS HAS TO BE ADDED
        list_of_invitations = list_of_invitation_numbers(read_list())
        if invitation_id not in list_of_invitations:
            new_input = [{"invitation_id": invitation_id, "name": name, "host": host, "extension_to_dial": extension_to_dial}]
            print(f'New Invitation Created: {new_input}')

            # Add new Invitation
            json_guest_list_int = read_list()
            new_list = json_guest_list_int + new_input
            print(f'This is the new FULL dictionary of invitations: {new_list}')
            with open("guest_list.json", "w") as invite:
                json.dump(new_list, invite, indent=2)
                invite.close()
            # Display alert that data has been added and return admin form again
            ### Update with tkinter - https://stackoverflow.com/questions/177287/alert-boxes-in-python
            flash('Invitation Created')
            return render_template('admin.html')
        else:
            flash(f'Invitation {invitation_id} is already in the list, please try a different number')
            return render_template('admin.html')
    else:
        return render_template('admin.html')


@app.route('/print_id')
def print_id():
    # TO DO: ADD CODE TO GET THE NAME AND HOST
    name = session.get('name')
    host = session.get('host')
    return render_template('print_id.html', name=name, host=host)


if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)