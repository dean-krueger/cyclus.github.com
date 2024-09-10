.. _constants:

|Cyclus| Defined Constants
======================================

Cyclus defines a set of constants to help standardize archetype properties and prevent
unexpected simulation failures.  These constants are determined at build time and may
depend on your system's architecture (specifically the size of an ``int`` type, in bytes).  
This set is defined twice, with identical values existing in the C++ namespace and Python library.
The numeric values are as follows:

.. list-table::
  :width: 100%
  :widths: 25 75
  :header-rows: 1

  * - Name
    - Value
  * - CY_LARGE_INT
    - | 2147483647 on most 64-bit machines.
      | This should be equal to ``std::numeric_limits<int>::max()``.
  * - CY_LARGE_DOUBLE
    - 1e299
  * - CY_NEAR_ZERO
    - 1e-08

Accessing constants in C++
--------------------------

The constants are defined in ``cyclus/cyc_limits.h`` and exist in the ``cyclus::`` namespace.  They can be
used in this way:

.. code-block:: cpp

  #include "cyclus.h"
  ...
  int my_large_int = cyclus::CY_LARGE_INT;
  ...

Accessing constants in Python
-----------------------------

The constants are defined in the ``cyclus.system`` module and can be imported and used as long as
the ``cyclus`` package is in your Python path:

.. code-block:: python

  from cyclus.system import CY_LARGE_DOUBLE, CY_LARGE_INT, CY_NEAR_ZERO
  ...
  my_small_value = CY_NEAR_ZERO
  ...

This holds true for |Cyclus| input files: 

.. code-block:: python

  from cyclus.system import CY_LARGE_DOUBLE
  SIMULATION = { 'simulation': 
    ...
    'facility': [
      { 'config': 
        { 'Source': 
          { 'capacity': CY_LARGE_DOUBLE,
    ...


.. warning::
  Only input files written in Python can access the constants in this way, since the variables are evaluated
  prior to schema validation.  Any attempt to use them in an XML input file will likely fail schema validation since
  they will be evaluated as strings instead of the corresponding values in C++/Python.

Using constants with the Cyclus Preprocessor
--------------------------------------------

Many archetype developers utilize the :ref:`Cyclus Preprocessor <cycpp>` and ``#pragma cyclus`` to
define state variables within an archetype.  The preprocessor allows any arbitrary
Python code to be executed via ``#pragma cyclus exec``.  Thus one can import the
set of Python constants into the global namespace that agent annotations are processed,
and reference them in state variable definitions.  Remember that the object
following ``#pragma cyclus var`` is evaluated by the Python interpreter, so you can
treat it as if it were Python code.

.. code-block:: cpp

  #pragma cyclus exec from cyclus.system import CY_LARGE_DOUBLE

  ...

  #pragma cyclus var {"default": CY_LARGE_DOUBLE, \
                    "tooltip": "sink maximum inventory size", \
                    "uilabel": "Maximum Inventory", \
                    "uitype": "range", \
                    "range": [0.0, CY_LARGE_DOUBLE], \
                    "doc": "total maximum inventory size of sink facility"}
  double max_inv_size;
