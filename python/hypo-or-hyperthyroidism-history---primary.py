# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"50275.0","system":"readv2"},{"code":"20035.0","system":"readv2"},{"code":"68626.0","system":"readv2"},{"code":"8038.0","system":"readv2"},{"code":"47695.0","system":"readv2"},{"code":"11322.0","system":"readv2"},{"code":"46630.0","system":"readv2"},{"code":"46057.0","system":"readv2"},{"code":"1567.0","system":"readv2"},{"code":"28822.0","system":"readv2"},{"code":"3611.0","system":"readv2"},{"code":"19367.0","system":"readv2"},{"code":"8268.0","system":"readv2"},{"code":"48167.0","system":"readv2"},{"code":"28852.0","system":"readv2"},{"code":"25913.0","system":"readv2"},{"code":"47521.0","system":"readv2"},{"code":"47658.0","system":"readv2"},{"code":"46640.0","system":"readv2"},{"code":"51416.0","system":"readv2"},{"code":"28530.0","system":"readv2"},{"code":"6245.0","system":"readv2"},{"code":"4937.0","system":"readv2"},{"code":"35608.0","system":"readv2"},{"code":"95885.0","system":"readv2"},{"code":"61069.0","system":"readv2"},{"code":"38976.0","system":"readv2"},{"code":"26362.0","system":"readv2"},{"code":"85661.0","system":"readv2"},{"code":"28735.0","system":"readv2"},{"code":"85955.0","system":"readv2"},{"code":"51706.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hypo-or-hyperthyroidism-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hypo-or-hyperthyroidism-history---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hypo-or-hyperthyroidism-history---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hypo-or-hyperthyroidism-history---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
