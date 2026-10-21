#!/usr/bin/env python3
"""Builds prototype/app-venus-themes.html: the module page in the Venus palette, three ways, each light and dark.
Run: python3 prototype/theme.py"""
import pathlib, re, sys, io, contextlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
with contextlib.redirect_stdout(io.StringIO()):
    import module as M

css = M.CSS + M.AI_CSS
# turn the fixed greys into theme variables
pairs = [
    (r"color: #fff\b", "color: var(--on-acc)"),
    (r"background: #1C1C1E\b", "background: var(--acc)"),
    (r"#1C1C1E\b", "var(--ink)"),
    (r"background: #fff\b", "background: var(--surface)"),
    (r"#fff\b", "var(--surface)"),
    (r"#F1F1F2\b", "var(--panel)"),
    (r"#F4F4F5\b|#F7F7F8\b", "var(--field)"),
    (r"#E9E9EC\b", "var(--sel)"),
    (r"#E6E6E8\b|#E4E4E7\b|#EDEDEF\b|#D9D9DC\b|#E2E2E5\b|#DADADD\b|#D2D2D6\b|#C9C9CE\b|#CFCFD3\b|#E0E0E3\b", "var(--line)"),
    (r"#8A8A90\b|#9A9AA0\b", "var(--muted)"),
    (r"#5E5E63\b|#6B6B70\b|#3A3A3E\b|#2A2A2E\b|#4A4A4F\b", "var(--ink2)"),
    (r"#C98A1B\b", "var(--amber)"), (r"#2F8F5B\b", "var(--green)"), (r"#C2413A\b|#E5484D\b", "var(--red)"),
    (r"#CFB783\b", "var(--gold)"),
]
for a, b in pairs:
    css = re.sub(a, b, css)

css += """
/* theme hooks */
.m-page { background: var(--surface); color: var(--ink); }
.m-rail { background: var(--rail); }
.m-rail .nv { color: var(--rail-ic); }
.m-rail .nv.on { background: var(--nav-on); color: var(--nav-on-ic); }
.m-rail .nv-sep { background: var(--rail-line); }
.m-rail .exp { background: var(--surface); color: var(--muted); }
.m-rail .dz-me { background: var(--nav-on); color: var(--nav-on-ic); }
.m-rail .bd { background: var(--badge); color: var(--badge-ic); }
.dz-lg i { background: var(--logo); } .dz-lg i:nth-child(3) { background: var(--gold); }
.tile.sel { background: var(--surface); }
.frame { background: var(--surface); }
.theme { margin-top: 18px; }
.pair { display: grid; gap: 14px; }
.tag-l { display: inline-flex; align-items: center; gap: 8px; font-size: 12px; color: #5E5E63; margin: 0 0 8px; }
.tag-l i { width: 10px; height: 10px; border-radius: 50%; border: 1px solid #CFC6B4; }
.where { display: flex; flex-wrap: wrap; gap: 8px; margin: 0 0 14px; padding: 0; list-style: none; }
.where li { font-size: 13px; background: #fff; border-radius: 99px; padding: 6px 12px; color: #3A3A3E; }
.sw { display: flex; gap: 8px; flex-wrap: wrap; margin: 6px 0 4px; }
.sw span { display: inline-flex; align-items: center; gap: 8px; background: #fff; border-radius: 99px; padding: 5px 12px 5px 5px; font-size: 12.5px; }
.sw b { width: 22px; height: 22px; border-radius: 50%; box-shadow: inset 0 0 0 1px rgba(0,0,0,.08); }
"""

STATUS_L = "--green:#2F8F5B; --amber:#E08A1E; --red:#C2413A;"
STATUS_D = "--green:#4CB27E; --amber:#F0A040; --red:#E5605A;"
THEMES = {
    "quiet": {
        "name": "1. Quiet", "blurb": "Warm neutrals do the work. Buttons and the active item are Luex Black; Pale Gold appears only on the logo tile and the Ask Luex mark.",
        "where": ["Panels: warm grey", "Buttons: Luex Black", "Active nav: Luex Black", "Gold: logo and AI only"],
        "light": "--surface:#FFFFFF; --panel:#F3F0EA; --field:#F7F4EF; --sel:#ECE6DB; --line:#E5DED2; --ink:#141414; --ink2:#4A4740; --muted:#8E8778; --acc:#141414; --on-acc:#FFFFFF; --gold:#CFB783; --rail:#F3F0EA; --rail-ic:#77664B; --rail-line:#DDD5C7; --nav-on:#141414; --nav-on-ic:#FFFFFF; --badge:#FFFFFF; --badge-ic:#141414; --logo:#141414;",
        "dark": "--surface:#161514; --panel:#211F1C; --field:#2A2724; --sel:#302C27; --line:#36322C; --ink:#F2EEE6; --ink2:#C9C2B5; --muted:#8E8778; --acc:#E7DECA; --on-acc:#141414; --gold:#CFB783; --rail:#211F1C; --rail-ic:#AAA091; --rail-line:#36322C; --nav-on:#E7DECA; --nav-on-ic:#141414; --badge:#E7DECA; --badge-ic:#141414; --logo:#E7DECA;",
    },
    "warm": {
        "name": "2. Warm", "blurb": "Cloud Cream panels, Warm Ochre buttons and a Bronze active item. The most 'Venus' of the three: it feels like the desert on the website.",
        "where": ["Panels: Cloud Cream", "Buttons: Warm Ochre", "Active nav: Bronze", "Text: Luex Black"],
        "light": "--surface:#FFFDF8; --panel:#F1EADC; --field:#F7F2E8; --sel:#EAE0CC; --line:#E3D8C3; --ink:#141414; --ink2:#4F4636; --muted:#8C7F66; --acc:#A68B55; --on-acc:#FFFFFF; --gold:#CFB783; --rail:#F1EADC; --rail-ic:#77664B; --rail-line:#E0D3BB; --nav-on:#77664B; --nav-on-ic:#FFFFFF; --badge:#A68B55; --badge-ic:#FFFFFF; --logo:#141414;",
        "dark": "--surface:#1A1713; --panel:#26211A; --field:#2F2920; --sel:#3A3226; --line:#3D3528; --ink:#F3ECDD; --ink2:#D2C6AE; --muted:#9A8D74; --acc:#CFB783; --on-acc:#141414; --gold:#CFB783; --rail:#26211A; --rail-ic:#AAA091; --rail-line:#3D3528; --nav-on:#CFB783; --nav-on-ic:#141414; --badge:#CFB783; --badge-ic:#141414; --logo:#E7DECA;",
    },
    "bold": {
        "name": "3. Bold", "blurb": "A Luex Black nav rail frames every page, with Pale Gold for the active item and the main buttons. The most recognisable, like the black business card.",
        "where": ["Nav rail: Luex Black", "Active nav: Pale Gold", "Buttons: Luex Black / Pale Gold in dark", "Panels: soft cream"],
        "light": "--surface:#FFFFFF; --panel:#F4EFE5; --field:#F8F4EC; --sel:#EDE5D6; --line:#E6DDCD; --ink:#141414; --ink2:#4A4740; --muted:#8E8778; --acc:#141414; --on-acc:#FFFFFF; --gold:#CFB783; --rail:#141414; --rail-ic:#AAA091; --rail-line:#2C2A27; --nav-on:#CFB783; --nav-on-ic:#141414; --badge:#CFB783; --badge-ic:#141414; --logo:#E7DECA;",
        "dark": "--surface:#121110; --panel:#1E1C19; --field:#272420; --sel:#2E2A24; --line:#33302A; --ink:#F2EEE6; --ink2:#C9C2B5; --muted:#8E8778; --acc:#CFB783; --on-acc:#141414; --gold:#CFB783; --rail:#000000; --rail-ic:#8E8778; --rail-line:#24221F; --nav-on:#CFB783; --nav-on-ic:#141414; --badge:#CFB783; --badge-ic:#141414; --logo:#E7DECA;",
    },
}

def themed_frame():
    h = M.ai_frame("closed")
    for a, b in [("#C98A1B", "var(--amber)"), ("#2F8F5B", "var(--green)"), ("#C2413A", "var(--red)"), ("#1C1C1E", "var(--ink)")]:
        h = h.replace(a, b)
    return h

FR = themed_frame()
blocks = ""
for key, t in THEMES.items():
    blocks += f'''<h2>{t["name"]}</h2><p class="lead">{t["blurb"]}</p>
    <ul class="where">{"".join(f"<li>{w}</li>" for w in t["where"])}</ul>
    <div class="pair">
      <div><p class="tag-l"><i style="background:#fff"></i>Light</p><div class="frame" style="{t["light"]} {STATUS_L}">{FR}</div></div>
      <div><p class="tag-l"><i style="background:#141414"></i>Dark</p><div class="frame" style="{t["dark"]} {STATUS_D}">{FR}</div></div>
    </div>'''

