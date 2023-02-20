from zipfile import ZipFile
i = 1000

while i != 0:
    zip = 'matreshka_' + str(i) + '.zip'
    print(zip)

    with ZipFile(zip, "a") as parent_zip:
        comment = str(parent_zip.comment)
        passwd1 = comment.partition(': ')[-1]
        passwd2 = passwd1.partition("'")[0]

        passwd = bytes(passwd2, 'UTF-8')

        parent_zip.extractall(pwd=passwd)

    i -= 1
