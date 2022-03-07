..
   Note: Items in this toctree form the top-level navigation. See `api.rst` for the `autosummary` directive, and for why `api.rst` isn't called directly.

.. toctree::
   :hidden:

   Home page <self>
   getting_started.md
   API reference <_autosummary/nasabreakup>

.. toctree::
   :hidden:
   :caption: Development:

   Contributing <contributing_guidelines>
   Change Log <change_log>

.. toctree::
   :hidden:
   :caption: Project Links:

   GitHub <https://github.com/ReeceHumphreys/NASA-breakup-model-python>
   PyPI <http://www.google.com>


Welcome to NASA Standard Breakup Model in Python
=====================================================
*NASA Standard Breakup Model in Python* is a Python library for simulating explosion and collision events
in orbit using the NASA Standard Breakup Model. The breakup model was implemented based on the following works:
NASA's new breakup model of evolve 4.0 (Johnson et al.) [#johnson]_, and
Proper Implementation of the 1998 NASA Breakup Model (Krisko et al.) [#krisko]_.

With this package you can:

* Generate the number of fragments produced in an orbital collision or explosion.
* Find the area and mass of the debris produced by the above fragmentation events.
* Determine the relative velocity of each debris fragment.


Additionally, *NASA Standard Breakup Model in Python* is used to power ODAP (Orbital Debris Analysis with Python)
which is a larger package that includes propagations, data analysis, and orbit visualization. This package
serves as a stand-alone version of the NASA Breakup Model in the scenario that you do not want the additional
tools provided by ODAP.

.. admonition:: Note - NASA Standard Breakup Model in Python is in development!

   *NASA Standard Breakup Model in Python* is currently under development. As a result, the API may change,
   and some functionality may not work as expected. As such, until version 1.0, this package should be
   considered pre-release. Please feel free to create an issue on the GitHub page with any issues or questions!

.. note::
   :doc:`NASA Breakup Model in Python is licensed under the MIT license <license>`.


.. [#johnson] `NASA's new breakup model of evolve 4.0 <https://www.sciencedirect.com/science/article/abs/pii/S0273117701004239>`_
.. [#krisko] `Proper Implementation of the 1998 NASA Breakup Model <https://orbitaldebris.jsc.nasa.gov/quarterly-news/pdfs/odqnv15i4.pdf>`_