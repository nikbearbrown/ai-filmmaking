"""filmkit: build a narrated teaching film from stills, clips and cards.
Folder: /Users/bear/Documents/CoWork/bear-textbooks/books/ai-filmmaking/tools

A film folder holds spec.py, which makes cards then calls filmkit.assemble(W, BEATS, OUT).
Beat dict: id, text (narration), segs (list of dicts), bg (video whose own sound plays under the beat), min (min seconds).
Seg dict: kind = clip | still | strip ; src (path, or list of tile paths for strip) ; overlay (PNG) ; zoom = in | out ; frac (share of the beat).
Voice: Kokoro am_onyx speed 0.95, voice starts 0.35 s into its beat, beat = voice + 0.85 s.
Mix: bg sound x0.35 ducked under the voice, fixed gain to -16 LUFS, limiter, fades. Captions: whisper word times.
"""
import json, os, re, subprocess, sys, glob
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFont
FF='/opt/homebrew/bin/ffmpeg'
FD='/Users/bear/Documents/CoWork/bear-textbooks/books/brutalist.art/runtime/'
CREAM=(250,249,245); INK=(26,24,21); TERRA=(217,119,87); GREY=(150,146,138)
S=int(os.environ.get('FILM_S','1'))   # 1 = 1080p, 2 = 4K (3840x2160). All card coordinates stay in 1920x1080 units and are scaled here.
FW,FH=1920*S,1080*S
ENC='-c:v libx264 -crf %d -preset fast -r 24 -pix_fmt yuv420p'%(16 if S==1 else 15)
class Draw:
    """ImageDraw proxy: takes 1920x1080 coordinates and sizes, draws at S times that. textlength returns 1080p units."""
    def __init__(s,im): s.d=ImageDraw.Draw(im)
    def _c(s,xy): return tuple(v*S for v in xy)
    def text(s,xy,t,**k): s.d.text(s._c(xy),t,**k)
    def rectangle(s,xy,**k): s.d.rectangle(s._c(xy),**k)
    def line(s,xy,width=1,**k): s.d.line(s._c(xy),width=width*S,**k)
    def textlength(s,t,font): return s.d.textlength(t,font=font)/S
def font(sz,serif=True): return ImageFont.truetype(FD+'fonts/'+('EB_Garamond/static/EBGaramond-Regular.ttf' if serif else 'Lato/static/Lato-Bold.ttf'),sz*S)
def run(cmd):
    r=subprocess.run(cmd,shell=True,capture_output=True,text=True)
    if r.returncode: raise SystemExit(cmd[:300]+'\n'+r.stderr[-1500:])
def probe(f): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',f]).strip())
def center(d,text,y,f,fill):
    w=d.textlength(text,font=f); d.text(((1920-w)/2,y),text,font=f,fill=fill)
def card(W,name,fn,bg=INK):
    os.makedirs(W+'/cards',exist_ok=True)
    im=Image.new('RGB',(FW,FH),bg); fn(im,Draw(im)); p=f'{W}/cards/{name}.png'; im.save(p); return p
def label(W,name,l1,l2):
    os.makedirs(W+'/cards',exist_ok=True)
    im=Image.new('RGBA',(FW,FH),(0,0,0,0)); d=Draw(im)
    d.rectangle((60,860,60+max(d.textlength(l1,font=font(64,False)),d.textlength(l2,font=font(40,False)))+60,1010),fill=(0,0,0,170))
    d.text((90,872),l1,font=font(64,False),fill=CREAM+(255,)); d.text((90,950),l2,font=font(40,False),fill=TERRA+(255,))
    p=f'{W}/cards/{name}.png'; im.save(p); return p
