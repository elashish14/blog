Title: Transferring Files Over HTTP Using Python
Date: 2020-05-17T20:54:46+00:00
Category: Computers
Tags: Software, python, HTTP
Slug: transferring-files-over-http-using-python

Sending files around a network always seems to be difficult for some reason.
But Python has a built-in utility that makes this much easier. Simply run this
at the command line:

    :::bash
    python3 -m http.server 8080

Python will start an HTTP server on port 8080 *and it will serve all files over
HTTP in its working directory*. If you navigate to `http://localhost:8080` in
your browser after running this command, you will see all the files in the
directory where the HTTP server was started!

This makes for an easy way to transfer files over a private network. You can
run a quick command to determine your IP address:

    :::bash
    ip -br -c a

And navigate to that IP address from another computer to see the same files
being served there as well. But be careful of course! Anyone on the network
will have access to these files as well. So it is a good idea to copy the files
you want to send to a separate directory and run the server from there if you
don't want everyone on the network snooping around your home directory and
accessing your SSH private keys.

The [http.server][1] module in Python's standard library has much more
functionality than just this, but note that it is not recommended for use in a
production server. (For that you would want something like [uwsgi][2] or
[gunicorn][3].) But I find this to be the easiest way to transfer files between
machines on a private LAN.

[1]: https://docs.python.org/3/library/http.server.html#module-http.server
[2]: https://uwsgi-docs.readthedocs.io/en/latest/WSGIquickstart.html
[3]: https://gunicorn.org/
