#2017510021 Hakan Cankul
#2020510026 Mustafa Efe Demir
import csv
import json

from blist import sorteddict
def jsonWrite(file):
    #writing to json
    json_object = json.dumps(file, indent=4)
    with open("query_done.json", "w") as outfile:
        outfile.write(json_object)
def delNameBased(students, operator, name , jsonFile):
    #deleting students by name matching
    temp = []
    if operator == '=':
        for key in students.keys():
            if students[key]['name'] == name:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)
    else:
        for key in students.keys():
            if students[key]['name'] != name:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)
def delIdBased(students, operator, id, jsonFile):
    #deleting students by id matching
    temp = []
    if operator == "=":
        for key in students.keys():
            if key == id:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)
    elif operator == "!=":
        for key in students.keys():
            if key != id:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)
    elif operator == "<" or operator == "!>":
        for key in students.keys():
            if key < id:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)
    elif operator == ">" or operator == "!<":
        for key in students.keys():
            if key > id:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)
    elif operator == ">=":
        for key in students.keys():
            if key >= id:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)
    elif operator == "<=":
        for key in students.keys():
            if key <= id:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)
    else:
        print("wrong operator")
def delLastnameBased(students, operator, lastname,jsonFile):
    # deleting students by lastname matching
    temp = []
    if operator == '=':
        for key in students.keys():
            if students[key]['lastname'] == lastname:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)
    else:
        for key in students.keys():
            if students[key]['lastname'] != lastname:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)
def delGradeBased(students, operator, grade,jsonFile):
    # deleting students by grade matching
    temp = []
    if operator == "=":
        for key in students.keys():
            if students[key]['grade'] == grade:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)

    elif operator == "!=":
        for key in students.keys():
            if students[key]['grade'] != grade:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)

    elif operator == "<" or operator == "!>":
        for key in students.keys():
            if students[key]['grade'] < grade:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)

    elif operator == ">" or operator == "!<":
        for key in students.keys():
            if students[key]['grade'] > grade:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)

    elif operator == ">=":
        for key in students.keys():
            if students[key]['grade'] >= grade:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)

    elif operator == "<=":
        for key in students.keys():
            if students[key]['grade'] <= grade:
                temp.append(key)
        if len(temp) == 0:
            print("there is no match")
        else:
            for key in temp:
                # json write
                a = students.pop(key)
                jsonFile.append(a)
                print(a)

    else:
        print("wrong operator")
def delLastnameAndGradeBased(students, lastname_op, lastname, grade_op, grade,jsonFile):
    # deleting students by lastname and grade matching
    if lastname_op == "=":
        temp = []
        if grade_op == "=":
            for key in students.keys():
                if students[key]['grade'] == grade and students[key]['lastname'] == lastname:
                    temp.append(key)
            if len(temp) == 0:
                print("there is no match")
            else:
                for key in temp:
                    # json write
                    a = students.pop(key)
                    jsonFile.append(a)
                    print(a)

        elif grade_op == "!=":
            for key in students.keys():
                if students[key]['grade'] != grade and students[key]['lastname'] == lastname:
                    temp.append(key)
            if len(temp) == 0:
                print("there is no match")
            else:
                for key in temp:
                    # json write
                    a = students.pop(key)
                    jsonFile.append(a)
                    print(a)

        elif grade_op == "<" or grade_op == "!>":
            for key in students.keys():
                if students[key]['grade'] < grade and students[key]['lastname'] == lastname:
                    temp.append(key)
            if len(temp) == 0:
                print("there is no match")
            else:
                for key in temp:
                    # json write
                    a = students.pop(key)
                    jsonFile.append(a)
                    print(a)

        elif grade_op == ">" or grade_op == "!<":
            for key in students.keys():
                if students[key]['grade'] > grade and students[key]['lastname'] == lastname:
                    temp.append(key)
            if len(temp) == 0:
                print("there is no match")
            else:
                for key in temp:
                    # json write
                    a = students.pop(key)
                    jsonFile.append(a)
                    print(a)

        elif grade_op == ">=":
            for key in students.keys():
                if students[key]['grade'] >= grade and students[key]['lastname'] == lastname:
                    temp.append(key)
            if len(temp) == 0:
                print("there is no match")
            else:
                for key in temp:
                    # json write
                    a = students.pop(key)
                    jsonFile.append(a)
                    print(a)

        elif grade_op == "<=":
            for key in students.keys():
                if students[key]['grade'] <= grade and students[key]['lastname'] == lastname:
                    temp.append(key)
            if len(temp) == 0:
                print("there is no match")
            else:
                for key in temp:
                    # json write
                    a = students.pop(key)
                    jsonFile.append(a)
                    print(a)
