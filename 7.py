kirill, arina, sergey = map(int, input().split())
if kirill > arina and kirill > sergey:
    print(kirill)
elif arina > kirill and arina > sergey:
    print(arina)
elif sergey > arina and sergey > kirill:
    print(sergey)