..
    Copyright (C) 2018-2020 CERN.
    Copyright (C) 2018-2020 RERO.
    Invenio-Circulation is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.

Changes
=======

Version 1.0.0a23 (released 2020-05-22)

- renames signals parameter from `prev_loan` to `initial_loan`
- adds an extra parameter `initial_loan` to the default duration functions
  in checkout policies

Version 1.0.0a22 (released 2020-05-22)

- adds additional checks when transitioning loans from and to Item at Desk
- removes example app and updates Invenio modules dependencies

Version 1.0.0a21 (released 2020-01-23)

- introduces `pid_type` for `item_pid` to uniquely identify an Item record
- changes methods that were expecting `item_pid`
- removed unused view circulation/items to retrieve the item from the loan

Version 1.0.0a20 (released 2019-11-01)

- adds a JSON resolver for the document of the loan

Version 1.0.0a19 (released 2019-09-27)

- adds a JSON resolver for the patron of the loan
- fixes deserialization bug on loan REST loader when a date/datetime
  field is missing

Version 1.0.0a18 (released 2019-09-26)

- handle date/time record fields as datetime object internally
- add `request_start_date` field to loan schema
- automatic assignement of item on request is now configurable
- add marshmallow loader for REST endpoint
- add support to ES7
- drop support for Python 2
- bugfixes

Version 1.0.0a17 (released 2019-09-13)

- add `delivery` object to the `loan` schema
- pin invenio-records-rest version to ensure compatibility with python 3
  and marshmallow 3

Version 1.0.0a16 (released 2019-08-09)

- change loan duration from number of days as int to timedelta

Version 1.0.0a15 (released 2019-08-07)

- remove ES 2 support
- change `loan_pid` to `pid` schema field

Version 1.0.0a14 (released 2019-06-24)

- now allows loans to be created solely on document_pid
- refactored and added more tests for transitions

Version 1.0.0a13 (released 2019-04-24)

- fixed item reference attachment on checkout

Version 1.0.0a12 (released 2019-04-17)

- Renamed is_item_available circulation policy to item_can_circulate.

Version 1.0.0a11 (released 2019-03-29)

- Add sort options to search api

Version 1.0.0a10 (released 2019-03-27)

- Fix for permissions check


Version 1.0.0a9 (released 2019-03-25)

- Introduce Circulation Exceptions

Version 1.0.0a8 (released 2019-03-06)

- Introduce `request` policy.
- Pass previous loan and trigger name on the state change signal.

Version 1.0.0a7 (released 2019-02-25)

- Replace item_pid with loan_pid in $ref Loan schema.

Version 1.0.0a6 (released 2019-02-04)

- Force user to implement configuration utils functions instead of returning a
  dummy value.

Version 1.0.0a5 (released 2019-01-28)

- Add config for defining loan `completed` state.

Version 1.0.0a4 (released 2019-01-26)

- Loan replace item endpoint.

Version 1.0.0a3 (released 2019-01-18)

- Creating item reference only when item pid is attached.

Version 1.0.0a2 (released 2019-01-18)

- Adding support for creating a reference inside `Loan` record to an item.

Version 1.0.0a1 (released 2018-12-04)

- Initial public release.
