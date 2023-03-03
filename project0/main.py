import argparse
import incidents

def main(url):
    data =incidents.getpdf(url)
    incidents.extractpdf(data)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True,  help="Incident summary url.")
    
    args = parser.parse_args()
    main(args.incidents)
    