def delNameAndGradeBased(students, name_op, name, grade_op, grade,jsonFile):
    # deleting students by name and grade matching
    if name_op == "=":
        temp = []
        if grade_op == "=":
            for key in students.keys():
                if students[key]['grade'] == grade and students[key]['name'] == name:
                    temp.append(key)
            if len(temp) == 0:
                print("there is no match")
            else:
                for key in temp:
                    # json write
                    a = students.pop(key)
                    jsonFile.append(a)
                    print(a)

        elif grade_op == "!=":
            for key in students.keys():
                if students[key]['grade'] != grade and students[key]['name'] == name:
                    temp.append(key)
            if len(temp) == 0:
                print("there is no match")
            else:
                for key in temp:
                    # json write
                    a = students.pop(key)
                    jsonFile.append(a)
                    print(a)

        elif grade_op == "<" or grade_op == "!>":
            for key in students.keys():
                if students[key]['grade'] < grade and students[key]['name'] == name:
                    temp.append(key)
            if len(temp) == 0:
                print("there is no match")
            else:
                for key in temp:
                    # json write
                    a = students.pop(key)
                    jsonFile.append(a)
                    print(a)

        elif grade_op == ">" or grade_op == "!<":
            for key in students.keys():
                if students[key]['grade'] > grade and students[key]['name'] == name:
                    temp.append(key)
            if len(temp) == 0:
                print("there is no match")
            else:
                for key in temp:
                    # json write
                    a = students.pop(key)
                    jsonFile.append(a)
                    print(a)

        elif grade_op == ">=":
            for key in students.keys():
                if students[key]['grade'] >= grade and students[key]['name'] == name:
                    temp.append(key)
            if len(temp) == 0:
                print("there is no match")
            else:
                for key in temp:
                    # json write
                    a = students.pop(key)
                    jsonFile.append(a)
                    print(a)

        elif grade_op == "<=":
            for key in students.keys():
                if students[key]['grade'] <= grade and students[key]['name'] == name:
                    temp.append(key)
            if len(temp) == 0:
                print("there is no match")
            else:
                for key in temp:
                    # json write
                    a = students.pop(key)
                    jsonFile.append(a)
                    print(a)
def selGradeBasedbyName(students, operator, grade,order,jsonFile):
    # selecting students name by grade matching (ASC/DSC optionally)
    temp = sorteddict()

    if operator == "=":
        for key in students.keys():
            if students[key]['grade'] == grade:
                temp[key] = {'name': students[key]['name'], 'grade': students[key]['grade']}
        if len(temp) == 0:
            print("there is no match")
        else:
            if order == 'ASC':
                for key in sorted(temp, key=lambda x: temp[x]['name']):
                    print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
            else:
                for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                    print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
    elif operator == "!=":
        for key in students.keys():
            if students[key]['grade'] != grade:
                temp[key] = { 'name': students[key]['name'], 'grade': students[key]['grade']}
        if len(temp) == 0:
            print("there is no match")
        else:
            if order == 'ASC':
                for key in sorted(temp, key=lambda x: temp[x]['name']):
                    print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
            else:
                for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                    print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
    elif operator == "<" or operator == "!>":
        for key in students.keys():
            if students[key]['grade'] < grade:
                temp[key] = { 'name': students[key]['name'], 'grade': students[key]['grade']}
        if len(temp) == 0:
            print("there is no match")
        else:
            if order == 'ASC':
                for key in sorted(temp, key=lambda x: temp[x]['name']):
                    print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
            else:
                for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                    print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
    elif operator == ">" or operator == "!<":
        for key in students.keys():
            if students[key]['grade'] > grade:
                temp[key] = {'name': students[key]['name'], 'grade': students[key]['grade']}
        if len(temp) == 0:
            print("there is no match")
        else:
            if order == 'ASC':
                for key in sorted(temp, key=lambda x: temp[x]['name']):
                    print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
            else:
                for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                    print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
    elif operator == ">=":
        for key in students.keys():
            if students[key]['grade'] >= grade:
                temp[key] = { 'name': students[key]['name'], 'grade': students[key]['grade']}
        if len(temp) == 0:
            print("there is no match")
        else:
            if order == 'ASC':
                for key in sorted(temp, key=lambda x: temp[x]['name']):
                    print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
            else:
                for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                    print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
    elif operator == "<=":
        for key in students.keys():
            if students[key]['grade'] <= grade:
                temp[key] = { 'name': students[key]['name'], 'grade': students[key]['grade']}
        if len(temp) == 0:
            print("there is no match")
        else:
            if order == 'ASC':
                for key in sorted(temp, key=lambda x: temp[x]['name']):
                    print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
            else:
                for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                    print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
    else:
        print("wrong operator")
