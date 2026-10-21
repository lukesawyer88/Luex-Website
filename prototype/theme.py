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
