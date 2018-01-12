=======
History
=======

0.1.2 (Current version)
-----------------------

* :py:func:`impax.csvv.get_gammas` has been deprecated. Use :py:func:`impax.read_csvv` instead (:issue:`37`)
* :py:meth:`~impax.csvv.Gammas._prep_gammas` has been removed, and :py:meth:`~impax.csvv.Gammas.sample` now
  takes no arguments and returns a sample by default. Seeding the random number generator is now left up to
  the user (:issue:`36`)


0.1.0 (2017-10-12)
------------------

* First release on PyPI.
