# Walkthrough example from
# https://towardsdatascience.com/create-netcdf-files-with-python-1d86829127dd
# http://schubert.atmos.colostate.edu/~cslocum/netcdf_example.html
# https://unidata.github.io/netcdf4-python/#groups-in-a-netcdf-file
# http://cfconventions.org/Data/cf-conventions/cf-conventions-1.7/cf-conventions.html
import netCDF4 as nc
import numpy as np

fn ="./test.nc"
ds = nc.Dataset(fn,'w',format='NETCDF4')


time = ds.createDimension('time', None)
lat = ds.createDimension('lat', 10)
lon = ds.createDimension('lon', 10)


times = ds.createVariable('time', 'f4', ('time',))
lats = ds.createVariable('lat', 'f4', ('lat',))
lons = ds.createVariable('lon', 'f4', ('lon',))
value = ds.createVariable('value', 'f4', ('time', 'lat', 'lon',))
value.units = 'Unknown'

lats[:] = np.arange(40.0, 50.0, 1.0)
lons[:] = np.arange(-110.0, -100.0, 1.0)

print('var size before adding data', value.shape)

value[0, :, :] = np.random.uniform(0, 100, size=(10, 10))

print('var size after adding first data', value.shape)
xval = np.linspace(0.5, 5.0, 10)
yval = np.linspace(0.5, 5.0, 10)
value[1, :, :] = np.array(xval.reshape(-1, 1) + yval)

print('var size after adding second data', value.shape)

# Adding linked metadata
# Set prefix list for vocabulary uris
group_pref = ds.createGroup('prefix_list')
group_pref.bald__ = 'https://www.opengis.net/def/binary-array-ld/'
group_pref.rdf__ = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
group_pref.so__ = 'https://schema.org/'
ds.bald__isPrefixedBy = 'prefix_list'
ds.rdf__type  = 'bald__Container'

# CF Conventions suggest  Title, institution, source, history, references, comment
# https://help.ceda.ac.uk/article/4507-the-cf-metadata-convention
# http://cfconventions.org/Data/cf-conventions/cf-conventions-1.7/cf-conventions.html#description-of-file-contents
# At a minimum Conventions CF-1.0 should be set
ds.Conventions = "CF-1.5"


# From the bald2schemaorg_mappings
# The integration test
# https://github.com/binary-array-ld/bald/blob/master/lib/bald/tests/integration/CDL/trajectoryProfile_template.cdl
# Should correctly map schema.org
# https://github.com/binary-array-ld/bald/blob/master/nc2rdf/bald2schemaorg_mappings.json
# CF --> sdo
# summary --> Description
# title --> name
# keywords --> keywords
# license --> license
# standard_name --> variableMeasured
ds.title = "NCAR/NEON example run"
ds.summary = "Computational Run from NEON site data using NCAR model"
ds.keywords = "EARTH SCIENCE, ATMOSPHERE"
ds.license = "https://spdx.org/licenses/CC-BY-4.0"


# Schema.org based vocabulary definitions
# http://docs.opengeospatial.org/DRAFTS/19-002.html#_netcdf_linked_data_on_schema_org

# Schema.org funder https://github.com/ESIPFed/science-on-schema.org/blob/master/guides/Dataset.md#funding



ds.close()
