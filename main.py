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

#html header
page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User_Signup</title>
    <style type="text/css">
        .container {
            width: 600px;
            clear: both;
            }
        .container input {
            width: 25%;
            clear: both;
            }
    </style>
</head>
<body>
    <div class="container">
    <form method='post'>"""

#html footer
page_footer = """
</form>
</div>
</body>
</html>"""

heading = '<strong><h1>Signup</h1></strong>'

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

error1 = ""
error2 = ""
error3 = ""
error4 = ""

line1 = """<label>Username:</label><input type="text" name="username"/>""" + error1 + """<br> <br>"""
line2 = """<label>Password:</label><input type="password" name="password"/>""" + error2 + """<br> <br>"""
line3 = """<label>Verify Password:</label><input type="password" name="verify"/>""" + error3 + """<br> <br>"""
line4 = """<label>Email Address (optional):</label><input type="text" name="email" "/>""" + error4 + """<br> <br>"""
#line5 = '<button style="height:40px;width:100px"><input type="submit" value="Submit"></button>'
line5 = '<input type="submit" value="Submit">'

def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASSWORD_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        body = heading + line1 + line2 + line3 + line4 + line5
        content = page_header + body + page_footer
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
        error1 = ""
        error2 = ""
        error3 = ""
        error4 = ""
        #username error
        flag = False
        if (username == "") or not (USER_RE.match(username)):
            error1 = " That's not a valid username."
            flag = True

        #password error
        if not PASSWORD_RE.match(password):
            error2 = " That wasn't a valid password."
            flag = True

        #passwords don't match
        if password != verify:
            error3 = " Your passwords didn't match!"
            flag = True

        #email error
        if len(email) > 0:
            if not EMAIL_RE.match(email):
                error4 = " That's not a valid email!"
                flag = True

        if flag == True:
            line1 = '<label>Username:</label><input type="text" name="username" value="' + username + '" />' + error1 + """<br> <br>"""
            line2 = """<label>Password:</label><input type="password" name="password" value=""/>""" + error2 + """<br> <br>"""
            line3 = """<label>Verify Password:</label><input type="password" name="verify" value=""/>""" + error3 + """<br> <br>"""
            line4 = '<label>Email Address (optional):</label><input type="text" name="email" value="' + email + '" />' + error4 + """<br> <br>"""
            body = heading + line1 + line2 + line3 + line4 + line5
            content = page_header + body + page_footer
            self.response.write(content)
        else:
            self.response.write("Welcome: " + username)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
