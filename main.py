import csv

FILE="file.csv"
FILE_2="alloted.csv"
branch = {'1':7,'2':8,'3':13,'4':10,'7':22,'8':5,'A':13,'B':10}
cutoff = {'1':10,'2':10,'3':10,'4':10,'7':10,'8':10,'A':10,'B':10}

def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-like object"""

    opened_file = open(raw_file)

    csv_data = csv.reader(opened_file, delimiter=delimiter)

    parsed_data = []

    fields = next(csv_data)

    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    opened_file.close()

    return (parsed_data)

def addnew(new_data):
    """Writes back alloted stuff into csv file"""

    keys = new_data[0].keys()
    with open(FILE_2, 'w') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(new_data)


def allot(new_data):
    for i in range(len(new_data)):
        prefcount='1'
        for j in range(8):
            x=new_data[i][prefcount]
            a,b=x
            if(branch[b]>0):
                new_data[i]['alloted']=x
                branch[b]-=1
                cutoff[b]=new_data[i]['CG Year 1']
                break
            else:
                prefcount=ord(prefcount)-48
                prefcount+=49
                prefcount=chr(prefcount)

def main():
    new_data = parse(FILE, ",")
    allot(new_data)
    print(cutoff)
    addnew(new_data)



if __name__ == "__main__":
    main()
