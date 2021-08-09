# GVE_DevNet_Virtual_Receptionist_CUCM
Virtual Receptionist for Cisco Deskpro/Webex Board (or Kiosk using the Webex Teams client) that enables a user to login,
print a tag and call using the video device. 


## Contacts
* Maxime Acquatella

## Solution Components
* Cisco Telephony (CUCM or Webex Calling)
*  Python
*  Flask
*  Javascript

## Requirements

A dialing endpoint (can be a Cisco Webex Deskpro, a Webex Board or Webex Teams running on a PC - as a Kiosk). There should also be a reachable phone number destination for the called host (extension or Single Number Reach).

Modify the guest_list.json document with the following values:

Invitation format:
```json
    "invitation_id": "<add an invitation number>",
    "name": "<name of visiting guest>",
    "host": "<name of host>",
    "extension_to_dial": <dialiable phone number>
```
You can also add an operator number in /templates/guest_not_found.html:

```html
<a href="tel:<operator phone number>" onclick="">Dial Operator</a>
```

Limitation:
This sample code allows the user to print a tag using a local printer. 
In order to print a proper tag, a printing solution has to be selected and added to this code. 
The printing service is just provided to demonstrate that is possible to add third party printing solutions.

## Installation/Configuration

Clone the repo to a folder:

```git clone (link)```

Create Virtual Environment (recommended), and install requirements.txt:
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Once the Flask app is up and running, browse: 

Main page:

```http://127.0.0.1:5000/login ```

or 

Admin page (used to add more invitations using the aforementioned invitation format):

```http://127.0.0.1:5000/admin ```


## Usage

### Option Login
At the Main page:

```http://127.0.0.1:5000/login ```

Add your invitation id in the provided text box and click the "Login" button:

![/IMAGES/login.png](/IMAGES/login.png)

The following Dial Form screen should appear:

![/IMAGES/dial.png](/IMAGES/dial.png)

Here, verify that the Guest Name and Host Name are correct. Click the "Print ID" button if a printer is available, 
or the "Click here to dial" button, to dial the host.
The Webex Device or Webex Teams client should ask you to Dial the number, click to dial again to complete the call. 

### Option Admin
At the Admin page:

```http://127.0.0.1:5000/admin ```

Fill out the boxes with the required info. The code will detect existing invitation numbers (if repeated), and it won't let you progress
if either of the boxes is not filled with the required information. Click "register" to save, the .json document should be 
updated automatically with the provided info. To delete the information, modify the .json document. 

![/IMAGES/admin_sample.png](/IMAGES/admin_sample.png)

Sample invitation format document:

![/IMAGES/sample_json_document.png](/IMAGES/sample_json_document.png)


### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment, and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.