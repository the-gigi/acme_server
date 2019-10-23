acme_server
===========
The acme_server is a potentially complex distributed system based on Python. 
Its purpose is to demonstrate how to deploy such a system to various
environments and how to test all the components. I wrote an article to Dr. Dobbs
and intended to use code as a live example, but in the end I had too much to
write about and not enough room to show example code. 

The [link]((http://www.drdobbs.com/testing/testing-complex-systems/240168390?pgno=1).) to the article on Dr.Dobbs is broken.

Fortunately, I saved a local copy as a markdown file: [Testing Complex Systems](artcile.md)

ACME(tm) is your typical sinister corporation. Their main business as you
would expect is alien abduction.

The "server" has multiple components that serve different purposes:

1. acme_db - in charge of storing the alien abduction and probing data
2. acme_service - the backend service in charge of all the logic
3. acme_api - a REST API to expose the acme_service to the world
4. acme_sdk - a Python client library that provides read-only access to DB
5. acme_integration_tests - tests of multiple components
6. acme_system_tests - whole system tests (end-to-end workflow, load, etc)

Most of these components are Python packages. The packages follow roughly
the guidelines here: https://python-packaging-user-guide.readthedocs.org



