#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import cgi

page_header = ('<!DOCTYPE html><html><head><title>User_Signup</title><style type="text/css">.container {width: 500px; clear: both;} .container input {width: 100%; clear: both;}</style></head><body><div class="container"><form>')
page_footer = "</form></div></body></html>"

class MainHandler(webapp2.RequestHandler):
    def get(self):

        heading = '<strong><h1>Signup</h1></strong>'
        line1 = '<label>Username:</label><input type="text" name="username"/>' + '<br>' + '<br>'
        line2 = '<label>Password:</label><input type="password" name="password"/>' + '<br>' + '<br>'
        line3 = '<label>Verify Password:</label><input type="password" name="verify_password"/>' + '<br>' + '<br>'
        line4 = '<label>Email Address (optional):</label><input type="text" name="email_address"/>' + '<br>' + '<br>'
        line5 = '<input type="submit" name="Submit" value="Submit">'
        body = heading + line1 + line2 + line3 + line4 + line5
        content = page_header + body + page_footer
        self.response.write(content)


        def post(self):

            #Escape html on inputs
            username = self.request.get("username")
            username = cgi.escape(username)
            password = self.request.get("password")
            password = cgi.escape(password)
            verify_password = self.request.get("verify_password")
            verify_password = cgi.escape(verify_password)
            email_address = self.request.get("email_address")
            email_address = cgi.escape(email_address)





app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
