#!/usr/bin/env python3
"""Builds prototype/home-v3.html: the Luex homepage on Nubo's layout.
Eight sections, real wording, and empty labelled boxes wherever a picture or app screen will go.
Prices come from src/data/pricing.json. Run: python3 prototype/build-home.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from dash import DASH, DASH_CSS, DASH_JS

HERE = pathlib.Path(__file__).parent
PRICING = json.loads((HERE.parent / "src/data/pricing.json").read_text())
HUB, BANDS = PRICING["hub"], PRICING["singleApp"]["bands"]

ICON = '<i class="ic"></i>'
DOTS = '<svg viewBox="0 0 12 12" aria-hidden="true"><circle cx="3" cy="3" r="1.3"/><circle cx="3" cy="9" r="1.3"/><circle cx="6.5" cy="6" r="1.3"/><circle cx="9.5" cy="3" r="1"/><circle cx="9.5" cy="9" r="1"/><circle cx="3" cy="6" r="1"/></svg>'

def slot(label, size="", dark=False, cls=""):
    """An empty box that marks where a picture or screen goes."""
    d = " dark" if dark else ""
    s = f"<small>{size}</small>" if size else ""
    return f'<div class="slot{d} {cls}"><span>{label}{s}</span></div>'

def btn(text, kind="dark", href="#pricing"):
    return f'<a class="btn {kind}" href="{href}"><span class="roll"><span>{text}</span><span>{text}</span></span>{DOTS}</a>'

LOGO = '<img class="btn-logo" src="img/logo-mark.png" width="18" height="16" alt="">'
LOGO_D = '<img class="btn-logo" src="img/logo-mark-dark.png" width="18" height="16" alt="">'
def btn_trial(text, href="#pricing"):
    return f'<a class="btn dark" href="{href}"><span class="roll"><span>{text}</span><span>{text}</span></span>{LOGO_D}</a>'

def btn_logo(text, kind="white", href="#demo"):
    return f'<a class="btn {kind}" href="{href}"><span class="roll"><span>{text}</span><span>{text}</span></span>{LOGO}</a>'

def tag(text, cls=""):
    return f'<span class="tag {cls}">{ICON}<span>{text}</span></span>'

def odo(num, unit="", size="o100"):
    digits = "".join(
        f'<span class="d" data-v="{c}"><span>' + "".join(f"<b>{k}</b>" for k in range(10)) + "</span></span>"
        if c.isdigit() else f'<span class="sep">{c}</span>' for c in num)
    return f'<div class="odo {size}" aria-label="{num} {unit}">{digits}<span class="u">{unit}</span></div>'

TRIAL, DEMO = "Start free trial", "Book a demo"

# ---------------------------------------------------------------- 1 hero
hero = f"""
<div class="hero-wrap" id="top">
  <section class="hero dune">
    <img class="hero-img" src="img/dune-hero.webp" width="1536" height="1024" alt="Calm desert dunes at golden hour">
    <div class="hero-in" id="heroIn">
      <p class="kicker"><img class="kick-mark" src="img/logo-mark.png" width="26" height="23" alt=""><span>Every business. Every team. One place.</span></p>
      <h1 class="d110 split">Run your entire operation<br>from a single <em>hub</em><span class="dot">.</span></h1>
      <p class="sub cap18">Over <b class="b60">60</b> tools working together.<br>Enter it once, see it everywhere.</p>
      <div class="replaces"><span class="rl">Replaces</span>{"".join(f'<s>{t}</s>' for t in ["Rota app", "Timesheet app", "Spreadsheets", "CRM", "Shared drive"])}</div>
      <div class="ctas">{btn_trial(TRIAL)}{btn_logo(DEMO)}</div>
      <p class="trust">14-day free trial <i>·</i> No card needed <i>·</i> Works on desktop, tablet and phone</p>
    </div>
    <div class="showcase">
      <div class="win"><div class="win-bar"><i></i><i></i><i></i><span>app.luex.com</span></div><iframe class="appframe" src="app-screen-light.html" title="Luex app: Compliance page" loading="eager" scrolling="no"></iframe></div>
      <!-- phone screen returns once the staff app screen is designed -->
    </div>
  </section>
