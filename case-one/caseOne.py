import sys

def check4Duplicates(fileData):
    usersByIDs = {}
    for line in fileData:
        if line != '' or line != '\n':
            tmp = line.split(':') # tmp = ['user1', '100', '100']
            try:
                # if ID is already added as key into JSON
                # then append user in related list
                usersByIDs[tmp[1]].append(tmp[0])
            except:
                # if user ID is not exist yet as key in the JSON
                # then create a new key with an list and append user
                usersByIDs[tmp[1]] = [ tmp[0] ]

    #usersByIDs = {'100': ['user1', 'user3'], '101':['user2']}
    return usersByIDs

def printOutDuplicateUsers(usersByIds):
    for key in usersByIds.keys():
        if len(usersByIds[key]) > 1:
            print(key + ': ' + ', '.join(usersByIds[key]))

def main():
    with open("/Users/arbade/Desktop/passwd") as f:
        usersByIds = check4Duplicates(f)
        printOutDuplicateUsers(usersByIds)
    f.close()

if __name__ == '__main__':
    main()
