from airportdata import read_airport_data

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
    codes = read_airport_data(DATA_FILE)
    run_interactive_prompt(codes)



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

if __name__ == "__main__":  # if this is the main script, rather than an imported module
    main()