# PVGIS_API
Query data from PVGIS using the API

# Changelog
Version 1.1
- add a template input file (EU_random_points.xlsx) with random points across EU.
- include the time zone in the input file instead of a parameter for calculation. It allows now a data query from locations in different time zones.
- fix rounding problem of dates where hour = *:30h. 
- include a parameter to enable (or disable) the output file compression.

Version 1.0
- query data from point locations. The time zone will be automatically corrected based on the parameter added in the input session, however, it allows only one time zone at a time. If needed, the input file must be divided in multiple files according to the time zone locations.
- output files will be saved as csv compressed files. If errors are found, they will be saved in a separeted file.

