# PVGIS_API
Query data from PVGIS using the API

# Changelog
Version 1.1
- add an example input file (xlsx) as template
- include the time zone in the input file instead of parameter for calculation. It allows now the data query from locations in different time zones
- fix rounding problem of dates where hour = .30. 
- include a parameter to enable (or disable) the output file compression

Version 1.0
- query data from point locations. The time zone will be automatically corrected based on the parameter added in the input session, however, it allows only one time zone at a time
- output files will be saved as csv compressed files. If errors are found, they will be saved in a separeted file.

