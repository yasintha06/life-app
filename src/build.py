import re, os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src=open(os.path.join(R,'src/app.html')).read()
shim=open(os.path.join(R,'src/standalone-shim.html')).read()
def rep(s,a,b):
    assert s.count(a)==1,a[:60]; return s.replace(a,b)
s=src
s=rep(s,'<meta name="claude:viewport-fit-sides" content="cover">\n','')
s=rep(s,'["chat","Assistant"],["more","More"]];','["more","More"]];')
s=rep(s,'\n  ["chat","Assistant","Type and it logs for you"],',' ')
s=rep(s,'return[body,h("div",{class:"meta"},"Never type card numbers','return[body,window.lifeSignOut?h("button",{class:"btn ghost",type:"button",onclick:window.lifeSignOut},"Sign out"):null,h("div",{class:"meta"},"Never type card numbers')
# insert shim (gate + supabase layer) just before the app script
i=s.index('<script>\n/*CALC*/')
style_end=s.index('</style>')+len('</style>')
head_part=s[:style_end]; body_part=s[style_end:]
i=body_part.index('<script>\n/*CALC*/')
body_part=body_part[:i]+shim+'\n'+body_part[i:]
out=('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
 '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
 '<meta name="theme-color" content="#005B52">\n<meta name="apple-mobile-web-app-capable" content="yes">\n'
 '<meta name="apple-mobile-web-app-title" content="Yasi Life">\n<link rel="manifest" href="manifest.webmanifest">\n'
 '<link rel="icon" href="icon.svg">\n<link rel="apple-touch-icon" href="icon.svg">\n'
 +head_part+'\n</head>\n<body>\n'+body_part+'\n</body>\n</html>\n')
open(os.path.join(R,'index.html'),'w').write(out)
print(len(out))