def still(img,dur,out,zoom='in',overlay=None):
    fr=int(round(dur*24)); z=f"1+0.06*on/{fr}" if zoom=='in' else f"1.06-0.06*on/{fr}"
    if S>1:   # pre-scale once (Lanczos) to 2x frame size so zoompan has headroom, instead of scaling every frame
        pre=f"{os.path.dirname(out)}/pre_{abs(hash(img))}.png"
        if not os.path.exists(pre):
            im=Image.open(img).convert('RGB'); r=max(2*FW/im.width,2*FH/im.height); im=im.resize((round(im.width*r),round(im.height*r)),Image.LANCZOS)
            l=(im.width-2*FW)//2; t=(im.height-2*FH)//2; im.crop((l,t,l+2*FW,t+2*FH)).save(pre)
        img=pre; flt=f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={FW}x{FH}:fps=24,format=yuv420p"
    else:
        flt=f"scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:2160,zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s=1920x1080:fps=24,format=yuv420p"
    if overlay: run(f'{FF} -hide_banner -loglevel error -y -loop 1 -i "{img}" -i "{overlay}" -filter_complex "[0]{flt}[a];[a][1]overlay=0:0,format=yuv420p" -frames:v {fr} {ENC} {out}')
    else: run(f'{FF} -hide_banner -loglevel error -y -loop 1 -i "{img}" -vf "{flt}" -frames:v {fr} {ENC} {out}')
def clip(src,dur,out,overlay=None,start=0.0):
    hold=max(0,dur-(probe(src)-start)+0.04)
    base=f"[0:v]scale={FW}:{FH}:force_original_aspect_ratio=increase,crop={FW}:{FH},fps=24,tpad=stop_mode=clone:stop_duration={hold:.3f}"
    ss=f'-ss {start}' if start else ''
    if overlay: run(f'{FF} -hide_banner -loglevel error -y {ss} -i "{src}" -i "{overlay}" -filter_complex "{base}[a];[a][1]overlay=0:0,format=yuv420p" -t {dur} {ENC} {out}')
    else: run(f'{FF} -hide_banner -loglevel error -y {ss} -i "{src}" -vf "{base},format=yuv420p" -t {dur} {ENC} {out}')
def strip(W,tiles,dur,out,overlay=None,tw=720):
    os.makedirs(W+'/cards',exist_ok=True)
    for i,f in enumerate(tiles): run(f'{FF} -hide_banner -loglevel error -y -i "{f}" -vf scale={tw*S}:{FH}:force_original_aspect_ratio=increase,crop={tw*S}:{FH} -q:v 3 {W}/cards/t{i:02d}.jpg')
    inp=' '.join(f'-i {W}/cards/t{i:02d}.jpg' for i in range(len(tiles)))
    run(f'{FF} -hide_banner -loglevel error -y {inp} -filter_complex "hstack=inputs={len(tiles)}" -q:v 3 {W}/cards/strip.jpg')
    ov=f'-i "{overlay}"' if overlay else ''
    fc=f"[0]crop={FW}:{FH}:x='(iw-{FW})*t/{dur}':y=0[a];"+("[a][1]overlay=0:0,format=yuv420p" if overlay else "[a]format=yuv420p")
    run(f'{FF} -hide_banner -loglevel error -y -loop 1 -i {W}/cards/strip.jpg {ov} -filter_complex "{fc}" -t {dur} {ENC} {out}')
def render_vo(W,beats,lex=None,force=False):
    sys.path.insert(0,FD+'scripts'); import generate_audio_kokoro as g
    os.makedirs(W+'/vo',exist_ok=True); k=None; dur={}
    for b in beats:
        p=f"{W}/vo/vo-{b['id']}.wav"
        if force or not os.path.exists(p) or os.path.exists(p+'.stale'):
            if k is None: k=g.load_engine()
            sp=g.apply_lexicon(g.normalize_for_tts(b['text'],'am_onyx'),lex or {},'en-us')
            s,sr=k.create(sp,voice='am_onyx',speed=0.95,lang='en-us',is_phonemes=True); sf.write(p,s,sr)
            if os.path.exists(p+'.stale'): os.remove(p+'.stale')
        x,sr=sf.read(p); dur[b['id']]=len(x)/sr
    json.dump(dur,open(W+'/vo-durations.json','w'),indent=1); return dur