</div>"""

# ---------------------------------------------------------------- 2 what it looks like
screens = [
    ("Dashboard", "The morning summary: what needs you today."),
    ("Scheduling and shifts", "The weekly rota, with blocked shifts flagged."),
    ("Timesheets", "A week of clock-ins, ready to approve."),
    ("Time off", "Holiday requests and who is off when."),
    ("Compliance", "Every ticket and certificate, with expiry dates."),
    ("CRM and jobs", "Quotes, customers and jobs in one list."),
    ("Documents and forms", "Policies to sign and checks to fill in."),
]
slides = "".join(f'<div class="slide">{slot(f"APP SCREEN {i+1}: {n}", d + " · 850 × 640")}</div>' for i, (n, d) in enumerate(screens))
looks = f"""
<section class="caps" id="looks">
  <div class="head-c">
    <span class="tag"><i class="ic ic-logo"><img src="img/logo-mark-dark.png" alt=""></i><span>THE APP</span></span>
    <h2 class="d110 split">What Luex<br><span class="soft">looks like.</span></h2>
    <p class="sub cap18" style="width:650px">Every screen below is the real app. One login takes you from the morning dashboard to the rota, the timesheets and the compliance records.</p>
  </div>
  <div class="track"><div class="rail" id="rail">{slides}</div></div>
  <div class="ctrl"><button class="pause" id="pause" type="button" aria-label="Pause"><svg viewBox="0 0 21 21" id="pauseIcon"><rect x="6" y="5" width="3" height="11" rx="1"/><rect x="12" y="5" width="3" height="11" rx="1"/></svg></button><div class="dots" id="dots"></div></div>
</section>"""

# ---------------------------------------------------------------- 3 what it does
stories = [
    ("THE OFFICE", "The admin, already sorted.",
     "Luex pulls everything that needs a decision into one morning summary: renewals, timesheets to approve and holiday requests.",
     "One screen at 8am", "See the dashboard", "SCREENSHOT: dashboard morning summary"),
    ("THE MANAGER", "Only the right people on site.",
     "Rotas check tickets and certificates as you build them, so nobody gets booked with something out of date.",
     "Safe by default", "See the rota", "SCREENSHOT: rota with a blocked shift"),
    ("THE TEAM", "Simple on the phone.",
     "Staff clock in, book time off, fill in a check and read a document from one app on their own phone.",
     "One app for staff", "See the staff app", "SCREENSHOT: staff app on a phone"),
]
cards = "".join(f"""
    <article class="story">
      <div class="pic">{slot(pic, "447 × 320")}</div>
      <span class="chipdark">{l}</span>
      <h3 class="h32">{h}</h3>
      <p class="cap14">{p}</p>
      <div class="ft"><span>{f}</span><a href="#looks">{a} <i class="tri"></i></a></div>
    </article>""" for l, h, p, f, a, pic in stories)
does = f"""
<section class="home" id="does">
  <div class="head-c">
    {tag("WHAT IT DOES", "ink")}
    <h2 class="d110 split">One hub.<br><span class="soft">Every team.</span></h2>
    <p class="sub cap18" style="width:470px">From the office to the site, the van to the payroll run.</p>
  </div>
  <div class="stories">{cards}</div>
  <p class="sub cap20 center" style="width:410px;margin:100px auto 0">Start with one app or the whole hub. Everything works together.</p>
  <div class="center" style="margin-top:38px">{btn("See every app", "dark", "#looks")}</div>
</section>"""

# ---------------------------------------------------------------- 4 why
why = f"""
<div class="qs-wrap">
<section class="qs cream" id="why">
  <div class="qs-grid">
    <div class="qs-img">{slot("PICTURE: someone using Luex on their phone at work", "414 × 700")}</div>
    <div class="qs-main">
      <div class="lab"><span class="sq32">{ICON}</span><span class="cap18t">Why Luex</span></div>
      <h2 class="h52">Built to replace<br><span class="soft">the pile of apps,</span><br>not add to it.</h2>
      <p class="cap18 ink bottom" style="width:460px">Most businesses run on a rota app, a timesheet app, a spreadsheet for certificates, a CRM and a shared drive. None of them talk to each other. Luex puts it all in one place, so things are entered once and everyone sees the same thing.</p>
      {btn(DEMO, "dark", "#demo")}
    </div>
    <div class="qs-side">
      <div class="qs-card"><div class="lab"><span class="sq32">{ICON}</span><span class="cap18t">One login</span></div>{odo("1", "login")}<p class="cap14 ink" style="width:230px">One place for the office, the site and the van.</p></div>
      <div class="qs-card"><div class="lab"><span class="sq32">{ICON}</span><span class="cap18t">One bill</span></div>{odo("1", "bill")}<p class="cap16 ink" style="width:230px">One monthly price instead of a stack of subscriptions.</p></div>
    </div>
  </div>
