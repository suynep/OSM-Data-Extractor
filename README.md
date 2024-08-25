# To extract:

Run `extract_data.py` using `python3 extract_data.py`
> Note that the program uses `map.xml` as the data file, which must be present in the same directory as the `extract_data.py`

This step creates *3 files* -> `nodeData`, `wayData`, and `boundData`.

`nodeData` and `wayData` are colllections of dictionaries (new-line separated dict objects)
These extractions help in easy manipulation of OSM data.
