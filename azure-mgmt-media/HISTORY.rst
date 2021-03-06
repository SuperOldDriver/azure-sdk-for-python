.. :changelog:

Release History
===============

0.2.0 (2017-09-14)
++++++++++++++++++

**Bug fixes**

- Fix deserialization issue with check_name_availability

**Features**

- Adds operations.list

**Breaking changes**

- Operations will now throw a ValidationError if input string is longer than 24 characters (not CloudError)
- Some keyword arguments have been renamed "parameters"

0.1.2 (2016-06-27)
++++++++++++++++++

This wheel package is built with the azure wheel extension

0.1.1 (2016-12-12)
++++++++++++++++++

* Best parameters check (you might experience exception change from CloudError to TypeError)
* Delete account operation fix (random exception)
* Create account operation fix (random exception)

0.1.0 (2016-11-07)
++++++++++++++++++

* Initial preview release
