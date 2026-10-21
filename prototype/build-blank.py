#!/usr/bin/env python3
"""Builds prototype/blank.html: Nubo's layout, measured at 1440 x 900, with neutral photo blocks
and filler text that keeps each original word's length (so lines wrap in the same places).
Run: python3 prototype/build-blank.py"""
import hashlib, re, pathlib

WORDS = """a i o e u at in et ut id ad do se no si to re ve qua sit est vel non sed nam per sum tam
ante amet duis enim erat nisi odio quis sint ulla urna dolor ipsum lorem magna nulla culpa irure
velit minim lacus fusce neque porta nunc risus tempor labore dolore aliqua mollit fugiat cillum
quisque aliquam laoreet viverra pretium egestas posuere euismod commodo laborum officia proident
eiusmod pariatur deserunt incididunt consequat voluptate exercitation reprehenderit adipiscing
consectetur ullamco nostrud aliquip occaecat cupidatat sunt anim volutpat tristique vulputate
sagittis faucibus interdum molestie habitant fermentum ultricies dignissim elementum vestibulum
suspendisse condimentum scelerisque pellentesque sollicitudin""".split()
BY_LEN = {}
for w in WORDS:
    BY_LEN.setdefault(len(w), []).append(w)

def pick(n, h):
    if n in BY_LEN:
        opts = BY_LEN[n]
        return opts[h % len(opts)]
    # build long words from two shorter ones
    a = min(BY_LEN, key=lambda k: abs(k - n // 2))
    first = BY_LEN[a][h % len(BY_LEN[a])]
    return first + pick(n - len(first), h // 7 + 3) if n - len(first) > 0 else first[:n]

def G(text):
    """Gibberish with the same word lengths, case and punctuation as text."""
    seed = int(hashlib.md5(text.encode()).hexdigest(), 16)
    out, i = [], 0
    for tok in re.split(r"(\s+)", text):
        if not tok or tok.isspace():
            out.append(tok); continue
        def rep(m):
            nonlocal i
            w = m.group(0); i += 1
            if w.isdigit():
                return "".join(str((int(c) * 7 + i + seed) % 10) for c in w)
            g = pick(len(w), seed // (i * 13 + 1))
            if w.isupper() and len(w) > 1: return g.upper()
            if w[0].isupper(): return g[0].upper() + g[1:]
            return g
        out.append(re.sub(r"[A-Za-zÀ-ÿ]+|\d+", rep, tok))
    return "".join(out)

# Neutral photo blocks: warm greys like Nubo's photography. tone -> (light, dark)
TONES = {
    "a": ("#D9D2C7", "#B9AE9F"), "b": ("#E4DED5", "#C8BFB2"), "c": ("#CFC6B9", "#A99D8D"),
    "d": ("#E9E5DF", "#D3CCC1"), "e": ("#BFB4A5", "#8E8273"), "f": ("#DCD6CE", "#B3A898"),
    "k": ("#3A3936", "#151514"), "h": ("#9A8E7F", "#5E554B"),
}
def ph(tone="a", extra="", label=""):
    l, d = TONES[tone]
    return f'<div class="ph {extra}" style="--l:{l};--d:{d}" role="img" aria-label="{label or "Photo placeholder"}"></div>'

ICON = '<i class="ic"></i>'
ARROW = '<svg viewBox="0 0 12 12" aria-hidden="true"><circle cx="3" cy="3" r="1.3"/><circle cx="3" cy="9" r="1.3"/><circle cx="6.5" cy="6" r="1.3"/><circle cx="9.5" cy="3" r="1"/><circle cx="9.5" cy="9" r="1"/><circle cx="3" cy="6" r="1"/></svg>'

def btn(text, kind="dark", w=None, extra=""):
    t = G(text)
    style = f' style="width:{w}px"' if w else ""
    return f'<a class="btn {kind} {extra}" href="#top"{style}><span class="roll"><span>{t}</span><span>{t}</span></span>{ARROW}</a>'

def tag(text, cls=""):
    return f'<span class="tag {cls}">{ICON}<span>{G(text)}</span></span>'

def odo(num, unit="", size="o130", cls=""):
    digits = "".join(
        f'<span class="d" data-v="{c}"><span>' + "".join(f"<b>{k}</b>" for k in range(10)) + "</span></span>"
        if c.isdigit() else f'<span class="sep">{c}</span>' for c in num)
    u = f'<span class="u">{unit}</span>' if unit else ""
    return f'<div class="odo {size} {cls}" aria-label="{num} {unit}">{digits}{u}</div>'

def stars(n=5):
    return '<span class="stars">' + "".join("<i></i>" for _ in range(n)) + "</span>"

# ---------------------------------------------------------------- sections
hero = f"""
<div class="hero-wrap" id="top">
  <section class="hero">
    {ph("c", "bg under", "Behind the hero: same photo as the Hello section")}
    <div class="over" id="heroBg" style="position:absolute;inset:0">{ph("h", "bg", "Hero photo or video, 1440 by 900")}</div>
    <div class="hero-in" id="heroIn">
      <p class="kicker"><i class="ic w"></i><span>{G("Always kind. Mostly invisible.")}</span></p>
      <h1 class="d110 split">{G("A")} <em>{G("quieter")}</em> {G("kind of")}<br>{G("help at home")}<span class="dot">.</span></h1>
      <p class="sub cap18">{G("NUBO TAKES THE SMALL DAILY WORK OFF YOUR HANDS, WITHOUT ASKING FOR YOUR ATTENTION.")}</p>
      <div class="ctas">{btn("RESERVE FROM €3,290", "dark", 215)}{btn("WATCH SHOWREEL", "white", 196)}</div>
      <div class="marks">{"".join(f'<span class="mk"><i></i>{G(w)}</span>' for w in ["medusa", "elasticpath", "framer", "vercel"])}</div>
    </div>
  </section>
</div>"""

hello = f"""
<section class="hello" id="hello">
  {ph("c", "bg", "Full-bleed photo, 1440 by 900")}
  <h2 class="d110 split light" id="helloH">{G("Hello, I'm Nubo.")}</h2>
  <div class="hello-card">{ph("b", "", "Photo, 800 by 533")}</div>
</section>"""

slides = "".join(f'<div class="slide">{ph(t, "", f"Slide {i+1} photo, 850 by 640")}</div>' for i, t in enumerate("abcdefb"))
caps = f"""
<section class="caps" id="caps">
  <div class="head-c">
    {tag("CAPABILITIES")}
    <h2 class="d110 split">{G("What Nubo")}<br>{G("does")} <span class="soft">{G("quietly.")}</span></h2>
    <p class="sub cap18" style="width:650px">{G("NUBO LEARNS YOUR ROOMS IN AN AFTERNOON AND YOUR ROUTINES WITHIN THE WEEK, DOWN TO WHAT TIDY MEANS IN YOUR HOUSE RATHER THAN THE SHOWROOM.")}</p>
  </div>
  <div class="track"><div class="rail" id="rail">{slides}</div></div>
  <div class="ctrl"><button class="pause" id="pause" type="button" aria-label="Pause"><svg viewBox="0 0 21 21" id="pauseIcon"><rect x="6" y="5" width="3" height="11" rx="1"/><rect x="12" y="5" width="3" height="11" rx="1"/></svg></button><div class="dots" id="dots"></div></div>
</section>"""

stories = [
    ("THE KITCHEN", "A second pair of hands at dinner.", "NUBO LEARNS THE ORDER YOUR HOUSEHOLD WAKES IN — SURFACES CLEARED THE NIGHT BEFORE, THE SHOPPING LIST BUILT FROM WHAT ACTUALLY RAN OUT.", "ONE LESS THING AT 6PM", "Read the kitchen story", "a"),
    ("THE SCHOOL RUN", "Gentle with the small ones.", "FINDS THE LOST LEGO, TIDIES THE FLOOR BEFORE BED, READS A STORY ON A LOOP. FORCE-SENSING HANDS AND QUIET HOURS KEEP IT SAFE AND CALM.", "OUT THE DOOR ON TIME", "Read the family story", "f"),
    ("THE FRONT DOOR", "Takes the parcel when you can't.", "GREETS THE COURIER, SIGNS FOR THE BOX, SETS IT INSIDE. YOU GET A PHOTO AND A NOTE — NO MISSED-DELIVERY CARD ON THE MAT.", "NOTHING MISSED", "Read the daily duties story", "c"),
]
cards = "".join(f"""
    <article class="story">
      <div class="pic">{ph(t, "", "Photo, 447 by 320")}</div>
      <span class="chipdark">{G(l)}</span>
      <h3 class="h32">{G(h)}</h3>
      <p class="cap14">{G(p)}</p>
      <div class="ft"><span>{G(f)}</span><a href="#top">{G(a)} <i class="tri"></i></a></div>
    </article>""" for l, h, p, f, a, t in stories)
home = f"""
<section class="home" id="home">
  <div class="head-c">
    {tag("AT HOME", "ink")}
    <h2 class="d110 split">{G("One robot.")}<br><span class="soft">{G("Every room.")}</span></h2>
    <p class="sub cap18" style="width:470px">{G("DISCOVER EVERY USE CASE FROM THE KITCHEN TO THE FRONT DOOR, THE GARAGE TO THE SCHOOL RUN.")}</p>
  </div>
  <div class="stories">{cards}</div>
  <p class="sub cap20 center" style="width:410px;margin-top:100px">{G("DISCOVER EVERY USE CASE FROM THE KITCHEN TO THE FRONT DOOR, THE GARAGE TO THE SCHOOL RUN.")}</p>
  <div class="center" style="margin-top:38px">{btn("ALL USE CASES", "dark", 167)}</div>
</section>"""

def statcard(label, num, unit, desc, src, ongoing="Ongoing"):
    return f"""
    <div class="stat">
      <div class="stat-top"><span class="cap18t">{G(label)}</span><span class="cap16 soft2">{G("SO FAR")}</span></div>
      {odo(num, unit)}
      <p class="cap16">{G(desc)}</p>
      <div class="stat-ft"><span>{G(src)}</span><span class="grey">{G(ongoing)}</span></div>
    </div>"""

def acc(items, cls=""):
    out = []
    for i, (q, a) in enumerate(items):
        op = " open" if i == 0 else ""
        out.append(f"""<div class="acc-i{op}"><button type="button" class="acc-q"><span>{G(q)}</span><i class="pm"></i></button><div class="acc-a"><div><p>{G(a)}</p></div></div></div>""")
    return f'<div class="acc {cls}">' + "".join(out) + "</div>"

signals = f"""
<section class="signals cream" id="signals">
  <div class="head-l">
    {tag("EARLY SIGNALS")}
    <div class="row-b"><h2 class="h60">{G("The first numbers, from the")}<br>{G("first homes.")}</h2><p class="cap18 right" style="width:360px">{G("NUBO IS IN BETA. THESE ARE EARLY READINGS FROM THE HOUSEHOLDS LIVING WITH IT NOW, NOT LAUNCH-DAY PROMISES.")}</p></div>
  </div>
  <div class="dark-card">
    <div class="glow"></div>
    {odo("94", "%", "o130 white")}
    <p class="dc-txt">{G("Run without ever opening the app.")}<br>{G("Nubo reads the routine and acts before it's asked.")}</p>
    <div class="dc-img">{ph("d", "", "Photo, 330 by 250")}</div>
    <p class="dc-cap">{G("Of beta homes keep Nubo running daily, four weeks after delivery.")}</p>
  </div>
  <div class="live"><span class="mini">{ICON}</span><span class="cap18t ink">{G("LIVE BETA DATA")}</span><span class="line"></span><span class="cap14 ink">{G("UPDATED AS THE PROGRAM GROWS. SMALL SAMPLE, HONESTLY REPORTED, AND CHANGING WEEK TO WEEK.")}</span></div>
  <div class="stats">
    {statcard("SELF-SUFFICIENCY", "88", "%", "RUN WITHOUT EVER OPENING THE APP. NUBO READS THE ROUTINE AND ACTS BEFORE IT'S ASKED.", "BETA - 140 homes")}
    {statcard("WORD OF MOUTH", "9.2", "/10", "AVERAGE SCORE WHEN OWNERS ARE ASKED HOW LIKELY THEY'D RECOMMEND NUBO TO A FRIEND.", "Beta Survey")}
    {statcard("TIME RETURNED", "5.5", "hrs", "MEDIAN TIME OWNERS SAY THEY GET BACK EACH WEEK ON CHORES NUBO QUIETLY TAKES OVER.", "Self-Reported")}
  </div>
  <div class="measure">
    <h3 class="h32">{G("How we measure")}</h3>
    <p class="cap18">{G("WHAT EACH NUMBER MEANS, WHO IT COMES FROM, AND HOW OFTEN IT CHANGES.")}</p>
  </div>
  {acc([("What counts as \"still running\"?", "A home is counted as active if Nubo completes at least one task a day, on its own, without being opened in the app."),
        ("Who's in the sample?", "140 beta households across mixed home types and sizes. No cherry-picking; every active beta home is included."),
        ("How often it updates?", "Figures refresh as the program grows, so they move week to week. The date on each stat shows how current it is."),
        ("What we don't do?", "No paid reviews, no curated quotes, no rounding up. When a number dips, it dips here too.")], "wide a20")}
</section>"""

specs = [("SHELL", "FINE-GAUGE MERINO BLEND · 18GG"), ("WEIGHT", "540 G/M²"), ("COLOR", "CHALK / FLAX / GRAPHITE"), ("CARE", "REMOVABLE · 30°C WASH"), ("ORIGIN", "COMO, ITALY")]
materials = f"""
<section class="materials" id="materials">
  <div class="mat-l">
    {tag("MATERIALS & CRAFT")}
    <h2 class="h60" style="margin-top:52px">{G("Made in Como.")}<br><span class="soft">{G("Worn like a favorite jumper.")}</span></h2>
    <p class="cap18" style="width:500px;margin-top:52px">{G("NUBO'S SHELL IS A SINGLE PIECE OF SEAMLESS KNIT, WOVEN IN COMO FROM A COTTON AND RECYCLED NYLON BLEND.")}</p>
    <div class="chips">{"".join(f'<span>{G(c)}</span>' for c in ["MACHINE WASHABLE", "REPLACEABLE", "5 TONES", "RECYCLED YARN"])}</div>
    <dl class="spec">{"".join(f'<div><dt>{G(k)}</dt><dd>{G(v)}</dd></div>' for k, v in specs)}</dl>
  </div>
  <div class="mat-r">
    <div class="mat-main">{ph("b", "", "Photo, 680 by 444")}</div>
    <div class="thumbs">{"".join(f'<button type="button" class="th{" on" if i == 0 else ""}">{ph(t, "", "Thumbnail")}</button>' for i, t in enumerate("bafd"))}</div>
    <p class="cap16" style="width:520px;margin-top:36px">{G("QUIET AGAINST THE EAR, SOFT TO THE TOUCH, AND SIMPLE TO CHANGE WHEN YOU WANT SOMETHING DIFFERENT.")}</p>
    <div class="mat-ft">{btn("REQUEST SWATCH", "outline", 190)}<p class="cap16">{G("FABRIC SWATCH AVAILABLE ON REQUEST. SHIPS WITH EVERY UNIT.")}</p></div>
  </div>
</section>"""

bento = f"""
<section class="bento" id="bento">
  <div class="head-l">
    {tag("FOR EVERYONE")}
    <div class="row-b"><h2 class="h60">{G("Simple to live with.")}<br><span class="soft">{G("Not simple inside.")}</span></h2><p class="cap18 right" style="width:360px">{G("NOT THE NUMBERS ON THE BOX — THE THINGS YOU ONLY NOTICE ONCE IT'S LIVING WITH YOU.")}</p></div>
    <div class="row-b2"><p class="cap18" style="width:420px">{G("NUBO KEEPS A LOW PROFILE. UNDERNEATH THE QUIET IS A ROBOT THAT DOES CONSIDERABLY MORE THAN IT SHOWS.")}</p>{btn("FULL SPEC SHEET", "dark", 180)}</div>
  </div>
  <div class="grid">
    <div class="b wide cream2">
      <div class="half">{ph("a", "", "Photo, 459 by 600")}<span class="wm">{G("nubo")}</span></div>
      <div class="half pad">
        <p class="cap18t">{G("ON ITS FEET")}</p>
        <h3 class="h48">{G("Takes the stairs like the rest of the family.")}</h3>
        <p class="cap16 ink bottom" style="width:330px">{G("WALKS, BALANCES, AND STEPS OVER THE RUG INSTEAD OF DRAGGING IT. THRESHOLDS, STEPS, AND A SHOE LEFT IN THE HALL ARE NOT A PROBLEM.")}</p>
      </div>
    </div>
    <div class="b black center-col">
      <span class="sq w">{ICON}</span>
      <h3 class="h48 creamtxt" style="width:411px">{G("More mind than machine")}</h3>
      <div class="orb">{ph("k", "round", "Image, 280 by 280")}</div>
      <p class="cap16 creamtxt bottom" style="width:249px">{G("NEURAL ENGINE READS THE ROOM IN REAL TIME AND LEARNS MORE EVERY DAY.")}</p>
    </div>
    <div class="b white bd center-col">
      <span class="sq">{ICON}</span>
      <h3 class="h48" style="width:411px">{G("No one gets in.")}<br>{G("Not even us.")}</h3>
      <div class="obj">{ph("d", "round8", "Object image, 160 by 160")}</div>
      <p class="cap16 ink bottom" style="width:411px">{G("ZERO CLOUD DEPENDENCY. ENCRYPTED ON-DEVICE, WITH NO BACK DOOR.")}</p>
    </div>
    <div class="b wide cream2">
      <div class="half">{ph("f", "", "Photo, 459 by 600")}</div>
      <div class="half pad">
        <p class="cap18t">{G("ALL-DAY POWER")}</p>
        <h3 class="h48">{G("A full day, then it charges itself.")}</h3>
        <div class="power">{ph("d", "round8", "Image, 147 by 159")}<div><h3 class="h48">{G("23")}{G("hrs")}</h3><p class="cap14" style="width:272px">{G("WHEN IT RUNS LOW, NUBO FINDS THE DOCK ON ITS OWN. USUALLY BEFORE YOU'D NOTICE IT WAS GONE")}</p></div></div>
      </div>
    </div>
    <div class="stack">
      <div class="b motion">{ph("e", "", "Photo, 459 by 288")}<div class="ov"><h3 class="h32 wtxt">{G("Range of Motion")}</h3><p class="cap16 wtxt" style="width:300px">{G("REACHES THE TOP SHELF, KNEELS FOR THE BOTTOM DRAWER.")}</p></div></div>
      <div class="b alu">{ph("b", "", "Photo, 459 by 304")}<div class="ov2">{odo("76", "%", "o90")}<p class="cap16t ink" style="width:137px">{G("RECYCLED ALUMINIUM IN THE BASE UNIT")}</p></div></div>
    </div>
    <div class="b white bd review">
      <div class="rv-top"><span class="cap18t">{G("CUSTOMER REVIEW")}</span><span class="rate">{stars()}<span>{G("4.5/5")}</span></span></div>
      <p class="quote">"{G("It doesn't do tricks. It clears the table, it charges itself, it stays out of the kitchen when we're cooking. My last three smart home purchases wanted applause. This one just wants a dock.")}"</p>
      <div class="who"><div class="av">{ph("c", "", "Portrait, 80 by 110")}</div><div><p class="cap18t ink">{G("JOANNA ERIKSON")}</p><p class="cap14t grey2">{G("BERGEN/NORWAY")}</p></div><span class="pill">{G("BETA TESTER")}</span></div>
    </div>
    <div class="b cream2 center-col cta-card">
      <span class="sq">{ICON}</span>
      <h3 class="h48">{G("Bring one home.")}</h3>
      <p class="cap16 ink">{G("RESERVE NOW, PAY WHEN WE SHIP.")}</p>
      {btn("RESERVE NUBO", "dark", 168)}
      <div class="kb">{ph("d", "round8", "Image, 310 by 181")}</div>
    </div>
  </div>
</section>"""

faq_items = [
    ("When will Nubo ship?", "Beta units are in homes now. Reserved units ship in allocation order from early next year, and we'll confirm your window before charging anything beyond the deposit."),
    ("Is it safe around children and pets?", "Yes. Its hands are force-sensing and stop at the lightest resistance, so it can hold a child's toy or a full glass without crushing either. It moves slowly near small people and pets."),
    ("What happens to my data?", "It stays in your house. No cloud footage, no remote access, no third parties. If you sell or return Nubo, one press wipes everything it ever learned."),
    ("Does it need the internet?", "Only for overnight updates. Everything else — perception, decisions, your household model — runs on-device and keeps working if your connection doesn't."),
    ("How long does the battery last, and do I have to charge it?", "About 23 hours on a charge — a full day for most homes. You don't manage it: when it runs low, Nubo returns to its dock on its own, usually before you notice."),
    ("How hard is it to set up?", "Around 42 minutes from box to working. Unpack, place the dock, pair it once, walk it through your home, and let it learn. After that, it's designed to stay out of your way."),
    ("Do I own it, or is there a subscription?", "You own it. One purchase, the robot is yours. The only optional cost is the Care plan, and you can add or cancel that whenever you like."),
]
faq = f"""
<section class="faq" id="faq">
  <div class="head-c">
    {tag("BEFORE YOU PRE-ORDER", "ink")}
    <h2 class="d110 split" style="width:652px">{G("The")} <span class="soft">{G("practical")}</span><br>{G("answers.")}</h2>
    <p class="sub cap18" style="width:530px">{G("SHIPPING, RETURNS, WARRANTY, COMPATIBILITY. WHAT OUR SUPPORT TEAM GETS ASKED MOST OFTEN, ANSWERED WITHOUT THE FLUFF.")}</p>
  </div>
  {acc(faq_items, "narrow a22")}
</section>"""

quick = f"""
<div class="qs-wrap">
<section class="qs cream" id="qs">
  <div class="qs-grid">
    <div class="qs-img">{ph("a", "", "Photo, 414 by 700")}
      <div class="qs-num">{odo("0.2", "sec", "o100")}<p class="cap18t ink">{G("UNDERSTANDS BEFORE YOU FINISH")}</p></div>
      <p class="qs-bot">{G("Hears the room,")}<br>{G("not just the command.")}</p>
    </div>
    <div class="qs-main">
      <div class="lab"><span class="sq32">{ICON}</span><span class="cap18t">{G("QUICK STATS")}</span></div>
      <h2 class="h52">{G("Designed around")}<br><span class="soft">{G("behavior,")}</span><br>{G("not a spec sheet.")}</h2>
      <p class="cap18 ink bottom" style="width:460px">{G("MOST HOME ROBOTS ARE ENGINEERED TO IMPRESS IN A DEMO. NUBO IS ENGINEERED TO BE TOLERABLE ON A TUESDAY — WHICH TURNS OUT TO BE THE HARDER PROBLEM.")}</p>
      {btn("FULL SPECIFICATION", "dark", 203)}
    </div>
    <div class="qs-side">
      <div class="qs-card"><div class="lab"><span class="sq32">{ICON}</span><span class="cap18t">{G("AVAILABILITY")}</span></div>{odo("23", "h", "o100")}<p class="cap14 ink" style="width:230px">{G("A FULL WAKING DAY OF HELP ON ONE OVERNIGHT CHARGE.")}</p></div>
      <div class="qs-card"><div class="lab"><span class="sq32">{ICON}</span><span class="cap18t">{G("SETUP")}</span></div>{odo("42", "min", "o100")}<p class="cap16 ink" style="width:200px">{G("FROM OPENING THE BOX TO THE FIRST FINISHED TASK.")}</p></div>
    </div>
  </div>
</section>
</div>"""

plans = [
    ("Nubo", "THE STANDARD HOME SYSTEM. EVERYTHING MOST HOMES NEED.", "ESSENTIALS", "€3,290", "", "ONE-TIME · FREE SHIPPING", ["ROUTINE SUPPORT", "HOME AWARENESS", "3 FINISHES", "18-HOUR BATTERY", "2-YEAR WARRANTY"]),
    ("Nubo Pro", "EXTENDED SENSING, ALL FINISHES, LONGER BATTERY. RECOMMENDED FOR LARGER HOMES.", "MOST POPULAR", "€4,490", "", "ONE-TIME · FREE SHIPPING", ["EVERYTHING IN STANDARD", "CARRIES AND FETCHES", "5 FINISHES", "23-HOUR BATTERY", "3-YEAR WARRANTY", "PRIORITY SUPPORT"]),
    ("Nubo Care", "OPTIONAL SERVICE PLAN. SOFTWARE UPDATES, REPAIR, AND REPLACEMENT COVERED.", "OPTIONAL COVER", "€14", "/month", "ADD TO ANY NUBO", ["ANNUAL HOME CHECK", "COVER DAMAGE", "SOFTWARE UPDATES", "REPLACEMENT LOAN UNIT", "ADD ANYTIME, CANCEL ANYTIME"]),
]
def price(p):
    return "".join(c if not c.isdigit() else str((int(c) + 3) % 10) for c in p)
plan_html = "".join(f"""
    <article class="plan">
      <div class="plan-top"><h3 class="h32">{G(n)}</h3><p class="cap14">{G(d)}</p><span class="disc">{ph("b", "round", "Circle image")}</span></div>
      <div class="plan-body">
        <p class="lab2"><span class="sq">{ICON}</span><span class="cap14t">{G(t)}</span></p>
        <p class="price">{price(pr)}{f'<span>{G(per)}</span>' if per else ''}</p>
        <span class="pill2">{G(note)}</span>
        <ul>{"".join(f'<li>{G(f)}</li>' for f in feats)}</ul>
        {btn("CHOOSE PLAN", "dark", 165)}
      </div>
    </article>""" for n, d, t, pr, per, note, feats in plans)
logos = "".join(f'<span class="lg"><i></i>{G(w)}</span>' for w in ["sveltekit", "simplestore", "linear", "elasticpath", "xata"])
pricing = f"""
<section class="pricing" id="pricing">
  <div class="head-l">
    {tag("PRICING")}
    <div class="row-b"><h2 class="h60">{G("Choose how you")}<br>{G("bring it home.")}</h2><p class="cap18 right" style="width:633px;align-self:end;margin-bottom:5px">{G("WORKS WITH WHAT YOU ALREADY HAVE.")}</p></div>
    <div class="row-b2"><p class="cap18" style="width:600px">{G("NO TIERS LOCKED BEHIND SUBSCRIPTIONS. THE ROBOT IS YOURS. THE CARE PLAN IS OPTIONAL.")}</p><div class="tiny-logos">{"".join('<i></i>' for _ in range(4))}</div></div>
  </div>
  <div class="plans">{plan_html}</div>
  <p class="cap20 center" style="margin-top:60px">{G("SERVICES INTEGRATED WITH NUBO")}</p>
  <div class="logos">{logos}</div>
</section>"""

reviews_data = [
    ("4.8/5", "\"It took the dog three days. It took my husband three weeks.\"", "We expected a gadget. What we got was closer to a very polite housemate who happens to be excellent at finding lost things. My husband came around — mostly since it started remembering where he leaves his glasses.", "BETA TESTER", "NATALIE K.", "FLORENCE, ITALY", "c"),
    ("5/5", "\"It knows my daughter better than I remembered to.\"", "She likes the blinds half-open, I like them shut. Nubo picked up on both within a week and stopped asking. I've lived with people who took longer to learn that.", "VERIFIED OWNER", "JOAN P.", "GÖTEBORG, SWEDEN", "e"),
    ("4.9/5", "\"My kids named it before I did.\"", "It's Barnaby now, apparently, and there's no walking that back. What surprised me wasn't the tech, it was how fast it stopped feeling like tech. Three weeks in, it's just the thing that gets the door.", "EARLY ACCESS", "DANIEL O.", "PORTLAND, OREGON", "a"),
    ("5/5", "\"I braced for another device to babysit.\"", "Instead I got a system that runs itself. No app I have to open, no light that blinks until I pay attention to it. It does the job and gets out of the room, which is more than I can say for most of my houseguests.", "BETA TESTER", "NAO F.", "TOKYIO, JAPAN", "f"),
    ("4.3/5", "\"Six weeks in, and the novelty still hasn't worn off — because there wasn't much novelty to wear off.\"", "It doesn't do tricks. It clears the table, it charges itself, it stays out of the kitchen when we're cooking. My last three smart home purchases wanted applause.", "SMART HOME SKEPTIC", "MARCUS W.", "AUSTIN, TEXAS", "h"),
    ("4.7/5", "\"The first robot I've owned that doesn't ask to be noticed.\"", "That's rarer than it sounds. Everything else in this house beeps, glows, or asks me to rate my experience. Nubo has opinions about none of that. It just gets on with it.", "BETA TESTER", "FREYA H.", "COPENHAGEN, DENMARK", "b"),
]
rv = "".join(f"""
      <article class="rv">
        <div class="rv-h">{stars()}<span class="score">{G(s)}</span></div>
        <p class="rv-q">{G(q)}</p>
        <p class="rv-b">{G(b)}</p>
        <div class="rv-who"><div class="av">{ph(t, "", "Portrait, 80 by 110")}</div><div class="rv-meta"><span class="pill">{G(tg)}</span><p class="cap18t ink">{G(n)}</p><p class="cap14t grey2">{G(c)}</p></div></div>
      </article>""" for s, q, b, tg, n, c, t in reviews_data)
reviews = f"""
<section class="reviews cream" id="reviews">
  <div class="head-l">
    {tag("LIVING WITH NUBO")}
    <div class="row-b"><h2 class="h60">{G("From the homes already")}<br><span class="soft">{G("running Nubo.")}</span></h2><p class="cap18 right" style="width:633px">{G("PART OF THE BETA PROGRAM?")}<br>{G("TELL US HOW NUBO IS SETTLING IN.")}</p></div>
    <div class="row-b2"><p class="cap18" style="width:420px">{G("REAL HOMES HAVE BEEN LIVING WITH NUBO FOR MONTHS. HERE'S WHAT THE FIRST TESTERS MAKE OF IT.")}</p>{btn("WRITE REVIEW", "dark", 162)}</div>
  </div>
  <div class="marquee"><div class="mq-track">{rv}{rv}</div></div>
</section>"""

closing = f"""
<section class="closing" id="closing">
  {ph("h", "bg", "Full-bleed photo, 1440 by 1080")}
  <div class="cl-in">
    <p class="kicker"><i class="ic w"></i><span>{G("You'll wonder how the house ran without it.")}</span></p>
    <h2 class="d110 split" style="width:700px">{G("Make room for")}<br>{G("your Nubo.")}</h2>
    <div class="ctas">{btn("RESERVE NUBO", "dark", 168)}{btn("GET IN TOUCH", "white", 163)}</div>
  </div>
</section>"""

cols = [("NAVIGATION", ["HOME", "CASES", "ABOUT", "PRICING", "UPDATES", "WAITLIST", "CONTACT"]),
        ("LEGAL", ["PRIVACY & COOKIES", "TERMS OF SERVICE", "404"]),
        ("FOLLOW", ["YOUTUBE", "TIKTOK", "INSTAGRAM", "X (TWITTER)"])]
footer = f"""
<footer class="foot" id="foot">
  <div class="wordmark" aria-hidden="true">
    <svg viewBox="0 0 1392 464" preserveAspectRatio="none" class="wm-sharp"><text x="0" y="420" textLength="1392" lengthAdjust="spacingAndGlyphs">{G("nubo")}</text></svg>
    <svg viewBox="0 0 1392 464" preserveAspectRatio="none" class="wm-blur"><text x="0" y="420" textLength="1392" lengthAdjust="spacingAndGlyphs">{G("nubo")}</text></svg>
  </div>
  <div class="foot-grid">
    <div class="foot-cols">{"".join(f'<div><p class="cap14 grey">{G(h)}</p><ul>{"".join(f"<li><a href=\"#top\">{G(l)}</a></li>" for l in ls)}</ul></div>' for h, ls in cols)}</div>
    <form class="news" onsubmit="return false">
      <p class="news-k"><span class="sq">{ICON}</span>{G("Stay in the loop, gently.")}</p>
      <h3 class="h32">{G("Nubo Newsletter")}</h3>
      <label><span class="sr">{G("YOUR NAME")}</span><input placeholder="{G("YOUR NAME")}"></label>
      <label><span class="sr">{G("YOUR EMAIL")}</span><input type="email" placeholder="{G("YOUR EMAIL")}"></label>
      <div class="news-ft"><button type="submit" class="btn dark sub-btn"><span class="roll"><span>{G("SUBSCRIBE")}</span><span>{G("SUBSCRIBE")}</span></span>{ARROW}</button><p class="cap14">{G("WE RESPECT YOUR INBOX.")}<br>{G("NO SPAM, JUST VALUABLE UPDATES.")}</p></div>
    </form>
  </div>
  <div class="foot-bot"><span>{G("© 2026 NUBO ALL WORK, ALL RIGHTS.")}</span><span class="fb-r"><i></i>{G("Template credit")}</span></div>
</footer>"""

nav = f"""
<nav class="nav" aria-label="Main">
  <a class="logo" href="#top" aria-label="Home"><span class="logo-ph">{G("nubo")}</span></a>
  <button type="button" id="menuBtn" aria-label="Toggle menu" aria-expanded="false"><i></i><i></i><i></i></button>
</nav>
<div class="drop" id="drop">
  <div class="drop-links">{"".join(f'<a href="#{h}">{G(t)}</a>' for t, h in [("Capabilities", "caps"), ("At home", "home"), ("Signals", "signals"), ("Pricing", "pricing"), ("Questions", "faq"), ("Reviews", "reviews")])}</div>
  <div class="drop-ft"><p class="cap14">{G("THE HELPFUL HOME ROBOTICS COMPANY.")}</p><div class="cd"><p>{G("Time Until Launch")}</p><div id="cd">{"".join(f'<span><b>00</b><small>{u}</small></span>' for u in ["DAYS", "HRS", "MIN", "SEC"])}</div></div></div>
</div>"""

css = pathlib.Path(__file__).with_name("blank.css").read_text()
js = pathlib.Path(__file__).with_name("blank.js").read_text()

html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Blank Canvas</title>
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
{hello}
{caps}
{home}
{signals}
{materials}
{bento}
{faq}
{quick}
{pricing}
{reviews}
{closing}
</main>
{footer}
<script>
{js}
</script>
</body>
</html>
"""
out = pathlib.Path(__file__).with_name("blank.html")
out.write_text(html)
print("wrote", out, len(html), "bytes")
