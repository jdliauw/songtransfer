import os
import shutil

def run():

    cwd = os.getcwd()
    print ('cwd = {0}'.format(cwd))
    dst = str(cwd) + "/filtered"
    print ('dst = {0}'.format(dst))

    file_list = open('./mp3s.txt', 'r')

    for file in file_list:
        # Remove new lines and just get mp3 file name
        file = file.replace('\n', '')
        dst_file = file.replace('\n','')[file.rfind("/") + 1:]
        shutil.copy2(file, os.path.join(dst, dst_file))

if __name__ == "__main__":
    run()