</section>
</div>"""

# ---------------------------------------------------------------- 5 pricing
lo, hi = BANDS[0]["pricePerMonth"], BANDS[-1]["pricePerMonth"]
plans = [
    ("Single app", "One app on its own, priced by the size of your team.", "START SMALL", f"£{lo}", "/month",
     "Per company · excl. VAT", [f'{b["label"]}: £{b["pricePerMonth"]}' for b in BANDS], "Single app icon or screen"),
    (HUB["name"], f'Every app in one place. {HUB["usersIncluded"]} users included.', "MOST POPULAR", f'£{HUB["basePricePerMonth"]}', "/month",
     f'{HUB["usersIncluded"]} users included · excl. VAT', ["Every app included", f'{HUB["usersIncluded"]} users included', "One login, one bill", "Upgrade from a single app any time"], "Hub icon or dashboard"),
    ("Extra users", "Add people as your team grows, on the Hub.", "ADD ON", f'£{HUB["extraLightUserPerMonth"]}', "/user",
     "Per user, per month · excl. VAT", [f'Light user: £{HUB["extraLightUserPerMonth"]}', "Forms, timesheets, documents", f'Full user: £{HUB["extraFullUserPerMonth"]}', "Manages and sees everything"], "Team or user icon"),
]
plan_html = "".join(f"""
    <article class="plan">
      <div class="plan-top"><h3 class="h32">{n}</h3><p class="cap14">{d}</p><span class="disc">{slot("ICON", "", False, "round")}</span></div>
      <div class="plan-body">
        <p class="lab2"><span class="sq">{ICON}</span><span class="cap14t">{t}</span></p>
        <p class="price">{pr}<span>{per}</span></p>
        <span class="pill2">{note}</span>
        <ul>{"".join(f'<li>{f}</li>' for f in feats)}</ul>
        {btn_trial(TRIAL)}
      </div>
    </article>""" for n, d, t, pr, per, note, feats, ic in plans)
pricing = f"""
<section class="pricing" id="pricing">
  <div class="head-l">
    {tag("PRICING")}
    <div class="row-b"><h2 class="h60">Simple pricing.<br><span class="soft">No surprises.</span></h2><p class="cap18 right" style="width:633px;align-self:end;margin-bottom:5px">Try every app free for 14 days.</p></div>
    <div class="row-b2"><p class="cap18" style="width:600px">Start with one app or go straight to the hub. No card needed for the trial, and you can upgrade at any time.</p><div class="tiny-logos">{"".join('<i></i>' for _ in range(4))}</div></div>
  </div>
  <div class="plans">{plan_html}</div>
  <p class="cap20 center" style="margin-top:60px">Works with the tools you already use</p>
  <div class="logos">{"".join(slot("LOGO", "", False, "logo") for _ in range(5))}</div>
</section>"""

# ---------------------------------------------------------------- 6 questions
faq_items = [
    ("How does the free trial work?", "Sign up, add your team and use every app for 14 days. You don't need a card to start, and nothing is charged unless you choose a plan."),
    ("Can I start with just one app?", "Yes. Each single app is priced by the size of your team. When you want more, upgrade to the Luex Hub and everything you've already entered comes with you."),
    ("What's the difference between a full and a light user?", "Full users manage and see everything. Light users fill in forms and timesheets, book time off and read documents, which is all most staff need."),
    ("Does it work on phones?", "Yes. Luex works on a computer, a tablet and a phone, so the office, the site and the van all use the same app."),
    ("Can you help me move my records over?", "Yes. Book a demo and we'll walk you through bringing your staff, records and documents across from your current tools."),
    ("Who is Luex for?", "Businesses in the UK and Ireland with teams on site, on the road or in the office, from a handful of people to a few hundred."),
]
faq = f"""
<section class="faq" id="faq">
  <div class="head-c">
    {tag("QUESTIONS", "ink")}
    <h2 class="d110 split" style="width:652px">The <span class="soft">practical</span><br>answers.</h2>
    <p class="sub cap18" style="width:530px">Pricing, the trial, phones and moving your records over. The things people ask first, answered plainly.</p>
  </div>
  <div class="acc narrow a22">{"".join(f'<div class="acc-i{" open" if i == 0 else ""}"><button type="button" class="acc-q"><span>{q}</span><i class="pm"></i></button><div class="acc-a"><div><p>{a}</p></div></div></div>' for i, (q, a) in enumerate(faq_items))}</div>
