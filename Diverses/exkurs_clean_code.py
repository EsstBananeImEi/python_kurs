""""""
"""
    Clean Code ist ein Begriff aus der Softwaretechnik,
    der seinen Ursprung im gleichnamigen Buch von Robert Cecil Martin hat.
    Als „sauber“ bezeichnen Softwareentwickler in erster Linie Quellcode, aber auch Dokumente, Konzepte,
    Regeln und Verfahren, die intuitiv verständlich sind. Als intuitiv verständlich gilt alles,
    was mit wenig Aufwand und in kurzer Zeit richtig verstanden werden kann.
    Vorteile von Clean Code sind stabilere und effizient wartbarere Programme,
    d. h. kürzere Entwicklungszeiten bei Funktionserweiterung und Fehlerbehebungen.
    Die Bedeutung wächst mit der Beobachtung, dass im Schnitt 80 % der Lebensdauer einer Software auf den
    Wartungszeitraum entfällt.

    Schwierigkeiten beim Entwickeln von Clean Code liegen

        1. häufig in zunächst unklaren oder sich widersprechenden Anforderungen,
        2. zum Teil begründet im Fehlen von Erfahrung im Entwickeln von Clean Code,
        3. im Mangel an Disziplin beim Programmieren und
        4. im Aufwand nachträglicher Quellcode-Bereinigungen (dem sog. Refactoring).

    Die Notwendigkeit, Code noch nach der Entwicklung von „unsauberen“ Stellen zu reinigen,
    wird häufig nicht gesehen oder vom Management nicht bewilligt, sobald das Programm seine vorgesehene Funktion ausübt.
    Ein direktes Schreiben von „sauberem“ Code ist nahezu unmöglich,
    kann jedoch durch den bewussten Umgang mit den Prinzipien und Praktiken von Clean Code verbessert werden.

    Eng verbunden mit dem Begriff Clean Code sind Maßnahmen,
    die bei der Entwicklung von Software zu „sauberem“ Programmcode führen.
    So zahlreich wie die Gründe für „unsauberen“ Code sind, so vielfältig sind auch die vorgeschlagenen
    Regeln in den aufgestellten Maßnahmenkatalogen. Dazu gehören:

       - Quelltextformatierung (engl. code conventions),
       - Entwurfsmuster (engl. design patterns),
       - Konvention vor Konfiguration (engl. convention over configuration),
       - eine umfangreiche Menge an Vorschlägen aus dem Buch Clean Code von Robert C. Martin.

    Darüber hinaus gibt es seit einigen Jahren eine Clean-Code-Developer-Bewegung,
    die das Ziel verfolgt, ein einheitliches und umfassendes Regelwerk auf eine didaktisch ansprechende
    Weise in das Bewusstsein der Entwickler zu rücken und damit die Disziplin zu fördern,
    die Clean-Code-Maßnahmen im Programmieralltag auch tatsächlich anzuwenden.

    Die wichtigsten Clean-Code Regeln:
    
    #### Lesbarkeit vor Prägnanz ####
        Code muss funktionieren und von der ausführenden Maschine verstanden werden. 
        Aber insbesondere dann, wenn Sie mit mehreren Personen an einem Projekt arbeiten, 
        müssen auch andere Entwickler den Code verstehen können. 
        Deshalb ist Lesbarkeit in der Software-Entwicklung immer wichtiger als ein möglichst prägnanter Code. 
        Es hat keinen Sinn, prägnanten Code zu schreiben, wenn andere Entwickler ihn nicht verstehen. 
        Ein gutes Clean-Code-Beispiel für Lesbarkeit ist die Benennung von Variablen.

        Ein Variablenname sollte immer aus sich heraus verständlich sein. 
        Die folgende Variable ist ohne Hintergrundwissen und Erklärung nicht verständlich:
            
            d = int;
        
        Mit folgender Namensgebung ist die gleiche Variable hingegen selbsterklärend:
        
            elapsedTimeinDays = int
    
    #### YAGNI – You ain‘t gonna need it ####
        Es sollte nichts implementiert werden, was vielleicht in der Zukunft verwendet werden kann, 
        denn es ist sehr wahrscheinlich, dass es nicht benötigt wird und es würde sonst nur den 
        Code größer und komplexer machen und somit schwieriger zu verstehen und schwerer zu warten.
        
    #### KISS – Keep it Simple Stupid ####
        Halte den Source-Code möglichst einfach und simple. 
        Wenn es einen einfachen Weg gibt etwas zu implementieren sollte dieser Weg begangen werden. 
        Zusätzliche Komplexität macht den Code schwieriger zu verstehen und somit schwer wartbar.
        
    #### DRY – Don’t repeat yourself ####    
        Jede Verdopplung von Source-Code oder Information in einer Software ist schlecht, 
        denn dies kann zu potenziellen Inkonsistenzen führen und macht es schwierig die Software zu warten.
       
        # WET-Code:
            # Variante A
            username = getUserName();
            password= getPassword();
            user = { username, password};
            client.post(user).then(/*Variante A*/);
            
            # Variante B
            let username = getUserName();
            let password= getPassword();
            let user = { username, password};
            client.get(user).then(/*Variante B*/);
            
        # DRY-Code:
            function getUser(){
              return {
                user:getUserName();
                password:getPassword();
              }
            }
            
            //Variante A
            client.post(getUser()).then(/*Variante A*/ );
            
            //Variante B
            client.get(getUser()).then(/*Variante B*/);
        
    #### Principle of least astonishment surprise ####
        Eine Komponente eines Systems muss sich immer so verhalten wie es die meisten Menschen erwarten würden. 
        Das Verhalten sollte nie den Aufrufer erstaunen oder überraschen, 
        sondern logisch sein und sich „richtig anfühlen“
        
    #### Seperation of Conserns ####
        Eine Software oder ein Software-System soll in verschiedene eindeutige Abschnitte zerteilt werden, 
        wobei jeder Abschnitt seine eigenen spezifischen Aspekte abbildet.    
        
    #### Law of Demeter ####    
        Das Law of Demeter wird auch Prinzip des geringsten Wissens genannt. 
        Jede Einheit in einem Software-System soll so wenig Wissen wie möglich und so viel wie nötig enthalten. 
        Jede Einheit sollte auch nur mit seinen “Freunden” sprechen und nicht mit „Fremden“. 
        Das heißt es sollen nur Methoden von Objekten aufgerufen werden die als Argumente übergeben wurden, 
        lokal erzeugt wurden, global verfügbar sind oder bei der Instanziierung übergeben wurden.

        Beispiel: Ein Aufruf HundàBein 1 bis 4 à gehen() ist nicht ok. Hundà gehen() ist ok. Hund à Schwanz à Wedeln() ist auch ok.
        
    #### Encapsulation ####
        Encapsulation oder Kapselung ist ein Mechanismus zum Einschränken des Zugriffs auf Objekte oder Komponenten. 
        Der Zugriff auf interne Daten eines Objekts von außen ist nur durch definierte Interfaces erlaubt, 
        wie zum Beispiel public Methoden.
        
    #### Single Level of Abstraction ####
        Alle Statements und Befehle einer Methode sollten zum selben Abstraktionslevel gehören. 
        Wenn einige Befehle zu einen niedrigeren Abstraktionslevel gehören, 
        sollten sie in eine private Methode ausgelagert werden, 
        die diese niedrigeren Abstraktionslevel-Befehle zusammenfasst. Dies Reduziert dann die mentale Last, 
        die der Leser benötigt, um den Code zu verstehen. 
        Menschen können immer nur eine Hand voll an Informationen halten und sind somit auf dies Vereinfachung angewiesen.
        
    #### Inversion of Control ####
        Inversion of Control oder Dependency-Injection ist die Anwendung des Hollywood-Prinzips. 
        „Rufen Sie nicht an wir rufen Sie an.“ Normalerweise sind in der objektorientierten Welt Objekte und Komponenten 
        fest miteinander verkoppelt. Der Programmfluss wird bestimmt von den Objekten, 
        die aneinander gebunden sind. Bei Inversion of Control Erzeugen sich die Objekte ihre Abhängigkeiten nicht selbst
        sondern bekommen die Objekte von einem Containermanager von außen geliefert. Dies führt zu einer losen Kopplung.
        
        
    #### Unittests ####
        Unittests sind ein maßgeblicher Teil von Clean-Code. 
        Sie bilden die Funktionalität der Software in Form von abgekapselten elementaren automatisierten Tests ab. 
        Unittests sollen immer unabhängig voneinander sein und möglichst Elementare Funktionalitäten abtesten.
        
    #### Single Point of Truth ####
        Jede Art von Wissen in einem Software-System soll eine eindeutige unmissverständliche und autoritär 
        verbindliche Stelle sein, die nur einmal im System vorkommt. 
        Dabei geht es nicht nur um Source-Code sondern auch um Informationen, Datenbanken, Daten, Tests, 
        Tools und Buildsysteme bzw. Buildartefakte, sowie Dokumentationen.
    
    #### SOLID ####
    #### Single Responsibility Principle ####
        Jede Einheit, jedes Modul eines Software-Systems soll nur eine einzige Verantwortung/Aufgabe haben die es erfüllt. 
        Es soll auch immer nur einen Grund geben ein Modul zu ändern.
    
    #### Open-Close Principle ####
        Komponenten sollen offen sein für Änderungen und Erweiterungen aber geschlossen für Modifikation von außen.
    
    #### Liskov-Substitution Principle ####
        Objekte in einem Software-System sollten durch ihre Sub-Typen und Ableitungen jederzeit ersetzt werden können 
        ohne das sich etwas an der Korrekten Ausführung des Systems ändert.
    
        Ein Beispiel:
        
        Wenn man ein Gefäß zum Ausschaufeln eines vollgelaufenen Bootes verwenden kann, 
        sollte man auch eine Tasse zum Ausschaufeln eines vollgelaufenen Bootes verwenden können, 
        weil die Tasse ebenfalls ein Gefäß ist. Sonst geht man mit dem Boot unter.
    
    #### Interface seregation Principle ####
        Ein Developer sollte nie gezwungen sein in einem Interface nicht für ihn benötigte Methoden aus zu programmieren.
         Wenn dem so ist wäre es sinnvolle das Interface in mehrere Interfaces zu trennen.
    
        Beispiel:
        
        Ein Interface Schweizer Taschenmesser ist schlecht es sollte in viele Interface für 
        Messer, Schere, Säge, Feile, … aufgeteilt werden
    
    #### Dependency Inversion Principle ####
        Ein Element sollte immer von Abstraktionen abhängig sein, nicht von abgeleiteten konkreten Klassen. 
        Das heißt Highlevel-Module sollten nur von Abstraktionen abhängig sein nicht von Lowlevel-Modulen.
"""
