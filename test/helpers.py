# helper functions
import pvgis

def get_tilename_for_coordinates(dataset, variable, longitude, latitude):
    """
    Retrieve a tile's row and column for a given pair of geographic coordinates 
    """
    row, column = pvgis.get_tile_from_coords(longitude, latitude)
    column = str(column).zfill(3)
    #print(f'Row: {tile_row}, Column: {tile_column}')
    # Why input is (longitude, latitude) and output is then (row, column)?
    tilename_template = f'{dataset}_{variable}_{row}_{column}'
    return tilename_template


def get_da(path, observations_per_hour):
    """
    Read a "tile" from the data as a data array object
    """    
    tile = pvgis.load_bz2_tile(path, observations_per_hour=observations_per_hour)
    da = pvgis.da_from_bz2_tile(tile=tile, mask_and_scale=True, observations_per_hour=observations_per_hour)
    return da


def get_pvgis_data_array(
    path,
    dataset,
    variable,
    longitude,
    latitude,
    observations_per_hour,
):
    """
    Get an xarray out of a tile in which a given location is located
    """    
    tilename = get_tilename_for_coordinates(dataset, variable, longitude, latitude)
    path = pvgis.DATA / path / tilename
    data_array = get_da(path, observations_per_hour=1)
    return data_array


def get_pvgis_data_via_the_web_api(
    curl_object,
    column_names,
    ):
    """
    Get CSV data via the public web API
    Note: for `skiprows=2` see issue # ?
    """
    buffer = BytesIO()
    curl_object.setopt(
        curl_object.WRITEDATA,
        buffer
    )
    curl_object.perform()
    body = buffer.getvalue()
    csv = body.decode('utf8')
    data = pandas.read_csv(
        BytesIO(body),
        encoding='utf8',
        names=column_names,
        skiprows=2,
    )
    return data


def set_time_index_from_api_data(
    data,
    time_column,
    ):
    """
    Convert date-time strings in column 'time_column'
    to type `datetime64` and set 'time' as the input data frame's
    index
    """
    # convert
    data[time] = pandas.to_datetime(data[time], format="%Y%m%d:%H%M")
    
    # floor down to hourly
    data[time] = data[time].dt.floor('H')
    
    # 'time' is the index 
    data = data.set_index(time)
    
    # sorting applies
    data = data.sort_index()
    return data
