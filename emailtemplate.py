from datatohtml import getMoneyLineHTML
from test import listOfBets

ml = getMoneyLineHTML(listOfBets)

template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <table border="3" 
           style="background-color: #FFFFFF;
                  border:1.5px solid #000000;
                  border-radius: 10px;
                  width:100%;
                 " 
           cellpadding="10"
           cellspacing="3"           
    >
        <tr>
            <td style="border-radius: 10px;
                       text-align: center;
                       "> 
                Game 
            </td>

            <td style="border-radius: 10px;
                       text-align: center;
                       "> 
                Home 
            </td>

            <td style="border-radius: 10px;
                       text-align: center;
                       "> 
                Away 
            </td>
        </tr>
        
        {moneyLines}

        
    </table>
</body>
</html>
""".format(moneyLines = ml)



