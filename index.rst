.. Tin Can Technical Workshop documentation master file, created by
   sphinx-quickstart on Mon Dec 10 08:45:39 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Hello!
======================================================

I'm Russell, and we're Saltbox.



Statements
-------------------

* Person
* Verbed
* Object



Statements
-------------------

* Person
* Verbed
* Object
* at a Time


Statements
-------------------

* Person
* Verbed
* Object
* at a Time
* with a Result


Statements
-------------------

* Person
* Verbed
* Object
* at a Time
* with a Result
* in a Context

Statements
-------------------

* Person
* Verbed
* Object
* at a Time
* with a Result

  * oh, and a Score

* in a Context



Statements
-------------------

* in a Context 

  * with a parent Activity
  * instructed by someone
  * as part of a team
  * and so on...

Okay, time to break that down
--------------------------------

Sounds a bit complicated, but really pretty simple


Person (well, Agent)
------------

.. code-block:: javascript

    {
        "name": "Mal Reynolds",
        "objectType": "Agent",
        "mbox": "mailto:mal@serenity0x58.ship"
    }


. . . objectType?
-------------------

.. code-block:: javascript

    "objectType": "Agent"

or "Group", "Activity", or maybe "SubStatement" or "StatementRef"


Isn't mbox just a fancy way to say email?
--------------------------------------------

Inverse functional identifiers!

* mbox
* mbox_sha1sum
* account (name, homePage)
* openid

Verbed
-----------

.. code-block:: javascript

    {
        "id": "http://example.com/verbs#flew",
        "display": {
            "en": "flew"
        }
    }

Pulling an ID out of a hat
--------------------------

Figure out what you mean, then figure out if anyone has meant it before.

Err on the side of specificity.

Display
------------

Language map!

.. code-block:: javascript

    {
        "en": "flew",
        "es": "voló",
        "gu-IN": "ઝટપટ જવું"
    }

Object
-----------

We usually mean Activity.

.. code-block:: javascript

    {
      "id":
        "http://example.com/activities#ArieltoBeaumonde",
      "objectType": "Activity",
      "definition": {
        "type":
          "http://example.com/activitytypes#spaceroute",
        "name": {
          "en": "Ariel to Beaumonde"
        },
        "description": {
          "en":
            "The route between the planets
            Ariel and Beaumonde"
        }
      }
    }

A lot to process, but not so bad as all that
------------------------------------

ID and objectType again & language maps for name and description.

* ID is reused less often than verbs
* "type" is for grouping activities of like categorization


And that's the most basic parts of a statement
--------------------

* Person
* Verbed
* Object
* (id! 12345678-1234-5678-1234-567812345678)
* (timestamp! 1999-12-31T12:59:59Z)

Briefly, the parts you can mostly ignore when creating statements
-----------------------
* stored
* authority
* voided

So we know who verbed what
-------------------

* but what happened when they did it?

  * result

* and what situation did all that happen in?

  * context


Result
--------------

.. code-block:: javascript

    {
      "score": {
        "scaled": 0.95,
        "raw": 19
      },
      "success": true,
      "completion": true,
      "response": "The text of the answer, perhaps.",
      "duration": "P1H"
    }


Context
----------

* registration: UUID
* instructor: Agent
* team: Group
* contextActivities

  * parent
  * grouping
  * other


Extensions!
-------------

URI key to arbitrary values

* activity definition
* result
* context





Three Scenarios
------------

* Blog Post Comments
* Simple Quiz
* Mobile Task Simulation Game




Blog Post Comments
----------------------

Recorded: Who Commented on What



Simple Quiz
---------------

Recorded: Question Answers and Overall Quiz




Mobile Task Simulation Game
------------------

Recorded: ?




Best Practices
-------------

To the blog!


And State and Profiles and Persons, oh my!
--------------------------------------

* transient information
* very app-specific information
* possibly the site of future standardization 
* also discovering identities


Common Errors and Antipatterns
---------------------------

* overly generic verbs
* empty strings instead of URIs
* using an activity for agent-agent interaction



Time to send some statements
--------------------------------


Time to fix some statements
----------------------