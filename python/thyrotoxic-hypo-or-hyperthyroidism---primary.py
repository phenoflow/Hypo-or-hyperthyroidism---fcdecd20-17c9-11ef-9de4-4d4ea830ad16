# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"C022000","system":"readv2"},{"code":"C023000","system":"readv2"},{"code":"1431.11","system":"readv2"},{"code":"C021.00","system":"readv2"},{"code":"F381600","system":"readv2"},{"code":"C05y400","system":"readv2"},{"code":"C02z000","system":"readv2"},{"code":"F4G2000","system":"readv2"},{"code":"C023.00","system":"readv2"},{"code":"C022.00","system":"readv2"},{"code":"C020100","system":"readv2"},{"code":"C02..12","system":"readv2"},{"code":"Cyu1300","system":"readv2"},{"code":"C023z00","system":"readv2"},{"code":"C02y000","system":"readv2"},{"code":"C02z.00","system":"readv2"},{"code":"C023100","system":"readv2"},{"code":"C022z00","system":"readv2"},{"code":"C020.00","system":"readv2"},{"code":"C02..00","system":"readv2"},{"code":"C02y100","system":"readv2"},{"code":"C021000","system":"readv2"},{"code":"C020000","system":"readv2"},{"code":"C02zz00","system":"readv2"},{"code":"C02z100","system":"readv2"},{"code":"G557500","system":"readv2"},{"code":"C02y.00","system":"readv2"},{"code":"C021z00","system":"readv2"},{"code":"C020z00","system":"readv2"},{"code":"C02yz00","system":"readv2"},{"code":"E05.9","system":"readv2"},{"code":"E06.2","system":"readv2"},{"code":"E05.2","system":"readv2"},{"code":"E05.0","system":"readv2"},{"code":"E05.8","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hypo-or-hyperthyroidism-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["thyrotoxic-hypo-or-hyperthyroidism---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["thyrotoxic-hypo-or-hyperthyroidism---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["thyrotoxic-hypo-or-hyperthyroidism---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
