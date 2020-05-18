from datetime import datetime

records = [
    {'source': '48-996355555', 'destination': '48-666666666', 'end': 1564610974, 'start': 1564610674},
    {'source': '41-885633788', 'destination': '41-886383097', 'end': 1564506121, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-886383097', 'end': 1564630198, 'start': 1564629838},
    {'source': '48-999999999', 'destination': '41-885633788', 'end': 1564697158, 'start': 1564696258},
    {'source': '41-833333333', 'destination': '41-885633788', 'end': 1564707276, 'start': 1564704317},
    {'source': '41-886383097', 'destination': '48-996384099', 'end': 1564505621, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '48-996383697', 'end': 1564505721, 'start': 1564504821},
    {'source': '41-885633788', 'destination': '48-996384099', 'end': 1564505721, 'start': 1564504821},
    {'source': '48-996355555', 'destination': '48-996383697', 'end': 1564505821, 'start': 1564504821},
    {'source': '48-999999999', 'destination': '41-886383097', 'end': 1564610750, 'start': 1564610150},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564505021, 'start': 1564504821},
    {'source': '48-996383697', 'destination': '41-885633788', 'end': 1564627800, 'start': 1564626000}
]

def get_tarifs(start, end):    
    #Calcula o valor da ligação, levando em conta os critérios de horário
    TAXA_FIXA = 0.36
    TAXA_VARIAVEL = 0.09
    
    # Para ligações que ocorrem totalmente entre as 6h e 22h (Tarifação diurna)
    if (22>start.hour>=6) and (22>end.hour>=6):
        duration = end - start 
        valor = (((duration.total_seconds()) // 60) * TAXA_VARIAVEL) + TAXA_FIXA 
        
        return valor
    
    #Ligação com início antes e término após as 22h.
    # A tarifa de 0.09 só é cobrada até as 22h
    elif (start.hour<22) and (end.hour>=22 and end.minute>=1):
        end = datetime(start.year, start.month, start.day, 22, 00, 59)
        duration = end - start
        valor = (((duration.total_seconds()) // 60) * TAXA_VARIAVEL) + TAXA_FIXA
        
        return valor

    #Para ligações que iniciam após as 22h e terminam antes das 6h
    elif ((start.hour>=22) and (start.minute>=1)) or (start.hour<6 and end.hour<6):
        valor = TAXA_FIXA
        
        return valor

def classify_by_phone_number(records):
    results = []
    dic = {}
    
    for record in records:
        
        start = datetime.fromtimestamp(int(record['start']))
        end = datetime.fromtimestamp(int(record['end']))
        
        price = get_tarifs(start, end)
        
        if record['source'] not in dic:
            dic[record['source']] = price
        else:
            dic[record['source']] += price
        
    for k, v in dic.items():
        results.append({'source': k, 'total': round(v, 2)})    
        
    final_result = sorted(results,
                          key=lambda item: item['total'],
                          reverse=True)
       
    return final_result