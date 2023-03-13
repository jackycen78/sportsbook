def getCellHTML(text, size, rows=1):
    outputStr =  f'''
                    <td style="border-radius: 4px;
                               text-align: center;
                               width: {100 / size}%;
                               background-color: #FFFFFF;
                               padding: 0.5rem;
                               margin: 1.5px;
                              "
                        rowspan="{rows}"
                    > '''
    if type(text) == str:
            outputStr += f'{text} \n'
    elif type(text) == list:
        for t in text:
            outputStr += f'<br> {t} </br>'
    outputStr += '</td>'
    return outputStr

def getColumnHeadersHTML(columns):
    outputStr = '<tr> \n'

    for col in columns:
        outputStr +=  f'''
                        <th style="border-radius: 4px;
                                text-align: center;
                                width: {100 / len(columns)}%;
                                background-color: #FFFFFF;
                                padding: 0.5rem;
                                margin: 1.5px;
                                " 
                        > 
                        {col}
                        </th>
                       '''
    outputStr += '</tr>'
    return outputStr


def getTableHTML(title, columns, dataRows):
     
    outputStr = f'''
                    <h1> {title} </h1>

                        <table border="3" 
                               style="background-color: #FFFFFF;
                                      border:0px solid #000000;
                                      border-radius: 4px;
                                      width: 100%;
                                    " 
                               cellpadding="10"
                               cellspacing="3"       
                        >
                            {columns}
                            {dataRows}
                        </table>
                  '''     
    print(outputStr)
    return outputStr
