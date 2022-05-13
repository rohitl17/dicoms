import os 
from pathlib import Path
import glob
import pydicom
import sys 
import shutil


def get_dcm_files(base_dir):
    '''
    Scan files from root directory to child node

    Input - Base Path
    Output - Its a generator 
    '''
    for entry in os.scandir(base_dir):
        if entry.is_file() and entry.name.endswith(".dcm"):
            yield entry.path
        elif entry.is_dir():
            yield from get_dcm_files(entry.path)
        else:
            print(f"Neither a file, nor a dir: {entry.path}")


def search_dcm(path):
    '''
    Search dicom and call function dicom anonymizer and saver.

    Input - Path of dicom files 
     
    Output - None 

    '''
    #mri_dicoms = []
    for dicom in get_dcm_files(path):
        print(dicom)
        try:
            dcm = pydicom.dcmread(dicom)
            if dcm.Modality == 'MRI' or dcm.Modality == 'MR' or dcm.Modality == 'CT' or dcm.Modality == 'OT':
                #mri_dicoms.append(dicom)
                dicom_anonymizer_saver(dicom)
                print('-------------------------------------------------------------------------------')
                #print(mri_dicoms)
        except :
            pass  
        
    return None
        

def dicom_anonymizer_saver(path_of_dicom):
    '''
    This function anonymize the dicom and save them in predefine folders of based on modality.

    Input = Path of dicom file where it is stored.

    Output = None 
    '''
    #mri_dicoms = list_of_dicoms
    #for i in range(len(mri_dicoms)):
    
    try:

        dcm = pydicom.dcmread(path_of_dicom)
        name = path_of_dicom
        name = name.split('/')
        name = name[-1]

        sid = dcm.StudyInstanceUID
        print(sid)

        list_of_tags = ['InstitutionName','InstitutionAddress','ReferringPhysicianName','ReferringPhysicianTelephoneNumbers',
        'StationName','InstitutionalDepartmentName','PhysiciansOfRecord','PerformingPhysicianName','NameOfPhysiciansReadingStudy','OperatorsName','AdmittingDiagnosesDescription',
        'MedicalRecordLocator','EthnicGroup','Occupation','AdditionalPatientHistory','PatientComments','PatientName','PatientID','OtherPatientIDs','OtherPatientNames','StudyID','RequestingPhysician','PhysicianOfRecord']


        for tag in list_of_tags:
            attribute = dcm.dir(tag)

            if len(attribute) == 1:
                if attribute[0] == 'InstitutionName':
                    dcm.InstitutionName = ''
                elif attribute[0] == 'InstitutionAddress':
                    dcm.InstitutionAddress = ''
                elif attribute[0] == 'ReferringPhysicianName':
                    dcm.ReferringPhysicianName = ''
                elif attribute[0] == 'ReferringPhysicianTelephoneNumbers':
                    dcm.ReferringPhysicianTelephoneNumbers = ''
                elif attribute[0] == 'StationName':
                    dcm.StationName = ''
                elif attribute[0] == 'InstitutionalDepartment':
                    dcm.InstitutionalDepartment = ''
                elif attribute[0] == 'PhysiciansOfRecord':
                    dcm.PhysiciansOfRecord = ''
                elif attribute[0] == 'PerformingPhysicianName':
                    dcm.PerformingPhysicianName = ''
                elif attribute[0] == 'NameOfPhysiciansReadingStudy':
                    dcm.NameOfPhysiciansReadingStudy = ''
                elif attribute[0] == 'OperatorsName':
                    dcm.OperatorsName = ''
                elif attribute[0] == 'AdmittingDiagnosesDescription':
                    dcm.AdmittingDiagnosesDescription = ''
                elif attribute[0] == 'MedicalRecordLocator':
                    dcm.MedicalRecordLocator = ''
                elif attribute[0] == 'EthnicGroup':
                    dcm.EthnicGroup = ''
                elif attribute[0] == 'Occupation':
                    dcm.Occupation = ''
                elif attribute[0] == 'AdditionalPatientHistory':
                    dcm.AdditionalPatientHistory = ''
                elif attribute[0] == 'PatientComments':
                    dcm.PatientComments = '' 
                elif attribute[0] == 'PatientName':
                    dcm.PatientName = '' 
                elif attribute[0] == 'PatientID':
                    dcm.PatientID = '' 
                elif attribute[0] == 'OtherPatientIDs':
                    dcm.OtherPatientIDs = '' 
                elif attribute[0] == 'OtherPatientNames':
                    dcm.OtherPatientNames = '' 
                elif attribute[0] == 'StudyID':
                    dcm.StudyID = ''
                elif attribute[0] == 'RequestingPhysician':
                    dcm.RequestingPhysician = ''
                elif attribute[0] == 'PhysicianOfRecord':
                    dcm.PhysicianOfRecord = ''
                else:
                    pass



        if dcm.Modality == 'CT':
            save_path = './CT/'
            if os.path.isdir(save_path+str(sid)):
                if os.path.isfile(save_path+str(sid)+'/'+'anonymize_'+name):
                    print('Already Exist')
                    #os.remove(save_path+str(sid))
                    #os.mkdir(save_path+str(sid))
                    #shutil.copy(mri_dicoms[i],save_path + str(sid)+'/'+name)
                    #shutil.move(mri_dicoms[i],save_path + str(sid)+'/'+name)
                else:
                    dcm.save_as(save_path+str(sid)+'/'+'anonymize_'+name)
                    #os.remove(mri_dicoms[i])
            else:
                os.mkdir(save_path+str(sid))
                if os.path.isfile(save_path+str(sid)+'/'+'anonymize_'+name):
                    print('Already Exist')
                    #shutil.copy(mri_dicoms[i],save_path + str(sid)+'/'+name)
                    #shutil.move(mri_dicoms[i],save_path + str(sid)+'/'+name)
                else:
                    dcm.save_as(save_path+str(sid)+'/'+'anonymize_'+name)
                    #os.remove(mri_dicoms[i])
                

        elif dcm.Modality == 'MRI' or dcm.Modality == 'MR':
            save_path = './MRI/'

            if os.path.isdir(save_path+str(sid)):
                if os.path.isfile(save_path+str(sid)+'/'+'anonymize_'+name):
                    print('Already Exist')
                    pass
                    #os.remove(save_path+str(sid))
                    #os.mkdir(save_path+str(sid))
                    #shutil.copy(mri_dicoms[i],save_path + str(sid)+'/'+name)
                    #shutil.move(mri_dicoms[i],save_path + str(sid)+'/'+name)
                else:
                    dcm.save_as(save_path+str(sid)+'/'+'anonymize_'+name)
                    #os.remove(path_of_dicom)
            else:
                os.mkdir(save_path+str(sid))
                if os.path.isfile(save_path+str(sid)+'/'+name):
                    print('Already Exist')
                    #shutil.copy(mri_dicoms[i],save_path + str(sid)+'/'+name)
                    #shutil.move(mri_dicoms[i],save_path + str(sid)+'/'+name)
                else:
                    dcm.save_as(save_path+str(sid)+'/'+'anonymize_'+name)
                    #os.remove(path_of_dicom)

        else:
            save_path = './XRAYS/'
            if os.path.isdir(save_path+str(sid)):
                if os.path.isfile(save_path+str(sid)+'/'+'anonymize_'+name):
                    print('Already Exist')
                    #os.remove(save_path+str(sid))
                    #os.mkdir(save_path+str(sid))
                    #shutil.copy(mri_dicoms[i],save_path + str(sid)+'/'+name)
                    #shutil.move(mri_dicoms[i],save_path + str(sid)+'/'+name)
                else:
                    dcm.save_as(save_path+str(sid)+'/'+'anonymize_'+name)
                    #os.remove(path_of_dicom)
            else:
                os.mkdir(save_path+str(sid))
                if os.path.isfile(save_path+str(sid)+'/'+name):
                    print('Already Exist')
                    #shutil.copy(mri_dicoms[i],save_path + str(sid)+'/'+name)
                    #shutil.move(mri_dicoms[i],save_path + str(sid)+'/'+name)
                else:
                    dcm.save_as(save_path+str(sid)+'/'+'anonymize_'+name)
                    #os.remove(path_of_dicom)
        #dcm = mri_dicoms[i]
        #dcm.studyId
        #shutil.copy(mri_dicoms[i],save_path + str(sid)+'/'+name)
        #shutil.move(mri_dicoms[i],save_path + str(sid)+'/'+name)
    except :
        pass




if __name__ == '__main__':
    all_paths = sys.argv
    print(all_paths)
    path = all_paths[1]
    search_dcm(path)
    
    
    