def assemble(W,beats,out_name,lex=None,fade_in=0.5,fade_out=1.2,tail=None):
    os.makedirs(W+'/seg',exist_ok=True)
    V=render_vo(W,beats,lex)
    segfiles=[]; starts={}; t=0
    for b in beats:
        D=max(V[b['id']]+0.85,b.get('min',0)); b['D']=D; segs=b['segs']
        fr=[s.get('frac',1/len(segs)) for s in segs]
        starts[b['id']]=t
        for i,s in enumerate(segs):
            d=D*fr[i]/sum(fr); o=f"{W}/seg/{b['id']}{i}.mp4"
            k=s['kind']
            if k=='clip': clip(s['src'],d,o,s.get('overlay'),s.get('start',0.0))
            elif k=='still': still(s['src'],d,o,s.get('zoom','in'),s.get('overlay'))
            elif k=='strip': strip(W,s['src'],d,o,s.get('overlay'),s.get('tw',720))
            segfiles.append(o)
        t+=D
    if tail:   # list of (png, seconds) silent end cards
        for j,(png,sec) in enumerate(tail):
            o=f"{W}/seg/tail{j}.mp4"; still(png,sec,o,'in'); segfiles.append(o); t+=sec
    open(W+'/seg/list.txt','w').write(''.join(f"file '{s}'\n" for s in segfiles))
    run(f'{FF} -hide_banner -loglevel error -y -f concat -safe 0 -i {W}/seg/list.txt -c copy {W}/seg/video-raw.mp4')
    total=probe(W+'/seg/video-raw.mp4'); SR=48000
    vo=np.zeros(int((total+1)*SR),dtype=np.float32); amb=np.zeros_like(vo)
    for b in beats:
        run(f'{FF} -hide_banner -loglevel error -y -i {W}/vo/vo-{b["id"]}.wav -ar 48000 -ac 1 -af highpass=f=70 {W}/tmp.wav')
        x,_=sf.read(W+'/tmp.wav',dtype='float32'); f=int(.03*SR); x[:f]*=np.linspace(0,1,f); x[-f:]*=np.linspace(1,0,f)
        a=int((starts[b['id']]+0.35)*SR); vo[a:a+len(x)]+=x
        if b.get('bg'):
            has=subprocess.run(['ffprobe','-v','error','-select_streams','a','-show_entries','stream=codec_type','-of','csv=p=0',b['bg']],capture_output=True,text=True).stdout.strip()
            if has:
                run(f'{FF} -hide_banner -loglevel error -y -i "{b["bg"]}" -vn -ar 48000 -ac 1 {W}/tmp2.wav')
                y,_=sf.read(W+'/tmp2.wav',dtype='float32'); a2=int(starts[b['id']]*SR); n=min(len(y),int(b['D']*SR),len(amb)-a2); amb[a2:a2+n]+=y[:n]
    for f in ('tmp.wav','tmp2.wav'):
        if os.path.exists(W+'/'+f): os.remove(W+'/'+f)
    sf.write(W+'/vo-track.wav',np.stack([vo,vo],1),SR,subtype='PCM_16'); sf.write(W+'/amb-track.wav',np.stack([amb,amb],1),SR,subtype='PCM_16')
    T=total
    run(f'{FF} -hide_banner -loglevel error -y -i {W}/amb-track.wav -i {W}/vo-track.wav -filter_complex "[0:a]volume=0.35[amb];[1:a]asplit=2[vo][key];[amb][key]sidechaincompress=threshold=0.02:ratio=6:attack=30:release=800:makeup=1[duck];[duck][vo]amix=inputs=2:normalize=0:duration=first,atrim=0:{T}[out]" -map "[out]" -ar 48000 -c:a pcm_f32le {W}/mix-raw.wav')
    I=subprocess.run(f'{FF} -hide_banner -nostats -i {W}/mix-raw.wav -af ebur128 -f null - 2>&1 | grep -A12 Summary | grep "I:"',shell=True,capture_output=True,text=True).stdout.split()[1]
    G=round(-16-float(I),2)
    run(f'{FF} -hide_banner -loglevel error -y -i {W}/mix-raw.wav -af "volume={G}dB,alimiter=limit=0.84:level=disabled:attack=5:release=80,afade=t=in:d={fade_in},afade=t=out:st={T-fade_out}:d={fade_out}" -c:a pcm_s16le {W}/mix.wav')
    run(f'{FF} -hide_banner -loglevel error -y -i {W}/seg/video-raw.mp4 -i {W}/mix.wav -map 0:v -map 1:a -vf "fade=t=in:d={fade_in},fade=t=out:st={T-fade_out}:d={fade_out}" -c:v libx264 -crf 16 -preset medium -pix_fmt yuv420p -c:a aac -b:a 256k -movflags +faststart {W}/{out_name}')
    json.dump(starts,open(W+'/beat-starts.json','w'),indent=1)
    captions(W,beats,starts,out_name.replace('.mp4','-captions.srt'))
    return total
