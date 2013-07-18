# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-2013 Bluestar Solutions Sàrl (<http://www.blues2.ch>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Webservice Handler",
    'version': 'master',
    "category" : "Bluestar/Addons/WS",
    "complexity": "easy",
    "description": """
A simple handling of webservice calls
=====================================

The module allows a simple handling of webservice calls. It creates a menu item in the scheduler admin configuration to set up services 
for given OpenERP objects. By default, the services handler is automatically called by the scheduler every minute. The webservice object 
handles everything for a specific service. Default encoding / decoding methods are provided to send or decode complete objects as JSON.

Technical description
---------------------

For every service you add, you can set :

* Name: Name of the service.
* Type: Get / Push / Push Get Sync / Get Push Sync.
* Webservice Protocol / Host / Port / Path: The webservice url.
* HTTP Authentication / Login / Password: Credential for http auth.
* Model Name: The main OpenERP object used in the service.
* Before Method Name: an (optional) method of the OpenERP object called at the start of the transaction.
* After Method Name: an (optional) method of the OpenERP object called at the end of th transaction (before commit).
* Encode Method Name: an (optional) method of the OpenERP object called to get data and encode it in JSON. If no method name is provided, the webservice.default_read_encode method is called.
* Decode Method Name: an (optional) method of the OpenERP object called to decode data and write it in database. If no method name is provided, the webservice.default_decode_write method is called.
* Push filter: an (optional) filter in OpenERP search format added to the default_read_encode filter. 
* Get DB Key: the database key for a record if the default id is not used.
* Date & Time Format: datetime format used in JSON data.
* Wait Retry: Number of minutes to wait before a new request when the request failed.
* Wait Next: Number of minutes to wait before a new request when the request succeeded.
* Priority: Order of call of the webservices.

Constraints on object
---------------------

To be used with the module, the object must provide create_date and write_date (must be declared in the _columns field).

Methods signatures
------------------

The methods called by the webservice system are called with the following parameters:

Before method
-------------

method(cr, uid)

* cr: the database cursor
* caller_uid: current user id

Any returned result is ignored.

After method
------------

method(cr, uid, get_resp_content, push_resp_content)

* cr: the database cursor
* caller_uid: current user id
* get_resp_content : response content of the GET request or None if webservice type is not GET, GET PUSH or PUSH GET
* push_resp_content : response content of the PUSH request or None if webservice type is not PUSH, GET PUSH or PUSH GET

Any returned result is ignored.

Read encode method
------------------

content = method(cr, uid, model, last_success, service.push_filter, service.datetime_format)

* cr: the database cursor
* caller_uid: current user id
* model: the OpenERP model object (allows browse and search on the object)
* last_success: the last time the service succeeded.
* push_filter: filter to be added to the search for new records.
* datetime_format: the date/time format used in the JSON content.

The last 2 fields are mainly used in the default encode method. They are provided to allow customization.

The returned result is sent as content in the webservice.

Decode write method
-------------------

success = method(cr, uid, model, content, service.datetime_format)

* cr: the database cursor
* caller_uid: current user id
* model: the OpenERP model object (allows browse and search on the object)
* content: the content returned by the webservice call.
* datetime_format: the date/time format used in the JSON content.

The returned result indicates if the decoding was successfull.
    """,
    "author": "Bluestar Solutions Sàrl",
    "website": "http://www.blues2.ch",
    'depends': [],
    'init_xml': [],
    'update_xml': ['module_data.xml',
                   
                   'security/ws_handler_security.xml',
                   'security/ir.model.access.csv',
                   
                   'webservice_handler.xml'],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images' : ['images/webservice_edit.png',],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