def selGradeBasedbyLastname(students, operator, grade,order,jsonFile):
    # selecting students lastname by grade matching (ASC/DSC optionally)
    temp = sorteddict()

    if operator == "=":
        for key in students.keys():
            if students[key]['grade'] == grade:
                temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
        if len(temp) == 0:
            print("there is no match")
        else:
            if order == 'ASC':
                for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                    print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
            else:
                for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                    print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
    elif operator == "!=":
        for key in students.keys():
            if students[key]['grade'] != grade:
                temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
        if len(temp) == 0:
            print("there is no match")
        else:
            if order == 'ASC':
                for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                    print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
            else:
                for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                    print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
    elif operator == "<" or operator == "!>":
        for key in students.keys():
            if students[key]['grade'] < grade:
                temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
        if len(temp) == 0:
            print("there is no match")
        else:
            if order == 'ASC':
                for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                    print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
            else:
                for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                    print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
    elif operator == ">" or operator == "!<":
        for key in students.keys():
            if students[key]['grade'] > grade:
                temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
        if len(temp) == 0:
            print("there is no match")
        else:
            if order == 'ASC':
                for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                    print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
            else:
                for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                    print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
    elif operator == ">=":
        for key in students.keys():
            if students[key]['grade'] >= grade:
                temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
        if len(temp) == 0:
            print("there is no match")
        else:
            if order == 'ASC':
                for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                    print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
            else:
                for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                    print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
    elif operator == "<=":
        for key in students.keys():
            if students[key]['grade'] <= grade:
                temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
        if len(temp) == 0:
            print("there is no match")
        else:
            if order == 'ASC':
                for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                    print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
            else:
                for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                    print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                    a = students.pop(key)
                    jsonFile.append(a)
    else:
        print("wrong operator")
