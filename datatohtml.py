
def getMoneyLineHTML(lst):
    outputStr = ''

    for bet in lst:
        outputStr += f""" 
                        <tr>
                            <td style="border-radius: 10px;
                                       text-align: center;
                                       width: 33%;
                                      "> 
                                {bet.teams['away']} at {bet.teams['home']} 
                            </td>

                            <td style="border-radius: 10px;
                                       text-align: center;
                                       width: 33%;
                                      "> 
                                {bet.moneyLine['homeMoneyLine']} 
                            </td>

                            <td style="border-radius: 10px;
                                       text-align: center;
                                       width: 33%;
                                      "> 
                                {bet.moneyLine['awayMoneyLine']} 
                            </td>
                        </tr>
                     """
    
    return outputStr