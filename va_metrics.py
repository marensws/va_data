import os
def get_dose(file_name):
    doses=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 20, 25]
    file_number = int(file_name.split(sep='_')[3]) % 13
    return doses[file_number-1]

drugs = {
    'chlorpromazine': '34.5',
    "cisapride": "2.6",
    'diltiazem': '127.5',
    'dofetilide': '2.1',
    'mexiletine': '2503.2',
    'ondansetron': '358.5',
    'quinidine': "842.9",
    'ranolazine': '1948.2',
    'sotalol': "2.1",
    'terfenadine': '9',
    'verapamil': '45'
}
path = "/Users/sofiestubo/Documents/CS/MSc/project/data_convertion/va_data-main/50-150%"
with open("va_metrics-50-150.csv", "w") as metrics:
    metrics.write("Param#,Peak Voltage,RMP,Max Upstroke Velocity,APD1,APD2,APD3,Tri90-40,CTD90,CTD50,CaTamp,CaTmax,CaiD,EMw,qNet,EAD,Depolarization,Index,GNa,GNaL,Gto,GKr,GKs,GK1,Gncx,Pnak,PCa,drug,cnet,dose")
    metrics.write('\n')
    print(os.listdir(path + '/' + 'sotalol'))
    for drug in drugs.keys():
        for file in os.listdir(path+'/'+drug):
            if file != (".DS_Store" or ".git"):
                with open(path+'/'+drug+'/'+file) as f:
                    print(f)
                    lis = [line.split() for line in f]
                    print (lis)
                    dose = str(get_dose(f.name))
                    print(dose)
                    cnet = drugs.get(drug)
                    for i in range(42, len(lis)):
                        line = str(lis[i][0])
                        metrics.writelines(line+','+drug+','+cnet+','+dose+ '\n')
                f.close()
    metrics.close()




