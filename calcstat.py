import pandas as pd
from sys import argv

def CalcValues(data):
    arr = [0,0,0,0,0]
    arr[0] = data['elapsed'].mean()
    arr[1] = data['elapsed'].max()
    arr[2] = data['elapsed'].min()
    arr[3] = data['elapsed'].count()
    arr[4] = data['elapsed'].median()
    return arr

def PrintValues(record):
    label = ['Average','Max','Min','Count','Median']
    list_len = len(label)
    for i in range (0,list_len):
        print(label[i] + ': ' + str(record[i]))

def run(pathtofile):
    df = pd.read_csv(pathtofile)
    one_filter = df[df.label != 'youtube']
    #print(one_filter)
    sec_filter = one_filter[one_filter.success != 'true']
    #print(sec_filter)
    test_val = CalcValues(sec_filter)
    PrintValues(test_val)

if __name__ == '__main__':
    num = len(argv)
    if num != 2:
        print(argv[0] + ' require only the path to the csv file')
        filepath = input("please supply path to file:")
    else:
        filepath = argv[1]
    run(filepath)










