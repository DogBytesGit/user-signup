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
            width: 300px;
            clear: both;
            }
        .container input {
            width: 100%;
            clear: both;
            }
    </style>
</head>
<body>
    <div class="container">
    <form>"""

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
line3 = """<label>Verify Password:</label><input type="password" name="verify"/>""" +error3 + """<br> <br>"""
line4 = """<label>Email Address (optional):</label><input type="text" name="email" "/>""" + error4 + """<br> <br>"""
line5 = '<button style="height:40px;width:100px"><input type="submit" name="Submit" value="Submit"></button>'

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

        # if we have an error, make a <p> to display it
        #error = self.request.get("error")
        #error_element = "<p class='error'>" + error + "</p>" if error else ""
        self.response.write(content)


    def post(self):
        username = self.request.get("username")
        #username error messages here
        if username == "":
            error1 = " Nothing entered!"
            line1 = """<label>Username:</label><input type="text" name="username"/>""" + error1 + """<br> <br>"""
            body = heading + line1 + line2 + line3 + line4 + line5
            content = page_header + body + page_footer
            self.response.write(content)

        if ' ' in username:
            error1 = " Spaces aren't allowed!"
            line1 = """<label>Username:</label><input type="text" name="username"/>""" + error1 + """<br> <br>"""
            body = heading + line1 + line2 + line3 + line4 + line5
            content = page_header + body + page_footer
            self.response.write(content)

        if USER_RE.match(username):
            error1 = " Illegal characters in username!"
            line1 = """<label>Username:</label><input type="text" name="username"/>""" + error1 + """<br> <br>"""
            body = heading + line1 + line2 + line3 + line4 + line5
            content = page_header + body + page_footer
            self.response.write(content)

        #password error messages here
        if PASSWORD_RE.match(password):
            error2 = " Illegal characters in password!"
            line2 = """<label>Password:</label><input type="password" name="password"/>""" + error2 + """<br> <br>"""
            body = heading + line1 + line2 + line3 + line4 + line5
            content = page_header + body + page_footer
            self.response.write(content)

        #passwords don't match error messages here
        if password != verify:
            error3 = " Passwords don't match!"
            line3 = """<label>Verify Password:</label><input type="password" name="verify"/>""" +error3 + """<br> <br>"""
            body = heading + line1 + line2 + line3 + line4 + line5
            content = page_header + body + page_footer
            self.response.write(content)

        #email error messages here
        if EMAIL_RE.match(email):
            error4 = " Error in email address!"
            line4 = """<label>Email Address (optional):</label><input type="text" name="email" "/>""" + error4 + """<br> <br>"""
            body = heading + line1 + line2 + line3 + line4 + line5
            content = page_header + body + page_footer
            self.response.write(content)

        #Escape html on inputs
        username = cgi.escape(username)
        password = self.request.get("password")
        password = cgi.escape(password)
        verify = self.request.get("verify")
        verify = cgi.escape(verify)
        email = self.request.get("email")
        email = cgi.escape(email)



app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
