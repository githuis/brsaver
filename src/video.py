import os


class Video:
    name = ""
    directory = ""
    file_format = ""
    bytes = 0
    seconds = 0
    bitrate_kbps = 0
    streams = []

    def __init__(self, fullpath):
        self.fullpath = fullpath
        self.directory = os.path.dirname(os.path.realpath(fullpath))
        tmp = fullpath.split('/')[-1]
        self.name = os.path.splitext(tmp)[0]
        self.format = os.path.splitext(tmp)[1]
        self.streams = []

    def __repr__(self):
        return "{}:{}".format(self.name, self.bitrate_kbps)

    def get_tempfile_path(self):
        return self.directory + "/new" + self.name + self.format
