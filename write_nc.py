# Walkthrough example from
# https://towardsdatascience.com/create-netcdf-files-with-python-1d86829127dd
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
# ds.attrs['rdf__type'] = 'bald__Container'
group_pref = ds.createGroup('prefix_list')
group_pref.bald__ = 'https://www.opengis.net/def/binary-array-ld/'
group_pref.rdf__ = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#'
group_pref.so__ = 'https://schema.org/'
ds.bald__isPrefixedBy = 'prefix_list'

ds.Conventions = "CF_1.0"

ds.close()
