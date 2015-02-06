Version: __0.3.2__

About
=====

__pysimplelogs__ is a python client library for [Simplelogs] [sl] logging system.


Requirements
============
  * [Requests] [requests]


[sl]: https://github.com/SkyFox/simplelogs
[requests]: http://docs.python-requests.org/en/latest/

Config-file description
=======================

Before using this lib in your code, please change settings in config.py:

    SLEEP_TIME = 0.1  # Time between attempts for sending log entry.
    NUMBER_OF_ATTEMPTS = 5  # Attempts.
    CONNECTION_TIMEOUT = 3  # Connections timeout in seconds.


How to use
==========

Very simple!

    from pysimplelogs import Simplelog
    simplelog = Simplelog("http://hostname/")
    simplelog.warning({'ip': '127.0.0.1', 'name': 'Jon'}, "Hello, world!", ["core", "client"])

__Message format__:

    simplelog.level-name(owner, data, tags)

__Description__:

  * __level-name__ - any level, that server returns by URI http://host/api/level/. It can be customized in
  [simplelogs] [sl] config-file.
  * __owner__ - entry owner. String or dictionary. [Required]
  * __data__ - entry owner. String or dictionary. [Required]
  * __tags__ - list only.

What's new
==========

__0.3.2__

  * If asynchronous send not allowed, make the synchronous one.

__0.3.1__

  * Fix in datetime JSONEncoding,
  * Added skip parameter for possibility to use pagination.

__0.3.0__

  * Logger class. Now you can use pysimplelogs like standard python logger.

__0.2.3__

  * Refactoring and bugfixes.

__0.2.1__

  * Added json-encoder for datetime objects serialization.
  * Bugfixes.

__0.2.0__

  * Methods for getting data;
  * Added requirements.txt.

__0.1.1__

  * If server is not available, default levels list will be initialized:
  critical, error, warning, notice, info, debug;
  * Server URL was deleted from config-file. Now you need to create instance.
  I recommend you to write 1 function for it. DRY.