filestream = open('./zarobki.dat')
text = filestream.read()
filestream.close()

def parseRows(text): 
  lines=text.splitlines()
  def lineToObject(line):
    fragments = line.split()  #sx rk yr dg yd sl
    obj = dict();
    obj['sx'] = fragments[0]
    obj['rk'] = fragments[1]
    obj['yr'] = fragments[2]
    obj['dg'] = fragments[3]
    obj['yd'] = fragments[4]
    obj['sl'] = fragments[5]
    return obj
  return map(lineToObject, lines)


objs = parseRows(text)

# Statystyki opisowe

