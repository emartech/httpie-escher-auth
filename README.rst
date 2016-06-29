httpie-escher-auth
==================

This `HTTPie <http://httpie.org/>`_ auth plugin implements Escher authentication for endpoints
using Escher authentication with default settings.

Installation
------------

Be sure that `HTTPie <http://httpie.org/>`_ is installed, and install this plugin:

.. code-block:: bash

   $ pip install httpie-escher-auth

After installing, you will see the option ``escher-auth`` under ``--auth-type`` if you run
``$ http --help``.

Example
-------

.. code-block:: bash

   $ http --auth-type=escher-auth --auth=escher_key:escher_secret https://api.example.com/users

The default Escher credential scope is "escher_request". You can define the credential scope like this:

.. code-block:: bash

   $ http --auth-type=escher-auth --auth=credential_scope/escher_key:escher_secret https://api.example.com/users

Check out `HTTPie sessions <https://github.com/jkbrzt/httpie#sessions>`_ if you would like to
save authentication information between your requests.