def captions(W,beats,starts,srt_name):
    from faster_whisper import WhisperModel
    m=WhisperModel('base.en',device='cpu',compute_type='int8')
    def fmt(t):
        h=int(t//3600); mi=int(t%3600//60); s=t%60
        return f"{h:02d}:{mi:02d}:{int(s):02d},{int(round((s-int(s))*1000)):03d}"
    cues=[]; mism=[]
    for b in beats:
        words=b['text'].split()
        segs,_=m.transcribe(f'{W}/vo/vo-{b["id"]}.wav',word_timestamps=True,language='en')
        w=[x for s in segs for x in s.words]
        if len(w)!=len(words):
            dur=probe(f'{W}/vo/vo-{b["id"]}.wav'); tot=sum(len(x)+2 for x in words); t=0; tm=[]
            for x in words:
                d=dur*(len(x)+2)/tot; tm.append((t,t+d)); t+=d
            mism.append(b['id'])
        else: tm=[(x.start,x.end) for x in w]
        base=starts[b['id']]+0.35; cur=[]
        def flush():
            nonlocal_cur=cur
            if cur: cues.append((base+tm[cur[0]][0],base+tm[cur[-1]][1],' '.join(words[k] for k in cur)))
            cur.clear()
        for k,x in enumerate(words):
            cur.append(k); chars=len(' '.join(words[j] for j in cur))
            if re.search(r'[.!?]$',x) or (x.endswith((',',':')) and chars>=60) or chars>=84: flush()
        flush()
    mg=[]
    for c in cues:
        if mg and (mg[-1][1]-mg[-1][0])<1.4 and abs(c[0]-mg[-1][1])<0.8 and len(mg[-1][2])+len(c[2])+1<=84: mg[-1]=(mg[-1][0],c[1],mg[-1][2]+' '+c[2])
        else: mg.append(c)
    with open(f'{W}/{srt_name}','w') as f:
        for n,(a,b,t) in enumerate(mg,1):
            nxt=mg[n][0] if n<len(mg) else b+1; b2=max(min(b+0.35,nxt-0.05),b)
            if len(t)>42:
                ws=t.split(); best=min(range(1,len(ws)),key=lambda j:abs(len(' '.join(ws[:j]))-len(' '.join(ws[j:])))); t=' '.join(ws[:best])+'\n'+' '.join(ws[best:])
            f.write(f"{n}\n{fmt(a)} --> {fmt(b2)}\n{t}\n\n")
    print(len(mg),'cues; proportional timing for beats',mism)
