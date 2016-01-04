import sys
import os
import subprocess
import csv

if len(sys.argv) < 2:
    print('Usage: batchClone [path to csv file with urls] [path to output folder]')
    exit()
else:
    csv_path = os.path.abspath(sys.argv[1])
    out_path = os.path.abspath(sys.argv[2])

    if not (os.path.isdir(out_path)):
        os.system("mkdir %s" % out_path)
    
    reader = csv.reader(open(csv_path, 'rt', encoding='utf8'), delimiter=';')
    for row in reader:
        print(row)
        url = row[1] # this is the column with the GitHub url
        stub = '/'.join(url.split('/')[-2:])
        folder_name = os.path.join(out_path, '_____'.join(stub.split('/')))
        stub.lstrip(' \t')
        url.lstrip(' \t')
        print(stub)
        try:
            if not os.path.exists(folder_name):
                proc = subprocess.Popen(['git', 'clone', url, folder_name],
                                    stderr=subprocess.PIPE,
                                    stdout=subprocess.PIPE)
                stdout_value = proc.communicate()[0]
                print('DONE:', folder_name)
            else:
                print('SKIPPED:', folder_name)
        except:
            print('FAILED:', folder_name)