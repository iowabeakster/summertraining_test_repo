Test file
=============

Subsection Title
----------------
A paragraph for the subsection.
Regenerate the test.html file and see how it looks :)

Bulleted List
-------------

- Item 1
- Item 2
- Item 3

Not part of the list

Ordered Lists
-------------

1. Item 1 text
2. Item 2 text
3. Text from item 3

Auto-enumerated ordered lists
-----------------------------

1. New item 1
#. Auto-enumerated item 2
#. Another auto-enumerated item 3


Definition lists
----------------

Definition list 1
 composed of three items

definition list 2
 first item is a "term"

defintion list 3
 second item is a classifier.  after the term " : " (space colon space) the classifier

definition list 4 : classifier
 the third item is the definition indented below (indented by a single space).


Option Lists
------------

Option lists are two-colum lists of command line arguments and their definitions.  The argument and the defintion must me separated by two spaces. A space preceding the argument will indent both colums.

 -a  Output all.
 -b  Output both (this description is quite long for an option list)
 -c arg  Output just arg.
 --long  Output all day long.


Literal Blocks
--------------

Literal blocks are the places wher no markup is done.  This is for display of code.  I believe it is started with a double colon and all lines indented for the block to be included.

::
 
 # like this
 # sample code

 for i [1, 10, 100] <= $string bvalue
 	return 0
 
 # not real code

Doctest blocks
--------------

::

 Normal plain text paragraph.  They begin with a "``>>>``" and end with a blank line.


Normal plain text paragraph.  They begin with a "``>>>``" and end with a blank line.

 ``>>>`` print 'this is a Doctest block'

this is a Doctest block


Hyperlinks
----------

::
 
 This is a `link <http://google.com>`_

This is a `link <http://google.com>`_


Targetd Links
-------------

Another way of doing links is the targeted method.

::

 `Python programming language`_ is very nice for students

 .. _Python programming language: http://python.org


`Python programming language`_ is very nice for students

.. _Python programming language: http://python.org

Simple Tables
-------------

The good is that Simple tables are easy to create and modify.  But spanning rows is not possible or text blocks, etc. Plain text example of simple table input and html output.

::
 
 =========  ======  ======
        Inputs      Output
 -------------------------
     A        B     A or B
 =========  ======  ======
 False      False   False
 True       False   False
 False      True    TRue
 True       Tue     True
 =========  ======  ======

=========  ======  =======
        Inputs     Output
-----------------  -------
     A        B     A or B
=========  ======  =======
False      False   False
True       False   False
False      True    TRue
True       Tue     True
=========  ======  =======

Grid Tables
-----------

Grid tables are a pain to create, but all far more capability in what they do. Plain text input and html output.

::
 
 +------------+------------+-----------+
 | Header 1   | Header 2   | Header 3  |
 +============+============+===========+
 | body row 1 | column 2   | column 3  |
 +------------+------------+-----------+
 | body row 2 | Cells may span columns.|
 +------------+------------+-----------+
 | body row 3 | Cells may  | - Cells   |
 +------------+ span rows. | - contain |
 | body row 4 |            | - blocks. |
 +------------+------------+-----------+

+------------+------------+-----------+
| Header 1   | Header 2   | Header 3  |
+============+============+===========+
| body row 1 | column 2   | column 3  |
+------------+------------+-----------+
| body row 2 | Cells may span columns.|
+------------+------------+-----------+
| body row 3 | Cells may  | - Cells   |
+------------+ span rows. | - contain |
| body row 4 |            | - blocks. |
+------------+------------+-----------+

Notes
-----

Using directives to create notes.

::
 
 ..note:: This a note.

 - List item 1
 - List item 2

.. note:: This is a note.

 - List item 1
 - List item 2

Emphasis
--------

For *emphasis* use the single asterisk to bracket the desire text (itlaics). For **strong emphasis** use double asterisks as brackets.  

Footnotes
---------

This is how you make auto-numbered footnotes.  Plain text input and html output.

::
 
 Please RTFM [#]_ or you can read [#]_.

 .. [#] Read the Fine Manual
 .. [#] The other Fine manual

Please RTFM [#]_ or you can read [#]_.

.. [#] Read the Fine Manual
.. [#] The next Fine Manual


