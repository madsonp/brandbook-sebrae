from pathlib import Path
import hashlib,json,re
from urllib.parse import unquote

root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'dados/manifesto.json').read_text(encoding='utf-8'))
inventory=json.loads((root/'dados/inventario-sha256.json').read_text(encoding='utf-8'))
checked=0
for relative,meta in inventory['arquivos'].items():
    p=root/relative
    assert p.is_file(),f'Arquivo ausente: {relative}'
    assert p.stat().st_size==meta['bytes'],f'Tamanho alterado: {relative}'
    assert hashlib.sha256(p.read_bytes()).hexdigest()==meta['sha256'],f'Hash alterado: {relative}'
    checked+=1
assert hashlib.sha256((root/'original.pdf').read_bytes()).hexdigest()==manifest['fonte_pdf']['sha256']
links=0
for p in root.rglob('*.md'):
    if '.git' in p.relative_to(root).parts:continue
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
        if re.match(r'https?://',target):continue
        d=(p.parent/unquote(target.split('#')[0])).resolve()
        assert d.is_relative_to(root) and d.exists(),f'Link inválido: {p.name}: {target}'
        links+=1
print(json.dumps({'edicao':manifest['edicao_adaptacao'],'arquivos_do_pacote_verificados':checked,'links_locais_verificados':links,'estado':'aprovado'},ensure_ascii=False))
