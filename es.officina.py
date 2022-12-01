"flowchart verifica gestione progetto officina meccanica"
print("benvenuto nella nostra officina. Caspita! la tua auto ha riportato dei bei danni!")
disp_pezzi = input("dispongo di tutti i pezzi per ripararla? si/no\n")
if disp_pezzi == "si":
    print("ok ho tutti i pezzi per la tua auto!")
else: 
    print("porca miseria... non ho tutti i pezzi di ricambio per la tua auto!")
    pazienza = input("Il cliente è disposto ad aspettare i tempi di consegna dell'azienda per i ricambi? si/no\n")
    if pazienza == "si":
        print("perfetto, contatteremo il cliente appena avremo notizie dall'azienda")
    else: 
        print("ringraziamo il cliente comunque per essere passato")
pagamento = input("paga il cliente o l'assicurazione? c/a\n")
if pagamento == "c":
    print("ci concorderemo con il cliente per il pagamento")
else: 
    print("ci concorderemo con l'assicurazione per il pagamento")
lavori = input("i lavori procedono e vanno a buon fine? si/no\n")
if lavori == "si":
    print("comunico al cliente che i lavori sono andati a buon fine")
else:
    print("comunico al cliente che c'è stato un errore in fase di riparazione e ricontrollo ogni lavoro effettuato e la lista dei lavori da fare")
feedback = input("Chiedo al cliente se l'esperienza è stata positiva o negativa: p/n\n")
if feedback == "p":
    print("Lo ringraziamo e lo ivntiamo a ripassare e a farci pubblicità")
else:
    print("Gli chiediamo scusa per l'imprevisto e gli chiediamo quale sia stato il problema durante l'esperienza per lavorare e migliorare sul servizio offerto")
