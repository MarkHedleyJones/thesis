
import os

for filename in os.listdir('.'):
    if filename[-4:] == '.pdf':
        new_filename = filename[:-4].replace('.','p')
        os.rename('./' + filename, './' + new_filename + '.pdf')
        if filename.find('_mag') != -1:
            print("\dplot{" + filename.replace('_mag', '').replace('.pdf','') + "}{}")
    elif filename[-3:] != '.py' and filename [-4:] != '.pdf':
        os.rename('./' + filename, './' + filename + '.pdf')
