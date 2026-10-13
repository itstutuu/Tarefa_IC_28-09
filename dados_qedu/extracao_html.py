# VScode Copilot - GPT 6 Astra

from pathlib import Path; 
from html import unescape; 
import csv, re, collections;

source=Path('escolas_MSP_qedu.html');
output=Path('escolas_msp_qedu_extraidas.csv'); 
html=source.read_text(encoding='utf-8');
blocks=re.findall(r'<section>(.*?)</section>', html, re.S);
pattern=re.compile(r'<h1[^>]*>(.*?)</h1>.*?<p x-text="item.endereco[^>]*>(.*?)</p>.*?<p class="text-xs font-bold"[^>]*>(.*?)</p>', re.S); 
clean=lambda value: re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', unescape(value))).strip(); 
rows=[];
counts=collections.Counter(); 

labels={'Rede privada':'privada','Rede municipal':'pública','Rede estadual':'pública','Rede federal':'pública'}; 
[(rows.append((clean(match.group(1)),clean(match.group(2)),labels[clean(match.group(3)).split(' / ')[0]])),counts.update([labels[clean(match.group(3)).split(' / ')[0]]])) for block in blocks if (match:=pattern.search(block))]; 
assert len(rows)==9090, f'Expected 9090 parsed records, got {len(rows)}'; 
assert sum(counts.values())==len(rows); 
assert all(name and address and school_type for name,address,school_type in rows);

file=output.open('w',encoding='utf-8-sig',newline=''); 
writer=csv.writer(file); writer.writerow(['nome da escola','endereço','tipo']);
writer.writerows(rows); file.close(); print(f'Arquivo: {output.resolve()}');
print(f'Registros: {len(rows)}; públicas: {counts["pública"]}; privadas: {counts["privada"]}')

#####

import csv,collections;
from pathlib import Path; 

f=Path('escolas_msp_qedu_extraidas.csv').open(encoding='utf-8-sig',newline=''); 
rows=list(csv.DictReader(f)); 
counts=collections.Counter(row['tipo'] for row in rows); 

assert len(rows)==9090; 
assert counts=={'privada':6090,'municipal':1716,'estadual':1279,'federal':5};
assert all(row['nome da escola'] and row['endereço'] for row in rows); 
assert set(counts)=={'municipal','estadual','federal','privada'}; 
print('CSV validado:',len(rows),'registros;',dict(counts))