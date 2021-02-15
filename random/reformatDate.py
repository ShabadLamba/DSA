def reformData():
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
              "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    date = "6th Dec 1933"
    data = date.split()
    data = data[::-1]
    output = ['', '', '']
    if(len(data[2]) < 4):
        output[2] += '0'
        for items in data[2]:
            if(items in '1234567890'):
                output[2] += items
    else:
        for items in data[2]:
            if(items in '1234567890'):
                output[2] += items

    if(months.index(data[1]) + 1 > 9):
        output[1] += str(months.index(data[1]) + 1)
    else:
        output[1] += '0' + str(months.index(data[1]) + 1)

    output[0] += data[0]

    print('-'.join(output))


reformData()
