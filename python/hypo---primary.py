# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"34220.0","system":"readv2"},{"code":"53981.0","system":"readv2"},{"code":"49334.0","system":"readv2"},{"code":"15565.0","system":"readv2"},{"code":"23315.0","system":"readv2"},{"code":"26702.0","system":"readv2"},{"code":"11146.0","system":"readv2"},{"code":"14704.0","system":"readv2"},{"code":"3941.0","system":"readv2"},{"code":"43136.0","system":"readv2"},{"code":"677.0","system":"readv2"},{"code":"70244.0","system":"readv2"},{"code":"44405.0","system":"readv2"},{"code":"3290.0","system":"readv2"},{"code":"26699.0","system":"readv2"},{"code":"26833.0","system":"readv2"},{"code":"3194.0","system":"readv2"},{"code":"68512.0","system":"readv2"},{"code":"20310.0","system":"readv2"},{"code":"31971.0","system":"readv2"},{"code":"11426.0","system":"readv2"},{"code":"100476.0","system":"readv2"},{"code":"3857.0","system":"readv2"},{"code":"24748.0","system":"readv2"},{"code":"56722.0","system":"readv2"},{"code":"61498.0","system":"readv2"},{"code":"26701.0","system":"readv2"},{"code":"100004.0","system":"readv2"},{"code":"15790.0","system":"readv2"},{"code":"1472.0","system":"readv2"},{"code":"46985.0","system":"readv2"},{"code":"72690.0","system":"readv2"},{"code":"65907.0","system":"readv2"},{"code":"273.0","system":"readv2"},{"code":"57011.0","system":"readv2"},{"code":"23014.0","system":"readv2"},{"code":"26869.0","system":"readv2"},{"code":"1346.0","system":"readv2"},{"code":"106532.0","system":"readv2"},{"code":"69113.0","system":"readv2"},{"code":"65444.0","system":"readv2"},{"code":"3436.0","system":"readv2"},{"code":"53280.0","system":"readv2"},{"code":"20909.0","system":"readv2"},{"code":"18282.0","system":"readv2"},{"code":"51273.0","system":"readv2"},{"code":"5257.0","system":"readv2"},{"code":"49361.0","system":"readv2"},{"code":"10760.0","system":"readv2"},{"code":"1619.0","system":"readv2"},{"code":"59702.0","system":"readv2"},{"code":"95335.0","system":"readv2"},{"code":"73107.0","system":"readv2"},{"code":"19205.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('hypo-or-hyperthyroidism-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["hypo---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["hypo---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["hypo---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
