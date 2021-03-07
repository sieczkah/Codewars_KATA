"""https://www.codewars.com/kata/586538146b56991861000293/train/python"""

db = { 'A':'Alfa','B':'Bravo','C':'Charlie','D':'Delta','E':'Echo',
       'F':'Foxtrot','G':'Golf','H':'Hotel','I':'India','J':'Juliett',
       'K':'Kilo','L':'Lima','M':'Mike','N':'November','O':'Oscar',
       'P':'Papa','Q':'Quebec','R':'Romeo','S':'Sierra','T':'Tango',
       'U':'Uniform','V':'Victor','W':'Whiskey','X':'Xray','Y':'Yankee',
       'Z':'Zulu'
      }



def to_nato(words):
    return ' '.join([db[i] if i in db.keys() else i for i in words.upper().replace(' ', '')])
