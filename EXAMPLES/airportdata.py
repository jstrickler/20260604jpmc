def read_airport_data(file_name):
    """
    Read airport data from flat file and return a dictionary.
    """
    airport_codes = {}

    with open(file_name) as codes_in:
        for raw_line in codes_in:
            line = raw_line.rstrip('\n')
            code = line[:3]  # first three chars
            airport = line[4:]  # fifth char through end
            airport_codes[code] = airport
    return airport_codes