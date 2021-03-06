.. :changelog:

History
=======

2.0.11 (2013-12-21)
----------------

* Boundary types are now automatically identified for each comparison (fixes a bug in multiple boundary segmentation comparison where by default, only the boundary type ``1`` is compared)
* Fixed a bug where during agreement computation, an extra boundary was being counted and only the boundary-mass format was properly supported (oops)
* If someone uses a hypothesis or reference argument in mass format that is a single number (e.g., using ``(20)`` instead of the proper ``(20, )``), their argument is converted for them into a tuple


2.0.10 (2013-10-01)
----------------

* Fixed a bug where long mass sequences would not work for window metrics
* Removed duplicate unit test


2.0.9 (2013-09-07)
----------------

* Fixed a bug where agreement could not be computed on boundary-set-format segmentations and segmentations and segmentations containing multiple boundary types.


2.0.8 (2013-07-05)
----------------

* Added Python 2.6, 3.2, and 3.3 support
* Added support for converting NLTK-style segmentations into segmentation masses
	* Added ``convert_nltk_to_masses``
* Fixed minor comment/documentation typos


2.0.7 (2013-07-05)
----------------

* Fixed an issue with importing the Dataset object which resulted in an inablity to also build docs


2.0.6 (2013-07-04)
----------------

* Fixed an issue with subpackages not being included in the distribution


2.0.5 (2013-07-03)
----------------

* Fixed a README typo
* Updated this history


2.0.4 (2013-07-03)
----------------

* Fixed pep8 and flake errors


2.0.3 (2013-07-03)
----------------

* Increased branch code coverage to 100%
* Added coveralls support for builds


2.0.2 (2013-07-01)
----------------

* Corrected documentation and added examples
* Happy Canada Day!


2.0.1 (2013-06-16)
----------------

* Fixed a bug with the 'minus_one' keyword argument
* Improved code coverage


2.0 (2013-05-13)
----------------

* Re-created to make APIs easier to use
* Implemented boundary similarity


1.1.0 beta (2012-08-09)
-----------------------

* Inter-coder coefficient values are now only calculated over items coded by all coders (i.e., fully coded), and where coders do not code all items, the items are divided up into groups that have been fully coded
* Micro and macro averages are available, with macro averages indicating the standard error and number of items averaged
* Added support for an authorative reference coder (see the `Segmentation Representation Specification Version 1.1 PDF <http://nlp.chrisfournier.ca/publications/pdf/fournier_segeval_spec_2012.pdf>`_) and support for S-based precision, recall, and F-beta measure
* Modified the input JSON files to allow for an entire dataset to be contained within a single file (see the `Segmentation Representation Specification Version 1.1 PDF <http://nlp.chrisfournier.ca/publications/pdf/fournier_segeval_spec_2012.pdf>`_)
* Added additional unit tests


1.0.1 beta (2012-06-04)
-----------------------

* Fixed a distribution issue


1.0.0 beta (2012-06-04)
-----------------------

* Added CLI and prepared for presentation at NAACL-HLT 2012


0.3.0 (2012-04-08)
------------------

* Updated implenentation and tests in preparetion for camera-ready submission to NAACL


0.2.0 (2012-02-14)
------------------

* Updated implenentation and tests in response to feedback from discussions at uOttawa


0.1.0 (2012-01-06)
------------------

* Birth of a NAACL paper!


0.0.1 (2011-11-29)
------------------

* Curiosity
* Inception