</section>"""

# ---------------------------------------------------------------- 7 closing
closing = f"""
<section class="closing" id="demo">
  {slot("PICTURE: a calm, organised workplace using Luex", "full screen · 1440 × 1080", True, "bg")}
  <div class="cl-in">
    <p class="kicker"><i class="ic w"></i><span>14 days free. No card needed.</span></p>
    <h2 class="d110 split" style="width:900px">Try Luex<br>free today.</h2>
    <div class="ctas">{btn_trial(TRIAL)}{btn_logo(DEMO)}</div>
  </div>
</section>"""

# ---------------------------------------------------------------- 8 footer
cols = [("PRODUCT", [("What it looks like", "#looks"), ("What it does", "#does"), ("Individual apps", "#looks"), ("Pricing", "#pricing"), ("Book a demo", "#demo")]),
        ("COMPANY", [("About", "#top"), ("Contact", "#top")]),
        ("LEGAL", [("Privacy & cookies", "#top"), ("Terms of service", "#top")])]
footer = f"""
<footer class="foot" id="foot">
  <div class="wordmark" aria-hidden="true">
    <svg viewBox="0 0 1392 464" preserveAspectRatio="none" class="wm-sharp"><text x="0" y="420" textLength="1392" lengthAdjust="spacingAndGlyphs">luex</text></svg>
    <svg viewBox="0 0 1392 464" preserveAspectRatio="none" class="wm-blur"><text x="0" y="420" textLength="1392" lengthAdjust="spacingAndGlyphs">luex</text></svg>
  </div>
  <div class="foot-grid">
    <div class="foot-cols">{"".join(f'<div><p class="cap14 grey">{h}</p><ul>{"".join(f"<li><a href=\"{u}\">{l}</a></li>" for l, u in ls)}</ul></div>' for h, ls in cols)}</div>
    <form class="news" onsubmit="return false">
      <p class="news-k"><span class="sq">{ICON}</span>Product news, now and then.</p>
      <h3 class="h32">Luex updates</h3>
      <label><span class="sr">Your name</span><input placeholder="Your name"></label>
      <label><span class="sr">Your email</span><input type="email" placeholder="Your email"></label>
      <div class="news-ft"><button type="submit" class="btn dark sub-btn"><span class="roll"><span>Subscribe</span><span>Subscribe</span></span>{DOTS}</button><div class="badges">{slot("APP STORE BADGE")}{slot("GOOGLE PLAY BADGE")}</div></div>
    </form>
  </div>
  <div class="foot-bot"><span>© 2026 Luex Limited. All rights reserved.</span><span class="fb-r">Made for the UK and Ireland</span></div>
</footer>"""

nav = f"""
<nav class="nav" aria-label="Main">
  <a class="logo" href="#top" aria-label="Luex home"><img class="nav-mark" src="img/logo-mark-dark.png" width="24" height="21" alt=""><span class="logo-ph">luex</span></a>
  <button type="button" id="menuBtn" aria-label="Toggle menu" aria-expanded="false"><i></i><i></i><i></i></button>
</nav>
<div class="drop" id="drop">
  <div class="drop-links">{"".join(f'<a href="#{h}">{t}</a>' for t, h in [("What it looks like", "looks"), ("What it does", "does"), ("Why Luex", "why"), ("Pricing", "pricing"), ("Questions", "faq"), ("Book a demo", "demo")])}</div>
  <div class="drop-ft"><p class="cap14">Everything your business runs on, in one place.</p>{btn(TRIAL, "white")}</div>