pal = [("Luex Black", "#141414"), ("Bronze", "#77664B"), ("Warm Ochre", "#A68B55"), ("Pale Gold", "#CFB783"), ("Taupe", "#AAA091"), ("Cloud Cream", "#E7DECA")]
page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Luex Venus Themes</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500&display=swap">
<style>{css}</style></head><body>
<div class="wrap">
  <h1>Luex in Venus colours</h1>
  <p class="lead">The same module page with the Venus palette placed three different ways, each in light and dark. Status colours stay green, amber and red in every version; amber is brighter (#E08A1E) so it never reads as the brand gold.</p>
  <div class="sw">{"".join(f'<span><b style="background:{c}"></b>{n} {c}</span>' for n, c in pal)}</div>
  {blocks}
</div>
<script>{M.JS}</script>
</body></html>"""
out = pathlib.Path(__file__).with_name("app-venus-themes.html")
out.write_text(page)
print("wrote", out, len(page))

# =============================================================== mixed colours with gradients
MIX_CSS = """
.mix .m-page { background: var(--page-bg); }
.mix .m-rail { background: var(--rail-grad); }
.mix .m-rail .nv.on { background: var(--gold-grad); color: #141414; box-shadow: 0 6px 14px -6px rgba(166,139,85,.7); }
.mix .tile.sel { background: var(--sel-grad); box-shadow: inset 0 0 0 1.5px var(--sel-line), 0 10px 22px -12px rgba(119,102,75,.55); }
.mix .tile.sel .t-top, .mix .tile.sel small { color: var(--sel-ink2); } .mix .tile.sel b { color: var(--sel-ink); }
.mix .key { background: var(--key-grad); box-shadow: 0 14px 28px -16px rgba(60,45,20,.6); }
.mix .key-r p, .mix .key-r p b, .mix .mini-ring b { color: var(--key-ink); }
.mix .mini-ring small { color: var(--key-ink2); }
.mix .mini-ring .tr { stroke: rgba(255,255,255,.22); } .mix .mini-ring .pr { stroke: var(--key-ring); }
.mix .key .btn-d { background: var(--key-btn); color: var(--key-btn-ink); }
.mix .key .btn-l { background: rgba(255,255,255,.16); color: var(--key-ink); }
.mix .btn-d, .mix .rnd.dark, .mix .tabbar .add, .mix .cmt .i, .mix .snd { background: var(--btn-grad); color: var(--btn-ink); }
.mix .ask { border: 1.5px solid transparent; box-shadow: none; background: linear-gradient(var(--surface), var(--surface)) padding-box, var(--gold-grad) border-box; }
.mix .lr.open { box-shadow: 0 0 0 2px var(--open-line); }
.mix .mw, .mix .dw, .mix .tile:not(.sel) { background: var(--panel); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); }
.mix .user, .mix .srch, .mix .rnd:not(.dark):not(.sm) { background: var(--field); }
.mix .dz-lg i { background: var(--logo); } .mix .dz-lg i:nth-child(3) { background: var(--gold-grad); }
"""

GOLD = "linear-gradient(135deg, #E7D3A2 0%, #CFB783 45%, #A68B55 100%)"
MIX = {
    "subtle": {
        "name": "Mixed, subtle", "blurb": "Gradients only where your eye should go: the black-to-bronze nav rail, the selected tile and the 'next action' card. Everything you read stays plain.",
        "light": f"--surface:#FFFFFF; --panel:#F4EFE5; --field:#F8F4EC; --sel:#EDE5D6; --line:#E6DDCD; --ink:#141414; --ink2:#4A4740; --muted:#8E8778; --acc:#141414; --on-acc:#FFFFFF; --gold:#CFB783; --rail:#141414; --rail-ic:#AAA091; --rail-line:#3A342B; --nav-on:#CFB783; --nav-on-ic:#141414; --badge:#CFB783; --badge-ic:#141414; --logo:#E7DECA;"
                 f"--page-bg:#FFFFFF; --rail-grad:linear-gradient(180deg,#141414 0%,#2A241B 60%,#4A3F2E 100%); --gold-grad:{GOLD};"
                 "--sel-grad:linear-gradient(140deg,#FFFDF8 0%,#F3E8D2 100%); --sel-line:#CFB783; --sel-ink:#141414; --sel-ink2:#77664B;"
                 "--key-grad:linear-gradient(135deg,#2A241B 0%,#4A3F2E 55%,#77664B 100%); --key-ink:#F6F0E4; --key-ink2:#CFC3AB; --key-ring:#CFB783; --key-btn:#CFB783; --key-btn-ink:#141414;"
                 "--btn-grad:#141414; --btn-ink:#FFFFFF; --open-line:#141414;",
        "dark": f"--surface:#14120F; --panel:#211D18; --field:#2A251F; --sel:#2E2922; --line:#352F27; --ink:#F3ECDD; --ink2:#D2C6AE; --muted:#9A8D74; --acc:#CFB783; --on-acc:#141414; --gold:#CFB783; --rail:#000; --rail-ic:#8E8778; --rail-line:#2A251F; --nav-on:#CFB783; --nav-on-ic:#141414; --badge:#CFB783; --badge-ic:#141414; --logo:#E7DECA;"
                f"--page-bg:#14120F; --rail-grad:linear-gradient(180deg,#000 0%,#14110C 55%,#2E2619 100%); --gold-grad:{GOLD};"
                "--sel-grad:linear-gradient(140deg,#2E2619 0%,#4A3F2E 100%); --sel-line:#A68B55; --sel-ink:#F6F0E4; --sel-ink2:#CFC3AB;"
                "--key-grad:linear-gradient(135deg,#4A3F2E 0%,#77664B 55%,#A68B55 100%); --key-ink:#FFFDF8; --key-ink2:#E7DECA; --key-ring:#F3E2B8; --key-btn:#F6F0E4; --key-btn-ink:#141414;"
                "--btn-grad:#CFB783; --btn-ink:#141414; --open-line:#CFB783;",
    },
    "wow": {
        "name": "Mixed, wow", "blurb": "The desert comes into the app: a soft sand-to-gold glow behind see-through panels, gold gradient buttons, a gold ring round Ask Luex and the gold active item. Lists stay plain so they're still easy to read.",
        "light": f"--surface:#FFFDF9; --panel:rgba(255,252,246,.72); --field:rgba(255,255,255,.7); --sel:#EDE5D6; --line:#E6DCC9; --ink:#141414; --ink2:#4A4740; --muted:#8C7F66; --acc:#141414; --on-acc:#FFFFFF; --gold:#CFB783; --rail:#141414; --rail-ic:#AAA091; --rail-line:#3A342B; --nav-on:#CFB783; --nav-on-ic:#141414; --badge:#CFB783; --badge-ic:#141414; --logo:#E7DECA;"
                 f"--page-bg:radial-gradient(70% 90% at 85% 100%, #EBD7AE 0%, rgba(235,215,174,0) 60%), radial-gradient(60% 70% at 10% 0%, #F7EFE0 0%, rgba(247,239,224,0) 70%), linear-gradient(180deg,#FBF7EF 0%,#F2E6CF 100%);"
                 f"--rail-grad:linear-gradient(180deg,#141414 0%,#2A241B 55%,#77664B 100%); --gold-grad:{GOLD};"
                 "--sel-grad:linear-gradient(140deg,#FFF9EC 0%,#EBD7AE 100%); --sel-line:#A68B55; --sel-ink:#141414; --sel-ink2:#77664B;"
                 "--key-grad:linear-gradient(135deg,#141414 0%,#4A3F2E 50%,#A68B55 100%); --key-ink:#FFFDF8; --key-ink2:#E7DECA; --key-ring:#E7D3A2; --key-btn:linear-gradient(135deg,#F3E2B8,#CFB783); --key-btn-ink:#141414;"
                 f"--btn-grad:linear-gradient(135deg,#2A241B 0%,#141414 100%); --btn-ink:#FFFFFF; --open-line:#A68B55;",
        "dark": f"--surface:#13110E; --panel:rgba(32,28,22,.72); --field:rgba(48,42,33,.7); --sel:#2E2922; --line:#3A3329; --ink:#F3ECDD; --ink2:#D2C6AE; --muted:#9A8D74; --acc:#CFB783; --on-acc:#141414; --gold:#CFB783; --rail:#000; --rail-ic:#8E8778; --rail-line:#2A251F; --nav-on:#CFB783; --nav-on-ic:#141414; --badge:#CFB783; --badge-ic:#141414; --logo:#E7DECA;"
                f"--page-bg:radial-gradient(70% 90% at 85% 100%, rgba(166,139,85,.35) 0%, rgba(166,139,85,0) 60%), radial-gradient(60% 70% at 10% 0%, rgba(119,102,75,.25) 0%, rgba(119,102,75,0) 70%), linear-gradient(180deg,#14120F 0%,#1C1812 100%);"
                f"--rail-grad:linear-gradient(180deg,#000 0%,#14110C 50%,#4A3F2E 100%); --gold-grad:{GOLD};"
                "--sel-grad:linear-gradient(140deg,#3A3022 0%,#77664B 100%); --sel-line:#CFB783; --sel-ink:#FFFDF8; --sel-ink2:#E7DECA;"
                "--key-grad:linear-gradient(135deg,#4A3F2E 0%,#A68B55 60%,#CFB783 100%); --key-ink:#141414; --key-ink2:#3A3022; --key-ring:#141414; --key-btn:#141414; --key-btn-ink:#F6F0E4;"
                f"--btn-grad:{GOLD}; --btn-ink:#141414; --open-line:#CFB783;",
    },
}
mblocks = ""
for key, t in MIX.items():
    mblocks += f'''<h2>{t["name"]}</h2><p class="lead">{t["blurb"]}</p>
    <div class="pair">
      <div><p class="tag-l"><i style="background:#fff"></i>Light</p><div class="frame mix" style="{t["light"]} {STATUS_L}">{FR}</div></div>
      <div><p class="tag-l"><i style="background:#141414"></i>Dark</p><div class="frame mix" style="{t["dark"]} {STATUS_D}">{FR}</div></div>
    </div>'''
page2 = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Luex Mixed Venus</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500&display=swap">
<style>{css}{MIX_CSS}</style></head><body>
<div class="wrap">
  <h1>Luex in mixed Venus colours</h1>
  <p class="lead">Black and bronze frame the page, cream holds the work, gold marks what matters, with gradients in a few chosen places. Two strengths, each in light and dark. Status colours stay green, amber and red.</p>
  <div class="sw">{"".join(f'<span><b style="background:{c}"></b>{n} {c}</span>' for n, c in pal)}</div>
  {mblocks}
</div>
<script>{M.JS}</script>
</body></html>"""
pathlib.Path(__file__).with_name("app-venus-mix.html").write_text(page2)
print("wrote app-venus-mix.html", len(page2))

# =============================================================== soft style (inspired by the reference)
def rail_soft():
    I = M.ic
    groups = [("", [("grid", "Dashboard", "", False), ("star", "Favourites", "", False)]),
              ("Work", [("shield", "Compliance", "8", True), ("clock", "Timesheets", "14", False), ("cal", "Time off", "3", False), ("brief", "Jobs", "2", False)]),
              ("People and money", [("people", "People", "", False), ("pound", "Expenses", "", False)]),
              ("", [("gear", "Settings", "", False)])]
    nav = ""
    for g, items in groups:
        if g: nav += f'<p class="sg">{g}</p>'
        for icn, label, badge, on in items:
            b = f'<em>{badge}</em>' if badge else ""
            nav += f'<span class="sni{" on" if on else ""}"><span class="ico">{I(icn)}</span>{label}{b}</span>'
    return f'''<aside class="soft-rail">
      <div class="brand"><span class="dz-lg"><i></i><i></i><i></i></span><span>LUEX</span></div>
      <nav class="snav">{nav}</nav>
      <div class="modepill"><span class="on">{I("sun")}</span><span>{I("moon")}</span></div>
    </aside>'''

M.P["sun"] = '<circle cx="12" cy="12" r="3.5"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6l1.4 1.4M17 17l1.4 1.4M5.6 18.4L7 17M17 7l1.4-1.4"/>'
M.P["moon"] = '<path d="M19 14.5A7.5 7.5 0 1 1 9.5 5a6 6 0 0 0 9.5 9.5z"/>'

def soft_frame():
    h = f'''<div class="fit"><div class="m-page">{rail_soft()}<div class="m-main">{M.header_ai(True)}{M.tiles(2, False)}<div class="m-body">{M.main_window("listplain", False)}{M.detail(False)}</div></div></div></div>'''
    for a, b in [("#C98A1B", "var(--amber)"), ("#2F8F5B", "var(--green)"), ("#C2413A", "var(--red)"), ("#1C1C1E", "var(--ink)")]:
        h = h.replace(a, b)
    return h

SOFT_CSS = """
.frame.soft { padding: 22px; background: var(--backdrop); border-radius: 26px; }
.soft .m-page { grid-template-columns: 196px 1fr; gap: 12px; padding: 12px; border-radius: 22px; background: var(--surface); box-shadow: 0 30px 60px -30px rgba(40,30,15,.45); }
.soft-rail { background: var(--rail); border-radius: 20px; padding: 22px 12px 14px; display: flex; flex-direction: column; box-shadow: var(--soft-sh); }
.brand { display: flex; align-items: center; gap: 10px; padding: 0 8px; }
.brand span:last-child { font-size: 19px; font-weight: 500; letter-spacing: 4px; color: var(--ink); }
.snav { margin-top: 24px; display: grid; gap: 3px; }
.sg { margin: 14px 10px 6px; font-size: 10px; letter-spacing: .6px; text-transform: uppercase; color: var(--muted); }
.sni { display: flex; align-items: center; gap: 11px; height: 42px; padding: 0 10px 0 6px; border-radius: 14px; font-size: 13px; color: var(--rail-ic); }
.sni .ico { width: 30px; height: 30px; border-radius: 10px; display: grid; place-items: center; }
.sni em { margin-left: auto; font-style: normal; font-size: 10.5px; min-width: 20px; height: 20px; padding: 0 6px; border-radius: 99px; display: grid; place-items: center; background: var(--field); color: var(--ink2); }
.sni.on { background: var(--nav-on); color: var(--nav-on-ic); box-shadow: 0 10px 18px -10px rgba(20,15,5,.55); }
.sni.on .ico { background: var(--surface); color: var(--ink); border-radius: 50%; }
.sni.on em { background: var(--gold); color: #141414; }
.modepill { margin-top: auto; align-self: start; display: flex; gap: 4px; padding: 4px; border-radius: 99px; background: var(--surface); box-shadow: var(--soft-sh); }
.modepill span { width: 40px; height: 30px; border-radius: 99px; display: grid; place-items: center; color: var(--muted); }
.modepill .on { background: var(--nav-on); color: var(--nav-on-ic); }
.soft .tl h4 { font-size: 30px; letter-spacing: -1.1px; }
.soft .m-main { grid-template-rows: 58px 92px 1fr; }
.soft .tile, .soft .mw, .soft .dw { background: var(--panel); box-shadow: var(--soft-sh); }
.soft .tile.sel { background: var(--surface); box-shadow: inset 0 0 0 1.5px var(--c), var(--soft-sh); }
.soft .lr { background: var(--surface); box-shadow: inset 0 0 0 1px var(--line); }
.soft .lr.open { box-shadow: inset 0 0 0 1.5px var(--ink), 0 10px 20px -14px rgba(20,15,5,.45); }
.soft .key, .soft .facts div { background: var(--surface); box-shadow: inset 0 0 0 1px var(--line); }
.soft .mini-ring { width: 88px; height: 88px; }
.soft .mini-ring::before { content: ""; position: absolute; inset: 9px; border-radius: 50%; background: var(--surface); box-shadow: inset 0 2px 5px rgba(0,0,0,.06), 0 8px 16px -8px rgba(40,30,15,.35); }
.soft .mini-ring svg { position: relative; }
.soft .mini-ring .pr { stroke: var(--gold-ring); }
.soft .user, .soft .srch, .soft .rnd:not(.dark):not(.sm) { background: var(--panel); box-shadow: var(--soft-sh); }
.soft .tabbar { box-shadow: 0 12px 26px -12px rgba(40,30,15,.45), inset 0 0 0 1px var(--line); }
"""
SOFT = {
    "light": "--backdrop:#E7E3DC; --surface:#FFFFFF; --panel:#F6F4F0; --field:#F1EEE8; --sel:#EFEAE0; --line:#ECE7DE; --ink:#141414; --ink2:#4A4740; --muted:#8E8778; --acc:#141414; --on-acc:#FFFFFF; --gold:#CFB783; --gold-ring:#A68B55; --rail:#F6F4F0; --rail-ic:#4A4740; --rail-line:#E5DFD4; --nav-on:#141414; --nav-on-ic:#FFFFFF; --badge:#CFB783; --badge-ic:#141414; --logo:#141414; --soft-sh: inset 0 1px 0 rgba(255,255,255,.9), 0 10px 24px -18px rgba(70,55,30,.4);",
    "dark": "--backdrop:#0B0A09; --surface:#171614; --panel:#1F1D1A; --field:#29261F; --sel:#2B2823; --line:#2E2B26; --ink:#F2EEE6; --ink2:#C9C2B5; --muted:#8E8778; --acc:#E7DECA; --on-acc:#141414; --gold:#CFB783; --gold-ring:#CFB783; --rail:#1F1D1A; --rail-ic:#C9C2B5; --rail-line:#2E2B26; --nav-on:#E7DECA; --nav-on-ic:#141414; --badge:#CFB783; --badge-ic:#141414; --logo:#E7DECA; --soft-sh: inset 0 1px 0 rgba(255,255,255,.04), 0 12px 26px -16px rgba(0,0,0,.75);",
}
SF = soft_frame()
page3 = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Luex Soft Style</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500&display=swap">
<style>{css}{SOFT_CSS}</style></head><body>
<div class="wrap">
  <h1>Luex, soft style</h1>
  <p class="lead">Inspired by the reference: one floating card on a soft background, a labelled sidebar with a dark pill for the page you're on, soft warm-white panels with gentle depth, a big page title and a soft dial. Venus colours, light and dark. Same module layout as before.</p>
  <div class="pair">
    <div><p class="tag-l"><i style="background:#fff"></i>Light</p><div class="frame soft" style="{SOFT["light"]} {STATUS_L}">{SF}</div></div>
    <div><p class="tag-l"><i style="background:#141414"></i>Dark</p><div class="frame soft" style="{SOFT["dark"]} {STATUS_D}">{SF.replace('<span class="on"><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3.5"/>', '<span><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3.5"/>').replace('<span><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 14.5', '<span class="on"><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 14.5')}</div></div>
  </div>
</div>
<script>{M.JS}</script>
</body></html>"""
pathlib.Path(__file__).with_name("app-soft-style.html").write_text(page3)
print("wrote app-soft-style.html", len(page3))

# =============================================================== clean variations
def to_dark(h):
    return (h.replace('<span class="on"><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3.5"/>', '<span><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="3.5"/>')
             .replace('<span><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 14.5', '<span class="on"><svg class="i" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 14.5'))

VAR_CSS = """
/* Paper: flat, hairlines, table list, gold bar for the active item */
.v-paper .soft-rail, .v-paper .tile, .v-paper .mw, .v-paper .dw, .v-paper .user, .v-paper .srch, .v-paper .rnd:not(.dark):not(.sm), .v-paper .modepill { box-shadow: inset 0 0 0 1px var(--line); }
.v-paper .m-page { box-shadow: 0 1px 2px rgba(0,0,0,.04); }
.v-paper .tile.sel { box-shadow: inset 0 0 0 1.5px var(--c); }
.v-paper .sni.on { background: transparent; color: var(--ink); font-weight: 500; box-shadow: none; position: relative; }
.v-paper .sni.on::before { content: ""; position: absolute; left: -12px; top: 11px; width: 3px; height: 20px; border-radius: 0 3px 3px 0; background: var(--gold-ring); }
.v-paper .sni.on .ico { background: var(--panel); border-radius: 10px; }
.v-paper .lrows { gap: 0; }
.v-paper .lr { background: transparent; box-shadow: none; border-radius: 0; border-bottom: 1px solid var(--line); }
.v-paper .lr.open { background: var(--surface); border-radius: 12px; box-shadow: inset 0 0 0 1.5px var(--ink); border-bottom-color: transparent; }
.v-paper .key, .v-paper .facts div { box-shadow: inset 0 0 0 1px var(--line); }
.v-paper .mini-ring::before { box-shadow: none; }
.v-paper .tabbar { box-shadow: inset 0 0 0 1px var(--line), 0 8px 18px -12px rgba(0,0,0,.25); }

/* Ink sidebar */
.v-ink .soft-rail { background: var(--ink-rail); box-shadow: none; }
.v-ink .brand span:last-child { color: #F2EEE6; }
.v-ink .sni { color: #AAA091; } .v-ink .sg { color: #77664B; }
.v-ink .sni em { background: rgba(255,255,255,.08); color: #E7DECA; }
.v-ink .sni.on { background: #E7DECA; color: #141414; box-shadow: none; }
.v-ink .sni.on .ico { background: #141414; color: #E7DECA; }
.v-ink .modepill { background: rgba(255,255,255,.06); box-shadow: none; }
.v-ink .modepill span { color: #8E8778; } .v-ink .modepill .on { background: #E7DECA; color: #141414; }
.v-ink .dz-lg i { background: #E7DECA; }

/* Cream */
.v-cream .m-page { box-shadow: 0 24px 50px -30px rgba(90,70,30,.45); }
.v-cream .tile, .v-cream .mw, .v-cream .dw { box-shadow: 0 1px 0 rgba(255,255,255,.6) inset, 0 6px 16px -12px rgba(90,70,30,.35); }
.v-cream .soft-rail { box-shadow: none; }
.v-cream .sni.on { box-shadow: 0 8px 16px -10px rgba(119,102,75,.8); }
.v-cream .lr, .v-cream .key, .v-cream .facts div { background: var(--panel); }
.v-cream .mw, .v-cream .dw { background: var(--field); }
.v-cream .sni.on .ico { background: rgba(255,255,255,.22); color: var(--nav-on-ic); }

/* Outline */
.v-line .tile, .v-line .mw, .v-line .dw, .v-line .soft-rail { box-shadow: inset 0 0 0 1px var(--line); }
.v-line .tile.sel { box-shadow: inset 0 0 0 1px var(--line); overflow: hidden; }
.v-line .tile.sel::before { content: ""; position: absolute; left: 0; right: 0; top: 0; height: 3px; background: var(--gold-ring); }
.v-line .sni.on { background: var(--panel); color: var(--ink); box-shadow: inset 0 0 0 1px var(--line); }
.v-line .sni.on .ico { background: var(--ink); color: var(--surface); }
.v-line .sni.on em { background: var(--gold); }
.v-line .dtabs { background: transparent; border-bottom: 1px solid var(--line); border-radius: 0; padding: 0; gap: 0; }
.v-line .dtabs span { border-radius: 0; height: 34px; line-height: 34px; }
.v-line .dtabs .on { background: transparent; box-shadow: inset 0 -2px 0 var(--ink); }
.v-line .seg { background: transparent; box-shadow: inset 0 0 0 1px var(--line); }
.v-line .lr { box-shadow: none; border-bottom: 1px solid var(--line); border-radius: 0; background: transparent; }
.v-line .lrows { gap: 0; }
.v-line .lr.open { background: var(--panel); border-radius: 12px; box-shadow: inset 0 0 0 1.5px var(--ink); }
.v-line .key { box-shadow: inset 0 0 0 1px var(--line); }
.v-line .mini-ring::before { box-shadow: none; background: transparent; }
"""

base_l = SOFT["light"]; base_d = SOFT["dark"]
VARS = [
    ("v-paper", "Paper", "Flat and quiet: no shadows, fine lines, the list as a simple table, and a thin gold bar beside the page you're on.",
     base_l.replace("--panel:#F6F4F0", "--panel:#FAF8F5").replace("--rail:#F6F4F0", "--rail:#FAF8F5").replace("--backdrop:#E7E3DC", "--backdrop:#EFECE6"),
     base_d.replace("--backdrop:#0B0A09", "--backdrop:#0E0D0C")),
    ("v-ink", "Ink sidebar", "A Luex Black sidebar with cream text frames every page, like the black business card. The work area stays light and calm.",
     base_l + " --ink-rail:#141414;", base_d + " --ink-rail:#0B0A09;"),
    ("v-cream", "Cream", "The whole app sits on a soft Cloud Cream tint with crisp white cards on top. Warm Ochre marks the page you're on.",
     "--backdrop:#E2D9C8; --surface:#F3ECDF; --panel:#FFFDF9; --field:#F8F3EA; --sel:#EFE6D6; --line:#E6DCC9; --ink:#141414; --ink2:#4F4636; --muted:#8C7F66; --acc:#141414; --on-acc:#FFFFFF; --gold:#CFB783; --gold-ring:#A68B55; --rail:#F3ECDF; --rail-ic:#4F4636; --rail-line:#E0D3BB; --nav-on:#A68B55; --nav-on-ic:#FFFFFF; --badge:#CFB783; --badge-ic:#141414; --logo:#141414; --soft-sh: inset 0 1px 0 rgba(255,255,255,.9), 0 10px 24px -18px rgba(90,70,30,.4);",
     "--backdrop:#0E0C09; --surface:#1A1712; --panel:#24201A; --field:#2D2820; --sel:#332C22; --line:#3A3328; --ink:#F3ECDD; --ink2:#D2C6AE; --muted:#9A8D74; --acc:#CFB783; --on-acc:#141414; --gold:#CFB783; --gold-ring:#CFB783; --rail:#1A1712; --rail-ic:#D2C6AE; --rail-line:#3A3328; --nav-on:#A68B55; --nav-on-ic:#FFFFFF; --badge:#CFB783; --badge-ic:#141414; --logo:#E7DECA; --soft-sh: inset 0 1px 0 rgba(255,255,255,.04), 0 12px 26px -16px rgba(0,0,0,.75);"),
    ("v-line", "Outline", "White panels drawn with fine outlines, underline tabs and a gold top edge on the chosen tile. The crispest of the set.",
     base_l.replace("--panel:#F6F4F0", "--panel:#FFFFFF").replace("--rail:#F6F4F0", "--rail:#FFFFFF").replace("--surface:#FFFFFF", "--surface:#FBFAF7").replace("--backdrop:#E7E3DC", "--backdrop:#ECE8E1"),
     base_d.replace("--panel:#1F1D1A", "--panel:#151412").replace("--rail:#1F1D1A", "--rail:#151412").replace("--surface:#171614", "--surface:#100F0E")),
]
vb = ""
for cls, name, blurb, L, D in VARS:
    vb += f'''<h2>{name}</h2><p class="lead">{blurb}</p>
    <div class="pair">
      <div><p class="tag-l"><i style="background:#fff"></i>Light</p><div class="frame soft {cls}" style="{L} {STATUS_L}">{SF}</div></div>
      <div><p class="tag-l"><i style="background:#141414"></i>Dark</p><div class="frame soft {cls}" style="{D} {STATUS_D}">{to_dark(SF)}</div></div>
    </div>'''
page4 = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Luex Clean Variations</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500&display=swap">
<style>{css}{SOFT_CSS}{VAR_CSS}</style></head><body>
<div class="wrap">
  <h1>Luex, clean variations</h1>
  <p class="lead">Four clean takes on the soft style, each in Venus light and dark. Same layout, same labelled sidebar; only the surfaces, lines and the way the active item is marked change.</p>
  {vb}
</div>
<script>{M.JS}</script>
</body></html>"""
pathlib.Path(__file__).with_name("app-clean-variations.html").write_text(page4)
print("wrote app-clean-variations.html", len(page4))

# =============================================================== richer Ink variations
RICH_CSS = """
/* shared: Ink + gold touches */
.v-rich .brand { padding-bottom: 18px; border-bottom: 1px solid rgba(207,183,131,.35); }
.v-rich .sni.on { background: linear-gradient(135deg, #F3E2B8 0%, #CFB783 55%, #B39A63 100%); color: #141414; box-shadow: 0 10px 20px -10px rgba(207,183,131,.7); }
.v-rich .sni.on .ico { background: #141414; color: #CFB783; }
.v-rich .sni.on em { background: #141414; color: #CFB783; }
.v-rich .tile.sel { background: var(--sel-bg); box-shadow: 0 14px 26px -14px rgba(20,15,5,.6); }
.v-rich .tile.sel b { color: #CFB783; } .v-rich .tile.sel .t-top, .v-rich .tile.sel small { color: #C9BFAE; }
.v-rich .tile.sel .sdot { box-shadow: 0 0 0 3px rgba(224,138,30,.25); }
.v-rich .st-pill { background: color-mix(in srgb, var(--c) 15%, transparent); color: var(--ink); font-weight: 500; }
.v-rich .lr .ci, .v-rich .chip .i { color: var(--bronze); }
.v-rich .lr .ci { background: color-mix(in srgb, #CFB783 24%, transparent); }
.v-rich .lr.open { box-shadow: inset 0 0 0 1.5px var(--ink), 0 12px 22px -14px rgba(20,15,5,.45); }
.v-rich .mini-ring .pr { stroke: #CFB783; }
.v-rich .tl h4::after { content: "."; color: #CFB783; }

/* desert: photo behind, glow in the rail, bronze action card */
.v-desert.frame { background: var(--desert) center 40% / cover no-repeat; }
.v-desert .soft-rail { background: radial-gradient(130% 45% at 50% 108%, rgba(166,139,85,.55), rgba(166,139,85,0) 65%), var(--ink-rail); }
.v-desert .key { background: linear-gradient(135deg, #141414 0%, #3A3022 55%, #77664B 100%); box-shadow: 0 14px 28px -16px rgba(40,30,15,.6); }
.v-desert .key-r p, .v-desert .key-r p b, .v-desert .mini-ring b { color: #F6F0E4; } .v-desert .mini-ring small { color: #CFC3AB; }
.v-desert .mini-ring::before { background: rgba(255,255,255,.06); box-shadow: none; }
.v-desert .mini-ring .tr { stroke: rgba(255,255,255,.18); }
.v-desert .key .btn-d { background: linear-gradient(135deg, #F3E2B8, #CFB783); color: #141414; }
.v-desert .key .btn-l { background: rgba(255,255,255,.12); color: #F6F0E4; }
.v-desert .m-page { box-shadow: 0 40px 80px -30px rgba(40,25,5,.6); }

/* colour: tinted tiles, progress bars, split bar */
.v-colour .tile:not(.sel) { background: color-mix(in srgb, var(--c) 9%, var(--panel)); }
.v-colour .tile { padding-bottom: 20px; }
.v-colour .tile::after { content: ""; position: absolute; left: 16px; right: 16px; bottom: 9px; height: 4px; border-radius: 99px; background: linear-gradient(90deg, var(--bar-c, var(--c)) var(--w), color-mix(in srgb, var(--c) 18%, transparent) var(--w)); }
.v-colour .tile:nth-child(1) { --w: 100%; } .v-colour .tile:nth-child(2) { --w: 88%; } .v-colour .tile:nth-child(3) { --w: 8.5%; --bar-c: #CFB783; } .v-colour .tile:nth-child(4) { --w: 3.2%; }
.v-colour .tile:nth-child(1)::after { background: var(--ink); opacity: .85; }
.split { display: none; }
.v-colour .split { display: flex; height: 8px; border-radius: 99px; overflow: hidden; gap: 3px; margin-left: auto; width: 220px; }
.v-colour .split i { display: block; height: 100%; border-radius: 99px; }
.v-colour .mw-h { width: 100%; } .mw-h > span:nth-child(2) { font-size: 12px; color: var(--muted); font-weight: 400; }
.v-colour .split-l { display: none; } .v-colour .split-l { display: inline; font-size: 11px; color: var(--muted); }
"""
SPLIT = '<span class="split"><i style="flex:219;background:var(--green)"></i><i style="flex:21;background:var(--amber)"></i><i style="flex:8;background:var(--red)"></i></span>'
SFR = SF.replace('<div class="mw-h"><b>Due soon</b><span>21 records</span></div>', f'<div class="mw-h"><b>Due soon</b><span>21 records</span>{SPLIT}</div>')
inkL = base_l + " --ink-rail:#141414; --sel-bg:#141414; --bronze:#77664B;"
inkD = base_d + " --ink-rail:#0B0A09; --sel-bg:linear-gradient(135deg,#2A241B,#4A3F2E); --bronze:#CFB783;"
RICH = [
    ("v-ink v-rich", "Ink + gold", "Gold pill for the page you're on, a fine gold line under the logo, the chosen tile in black with a gold number, status pills tinted in their colour and icons in soft gold circles.", inkL, inkD),
    ("v-ink v-rich v-desert", "Ink + desert", "Everything above, with the dune photo from the website behind the app (dusk in dark mode), a bronze glow at the foot of the sidebar and a bronze 'next action' card.",
     inkL + " --desert: linear-gradient(rgba(255,250,240,.15), rgba(255,250,240,.15)), url(img/dune-hero.webp);",
     inkD + " --desert: linear-gradient(rgba(8,6,3,.72), rgba(8,6,3,.82)), url(img/dune-hero.webp);"),
    ("v-ink v-rich v-colour", "Ink + colour", "Everything in Ink + gold, with each status tile softly tinted in its colour and a small progress bar, and a split bar above the list showing valid, due and expired at a glance.", inkL, inkD),
]
rb = ""
for cls, name, blurb, L, D in RICH:
    rb += f'''<h2>{name}</h2><p class="lead">{blurb}</p>
    <div class="pair">
      <div><p class="tag-l"><i style="background:#fff"></i>Light</p><div class="frame soft {cls}" style="{L} {STATUS_L}">{SFR}</div></div>
      <div><p class="tag-l"><i style="background:#141414"></i>Dark</p><div class="frame soft {cls}" style="{D} {STATUS_D}">{to_dark(SFR)}</div></div>
    </div>'''
page5 = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Luex Ink Variations</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500&display=swap">
<style>{css}{SOFT_CSS}{VAR_CSS}{RICH_CSS}</style></head><body>
<div class="wrap">
  <h1>Luex, Ink sidebar with more life</h1>
  <p class="lead">The Ink sidebar you picked, three ways to make it richer while keeping it clean. Each in Venus light and dark. The list itself stays plain so it's always easy to read.</p>
  {rb}
</div>
<script>{M.JS}</script>
</body></html>"""
pathlib.Path(__file__).with_name("app-ink-variations.html").write_text(page5)
print("wrote app-ink-variations.html", len(page5))

# =============================================================== Ink + desert, white surfaces
WHITE_L = ("--backdrop:#E9E7E3; --surface:#FFFFFF; --panel:#F6F6F5; --field:#F2F2F1; --sel:#EFEFED; --line:#EAEAE8; --ink:#141414; --ink2:#47474A; --muted:#8A8A8E;"
           " --acc:#141414; --on-acc:#FFFFFF; --gold:#CFB783; --gold-ring:#A68B55; --rail:#141414; --rail-ic:#AAA091; --rail-line:#2C2A27; --nav-on:#CFB783; --nav-on-ic:#141414;"
           " --badge:#CFB783; --badge-ic:#141414; --logo:#E7DECA; --ink-rail:#141414; --sel-bg:#141414; --bronze:#77664B;"
           " --soft-sh: inset 0 1px 0 rgba(255,255,255,.95), 0 10px 24px -18px rgba(20,20,20,.28);"
           " --desert: linear-gradient(rgba(255,255,255,.12), rgba(255,255,255,.12)), url(img/dune-hero.webp);")
WHITE_D = ("--backdrop:#0B0B0B; --surface:#141414; --panel:#1B1B1B; --field:#232323; --sel:#262626; --line:#2B2B2B; --ink:#F5F3EF; --ink2:#C8C6C1; --muted:#8E8C88;"
           " --acc:#E7DECA; --on-acc:#141414; --gold:#CFB783; --gold-ring:#CFB783; --rail:#0B0B0B; --rail-ic:#AAA091; --rail-line:#222; --nav-on:#CFB783; --nav-on-ic:#141414;"
           " --badge:#CFB783; --badge-ic:#141414; --logo:#E7DECA; --ink-rail:#0A0A0A; --sel-bg:linear-gradient(135deg,#1F1B14,#3A3022); --bronze:#CFB783;"
           " --soft-sh: inset 0 1px 0 rgba(255,255,255,.04), 0 12px 26px -16px rgba(0,0,0,.8);"
           " --desert: linear-gradient(rgba(6,5,3,.74), rgba(6,5,3,.84)), url(img/dune-hero.webp);")
WHITE_CSS = """
.v-white .tile:not(.sel), .v-white .mw, .v-white .dw { background: var(--panel); }
.v-white .lr, .v-white .facts div { background: var(--surface); }
.v-white .m-page { background: var(--surface); }
.v-nobg.frame { background: var(--surface); padding: 0; }
.v-nobg .m-page { box-shadow: none; border-radius: 0; }
.v-blur.frame { position: relative; overflow: hidden; padding: 22px; background: var(--surface); }
.v-blur.frame::before { content: ""; position: absolute; inset: -60px; background: var(--desert) center 40% / cover no-repeat; filter: blur(26px) saturate(1.05); transform: scale(1.05); }
.v-blur .fit { position: relative; z-index: 1; }
.v-blur .m-page { box-shadow: 0 40px 80px -30px rgba(40,25,5,.55); }
"""
cls = "v-ink v-rich v-desert v-white v-blur"
page6 = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Luex Ink White</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500&display=swap">
<style>{css}{SOFT_CSS}{VAR_CSS}{RICH_CSS}{WHITE_CSS}</style></head><body>
<div class="wrap">
  <h1>Ink, in white</h1>
  <p class="lead">The Ink sidebar with clean white and neutral grey surfaces, and the desert softly blurred behind, so it reads as warm light rather than a photo. The Venus gold, bronze and black stand out as accents.</p>
  <div class="pair">
    <div><p class="tag-l"><i style="background:#fff"></i>Light</p><div class="frame soft {cls}" style="{WHITE_L} {STATUS_L}">{SFR}</div></div>
    <div><p class="tag-l"><i style="background:#141414"></i>Dark</p><div class="frame soft {cls}" style="{WHITE_D} {STATUS_D}">{to_dark(SFR)}</div></div>
  </div>
</div>
<script>{M.JS}</script>
</body></html>"""
pathlib.Path(__file__).with_name("app-ink-desert-white.html").write_text(page6)
print("wrote app-ink-desert-white.html", len(page6))

# =============================================================== glass over a sharp desert
GLASS_CSS = """
.v-glass.frame { padding: 0; background: var(--desert-sharp) center 45% / cover no-repeat; }
.v-glass .m-page { background: transparent; box-shadow: none; border-radius: 0; }
.v-glass .soft-rail { background: var(--glass-rail); backdrop-filter: blur(22px) saturate(1.1); -webkit-backdrop-filter: blur(22px) saturate(1.1); box-shadow: 0 20px 40px -20px rgba(0,0,0,.5); }
.v-glass .tile:not(.sel), .v-glass .mw, .v-glass .dw, .v-glass .user, .v-glass .srch, .v-glass .rnd:not(.dark):not(.sm), .v-glass .pill:not(.srch), .v-glass .tabbar, .v-glass .ask {
  background: var(--glass); backdrop-filter: blur(24px) saturate(1.15); -webkit-backdrop-filter: blur(24px) saturate(1.15);
  box-shadow: inset 0 0 0 1px var(--glass-edge), 0 14px 30px -18px rgba(40,25,5,.45); }
.v-glass .lr, .v-glass .facts div, .v-glass .cmt, .v-glass .dtabs { background: var(--glass-solid); box-shadow: inset 0 0 0 1px var(--glass-edge); }
.v-glass .dtabs .on { background: var(--surface); }
.v-glass .m-hd { padding: 4px 6px 0; }
.v-glass .m-title small, .v-glass .tl h4 { text-shadow: 0 1px 12px var(--title-glow); }
.v-glass .lr.open { box-shadow: inset 0 0 0 1.5px var(--ink), 0 12px 22px -14px rgba(20,15,5,.45); }
"""
GL = WHITE_L + (" --desert-sharp: url(img/dune-hero.webp); --glass: rgba(255,255,255,.62); --glass-solid: rgba(255,255,255,.86);"
                " --glass-edge: rgba(255,255,255,.7); --glass-rail: rgba(20,20,20,.78); --title-glow: rgba(255,255,255,.7);")
GD = WHITE_D + (" --desert-sharp: linear-gradient(rgba(6,5,3,.55), rgba(6,5,3,.7)), url(img/dune-hero.webp); --glass: rgba(20,20,20,.55); --glass-solid: rgba(24,24,24,.82);"
                " --glass-edge: rgba(255,255,255,.08); --glass-rail: rgba(8,8,8,.72); --title-glow: rgba(0,0,0,.6);")
gcls = "v-ink v-rich v-desert v-white v-glass"
page7 = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Luex Desert Glass</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500&display=swap">
<style>{css}{SOFT_CSS}{VAR_CSS}{RICH_CSS}{WHITE_CSS}{GLASS_CSS}</style></head><body>
<div class="wrap">
  <h1>Desert glass</h1>
  <p class="lead">The desert photo sharp behind the whole app. Every box is frosted glass, so the desert shows through blurred. List rows and facts are near-solid so they stay easy to read. Light and dark (dusk).</p>
  <div class="pair">
    <div><p class="tag-l"><i style="background:#fff"></i>Light</p><div class="frame soft {gcls}" style="{GL} {STATUS_L}">{SFR}</div></div>
    <div><p class="tag-l"><i style="background:#141414"></i>Dark</p><div class="frame soft {gcls}" style="{GD} {STATUS_D}">{to_dark(SFR)}</div></div>
  </div>
</div>
<script>{M.JS}</script>
</body></html>"""
pathlib.Path(__file__).with_name("app-desert-glass.html").write_text(page7)
print("wrote app-desert-glass.html", len(page7))

# =============================================================== reference lessons: plain bg, few big tinted boxes, air
REF_CSS = """
.v-ref.frame { padding: 28px; background: var(--plain); border-radius: 26px; }
.v-ref .m-page { background: var(--surface); border-radius: 30px; padding: 12px; gap: 12px; box-shadow: 0 30px 60px -34px rgba(0,0,0,.35); }
.v-ref .soft-rail { border-radius: 24px; }
.v-ref .m-main { gap: 12px; grid-template-rows: 58px 84px 1fr; }
.v-ref .tiles { gap: 12px; }
.v-ref .tile { border-radius: 24px; padding: 14px 18px; box-shadow: none !important; background: var(--t-plain); }
.v-ref .tile:nth-child(2) { background: var(--t-plain); }
.v-ref .tile.sel { background: var(--t-dark); }
.v-ref .tile.sel b { color: #fff; } .v-ref .tile.sel .t-top, .v-ref .tile.sel small { color: rgba(255,255,255,.75); }
.v-ref .tile small { display: none; }
.v-ref .tile b { font-size: 28px; }
.v-ref .m-body { gap: 12px; grid-template-columns: 1fr 360px; }
.v-ref .mw { background: var(--t-cream); border-radius: 26px; padding: 20px 20px 76px; box-shadow: none; }
.v-ref .dw { background: var(--t-grad); border-radius: 26px; padding: 20px; box-shadow: none; }
.v-ref .mw-tools .pill:nth-of-type(n+3):not(.ghost), .v-ref .mw-tools .ghost { display: none; }
.v-ref .mw-tools .pill { background: rgba(255,255,255,.7); box-shadow: none; }
.v-ref .mw-tools::after { content: "Filters"; order: 9; display: inline-flex; align-items: center; height: 32px; padding: 0 14px; border-radius: 99px; background: rgba(255,255,255,.7); font-size: 12px; color: var(--ink2); }
.v-ref .seg { order: 10; background: rgba(255,255,255,.55); }
.v-ref .lhead { display: none; }
.v-ref .lrows { gap: 8px; margin-top: 16px; }
.v-ref .lhead + .lrows { margin-top: 16px; }
.v-ref .lr { background: rgba(255,255,255,.82); box-shadow: none; border-radius: 18px; padding: 11px 14px; grid-template-columns: 0 36px 1.6fr 1fr 1fr 110px; }
.v-ref .lr .tk { visibility: hidden; }
.v-ref .lr .ci { background: var(--t-cream); }
.v-ref .lr.open { background: #fff; box-shadow: 0 12px 24px -14px rgba(60,45,20,.35); }
.v-ref .lr.open .lr-n b::before { content: ""; display: inline-block; width: 6px; height: 6px; border-radius: 50%; background: var(--ink); margin-right: 7px; vertical-align: 2px; }
.v-ref .st-pill { background: #fff; }
.v-ref .chip { background: rgba(255,255,255,.7); }
.v-ref .dw-r .rnd.sm { background: rgba(255,255,255,.7); box-shadow: none; }
.v-ref .key { flex-direction: column; text-align: center; background: rgba(255,255,255,.55) !important; box-shadow: none !important; padding: 18px; gap: 10px; border-radius: 22px; }
.v-ref .key-r p, .v-ref .key-r p b, .v-ref .mini-ring b { color: var(--ink) !important; }
.v-ref .mini-ring small { color: var(--ink2) !important; }
.v-ref .mini-ring { width: 128px; height: 128px; }
.v-ref .mini-ring::before { inset: 14px; background: #fff !important; box-shadow: inset 0 2px 6px rgba(0,0,0,.06), 0 10px 20px -10px rgba(60,45,20,.35) !important; }
.v-ref .mini-ring .tr { stroke: rgba(255,255,255,.7) !important; stroke-width: 6; } .v-ref .mini-ring .pr { stroke: var(--ink) !important; stroke-width: 6; }
.v-ref .mini-ring b { font-size: 30px; }
.v-ref .key-b { justify-content: center; }
.v-ref .key .btn-d { background: var(--ink) !important; color: #fff !important; }
.v-ref .key .btn-l { background: #fff !important; color: var(--ink) !important; }
.v-ref .facts { gap: 10px; }
.v-ref .facts div { background: rgba(255,255,255,.6) !important; box-shadow: none !important; border-radius: 16px; }
.v-ref .facts div:nth-child(n+3) { display: none; }
.v-ref .dtabs { background: rgba(255,255,255,.45); }
.v-ref .acts .act:nth-child(3) { display: none; }
.v-ref .cmt { background: rgba(255,255,255,.7); }
.v-ref .tabbar { box-shadow: 0 10px 24px -14px rgba(60,45,20,.4); }
.v-ref .m-hd .user, .v-ref .m-hd .srch, .v-ref .m-hd .rnd:not(.dark) { background: var(--t-plain); box-shadow: none; }
.v-ref .ask { background: var(--t-plain); box-shadow: none; }
"""
REF_L = WHITE_L + (" --plain:#E6E6E6; --t-plain:#F1F1F0; --t-dark:#141414; --t-cream:#ECE6D8;"
                   " --t-grad: linear-gradient(180deg, #DCDFE4 0%, #E9E6DC 55%, #F1E6C8 100%);")
REF_D = WHITE_D + (" --plain:#0E0E0E; --t-plain:#1C1C1C; --t-dark:#3A3226; --t-cream:#211E19;"
                   " --t-grad: linear-gradient(180deg, #1E2026 0%, #24211C 55%, #3A3022 100%);")
REF_D_FIX = """
.v-ref.dark .lr { background: rgba(255,255,255,.05); } .v-ref.dark .lr.open { background: rgba(255,255,255,.1); }
.v-ref.dark .st-pill, .v-ref.dark .key, .v-ref.dark .facts div, .v-ref.dark .chip, .v-ref.dark .cmt, .v-ref.dark .mw-tools .pill, .v-ref.dark .mw-tools::after { background: rgba(255,255,255,.07) !important; }
.v-ref.dark .mini-ring::before { background: #1C1C1C !important; }
.v-ref.dark .mini-ring .pr { stroke: #CFB783 !important; } .v-ref.dark .mini-ring .tr { stroke: rgba(255,255,255,.12) !important; }
.v-ref.dark .key .btn-d { background: #CFB783 !important; color: #141414 !important; } .v-ref.dark .key .btn-l { background: rgba(255,255,255,.1) !important; color: #F5F3EF !important; }
.v-ref.dark .tile.sel b { color: #CFB783; }
.v-ref.dark .dtabs { background: rgba(255,255,255,.06); } .v-ref.dark .dtabs span { color: #C8C6C1; } .v-ref.dark .dtabs .on { background: rgba(255,255,255,.14); color: #F5F3EF; }
.v-ref.dark .dw-r .rnd.sm { background: rgba(255,255,255,.08) !important; color: #F5F3EF; }
.v-ref.dark .seg { background: rgba(255,255,255,.06); } .v-ref.dark .seg .on { background: rgba(255,255,255,.16); color: #F5F3EF; }
"""
rcls = "v-ink v-rich v-white v-ref"
page8 = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Luex Reference Style</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500&display=swap">
<style>{css}{SOFT_CSS}{VAR_CSS}{RICH_CSS}{WHITE_CSS}{REF_CSS}{REF_D_FIX}</style></head><body>
<div class="wrap">
  <h1>Following the reference's rules</h1>
  <p class="lead">Plain grey background. One white frame. Fewer, bigger boxes with even gaps, each with its own soft colour: cream for the records, a grey-to-gold gradient for the detail, black for the chosen tile. Less on screen: extra filters behind one "Filters" button, column headings and tick boxes hidden until needed, only the key facts shown, and one big ring as the visual.</p>
  <div class="pair">
    <div><p class="tag-l"><i style="background:#fff"></i>Light</p><div class="frame soft {rcls}" style="{REF_L} {STATUS_L}">{SFR}</div></div>
    <div><p class="tag-l"><i style="background:#141414"></i>Dark</p><div class="frame soft {rcls} dark" style="{REF_D} {STATUS_D}">{to_dark(SFR)}</div></div>
  </div>
</div>
<script>{M.JS}</script>
</body></html>"""
pathlib.Path(__file__).with_name("app-reference-style.html").write_text(page8)
print("wrote app-reference-style.html", len(page8))

# =============================================================== best version (Claude's pick)
I = M.ic
def best_detail():
    return f'''<section class="dw best-dw">
      <div class="hero-obj">
        <div class="ho-top"><span class="live"><i></i>Due soon</span><span class="ho-r"><span class="gl">{I("edit")}</span><span class="gl">{I("dots")}</span></span></div>
        <div class="idcard">
          <div class="idc-top"><span class="idc-logo">CSCS</span><span class="idc-chip"></span></div>
          <div class="idc-mid"><span class="idc-ph">SB</span><div><b>SEÁN BYRNE</b><small>Skilled worker · Blue card</small><small class="mono">CS-4471 902</small></div></div>
          <div class="idc-ft"><span>Valid to</span><b>02 / 02 / 2026</b></div>
        </div>
        <div class="ho-pills"><span class="gp">{I("people")}Seán Byrne</span><span class="gp">{I("cal")}Docklands</span></div>
      </div>
      <div class="best-head"><div><small>Cards and tickets</small><h5>CSCS card</h5></div>
        <div class="ring-s" style="--p:12"><svg viewBox="0 0 80 80"><circle cx="40" cy="40" r="33" class="tr"/><circle cx="40" cy="40" r="33" class="pr"/></svg><span><b>12</b><small>days</small></span></div></div>
      <p class="best-note">Seán can't be booked on shifts after <b>2 February</b>.</p>
      <div class="best-acts"><span class="btn-d">{I("tick")}Renew</span><span class="btn-l">{I("bellring")}Remind</span></div>
      <div class="dtabs"><span class="on">Activity</span><span>Evidence <em>2</em></span><span>Linked <em>3</em></span><span>History</span></div>
      <div class="acts"><div class="act"><span class="av sm">CM</span><p><b>Ciara Murphy</b> sent a reminder<small>Today, 08:02</small></p></div>
        <div class="act"><span class="av sm">SB</span><p><b>Seán Byrne</b> booked a renewal for 30 Jan<small>Yesterday</small></p></div></div>
    </section>'''

TINTS = ["#E9DFC7", "#DDE6DF", "#E7D9D6", "#E3E0EA", "#EADBC9", "#DFE3E8"]
def best_frame(dark=False):
    mw = M.main_window("listplain", False)
    k = [0]
    def tint(m):
        c = TINTS[k[0] % len(TINTS)]; k[0] += 1
        return f'<span class="ci sm" style="--tint:{c}">'
    import re as _re
    mw = _re.sub(r'<span class="ci sm">', tint, mw)
    h = f'''<div class="fit"><div class="m-page">{rail_soft()}<div class="m-main">{M.header_ai(True)}{M.tiles(2, False)}<div class="m-body">{mw}{best_detail()}</div></div></div></div>'''
    for a, b in [("#C98A1B", "var(--amber)"), ("#2F8F5B", "var(--green)"), ("#C2413A", "var(--red)"), ("#1C1C1E", "var(--ink)")]:
        h = h.replace(a, b)
    return to_dark(h) if dark else h

BEST_CSS = """
.v-best .lr .ci { background: var(--tint); color: #3A3226; }
.v-best.dark .lr .ci { background: color-mix(in srgb, var(--tint) 18%, transparent); color: #E7DECA; }
.v-best .tile { position: relative; padding-bottom: 22px !important; }
.v-best .tile::after { content: ""; position: absolute; left: 18px; right: 18px; bottom: 11px; height: 3px; border-radius: 99px; background: linear-gradient(90deg, var(--c) var(--w), color-mix(in srgb, var(--c) 16%, transparent) var(--w)); }
.v-best .tile:nth-child(1) { --w: 100%; } .v-best .tile:nth-child(2) { --w: 88%; } .v-best .tile:nth-child(3) { --w: 9%; } .v-best .tile:nth-child(4) { --w: 4%; }
.v-best .tile.sel::after { background: linear-gradient(90deg, #CFB783 30%, rgba(255,255,255,.18) 30%); }
.v-best .tile.sel b { color: #CFB783; }
.best-dw { padding: 12px !important; display: flex; flex-direction: column; gap: 12px; }
.hero-obj { position: relative; height: 244px; border-radius: 20px; overflow: hidden; background: radial-gradient(90% 80% at 70% 100%, #F1E2BC 0%, rgba(241,226,188,0) 60%), linear-gradient(160deg, #E4E6EA 0%, #EDE6D6 60%, #E9D7AE 100%); display: grid; place-items: center; }
.v-best.dark .hero-obj { background: radial-gradient(90% 80% at 70% 100%, rgba(207,183,131,.35) 0%, rgba(207,183,131,0) 60%), linear-gradient(160deg, #1F2126 0%, #26221C 60%, #3A3022 100%); }
.ho-top { position: absolute; top: 12px; left: 12px; right: 12px; display: flex; justify-content: space-between; z-index: 2; }
.live { display: inline-flex; align-items: center; gap: 6px; height: 26px; padding: 0 10px; border-radius: 99px; background: #fff; font-size: 11px; color: #141414; box-shadow: 0 4px 10px -4px rgba(0,0,0,.2); }
.live i { width: 7px; height: 7px; border-radius: 50%; background: var(--amber); box-shadow: 0 0 0 3px color-mix(in srgb, var(--amber) 25%, transparent); }
.ho-r { display: flex; gap: 6px; }
.gl { width: 28px; height: 28px; border-radius: 50%; display: grid; place-items: center; background: rgba(255,255,255,.75); color: #141414; backdrop-filter: blur(6px); }
.gl .i { width: 13px; height: 13px; }
.ho-pills { position: absolute; left: 12px; right: 12px; bottom: 12px; display: flex; gap: 6px; z-index: 2; }
.gp { display: inline-flex; align-items: center; gap: 5px; height: 26px; padding: 0 10px; border-radius: 99px; background: rgba(255,255,255,.8); font-size: 11px; color: #141414; backdrop-filter: blur(6px); }
.gp .i { width: 12px; height: 12px; }
.idcard { width: 210px; height: 132px; margin-top: 4px; border-radius: 16px; padding: 14px 16px; color: #F6F0E4; display: flex; flex-direction: column; justify-content: space-between;
  background: linear-gradient(135deg, #141414 0%, #2A241B 55%, #6E5E43 100%); transform: rotate(-5deg); box-shadow: 0 24px 34px -14px rgba(40,25,5,.55), 0 2px 0 rgba(255,255,255,.08) inset; }
.idc-top { display: flex; justify-content: space-between; align-items: center; }
.idc-logo { font-size: 12px; font-weight: 500; letter-spacing: 2px; color: #CFB783; }
.idc-chip { width: 28px; height: 20px; border-radius: 5px; background: linear-gradient(135deg, #F3E2B8, #A68B55); }
.idc-mid { display: flex; gap: 10px; align-items: center; }
.idc-ph { width: 38px; height: 46px; border-radius: 8px; background: rgba(255,255,255,.12); display: grid; place-items: center; font-size: 12px; }
.idc-mid b { display: block; font-size: 12px; font-weight: 500; letter-spacing: .8px; }
.idc-mid small { display: block; font-size: 9.5px; color: #CFC3AB; }
.idc-mid .mono { font-family: ui-monospace, Menlo, monospace; letter-spacing: .5px; margin-top: 2px; }
.idc-ft { display: flex; justify-content: space-between; font-size: 9.5px; color: #CFC3AB; } .idc-ft b { font-weight: 500; color: #F6F0E4; letter-spacing: .5px; }
.best-head { display: flex; justify-content: space-between; align-items: center; padding: 2px 6px 0; }
.best-head small { font-size: 11px; color: var(--muted); } .best-head h5 { margin: 2px 0 0; font-size: 24px; font-weight: 500; letter-spacing: -.8px; }
.ring-s { position: relative; width: 62px; height: 62px; flex: none; }
.ring-s svg { width: 100%; height: 100%; transform: rotate(-90deg); }
.ring-s .tr { fill: none; stroke: var(--line); stroke-width: 6; } .ring-s .pr { fill: none; stroke: var(--amber); stroke-width: 6; stroke-linecap: round; stroke-dasharray: 207; stroke-dashoffset: calc(207 - 207 * var(--p) / 100); }
.ring-s span { position: absolute; inset: 0; display: grid; place-content: center; text-align: center; } .ring-s b { font-size: 18px; font-weight: 500; line-height: 1; } .ring-s small { font-size: 9px; color: var(--muted); }
.best-note { margin: -4px 6px 0; font-size: 12.5px; color: var(--ink2); font-weight: 400; } .best-note b { font-weight: 500; color: var(--ink); }
.best-acts { display: grid; grid-template-columns: 1fr 1fr; gap: 8px; padding: 0 2px; }
.best-acts .btn-d, .best-acts .btn-l { height: 40px; font-size: 13px; }
.v-best .best-acts .btn-l { background: var(--surface); box-shadow: inset 0 0 0 1px var(--line); }
.v-best.dark .best-acts .btn-d { background: #CFB783; color: #141414; }
.v-best.dark .best-acts .btn-l { background: rgba(255,255,255,.07); color: #F5F3EF; box-shadow: none; }
.best-dw .dtabs { margin-top: 0; }
.best-dw .acts { padding: 0 4px; }
"""
bcls = "v-ink v-rich v-white v-ref v-best"
page9 = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Luex Best Version</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500&display=swap">
<style>{css}{SOFT_CSS}{VAR_CSS}{RICH_CSS}{WHITE_CSS}{REF_CSS}{REF_D_FIX}{BEST_CSS}</style></head><body>
<div class="wrap">
  <h1>Luex: my best version</h1>
  <p class="lead">Ink sidebar, white frame, plain background, Venus accents and the reference's few big boxes. New: the open record shown as an object at the top of the detail window (here, Seán's CSCS card) in place of the reference's photo, softly coloured icons per record type, and a thin progress line on each status tile.</p>
  <div class="pair">
    <div><p class="tag-l"><i style="background:#fff"></i>Light</p><div class="frame soft {bcls}" style="{REF_L} {STATUS_L}">{best_frame()}</div></div>
    <div><p class="tag-l"><i style="background:#141414"></i>Dark</p><div class="frame soft {bcls} dark" style="{REF_D} {STATUS_D}">{best_frame(True)}</div></div>
  </div>
</div>
<script>{M.JS}</script>
</body></html>"""
pathlib.Path(__file__).with_name("app-best.html").write_text(page9)
print("wrote app-best.html", len(page9))

# =============================================================== main window colour options
OPT_CSS = """
.o-white .mw { box-shadow: inset 0 0 0 1px var(--line) !important; }
.o-white .lr { background: var(--panel) !important; }
.o-white.dark .lr { background: rgba(255,255,255,.05) !important; }
"""
OPTS = [
    ("Soft grey", "A light neutral grey. Calm and lets the white rows and gold accents stand out.", "--t-cream:#F1F1F0;", "--t-cream:#1C1C1C;", ""),
    ("Pure white", "White with a fine outline; the rows become pale grey. The cleanest and brightest.", "--t-cream:#FFFFFF;", "--t-cream:#141414;", "o-white"),
    ("Cool grey-blue", "The soft grey-blue from the top of the detail window, so the two big boxes feel like a pair.", "--t-cream:#E6E9EE;", "--t-cream:#1B1D22;", ""),
]
ob = ""
for name, blurb, L, D, extra in OPTS:
    ob += f'''<h2>{name}</h2><p class="lead">{blurb}</p>
    <div class="pair">
      <div><p class="tag-l"><i style="background:#fff"></i>Light</p><div class="frame soft {bcls} {extra}" style="{REF_L} {L} {STATUS_L}">{best_frame()}</div></div>
      <div><p class="tag-l"><i style="background:#141414"></i>Dark</p><div class="frame soft {bcls} {extra} dark" style="{REF_D} {D} {STATUS_D}">{best_frame(True)}</div></div>
    </div>'''
page10 = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Luex Main Window Options</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500&display=swap">
<style>{css}{SOFT_CSS}{VAR_CSS}{RICH_CSS}{WHITE_CSS}{REF_CSS}{REF_D_FIX}{BEST_CSS}{OPT_CSS}</style></head><body>
<div class="wrap">
  <h1>Main window: three colours instead of beige</h1>
  <p class="lead">Everything else is the same as the best version. Only the big records window changes.</p>
  {ob}
</div>
<script>{M.JS}</script>
</body></html>"""
pathlib.Path(__file__).with_name("app-main-options.html").write_text(page10)
print("wrote app-main-options.html", len(page10))

# =============================================================== status tile icons
M.P.update({
 "layers": '<path d="M12 4l8 4-8 4-8-4z"/><path d="M4 12l8 4 8-4"/><path d="M4 16l8 4 8-4"/>',
 "shieldok": '<path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/>',
 "hourglass": '<path d="M7 3.5h10M7 20.5h10M8 3.5c0 4 4 5 4 8.5s-4 4.5-4 8.5M16 3.5c0 4-4 5-4 8.5s4 4.5 4 8.5"/>',
 "alert": '<path d="M12 4l9 16H3z"/><path d="M12 10v4.5M12 17.5h.01"/>',
 "folder": '<path d="M3.5 7a1.5 1.5 0 0 1 1.5-1.5h4l2 2h8a1.5 1.5 0 0 1 1.5 1.5v8.5A1.5 1.5 0 0 1 19 19H5a1.5 1.5 0 0 1-1.5-1.5z"/>',
 "calok": '<rect x="4" y="5" width="16" height="15" rx="3"/><path d="M4 10h16M9 3v4M15 3v4M9 15l2 2 4-4"/>',
 "calclock": '<rect x="4" y="5" width="16" height="15" rx="3"/><path d="M4 10h16M9 3v4M15 3v4M12 13v2.5l1.6 1"/>',
 "calx": '<rect x="4" y="5" width="16" height="15" rx="3"/><path d="M4 10h16M9 3v4M15 3v4M10 13.5l4 4M14 13.5l-4 4"/>',
 "gridi": '<rect x="4" y="4" width="6" height="6" rx="1.5"/><rect x="14" y="4" width="6" height="6" rx="1.5"/><rect x="4" y="14" width="6" height="6" rx="1.5"/><rect x="14" y="14" width="6" height="6" rx="1.5"/>',
 "tickc": '<circle cx="12" cy="12" r="8.5"/><path d="M8.5 12.5l2.5 2.5 4.5-5"/>',
 "clockc": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
 "xc": '<circle cx="12" cy="12" r="8.5"/><path d="M9 9l6 6M15 9l-6 6"/>',
})
SETS = {
    "A": ("A. Meaning (my pick)", "What each tile is about: a stack for everything, a shield with a tick for valid, an hourglass for running out, a warning sign for expired.", ["layers", "shieldok", "hourglass", "alert"]),
    "B": ("B. Calendar", "All built on a calendar, because Compliance is about dates: a folder, then calendar with a tick, a clock and a cross.", ["folder", "calok", "calclock", "calx"]),
    "C. ": ("C. Simple marks", "The most minimal: a grid, a tick, a clock and a cross in circles. Works in any module with almost no thought.", ["gridi", "tickc", "clockc", "xc"]),
}
def iconify(h, icons):
    parts = h.split('<span class="sdot"></span>')
    # only the first four sdots belong to the tiles
    out = parts[0]
    for i, p in enumerate(parts[1:]):
        out += (f'<span class="tico">{M.ic(icons[i])}</span>' if i < 4 else '<span class="sdot"></span>') + p
    return out
TICO_CSS = """
.tico { width: 26px; height: 26px; border-radius: 50%; display: grid; place-items: center; flex: none; background: color-mix(in srgb, var(--c) 24%, #fff); color: color-mix(in srgb, var(--c) 85%, #000); }
.tico .i { width: 15px; height: 15px; stroke-width: 2; }
.v-ref .m-main { grid-template-rows: 58px 92px 1fr; }
.v-ref .tile { padding-top: 12px; }
.tile:first-child .tico { background: #E6E6E6; color: #141414; }
.dark .tico { background: color-mix(in srgb, var(--c) 26%, transparent); color: var(--c); }
.dark .tile:first-child .tico { background: rgba(255,255,255,.1); color: #F5F3EF; }
.tile.sel .tico { background: linear-gradient(135deg,#F3E2B8,#CFB783); color: #141414; }
.v-ref .t-top { gap: 10px; }
.strip .tiles { grid-template-columns: repeat(4, 1fr); }
.strip { background: #fff; padding: 14px; border-radius: 22px; }
.strip.dark { background: #141414; }
.strip { color: var(--ink); } .strip .tile b { color: var(--ink); } .strip .tile.sel b { color: #CFB783; }
"""
GB = "--t-cream:#E6E9EE;"; GBD = "--t-cream:#1B1D22;"
full = iconify(best_frame(), SETS["A"][2]); fulld = iconify(best_frame(True), SETS["A"][2])
strips = ""
for key, (name, blurb, icons) in SETS.items():
    t = iconify(M.tiles(2, False), icons)
    for a, b in [("#C98A1B", "var(--amber)"), ("#2F8F5B", "var(--green)"), ("#C2413A", "var(--red)"), ("#1C1C1E", "var(--ink)")]: t = t.replace(a, b)
    strips += f'''<h2>{name}</h2><p class="lead">{blurb}</p>
    <div class="pair"><div class="frame soft {bcls} strip" style="{REF_L} {GB} {STATUS_L}">{t}</div>
    <div class="frame soft {bcls} strip dark" style="{REF_D} {GBD} {STATUS_D}">{t}</div></div>'''
page11 = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Luex Tile Icons</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500&display=swap">
<style>{css}{SOFT_CSS}{VAR_CSS}{RICH_CSS}{WHITE_CSS}{REF_CSS}{REF_D_FIX}{BEST_CSS}{OPT_CSS}{TICO_CSS}</style></head><body>
<div class="wrap">
  <h1>Icons for the status tiles</h1>
  <p class="lead">The dot becomes an icon in a small circle tinted in the tile's status colour. On the black chosen tile it turns gold. Three sets to compare, then the full page with my pick.</p>
  {strips}
  <h2>Full page with set A</h2>
  <div class="pair">
    <div><p class="tag-l"><i style="background:#fff"></i>Light</p><div class="frame soft {bcls}" style="{REF_L} {GB} {STATUS_L}">{full}</div></div>
    <div><p class="tag-l"><i style="background:#141414"></i>Dark</p><div class="frame soft {bcls} dark" style="{REF_D} {GBD} {STATUS_D}">{fulld}</div></div>
  </div>
</div>
<script>{M.JS}</script>
</body></html>"""
pathlib.Path(__file__).with_name("app-tile-icons.html").write_text(page11)
print("wrote app-tile-icons.html", len(page11))
