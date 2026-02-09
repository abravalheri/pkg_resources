A (still deprecated) copy of ``pkg_resources`` as found in Setuptools v81.0.0.
Made available for a compatibility install in environments that previously dependended on Setuptools for this functionality.

In other words, ***DO NOT USE***.

Projects must migrate away from ``pkg_resources``. The recommended replacements are:

* Resource access: `importlib.resources`
  (or its backport `importlib_resources`).
* Distribution metadata & entry points: use `importlib.metadata`
  (or its backport `importlib_metadata`).
* Requirement and version parsing: use `packaging`.
  This includes parsing and evaluating ``extras`` and markers via
  ``packaging.requirements.Requirement`` and ``packaging.markers.Marker``.
  Note that automatic installation or detection of extras is not provided;
  projects requiring that behaviour must implement it themselves using
  a combination of ``packaging``, ``importlib.metadata`` and other tools
  as building blocks.
* Coexistence of multiple versions of a package: please consider using a different
  approach, as this functionality is not supported by Python itself.
  Alternatives include isolated environments and orchestration tools
  (`venv`, `tox`, `nox`, etc.).
* Handling of `.egg` distributions: please consider using a different
  approach, as the `.egg` and `easy_install` mechanisms have also been
  discontinued.
  Please use currently supported packaging formats
  and build/installation workflows (PEP 517).