</div>"""

extra_css = """
/* empty boxes that mark where pictures and screens go */
.slot { position: relative; width: 100%; height: 100%; display: grid; place-items: center; background: #ECEAE5; color: #8A8780; text-align: center; padding: 24px; }
.slot::before { content: ""; position: absolute; inset: 12px; border: 1.5px dashed rgba(120,116,108,.4); border-radius: 6px; pointer-events: none; }
.slot span { position: relative; display: grid; gap: 6px; max-width: 420px; font-family: var(--mono); font-size: 12px; line-height: 1.5; letter-spacing: .02em; text-transform: uppercase; }
.slot small { font-size: 11px; opacity: .7; }
.slot.dark { background: #3C3A36; color: rgba(255,255,255,.55); }
.slot.dark::before { border-color: rgba(255,255,255,.22); }
.slot.bg { position: absolute; inset: 0; place-items: end start; padding: 40px; }
.slot.round { border-radius: 50%; padding: 0; } .slot.round::before { inset: 8px; border-radius: 50%; }
.slot.round span { font-size: 9px; }
.slot.logo { width: 100px; height: 44px; padding: 0; } .slot.logo::before { inset: 4px; } .slot.logo span { font-size: 9px; }
.badges { display: flex; gap: 10px; }
.logo { display: flex; align-items: center; gap: 8px; } .nav-mark { width: 24px; height: auto; } .logo .logo-ph { width: auto; }
.ic-logo::before { display: none; } .ic-logo img { width: 15px; height: auto; display: block; }
.b60 { font-weight: 700; color: var(--ink); -webkit-text-stroke: .5px var(--ink); }
.kick-mark { width: 26px; height: auto; flex: none; }
.btn-logo { width: 18px; height: auto; flex: none; transition: transform .45s cubic-bezier(.2,.8,.2,1); }
.btn:hover .btn-logo { transform: rotate(-8deg) scale(1.08); }
.badges .slot { width: 130px; height: 44px; padding: 0; } .badges .slot::before { inset: 4px; } .badges .slot span { font-size: 8.5px; }
.closing .slot.bg { padding-bottom: 40px; }
.qs-img > .slot { position: absolute; inset: 0; }
.cl-in .ctas, .hero .ctas { z-index: 1; }
/* ---------- Venus / Dune palette ---------- */
:root { --ink: #141414; --ink2: #4A4740; --ink3: #77664B; --ink4: #8E8778; --accent: #A68B55; --cream: #F3EEE4; --dot: #CFC6B4; --line: #E9E3D7; }
.h60 .soft, .h52 .soft, .d110 .soft { color: #A69A84; }
.btn.white { background: rgba(255,255,255,.88); }

/* ---------- hero: desert, dark text, dashboard rising from the sand ---------- */
.hero-wrap { height: auto; margin-bottom: 0; }
.hero.dune { position: relative; height: 1382px; color: var(--ink); clip-path: none; }
.hero-img { position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: 50% 30%; }
.hero.dune::after { content: ""; position: absolute; left: 0; right: 0; bottom: 0; height: 160px; background: linear-gradient(transparent, var(--g7)); pointer-events: none; }
.hero.dune .kicker { top: 112px; color: var(--ink); }
.hero.dune h1.d110 { font-size: 84px; line-height: 88px; letter-spacing: -4.6px; width: 1200px; }
.hero.dune h1 { top: 150px; color: var(--ink); }
.hero.dune h1 em, .hero.dune h1 .dot { color: var(--accent); }
.hero.dune .sub { top: 346px; color: var(--ink2); width: 760px; }
.replaces { position: absolute; top: 420px; left: 50%; translate: -50% 0; display: flex; align-items: center; gap: 8px; white-space: nowrap; }
.replaces .rl { font-family: var(--body); font-size: 14px; letter-spacing: .4px; text-transform: uppercase; color: var(--ink); font-weight: 700; -webkit-text-stroke: .5px var(--ink); margin-right: 4px; }
.replaces s { font-family: var(--head); font-size: 14px; color: #6B6455; text-decoration: none; position: relative; padding: 6px 13px; border-radius: 99px; background: rgba(255,255,255,.55); box-shadow: inset 0 0 0 1px rgba(20,20,20,.08); }
.replaces s::after { content: ""; position: absolute; left: 10px; right: 10px; top: 50%; height: 1.5px; background: #141414; transform: rotate(-4deg); }
.trust { position: absolute; top: 536px; left: 50%; translate: -50% 0; white-space: nowrap; font-family: var(--head); font-size: 13.5px; color: var(--ink2); }
.trust i { font-style: normal; color: #A68B55; margin: 0 6px; }
.hero.dune .ctas { top: 470px; }
.showcase { position: absolute; left: 50%; top: 582px; translate: -50% 0; width: 1120px; max-width: calc(100% - 48px); z-index: 2; }
.win { border-radius: 14px; overflow: hidden; background: rgba(255,255,255,.72); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); box-shadow: 0 40px 80px -30px rgba(70,50,20,.45), 0 0 0 1px rgba(255,255,255,.6); }
.win-bar { height: 38px; display: flex; align-items: center; gap: 7px; padding: 0 16px; background: rgba(255,255,255,.65); border-bottom: 1px solid rgba(20,20,20,.06); }
.win-bar i { width: 10px; height: 10px; border-radius: 50%; background: #D8D0C0; }
.win-bar span { margin-left: auto; margin-right: auto; font-family: var(--mono); font-size: 11px; color: #8E8778; padding-right: 44px; }
.win .slot { aspect-ratio: 1120 / 662; height: auto; background: #F4F0E8; }
.appframe { display: block; width: 100%; aspect-ratio: 1280 / 800; border: 0; background: #fff; pointer-events: none; }
.phone { position: absolute; right: -86px; bottom: -96px; width: 196px; aspect-ratio: 390 / 844; border-radius: 38px; background: #141414; padding: 9px; box-shadow: 0 30px 60px -20px rgba(40,30,10,.55); }
.phone .slot { border-radius: 30px; background: #F4F0E8; padding: 14px; }
.phone .slot span { font-size: 10px; }
.notch { position: absolute; top: 18px; left: 50%; translate: -50% 0; width: 70px; height: 20px; border-radius: 99px; background: #141414; z-index: 2; }
.hero.dune + * { z-index: 1; }
.caps { padding-top: 0; } .hero-wrap + .caps .head-c { padding-top: 72px; }

@media (max-width: 1200px) { .phone { right: -10px; width: 180px; } }
@media (max-width: 809px) {
  .badges { flex-wrap: wrap; } .slot.bg { padding: 20px; }
  .hero.dune { height: auto; min-height: 0; padding: 112px 16px 80px; }
  .hero.dune .hero-in { position: relative; transform: none !important; }
  .hero.dune .kicker, .hero.dune h1, .hero.dune .sub, .hero.dune .ctas, .replaces, .trust { position: relative; top: auto; left: auto; translate: none; }
  .replaces { flex-wrap: wrap; justify-content: center; white-space: normal; margin-top: 18px; gap: 6px; } .replaces s { font-size: 12.5px; padding: 5px 10px; }
  .replaces .rl { width: 100%; text-align: center; margin: 0 0 2px; font-size: 12px; }
  .trust { white-space: normal; text-align: center; margin-top: 14px; font-size: 12.5px; }
  .hero.dune .kicker { justify-content: center; white-space: normal; }
  .hero.dune h1, .hero.dune h1.d110 { width: auto; margin-top: 18px; font-size: 41px; line-height: 44px; letter-spacing: -2.2px; }
  .hero.dune .sub { width: auto; margin-top: 18px; text-align: center; }
  .hero.dune .ctas { margin-top: 22px; flex-direction: row; gap: 8px; } .hero.dune .ctas .btn { height: 46px; padding: 0 16px; font-size: 12.5px; }
  .hero.dune { padding-top: 96px !important; } .hero.dune .sub { margin-top: 12px !important; } .showcase { margin-top: 30px !important; }
  .showcase { position: relative; left: auto; top: auto; translate: none; width: 100%; max-width: none; margin-top: 48px; }
  .win-bar { height: 26px; } .win-bar span { display: none; }
  .phone { width: 88px; right: -4px; bottom: -28px; border-radius: 22px; padding: 5px; } .phone .slot { border-radius: 18px; padding: 6px; } .phone .slot span { font-size: 7px; } .notch { width: 36px; height: 10px; top: 10px; }
}
"""

css = (HERE / "blank.css").read_text() + extra_css + DASH_CSS
js = (HERE / "blank.js").read_text() + DASH_JS
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Luex Homepage</title>
<meta name="description" content="Luex puts staff, rotas, timesheets, compliance, jobs and money in one app for businesses in the UK and Ireland.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:ital,wght@0,400;0,500;1,500&family=Abel&family=Fragment+Mono&display=swap">
<style>
{css}
</style>
</head>
<body>
{nav}
<main>
{hero}
{looks}
{does}
{why}
{pricing}
{faq}
{closing}
</main>
{footer}
<script>
{js}
</script>
</body>
</html>
"""
out = HERE / "home-v3.html"
out.write_text(html)
print("wrote", out, len(html), "bytes")
