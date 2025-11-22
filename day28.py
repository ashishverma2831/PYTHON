# Day 28 of 30DaysOfPython Challenge
# Working with APIs in Python


"""
Web API has been moving away from Simple Object Access Protocol (SOAP) based web services and service-oriented architecture (SOA) towards more direct representational state transfer (REST) style web resources.
"""


"""
The GET, POST, PUT and DELETE are the HTTP request methods which we are going to implement an API or a CRUD operation application.

GET: GET method is used to retrieve and get information from the given server using a given URI. Requests using GET should only retrieve data and should have no other effect on the data.

POST: POST request is used to create data and send data to the server, for example, creating a new post, file upload, etc. using HTML forms.

PUT: Replaces all current representations of the target resource with the uploaded content and we use it modify or update data.

DELETE: Removes data
"""


"""
HTTP uses client-server model. An HTTP client opens a connection and sends a request message to an HTTP server and the HTTP server returns response message which is the requested resources. When the request response cycle completes the server closes the connection.
"""


"""
The format of the request and response messages are similar. Both kinds of messages have

an initial line,
zero or more header lines,
a blank line (i.e. a CRLF by itself), and
an optional message body (e.g. a file, or query data, or query output).
"""