from pythonping import ping
from csv import reader
from datetime import datetime
timestamp = datetime.now()
timestamp = timestamp.strftime("%c")

with open ('devices.csv', 'r') as read_obj:
    csv_reader = reader(read_obj)
    hostNameList = list(csv_reader)

onlineCounter = 0
offlineCounter = 0


for hostRow in range (len(hostNameList)):
    r = ping (hostNameList[hostRow][1])
    if "Reply" in str(r):
        status = ("Online")
        onlineCounter +=1
    else:
        status = ("Offline")
        offlineCounter +=1

    hostNameList[hostRow].append(status)

hostNameList = sorted(hostNameList, key=lambda x:x[2])
itemCounter = onlineCounter + offlineCounter
print(hostNameList)

webWriter = open("webWriter.html", "w")
webWriter.write("""
<!DOCTYPE html>
<html>
<head>
<style>
#table1 {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}
#table1 td, # th {
  border: 1px solid #ddd;
  padding: 8px;
}
#table1 tr:nth-child(even){background-color: #f2f2f2;}
#table1 tr:hover {background-color: #ddd;}
#table1 th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: #04AA6D;
  color: white;
}
</style>
<H1> Ping Portal </H1>

""")
webWriter.close()

webWriter = open("webWriter.html", "a")
webWriter.write(f"""
<H2 style="color:black";">LAST CHECKED: {timestamp} </H2>
<H2 style="color:grey";">TOTAL ITEMS: {itemCounter} </H2>
<H2 style="color:red";">OFFLINE ITEMS:{offlineCounter} </H2>
<H2 style="color:green";">ONLINE  ITEMS:{onlineCounter} </H2>  
<table id="table1">
<tr> 
        <th>Hostname</th>
        <th>IP Address</th>
        <th>Status</th>
    </tr>
""")
webWriter.close()
for x in range (len(hostNameList)):
    for y in range (len(hostNameList[x])):
        print (x," ",y)
        if y == 0:
            tr = ("<tr>")
            print (tr)
        else:
            tr =f""""""
        #elif y == 2:
        if y == 2:
            tre = ("</tr>")
            print (tr)
        else:
            tre=f""""""
            print (tre)
    
        tableWriter = f"""
        {tr}<td style ="width 33.333%">{hostNameList[x][y]}</td>{tre}
    """



        ##print (myString)
    #closes writing
        webWriter = open("webWriter.html", "a")
        webWriter.write(tableWriter)
        webWriter.close()
webWriter = open("webWriter.html", "a")
webWriter.write ("""
</table>
</html>""")
webWriter.close()

pingerLog = open("PingerLog.txt", 'a')
pingerLog.write(str(timestamp) +" " + str(offlineCounter) + " Offline, " + str(onlineCounter) + " Online" +"\n")
pingerLog.close
print ("Finished")
exit
