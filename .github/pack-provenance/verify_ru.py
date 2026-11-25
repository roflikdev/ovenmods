"""Check that the Russian supplement covers every nonempty English mod key."""
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PACK = ROOT / 'resourcepacks/OvenSMP-Russian-1.0.zip'
SOURCE = ROOT / '.github/pack-provenance/ru_ru_missing.json'
META = ROOT / '.github/pack-provenance/resourcepacks.json'

translations = json.loads(SOURCE.read_text(encoding='utf-8'))
with zipfile.ZipFile(PACK) as archive:
    assert json.loads(archive.read('pack.mcmeta'))['pack']['pack_format'] == 34
    for namespace, values in translations.items():
        assert json.loads(archive.read(f'assets/{namespace}/lang/ru_ru.json')) == values
metadata = next(item for item in json.loads(META.read_text(encoding='utf-8'))
                if item['name'] == 'oven_ru_missing')
assert PACK.stat().st_size == metadata['size']
assert hashlib.sha256(PACK.read_bytes()).hexdigest() == metadata['sha256']

uncovered = []
for jar in (ROOT / 'mods').glob('*.jar'):
    with zipfile.ZipFile(jar) as archive:
        names = set(archive.namelist())
        for name in names:
            if not name.startswith('assets/') or not name.endswith('/lang/en_us.json'):
                continue
            namespace = name.split('/')[1]
            english = json.loads(archive.read(name).decode('utf-8-sig'))
            russian_name = f'assets/{namespace}/lang/ru_ru.json'
            russian = json.loads(archive.read(russian_name).decode('utf-8-sig')) if russian_name in names else {}
            for key, value in english.items():
                if value.strip() and key not in russian and key not in translations.get(namespace, {}):
                    uncovered.append(f'{jar.name}: {namespace}:{key}')
if uncovered:
    raise SystemExit('Untranslated keys:\n' + '\n'.join(uncovered))
print('Russian translation supplement verified:', sum(map(len, translations.values())), 'strings; 0 uncovered keys')
