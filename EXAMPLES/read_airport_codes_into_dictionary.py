DATA_FILE = '../DATA/world_airport_codes.txt'
# sample data
# ABE ALLENTOWN, PENNSYLVANIA, USA
# ABF ABAIANG, REP. OF KIRIBATI
# ABG ABINGDON, QLD., AUSTRALIA

def main():
    """
    Program entry point
    """
    # data_file = read_config() 
    codes = read_data(DATA_FILE)
    run_interactive_prompt(codes)

def read_data(file_name):
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

def run_interactive_prompt(codes):
    """
    Run interactive prompt to retrieve cities from airport codes.
    """
    while True:
        code = input("Enter airport code: ")
        if code == '': # user just pressed <ENTER>
            print("Please enter a code")
            continue
        if code == 'q':
            print("goodbye")
            break
        
        # use code.upper() so user can type in lower or upper
        city = codes.get(code.upper(), "NOT FOUND")
        print(city)

if __name__ == "__main__":
    main()