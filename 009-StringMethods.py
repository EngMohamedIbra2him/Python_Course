# Strings Methods

# Strip()                                      
# rstrip()  & lstrip()
msg1 = "     I Love Python      "   
print(msg1.strip())
print(msg1.rsplit())
print(msg1.lstrip())
msg2 = "#######I Love Python      "   
print(msg2.strip("#"))

# title()                                      

msg3 = "I Love programming with python "
print(msg3.title())

# capitalize()                                 

msg3 = "I Love programming with python "
print(msg3.capitalize())

# zfill()                                       
a , b ,c = "1", "11", "111"
print(a.zfill(4))
print(b.zfill(4))
print(c.zfill(4))

# upper()
msg4="Mohamed"
print(msg4.upper())

# lower()
msg5="MoHamed"
print(msg4.lower())

# split() rsplit()
msg6 = "I Love Python"
msg7 = "I-Love-Python"
print(msg6.split())
print(msg7.split("-"))
print(msg7.split("-",1))
print(msg7.rsplit("-",1))

# center()
msg8= "mohamed"
print(msg8.center(12,))
print(msg8.center(12,"$"))

# Count()
msg9="python python python Html Css sql sql sql sql"
print(msg9.count("python"))
print(msg9.count("sql"))
print(msg9.count("Html"))

# swapecase()
msg10="mY nAME iS mOHAMED"
print(msg10.swapcase())

#startwith()
msg11= "Mohamed"
print(msg11.startswith("M"))

#endswith()
msg11= "Mohamed"
print(msg11.endswith("d"))

# Index(start,end,step) & find()
msg12 = "I love Python"
print(msg12.find("I"))

# rjust(width , fill char) & ljust(width , fill char)
msg13 = "Mohamed"
print(msg13.rjust(10,"$"))
print(msg13.ljust(10,"$"))

# splitlines() 
msg14 ="""
first line 
second line 
third line
"""
print(msg14.splitlines())

# replce()
msg15 = "Hello world zpython"
msg16=msg15.replace("zpython","python")
print(msg15)
print(msg16)

# join(Iterable Object)
msg17= ["my","name","is","mohamed"]
print(" ".join(msg17))