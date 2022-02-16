Aufgabe 2: Test Driven Development

Dein Kollege musste die arbeit verlassen und du sollst die letzte benötigte Funktion in der Klasse "Account" implementieren

Dein Kollege hat dir einen Zettel hinterlassen.

Zettel:
    Hey Digga,
    sorry musste heute wieder früher schluss machen, hab fast einen Termin verschwizt,
    kennst das ja :)
    Ich hatte mir gedacht das die Funktion "initialize_payment" heißen soll
    und sie einen string zurückgibt.
    Du musst dann nur gucken ob es wieder zeit zum bezahlen ist wenn das nicht der fall ist,
    dann gib nen text zurück, wenn doch dann betrag berechnen und validieren dann für beide
    fälle texte ausgeben. 

    denk daran das wir erst die Tests schreiben dann den Code!

    danke Digga, bis morgen

    ps: 80% Coverage für die Klasse Account ist gut aber 100% wäre besser :)


TIP: 

als du bemerkst das du keine ahnung hast was du tun sollst, bekommst du eine email deines
Kollegen.

Email:
    Yo Digga,
    hab ganz vergessen, du bist ja noch neu, falls du Hilfe brauchst ich habe den Code schon vor augen vielleicht hilft dir das ja bei dem erstellen der Tests.

    wenn self.check_payment_intervall():
    dann reutrn ("nutzername" does not have to pay yet)

    sonst beitrag berechnen 
        -> self.payment_intervall.payment_intervall_in_months() * self.membership get_fee()
    
        wenn payment_service.validate_payment(True):
            dann bezahlen und 
            return f"payment on {self.current_date} successful"
        sonst return "payment not successful"
      
