class FilesHandle:

    def __new__(cls):

        if not hasattr(cls, 'instance'):
            cls.instance = super(FilesHandle, cls).__new__(cls)

        return cls.instance

    def delete_files_in_folder(self, mydir, endwith):
        import os
        filelist = [f for f in os.listdir(mydir) if f.endswith(endwith)]
        for f in filelist:
            os.chmod(os.path.join(mydir, f), 0o777)
            os.remove(os.path.join(mydir, f))
