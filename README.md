# NetCDF-LD test file

Quick test of using [OGC NetCDF-LD](http://docs.opengeospatial.org/DRAFTS/19-002.html) conventions for [Schema.org](https://schema.org) conventions. This follows ESIP recommendations for [science-on-schema.org](https://github.com/ESIPFed/science-on-schema.org) guidance of publication of Earth Science Datasets.

## NetCDF-LD Python processor
This uses the [binary-array-ld/bald](https://github.com/binary-array-ld/bald) nc2rdf command line tool to generate schema.org descriptions.

This feature provides users a way to create schema.org descriptions from
ACDD/CF/NUG conformant values in a nc file.

``
$ python nc2rdf.py -o json-ld --schema-org [cdl or nc file]
``

Example:
``
$ python nc2rdf.py -o json-ld --schema-org ../lib/bald/tests/integration/CDL/trajectoryProfile_template.cdl
``
`

## Files

* write_nc.py python test code using the [netCDF4](https://pypi.org/project/netCDF4/) python package.
* test.nc output from write_nc.py test code in netCDF4
* test.ncdump output from ncdump command excuted on test.nc