def selGradeAndNameBasedbyName(students,grade_op,grade,logic,name_op,name,order,jsonFile ):
    # selecting students name by grade and name matching (ASC/DSC optionally)
    # all selecting names are same so arrangment by id ( because we are selecting lastname that correct lastname condition
    temp = sorteddict()
    if logic == 'AND' or logic == 'and':
        if name_op == '=':
            if grade_op == "=":
                for key in students.keys():
                    if students[key]['grade'] == grade and students[key]['name'] == name:
                        temp[key] = {'name': students[key]['name'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['name']):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == "!=":
                for key in students.keys():
                    if students[key]['grade'] != grade and students[key]['name'] == name:
                        temp[key] = {'name': students[key]['name'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['name']):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == "<" or grade_op == "!>":
                for key in students.keys():
                    if students[key]['grade'] < grade and students[key]['name'] == name:
                        temp[key] = {'name': students[key]['name'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['name']):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == ">" or grade_op == "!<":
                for key in students.keys():
                    if students[key]['grade'] > grade and students[key]['name'] == name:
                        temp[key] = {'name': students[key]['name'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['name']):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == ">=":
                for key in students.keys():
                    if students[key]['grade'] >= grade and students[key]['name'] == name:
                        temp[key] = {'name': students[key]['name'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['name']):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == "<=":
                for key in students.keys():
                    if students[key]['grade'] <= grade and students[key]['name'] == name:
                        temp[key] = {'name': students[key]['name'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['name']):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            else:
                print("wrong grade_op")
        elif name_op == '!=':
            if grade_op == "=":
                for key in students.keys():
                    if students[key]['grade'] == grade and students[key]['name'] != name:
                        temp[key] = {'name': students[key]['name'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['name']):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == "!=":
                for key in students.keys():
                    if students[key]['grade'] != grade and students[key]['name'] != name:
                        temp[key] = {'name': students[key]['name'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['name']):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == "<" or grade_op == "!>":
                for key in students.keys():
                    if students[key]['grade'] < grade and students[key]['name'] != name:
                        temp[key] = {'name': students[key]['name'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['name']):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == ">" or grade_op == "!<":
                for key in students.keys():
                    if students[key]['grade'] > grade and students[key]['name'] != name:
                        temp[key] = {'name': students[key]['name'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['name']):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == ">=":
                for key in students.keys():
                    if students[key]['grade'] >= grade and students[key]['name'] != name:
                        temp[key] = {'name': students[key]['name'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['name']):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == "<=":
                for key in students.keys():
                    if students[key]['grade'] <= grade and students[key]['name'] != name:
                        temp[key] = {'name': students[key]['name'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['name']):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['name'], reverse=True):
                            print(key + " " + temp[key]['name'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            else:
                print("wrong grade_op")
def selGradeAndNameBasedbyLastname(students, grade_op, grade, logic, lastname_op, lastname, order,jsonFile):
    # selecting students lastname by grade and name matching (ASC/DSC optionally)
    # all selecting lastnames are same so arrangment by id (because we are selecting name that correct name condition)
    temp = sorteddict()
    if logic == 'AND' or logic == 'and':
        if lastname_op == '=':
            if grade_op == "=":
                for key in students.keys():
                    if students[key]['grade'] == grade and students[key]['lastname'] == lastname:
                        temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == "!=":
                for key in students.keys():
                    if students[key]['grade'] != grade and students[key]['lastname'] == lastname:
                        temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == "<" or grade_op == "!>":
                for key in students.keys():
                    if students[key]['grade'] < grade and students[key]['lastname'] == lastname:
                        temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == ">" or grade_op == "!<":
                for key in students.keys():
                    if students[key]['grade'] > grade and students[key]['lastname'] == lastname:
                        temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == ">=":
                for key in students.keys():
                    if students[key]['grade'] >= grade and students[key]['lastname'] == lastname:
                        temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == "<=":
                for key in students.keys():
                    if students[key]['grade'] <= grade and students[key]['lastname'] == lastname:
                        temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            else:
                print("wrong grade_op")
        elif lastname_op == '!=':
            if grade_op == "=":
                for key in students.keys():
                    if students[key]['grade'] == grade and students[key]['lastname'] != lastname:
                        temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == "!=":
                for key in students.keys():
                    if students[key]['grade'] != grade and students[key]['lastname'] != lastname:
                        temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == "<" or grade_op == "!>":
                for key in students.keys():
                    if students[key]['grade'] < grade and students[key]['lastname'] != lastname:
                        temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == ">" or grade_op == "!<":
                for key in students.keys():
                    if students[key]['grade'] > grade and students[key]['lastname'] != lastname:
                        temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            elif grade_op == ">=":
                for key in students.keys():
                    if students[key]['grade'] >= grade and students[key]['lastname'] != lastname:
                        temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)

            elif grade_op == "<=":
                for key in students.keys():
                    if students[key]['grade'] <= grade and students[key]['lastname'] != lastname:
                        temp[key] = {'lastname': students[key]['lastname'], 'grade': students[key]['grade']}
                if len(temp) == 0:
                    print("there is no match")
                else:
                    if order == 'ASC':
                        for key in sorted(temp, key=lambda x: temp[x]['lastname']):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
                    else:
                        for key in sorted(temp, key=lambda x: temp[x]['lastname'], reverse=True):
                            print(key + " " + temp[key]['lastname'] + " " + temp[key]['grade'])
                            a = students.pop(key)
                            jsonFile.append(a)
            else:
                print("wrong grade_op")
def QUERY(students,input,jsonFile):
    temp = []
    temp = input.split()
    #all queries done in def QUERY
    #for all query have case sensitive
    #inputs must be appropriate to format where assignment pdf!!

    if input[0:27] == "INSERT INTO STUDENTS VALUES" and input[27] == '(' and input[-1] == ')':
        #INSERT INTO STUDENTS VALUES(15000,Yaman,Efe,ali.veli@spacex.com,20) -> example input
        value = input[28:-1].split(',')
        students[value[0]] = {'name': value[1], 'lastname': value[2], 'email': value[3], 'grade': value[4]}
        print(students[value[0]])
        print("inserting succesfully!")
        jsonFile.append(input)
        jsonFile.append(students[value[0]])
    elif input[0:26] == "DELETE FROM STUDENTS WHERE" and len(temp) == 7:
        new_input = input[27:]
        temp = new_input.split(' ')
        attribute = temp[0]
        # DELETE FROM STUDENTS WHERE name = ‘Marvin’ -> example input
        if attribute == 'name':
            operator = temp[1]
            name = temp[2]
            name = name.replace("‘", "").replace("’", "")
            jsonFile.append(input)
            delNameBased(students, operator, name, jsonFile)

        # DELETE FROM STUDENTS WHERE grade <= 20 -> example input
        elif attribute == 'grade':
            operator = temp[1]
            grade = temp[2]
            jsonFile.append(input)
            delGradeBased(students, operator, grade,jsonFile)

        # DELETE FROM STUDENTS WHERE lastname = ‘Homenick’ -> example input
        elif attribute == 'lastname':
            operator = temp[1]
            las_name = temp[2]
            las_name = las_name.replace("‘", "").replace("’", "")
            jsonFile.append(input)
            delLastnameBased(students, operator, las_name,jsonFile)

        # DELETE FROM STUDENTS WHERE id <= 30000 -> example input
        elif attribute == "id":
            operator = temp[1]
            id = temp[2]
            jsonFile.append(input)
            delIdBased(students, operator, id,jsonFile)

        else:
            print("wrong command")
    elif input[0:26] == "DELETE FROM STUDENTS WHERE" and len(temp) == 11:
        # name OR grade in order
        if temp[4] == 'name' and temp[7] == 'or' and temp[8] == 'grade':
            # DELETE FROM STUDENTS WHERE name = ‘Saige’ or grade <= 30 -> example input
            new_input = input[27:]
            temp = new_input.split(' ')
            name_op = temp[1]
            name = temp[2]
            name = name.replace("‘", "").replace("’", "")
            grade = temp[6]
            grade_op = temp[5]
            jsonFile.append(input)
            delNameBased(students, name_op, name,jsonFile)
            delGradeBased(students, grade_op, grade,jsonFile)


        # name AND grade in order
        if temp[4] == 'name' and temp[7] == 'and' and temp[
            8] == 'grade':
            # DELETE FROM STUDENTS WHERE name = ‘Toni’ and grade <= 40 -> example input
            new_input = input[27:]
            temp = new_input.split(' ')
            name_op = temp[1]
            name = temp[2]
            name = name.replace("‘", "").replace("’", "")
            grade = temp[6]
            grade_op = temp[5]
            jsonFile.append(input)
            delNameAndGradeBased(students, name_op, name, grade_op, grade,jsonFile)


        # lastname AND grade in order
        if temp[4] == 'lastname' and temp[7] == 'and' and temp[
            8] == 'grade':
            # DELETE FROM STUDENTS WHERE lastname = ‘Skiles’ and grade = 50 -> example input
            new_input = input[27:]
            temp = new_input.split(' ')
            lastname_op = temp[1]
            lastname = temp[2]
            lastname = lastname.replace("‘", "").replace("’", "")
            grade = temp[6]
            grade_op = temp[5]
            jsonFile.append(input)
            delLastnameAndGradeBased(students, lastname_op, lastname, grade_op, grade,jsonFile)


        # lastname OR grade in order
        if input[0:26] == "DELETE FROM STUDENTS WHERE" and temp[4] == 'lastname' and temp[7] == 'or' and temp[
                8] == 'grade':
            # DELETE FROM STUDENTS WHERE lastname = ‘Predovic’ or grade <= 45 -> example input
            new_input = input[27:]
            temp = new_input.split(' ')
            lastname_op = temp[1]
            lastname = temp[2]
            lastname = lastname.replace("‘", "").replace("’", "")
            grade = temp[6]
            grade_op = temp[5]
            jsonFile.append(input)
            delLastnameBased(students,lastname_op, lastname,jsonFile)
            delGradeBased(students,grade_op,grade,jsonFile)

        # select name by grade
    elif input[0:31] == "SELECT name FROM STUDENTS WHERE" and len(temp) == 11:

        #SELECT name FROM STUDENTS WHERE grade > 50 ORDER BY DSC/ASC -> example input
        new_input = input[32:]
        temp = new_input.split()
        grade_op = temp[1]
        grade = temp[2]
        order = temp[5]
        jsonFile.append(input)
        selGradeBasedbyName(students,grade_op,grade,order,jsonFile)

    elif input[0:35] == "SELECT lastname FROM STUDENTS WHERE" and len(temp) == 11:
        # SELECT lastname FROM STUDENTS WHERE grade > 60 ORDER BY DSC/ASC -> example input
        new_input = input[36:]
        temp = new_input.split()
        grade_op = temp[1]
        grade = temp[2]
        order = temp[5]
        jsonFile.append(input)
        selGradeBasedbyLastname(students, grade_op, grade, order,jsonFile)

    elif input[0:31] == "SELECT name FROM STUDENTS WHERE" and len(temp) == 15:
        # SELECT name FROM STUDENTS WHERE grade > 50 AND name = ‘Ariane’ ORDER BY DSC -> example input

        new_input = input[32:]
        temp = new_input.split()
        grade_op =  temp[1]
        grade = temp[2]
        logic = temp[3]
        name_op = temp[5]
        name = temp[6]
        name = name.replace("‘", "").replace("’", "")
        order = temp[9]
        jsonFile.append(input)
        selGradeAndNameBasedbyName(students,grade_op,grade,logic,name_op,name,order,jsonFile)

    elif input[0:35] == "SELECT lastname FROM STUDENTS WHERE" and len(temp) == 15:
        #SELECT lastname FROM STUDENTS WHERE grade > 50 AND lastname = ‘Spencer’ ORDER BY DSC -> example input
        new_input = input[36:]
        temp = new_input.split()
        grade_op = temp[1]
        grade = temp[2]
        logic = temp[3]
        lastname_op = temp[5]
        lastname = temp[6]
        lastname = lastname.replace("‘", "").replace("’", "")
        order = temp[9]
        jsonFile.append(input)
        selGradeAndNameBasedbyLastname(students,grade_op,grade,logic,lastname_op,lastname,order,jsonFile)


    else:
        print("wrong command")

print("students.csv is reading..")
#studens.csv reading
studentsFile = open('students.csv', 'r')
#for sorted dic using soreddict
students = sorteddict()
#for write to json extra a 'jsonFile' list
jsonFile = []
for row in studentsFile:
    row = row.strip().split(';')
    if row[0] == 'id':
        continue
    students[row[0]] = {'name': row[1], 'lastname': row[2], 'email': row[3], 'grade': row[4]}
#avoiding the console closing
while True:
    #taking input again and again
    command = input("enter your command: ")
    if command == "exit":
        #writing all query to 'query_done.json' before closing
        #!!WARNING: don't terminate the program from IDE; json write doesn't work
        # for writing to json, 'exit' command must be entered
        jsonWrite(jsonFile)
        break
    else:
        QUERY(students, command,jsonFile)