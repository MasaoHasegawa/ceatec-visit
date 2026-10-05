# 公式出展者一覧を取得 → data.js → template.html に埋め込み → ceatec-visit.html
import subprocess, pathlib, re
d = pathlib.Path(__file__).parent
subprocess.run(['curl','-s','-A','Mozilla/5.0','-o',str(d/'ceatec.html'),'https://www.ceatec.com/ja/exhibition/exhibitor-list.php'],check=True)
subprocess.run(['python','parse.py'],cwd=d,check=True)
data = (d/'data.js').read_text(encoding='utf-8')
tpl = (d/'template.html').read_text(encoding='utf-8')
page = tpl.replace('/*DATA*/', data)
(d/'ceatec-visit.html').write_text(page, encoding='utf-8')
(d/'index.html').write_text('<!doctype html>\n<html lang="ja"><head><meta charset="utf-8">\n' + page + '\n</html>', encoding='utf-8')
print('ok', len(page))
