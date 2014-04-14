acme_server
===========
The acme_server is a potentially complex distributed system based on Python.
Its purpose is to demonstrate how to deploy such a system to various
environments and how to test all the components.

ACME(tm) is your typical sinister corporation. Their main business as you
would expect is alien abduction.

The "server" has multiple components that serve different purposes:

1. acme_db - in charge of storing the alien abduction and probing data
2. acme_service - the backend service in charge of all the logic
3. acme_api - a REST API to expose the acme_service to the world
4. acme_sdk - a Python client library that wraps the API
5. acme_integration_tests

Each of these components is a Python package. The packages follow roughly the
guidelines here: https://python-packaging-user-guide.readthedocs.org



