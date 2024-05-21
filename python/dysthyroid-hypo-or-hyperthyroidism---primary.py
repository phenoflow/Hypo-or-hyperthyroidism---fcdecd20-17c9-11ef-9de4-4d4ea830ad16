# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"C04..12","system":"readv2"},{"code":"C04z.12","system":"readv2"},{"code":"FyuBD00","system":"readv2"},{"code":"C06y100","system":"readv2"},{"code":"C02y300","system":"readv2"},{"code":"143..11","system":"readv2"},{"code":"1433.00","system":"readv2"},{"code":"66BZ.00","system":"readv2"},{"code":"66B4.00","system":"readv2"},{"code":"66B..00","system":"readv2"},{"code":"E05.5","system":"readv2"},{"code":"E05.1","system":"readv2"},{"code":"H06.2","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hypo-or-hyperthyroidism-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["dysthyroid-hypo-or-hyperthyroidism---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["dysthyroid-hypo-or-hyperthyroidism---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["dysthyroid-hypo-or-hyperthyroidism---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
