dirs = [
    ( 'folder1',
        [
            'file1',
            ( 'folder2', 
                [
                    'file2',
                    'file3'
                ] 
            ),
            ( 'folder3', 
                [
                    'file3', 
                    'file4',
                    ('folder4', ['file3'])
                ] 
            ),
            'file5'
        ]
    )
]
 
# ВАШ КОД ТУТ

def flat(S):
    if S == []:
        return S
    if type(S[0]) == list:
        return flat(S[0]) + flat(S[1:])
    return S[:1] + flat(S[1:])

def search(dirs, filename, string="", fold = ""): 
    arr = []
    for i in range(len(dirs)):
        repos = string
        if type(dirs[i]) == tuple:
            string += "/" + dirs[i][0]
            arr.append(search(dirs[i], filename, string, fold=dirs[i][0]))
        elif type(dirs[i]) == list:
            arr.append(search(dirs[i], filename, string))
        elif dirs[i] == filename:
            if filename != fold:
                arr.append(string+"/"+dirs[i])
            else:
                string_last = string[8:]
                if string_last == '':
                    string_last = []
                arr.append(string_last)
        string = repos
    return flat(arr)


# ПЕРЕВІРКА

print(search(dirs, 'file1'))
print(search(dirs, 'file2'))
print(search(dirs, 'file3'))
print(search(dirs, 'file4'))
print(search(dirs, 'file5'))
print(search(dirs, 'file6'))
print(search(dirs, 'folder1'))
 
assert search(dirs, 'file1') == ['/folder1/file1'], 'Failed test for file1'
assert search(dirs, 'file2') == ['/folder1/folder2/file2'], 'Failed test for file2'
assert search(dirs, 'file3') == ['/folder1/folder2/file3', '/folder1/folder3/file3', '/folder1/folder3/folder4/file3'], 'Failed test for file3'
assert search(dirs, 'file4') == ['/folder1/folder3/file4'], 'Failed test for file4'
assert search(dirs, 'file5') == ['/folder1/file5'], 'Failed test for file5'
assert search(dirs, 'file6') == [], 'Failed test for file6'
assert search(dirs, 'folder1') == [], 'Failed test for folder1'
print('All tests good!')














