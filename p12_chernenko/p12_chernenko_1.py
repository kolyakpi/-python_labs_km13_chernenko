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
 
def search(dirs, filename, string="", arr=[]): 
    if filename == dirs[0][0]:
        return []
    
    for i in range(len(dirs)):
        
        repos = string
        flag = 1
        if type(dirs[i]) == tuple:
            string += "/" + dirs[i][0]
            search(dirs[i], filename, string, arr)
        elif type(dirs[i]) == list:
            search(dirs[i], filename, string, arr)
        elif dirs[i] == filename:
            arr.append(string+"/"+dirs[i])
            flag = 0
        string = repos
        
    return arr


# ПЕРЕВІРКА
 
print(search(dirs, 'file1'))
print(search(dirs, 'file2', arr=[]))
print(search(dirs, 'file3', arr=[]))
print(search(dirs, 'file4', arr=[]))
print(search(dirs, 'file5', arr=[]))
print(search(dirs, 'file6', arr=[]))
print(search(dirs, 'folder1', arr=[]))
 
assert search(dirs, 'file1', arr=[]) == ['/folder1/file1'], 'Failed test for file1'
assert search(dirs, 'file2', arr=[]) == ['/folder1/folder2/file2'], 'Failed test for file2'
assert search(dirs, 'file3', arr=[]) == ['/folder1/folder2/file3', '/folder1/folder3/file3', '/folder1/folder3/folder4/file3'], 'Failed test for file3'
assert search(dirs, 'file4', arr=[]) == ['/folder1/folder3/file4'], 'Failed test for file4'
assert search(dirs, 'file5', arr=[]) == ['/folder1/file5'], 'Failed test for file5'
assert search(dirs, 'file6', arr=[]) == [], 'Failed test for file6'
assert search(dirs, 'folder1', arr=[]) == [], 'Failed test for folder1'
print('All tests good!')



















