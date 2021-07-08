# Die Elif Anweisung ist ähnlich wie die if Anweisung,
# jedoch wird sie nur aufgerufen, falls die if Anweisung nicht true war und somit nicht erfüllt wurde.
# Sollte die if Anweisung jedoch nicht erfüllt worden sein, und die elif Anweisung wurde erfüllt,
# dann wird der Code der elif Anweisung ausgeführt.


alter = 17
if alter >= 18 and alter < 100:
    print('Willkommen im Klub')
    # umstellen auf <= verändert das verhalten
elif alter == 16:
    print('Du bist 16')
elif alter == 17:
    print('Du bist 17')
else:
    print('Du bist zu alt')

