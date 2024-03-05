
def check_which_version_bigger(version1, version2):
    versionList1 = version1.split('.')
    #print(versionList1)
    versionList2 = version2.split('.')
    #print(versionList2)

    str_versionList1 = ''.join(versionList1)
    str_versionList2 = ''.join(versionList2)
    int1 = int(str_versionList1[:-1])
    int2 = int(str_versionList2[:-1])
    #print("Int version1", int1, ' version2:', int2)

    if int1>=int2: last_version = version1
    if int2>int1: last_version = version2

    return print("Method1. Bigger version", last_version)

def check_which_version_bigger_fast(version1, version2):
    list = [version1, version2]
    return print("Method2. Bigger version", sorted(list)[-1])


check_which_version_bigger('124.2.1.24b', '125.2.1.23a')
check_which_version_bigger_fast('126.2.1.24b', '125.2.1.23a')
