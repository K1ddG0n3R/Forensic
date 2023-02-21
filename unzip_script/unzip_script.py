from zipfile import ZipFile
import os

i = 1000

while i != 0:
    zip = 'matreshka_' + str(i) + '.zip'


    with ZipFile(zip, "a") as parent_zip:
        comment = str(parent_zip.comment)
        passwd1 = comment.partition(': ')[-1]
        passwd2 = passwd1.partition("'")[0]

        passwd = bytes(passwd2, 'UTF-8')

        parent_zip.extractall(pwd=passwd)
        print(zip + '  successfully unziped with password:  ' + passwd2)

    path = os.path.join(os.path.abspath(os.path.dirname(__file__)), zip)
    os.remove(path)

    i -= 1
