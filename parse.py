import re, json, html as H
h=open('ceatec.html',encoding='utf-8').read()
h=re.sub(r'<!--.*?-->','',h,flags=re.S)
arts=re.findall(r'<article class="exl-card[^"]*"(.*?)</article>',h,flags=re.S)
T=lambda s:re.sub(r'\s+',' ',H.unescape(re.sub(r'<[^>]+>',' ',s or ''))).strip()
def g(pat,s):
    m=re.search(pat,s,re.S); return T(m.group(1)) if m else ''
out=[]
for a in arts:
    at=dict(re.findall(r'data-([a-z-]+)="([^"]*)"',a[:600]))
    full=a.split('exl-card__compact')[0]
    comp=a[len(full):]
    r={'id':at.get('id'),'n':g(r'class="exl-card__name">(.*?)</h3>',full),
       'a':g(r'class="exl-card__area"[^>]*>(.*?)</span>',full).lstrip('● ').strip(),
       'h':g(r'class="exl-card__hall">(.*?)</span>',full),
       'b':g(r'class="exl-card__booth">(.*?)</span>',full),
       'd':g(r'class="exl-card__highlight[^"]*">(.*?)</p>',full),
       'ini':at.get('initial'),'rb':int(at.get('rank-booth',0)),'o':int(at.get('openable',0))}
    tags=[T(x) for x in re.findall(r'<span class="exl-tag-[a-z]+"[^>]*>(.*?)</span>',full,re.S)]
    if '学生' in ' '.join(tags) or '🎓' in full: r['st']=1
    if tags: r['t']=[x for x in dict.fromkeys(tags) if x]
    kids=[]
    for attrs,body in re.findall(r'<button type="button"\s+class="exl-child[^"]*"([^>]*)>(.*?)</button>',comp,re.S):
        kid={'n':T(re.sub(r'<span class="exl-child__(bullet|booth)">.*?</span>','',body,flags=re.S))}
        b=g(r'class="exl-child__booth">(.*?)</span>',body)
        if b and b!=r['b']: kid['b']=b
        m=re.search(r'data-exl-open-detail-id="(\d+)"',attrs)
        if m: kid['id']=m.group(1)
        kids.append(kid)
    if kids: r['k']=kids
    out.append(r)
print(len(out), sum(len(x.get('k',[])) for x in out))
import collections
print(collections.Counter(t for x in out for t in x.get('t',[])).most_common(20))
print(json.dumps([x for x in out if x.get('k')][:2],ensure_ascii=False)[:1500])
js=json.dumps(out,ensure_ascii=False,separators=(',',':'))
open('data.js','w',encoding='utf-8').write(js)
print(len(js))
