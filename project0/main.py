import argparse
import incidents

def main(url,flag):
    if flag:
        #print("local_copy")
        pdf_string = incidents.extractpdflocal(url)
    else:
        #print("online_copy")
        data = incidents.getpdf(url)
        pdf_string = incidents.extractpdf(data)
    parsed_data = incidents.parsepdf(pdf_string)
    incidents.database(parsed_data)
    result = incidents.digest()
    for x in result:
        print(x[0],' | ',x[1])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--incidents', type=str, required=True,  help="Incident summary url.")
    parser.add_argument('--local',action='store_true')
    parser.add_argument('--online',dest = 'local', action = 'store_false')
    parser.set_defaults(local=False)
    args = parser.parse_args()
    main(args.incidents,args.local)
    
