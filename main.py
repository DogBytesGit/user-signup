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
import re
    
page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>User_Signup</title>
        <style type="text/css">
            .error {
                color: red;
            }
            td{
            font-family:Arial, sans-serif; font-size:14px;
            }
            label{
            font-weight:bold;
            }
        </style>
    </head>
    <body>"""

heading = '<strong><h1>Signup</h1></strong>'
username = ''
username_error = ''
password = ''
password_error = ''
verify = ''
verify_error = ''
email = ''
email_error = ''

def build_page(username, username_error, password, password_error, verify, verify_error, email, email_error):
    page_body = """
        <form method='post'>""" + heading + """
            <table>
                <tbody>
                    <tr>
                        <td align="right">
                            <label>Username:</label>
                        </td>
                        <td>
                            <input type="text" name="username" value=""" + username + """>
                        </td>
                        <td>
                            <span class="error">""" + username_error + """
                            </span>
                        </td>
                    </tr>
                    <tr>
                        <td align="right">
                            <label>Password:</label>
                        </td>
                        <td>
                            <input type="password" name="password" value=""" + password + """>
                        </td>
                        <td>
                            <span class="error">""" + password_error + """
                            </span>
                        </td>
                    </tr>   
                    <tr>
                        <td align="right">
                            <label>Verify:</label>
                        </td>
                        <td>
                            <input type="password" name="verify" value=""" + verify + """>
                        </td>
                        <td>
                            <span class="error">""" + verify_error + """
                            </span>
                        </td>
                    </tr>
                    <tr>
                        <td align="right">
                            <label>Email (optional):</label>
                        </td>
                        <td>
                            <input type="text" name="email" value=""" + email + """>
                        </td>
                        <td>
                            <span class="error">""" + email_error + """
                            </span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                        </td>
                        <td align="right">
                            <input type="submit" value="Submit">                    
                        </td>
                    </tr>
                </tbody>
            </table>

        </form>
        </body>
    </html>"""
    return page_body

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASSWORD_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        page_body = build_page(username,username_error,password,password_error,verify,verify_error,email,email_error)
        content = page_header + page_body
        self.response.write(content)

    def post(self):
        #Escape html on inputs
        username = self.request.get("username")
        username = cgi.escape(username)
        password = self.request.get("password")
        password = cgi.escape(password)
        verify = self.request.get("verify")
        verify = cgi.escape(verify)
        email = self.request.get("email")
        email = cgi.escape(email)

        #username error
        flag = False
        if (username == "") or not (USER_RE.match(username)):
            username_error = " That's not a valid username."
            flag = True
        else:
            username_error = ""

        #password error
        if not PASSWORD_RE.match(password):
            password_error = " That wasn't a valid password."
            flag = True
        else:
            password_error = ""

        #passwords don't match
        if password != verify:
            verify_error = " Your passwords didn't match!"
            flag = True
        else:
            verify_error = ""

        #email error
        if len(email) > 0:
            if not EMAIL_RE.match(email):
                email_error = " That's not a valid email!"
                flag = True
            else:
                email_error = ""
        else:
            email_error = ""

        if flag == True:
            page_body = build_page(username,username_error,"",password_error,"",verify_error,email,email_error)            
            content = page_header + page_body
            self.response.write(content)
        else:
            flag = False
            self.response.write("Welcome: " + username)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
