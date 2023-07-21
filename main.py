#User input data

HP=float(print("Enter HP Value: "))
DEF=float(print("Enter DEF Value: "))
SHD=float(print("Enter Shield Value: "))
RED=float(print("Enter DMG Reduction Value: ")

#Operation starts
if DEF>=500:
          Result=HP-(25*(15-SHD)*((100-RED)/100))
else:
Result=HP-((500-DEF)*(15-SHD))*((100-RED)/100))

#Display Result
if Result<0:
  print("Operator did not survive")
else:
  print(f"Operator survive with {Result} HP left")
