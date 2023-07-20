from abc import ABC, abstractmethod

class Data_Storage(ABC):

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def delete(self):
        pass

class Data_Base_Saving(Data_Storage):

    def save(self):
        print('Data is Saved in the DB.')

    def load(self):
        print('Uploading Data to DB...\nDone.')

    def delete(self):
        print('Data is removed from the DB')

class File_Saving(Data_Storage):

    def save(self):
        print('Data is Saved in the File.')

    def load(self):
        print('Uploading Data to File...\nDone.')

    def delete(self):
        print('Data is removed from the File')

DBS = Data_Base_Saving()
DBS.save()
DBS.load()
DBS.delete()

print()

FS = File_Saving()
FS.save()
FS.load()
FS.delete()