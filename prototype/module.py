#!/usr/bin/env python3
"""Builds prototype/app-module.html: the one page template every Luex module uses (all except the Dashboard).
Three states of the same page, numbered regions, and a table of how modules fill it.
Run: python3 prototype/module.py"""
import pathlib

P = {
    "grid": '<rect x="4" y="4" width="6" height="6" rx="1.5"/><rect x="14" y="4" width="6" height="6" rx="1.5"/><rect x="4" y="14" width="6" height="6" rx="1.5"/><rect x="14" y="14" width="6" height="6" rx="1.5"/>',
    "list": '<path d="M9 6h11M9 12h11M9 18h11"/><circle cx="4.5" cy="6" r="1"/><circle cx="4.5" cy="12" r="1"/><circle cx="4.5" cy="18" r="1"/>',
    "people": '<circle cx="9" cy="8" r="3.2"/><path d="M3.5 19c.8-3.2 3-5 5.5-5s4.7 1.8 5.5 5"/><circle cx="17" cy="9" r="2.4"/><path d="M15.5 14.2c2.3.2 4 1.8 4.6 4.3"/>',
    "cal": '<rect x="4" y="5" width="16" height="15" rx="3"/><path d="M4 10h16M9 3v4M15 3v4"/>',
    "clock": '<circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/>',
    "shield": '<path d="M12 3l7 3v5c0 4.5-3 8-7 10-4-2-7-5.5-7-10V6z"/><path d="M9 12l2 2 4-4"/>',
    "brief": '<rect x="4" y="7" width="16" height="12" rx="2.5"/><path d="M9 7V5.5A1.5 1.5 0 0 1 10.5 4h3A1.5 1.5 0 0 1 15 5.5V7M4 12h16"/>',
    "pound": '<path d="M16 6.5A3.5 3.5 0 0 0 9.5 8v9.5M7 12.5h6.5M7 18h10"/>',
    "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 3v2.5M12 18.5V21M3 12h2.5M18.5 12H21M5.6 5.6l1.8 1.8M16.6 16.6l1.8 1.8M5.6 18.4l1.8-1.8M16.6 7.4l1.8-1.8"/>',
    "bell": '<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
    "inbox": '<path d="M4 13l2.5-7h11L20 13v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1z"/><path d="M4 13h4.5l1 2h5l1-2H20"/>',
    "help": '<circle cx="12" cy="12" r="8.5"/><path d="M9.6 9.5a2.5 2.5 0 0 1 4.8.8c0 1.7-2.4 2-2.4 3.4M12 17h.01"/>',
    "search": '<circle cx="11" cy="11" r="6"/><path d="M20 20l-4.5-4.5"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "down": '<path d="M7 10l5 5 5-5"/>',
    "chev": '<path d="M9 6l6 6-6 6"/>',
    "back": '<path d="M15 6l-6 6 6 6"/>',
    "dots": '<circle cx="5" cy="12" r="1.4"/><circle cx="12" cy="12" r="1.4"/><circle cx="19" cy="12" r="1.4"/>',
    "x": '<path d="M6 6l12 12M18 6L6 18"/>',
    "tick": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    "edit": '<path d="M5 19l1-4L15.5 5.5a2.1 2.1 0 0 1 3 3L9 18z"/><path d="M13.5 7.5l3 3"/>',
    "upload": '<path d="M12 16V5M7.5 9.5L12 5l4.5 4.5M5 19h14"/>',
    "filter": '<path d="M4 6h16M7 12h10M10 18h4"/>',
    "card": '<rect x="3.5" y="6" width="17" height="12" rx="2.5"/><path d="M3.5 10h17M7 14.5h4"/>',
    "hat": '<path d="M4 16h16M6 16v-2a6 6 0 0 1 12 0v2M10 8.5V6h4v2.5"/>',
    "aid": '<rect x="4" y="6" width="16" height="13" rx="2.5"/><path d="M12 9.5v6M9 12.5h6M9 6V4.5h6V6"/>',
    "crane": '<path d="M6 20V5h1.5L19 8M6 8h13M14 8v5"/><path d="M12.5 13h3v2.5h-3z"/><path d="M4 20h5"/>',
    "fire": '<path d="M12 21c3.5 0 6-2.4 6-5.6 0-3.8-3.4-5.6-4-9.4-2.5 1.6-3.6 3.8-3.6 6-1.2-.7-1.8-1.8-2-3C6.6 10.6 6 12.7 6 15.4 6 18.6 8.5 21 12 21z"/>',
    "link": '<path d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7L11.5 6.8"/><path d="M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1.5-1.5"/>',
    "doc": '<path d="M7 3.5h7l4 4V20a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V4.5a1 1 0 0 1 1-1z"/><path d="M14 3.5V8h4M9 13h6M9 16.5h6"/>',
    "bellring": '<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20a2 2 0 0 0 4 0M3.5 8.5A8 8 0 0 1 6 4.5M20.5 8.5A8 8 0 0 0 18 4.5"/>',
    "export": '<path d="M12 4v11M7.5 8.5L12 4l4.5 4.5M5 14v5h14v-5"/>',
    "archive": '<rect x="4" y="5" width="16" height="4" rx="1.2"/><path d="M5.5 9v9.5a1 1 0 0 0 1 1h11a1 1 0 0 0 1-1V9M10 13h4"/>',
    "star": '<path d="M12 4l2.4 5 5.4.6-4 3.7 1.1 5.3L12 16l-4.9 2.6 1.1-5.3-4-3.7 5.4-.6z"/>',
}
def ic(n, cls="i"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{P[n]}</svg>'

def num(n):
    return f'<span class="mk">{n}</span>'

GREEN, AMBER, RED, NEUTRAL = "#2F8F5B", "#C98A1B", "#C2413A", "#1C1C1E"

# --------------------------------------------------------------- shared regions
def rail():
    items = [("grid", False, ""), ("star", False, ""), (None, 0, 0), ("shield", True, "8"), ("clock", False, "14"), ("cal", False, "3"),
             ("people", False, ""), ("brief", False, "2"), ("pound", False, ""), (None, 0, 0), ("gear", False, "")]
    nav = ""
    for n, on, b in items:
        if n is None:
            nav += '<span class="nv-sep"></span>'; continue
        badge = f'<em class="bd">{b}</em>' if b else ""
        nav += f'<span class="nv{" on" if on else ""}">{ic(n)}{badge}</span>'
    return f'''<aside class="m-rail">
      <span class="dz-lg"><i></i><i></i><i></i></span>
      <span class="exp">{ic("chev")}</span>
      <nav>{nav}</nav>
      <span class="dz-me">CM</span>
    </aside>'''

def header(marks=True):
    m = (lambda k: num(k)) if marks else (lambda k: "")
    return f'''<header class="m-hd">
      <div class="m-title">{m(2)}
        <small>Safety and quality <i>·</i> Compliance</small>
        <div class="tl"><h4>Compliance</h4><span class="pill">{ic("cal")}All sites {ic("down")}</span></div>
      </div>
      <div class="m-act">
        <span class="pill srch">{ic("search")}Search everything<kbd>Ctrl K</kbd></span>
        <span class="rnd dark" title="Create">{ic("plus")}</span>
        <span class="rnd" title="Inbox">{ic("inbox")}<em class="cnt">5</em></span>
        <span class="rnd" title="Notifications">{ic("bell")}<i class="dotr"></i></span>
        <span class="rnd" title="Help">{ic("help")}</span>
        <span class="user"><span class="av">CM</span><span><b>Ciara Murphy</b><small>Operations manager</small></span>{ic("down")}</span>
      </div>
    </header>'''

def tiles(sel=2, marks=True):
    T = [(NEUTRAL, "All records", "248", "Across 4 sites"), (GREEN, "Valid", "219", "88% of records"),
         (AMBER, "Due soon", "21", "Next 30 days"), (RED, "Expired", "8", "3 blocking shifts")]
    out = ""
    for k, (c, l, n, cap) in enumerate(T):
        out += f'''<button class="tile{" sel" if k == sel else ""}" style="--c:{c}">
          <span class="t-top"><span class="sdot"></span><span class="tl-l">{l}</span>{ic("chev")}</span>
          <b>{n}</b><small>{cap}</small></button>'''
    return f'<div class="tiles">{num(3) if marks else ""}{out}</div>'

RECS = [
    ("card", "CSCS card", "Seán Byrne", "Docklands", "Expires 2 Feb", "12 days", AMBER, 0.12),
    ("aid", "First aid at work", "Aoife Kelly", "Ringsend", "Expires 9 Feb", "19 days", AMBER, 0.2),
    ("crane", "LOLER examination", "Telehandler TH-04", "Docklands", "Expired 20 Jan", "9 days ago", RED, 0.0),
    ("hat", "SSSTS", "Mark Doyle", "Kingsway", "Expires 14 Feb", "24 days", AMBER, 0.27),
    ("fire", "Fire marshal", "Niamh Walsh", "Head office", "Expires 18 Feb", "28 days", AMBER, 0.31),
    ("doc", "Public liability", "Luex Ltd", "All sites", "Expires 21 Feb", "30 days", AMBER, 0.34),
]

def cards(open_i=0, marks=True):
    out = ""
    for k, (i, name, who, site, date, left, c, frac) in enumerate(RECS):
        cls = " open" if k == open_i else ""
        out += f'''<article class="rc{cls}" style="--c:{c}">
          <div class="rc-top"><span class="ci">{ic(i)}</span><span class="sdot"></span></div>
          <b>{name}</b><small>{who} · {site}</small>
          <div class="rc-ft"><span>{date}</span><em>{left}</em></div>
          <span class="bar"><i style="width:{max(frac, .04) * 100:.0f}%"></i></span>
        </article>'''
    return out

def main_window(view="cards", marks=True):
    m = num if marks else (lambda k: "")
    top = f'''<div class="mw-top">
        <div class="mw-h">{m(4)}<b>Due soon</b><span>21 records</span></div>
        <div class="mw-tools">
          <span class="pill srch2">{ic("search")}Search this list</span>
          <span class="pill">Category {ic("down")}</span><span class="pill">Person {ic("down")}</span><span class="pill">Date {ic("down")}</span>
          <span class="pill ghost">{ic("star")}Saved views {ic("down")}</span>
          <span class="seg"><span class="{"on" if view == "cards" else ""}">{ic("grid")}</span><span class="{"on" if view.startswith("list") else ""}">{ic("list")}</span></span>
        </div>
      </div>'''
    if view == "cards":
        body = f'<div class="cards">{cards()}</div>'
        bar = f'''<div class="tabbar">{m(6)}<span class="on">{ic("list")}List</span><span>{ic("cal")}Calendar</span><span>{ic("filter")}Insights</span><span>{ic("doc")}Requirements</span><span class="add">{ic("plus")}</span></div>'''
    else:
        rows = ""
        for k, (i, name, who, site, date, left, c, frac) in enumerate(RECS):
            sel = view == "list" and k in (0, 1, 3)
            opn = view == "listplain" and k == 0
            rows += f'''<div class="lr{" sel" if sel else ""}{" open" if opn else ""}" style="--c:{c}">
              <span class="tk">{ic("tick") if sel else ""}</span><span class="ci sm">{ic(i)}</span>
              <span class="lr-n"><b>{name}</b><small>{who}</small></span><span class="lr-s">{site}</span><span class="lr-d">{date}</span>
              <span class="st-pill"><span class="sdot"></span>{left}</span></div>'''
        body = f'''<div class="lhead"><span class="tk{" all" if view == "list" else ""}"></span><span></span><span>Name</span><span>Site</span><span>Date</span><span>Status</span></div><div class="lrows">{rows}</div>'''
        bar = f'''<div class="tabbar"><span class="on">{ic("list")}List</span><span>{ic("cal")}Calendar</span><span>{ic("filter")}Insights</span><span>{ic("doc")}Requirements</span><span class="add">{ic("plus")}</span></div>''' if view == "listplain" else f'''<div class="tabbar bulk">{num(8)}<b>3 selected</b><span>{ic("bellring")}Remind</span><span>{ic("export")}Export</span><span>{ic("archive")}Archive</span><span class="x">{ic("x")}</span></div>'''
    return f'<section class="mw">{top}{body}{bar}</section>'

def detail(marks=True):
    m = num if marks else (lambda k: "")
    facts = [("Issued", "2 Feb 2021"), ("Expires", "2 Feb 2026"), ("Card number", "CS-4471 902"), ("Verified by", "Ciara M., 3 Feb 2021")]
    acts = [("CM", "Ciara Murphy", "sent a reminder to Seán", "Today, 08:02"),
            ("SB", "Seán Byrne", "booked a renewal for 30 Jan", "Yesterday"),
            ("LX", "Luex", "marked this as due soon", "3 Jan")]
    return f'''<section class="dw">{m(5)}
      <div class="dw-hd"><span class="chip">{ic("card")}Cards and tickets</span><span class="chip" style="--c:{AMBER}"><span class="sdot"></span>Due soon</span>
        <span class="dw-r"><span class="rnd sm">{ic("edit")}</span><span class="rnd sm">{ic("dots")}</span></span></div>
      <h5>CSCS card</h5>
      <p class="dw-sub"><span class="av sm">SB</span>Seán Byrne <i>·</i> Docklands</p>
      <div class="key">
        <div class="mini-ring" style="--p:12"><svg viewBox="0 0 80 80"><circle cx="40" cy="40" r="32" class="tr"/><circle cx="40" cy="40" r="32" class="pr"/></svg><span><b>12</b><small>days left</small></span></div>
        <div class="key-r"><p>Expires on <b>2 February</b>. Seán can't be booked on shifts after that date.</p>
          <div class="key-b"><span class="btn-d">{ic("tick")}Renew</span><span class="btn-l">{ic("bellring")}Remind</span></div></div>
      </div>
      <div class="facts">{"".join(f'<div><small>{a}</small><b>{b}</b></div>' for a, b in facts)}</div>
      <div class="dtabs"><span class="on">Activity</span><span>Evidence <em>2</em></span><span>Linked <em>3</em></span><span>History</span></div>
      <div class="acts">{"".join(f'<div class="act"><span class="av sm">{i}</span><p><b>{n}</b> {t}<small>{w}</small></p></div>' for i, n, t, w in acts)}</div>
      <div class="cmt"><span>Write a comment, @ to mention</span>{ic("plus")}</div>
    </section>'''

def slidein(marks=True):
    m = num if marks else (lambda k: "")
    return f'''<section class="si">{m(7)}
      <div class="si-hd"><span class="rnd sm">{ic("x")}</span><b>Edit record</b><span class="draft">Draft saved</span></div>
      <div class="fields">
        <label><small>Type</small><span class="inp">{ic("card")}CSCS card {ic("down")}</span></label>
        <label><small>Person</small><span class="inp"><span class="av sm">SB</span>Seán Byrne {ic("down")}</span></label>
        <div class="two"><label><small>Issue date</small><span class="inp">2 Feb 2021</span></label>
          <label class="bad"><small>Expiry date</small><span class="inp">2 Feb 2020</span><em>Expiry can't be before the issue date.</em></label></div>
        <label><small>Card number</small><span class="inp">CS-4471 902</span></label>
        <label><small>Evidence</small><span class="drop">{ic("upload")}<span>Drop a photo or file, or <u>browse</u></span></span></label>
        <label><small>Notes</small><span class="inp area">Renewal booked with CITB for 30 Jan.</span></label>
      </div>
      <div class="si-ft"><span class="btn-l">Cancel</span><span class="btn-d">Save changes</span></div>
    </section>'''

def frame(kind):
    marks = kind == "open"
    if kind == "open":
        body = f'<div class="m-body">{main_window("cards")}{detail()}</div>'
    elif kind == "edit":
        body = f'<div class="m-body">{main_window("cards", False)}{detail(False)}<div class="scrim"></div>{slidein()}</div>'
    else:
        body = f'<div class="m-body">{main_window("list", False)}{detail(False)}</div>'
    return f'''<div class="fit"><div class="m-page">
      {rail()}{num(1) if marks else ""}
      <div class="m-main">{header(marks)}{tiles(2, marks)}{body}</div>
    </div></div>'''

# --------------------------------------------------------------- legend and module table
LEGEND = [
    (1, "Nav rail", "Every module, with a badge showing how many things need you there. Expands to show names; favourites at the top."),
    (2, "Header", "Where you are (group · module), the site switcher, search everything, one Create (+), Inbox, bell, Help and your profile. Identical on every page."),
    (3, "Status tiles", "Three to five counts that matter for this module. Tap one to filter the records window; the chosen tile is highlighted."),
    (4, "Records window", "The biggest box: every record you can see, as cards or a list. Heading says what's showing and how many. Search, filters and saved views across the top."),
    (5, "Detail window", "Opens when you tap a record. Who and where, the one thing to do next (Renew, Approve, Pay), key facts, then Activity, Evidence, Linked and History."),
    (6, "View tabs", "The module's views: List, Calendar, Insights and so on. The dark + is the module's main 'add' action."),
    (7, "Edit panel", "Every add and edit form slides in from the right. Checks as you type, saves a draft automatically, and Cancel puts everything back as it was."),
    (8, "Bulk bar", "Tick records and the tab bar becomes the bulk bar: how many are selected and what you can do to all of them at once."),
]
MODULES = [
    ("Compliance", "All · Valid · Due soon · Expired", "Certificate, person, expiry countdown", "Renew / Remind", "List · Calendar · Insights · Requirements"),
    ("Timesheets", "This week · To approve · Queried · Approved", "Person, week, hours, overtime", "Approve / Query", "Week · List · Insights"),
    ("Time off", "Requests · Pending · Approved · Off today", "Person, dates, type, days", "Approve / Decline", "Calendar · List · Balances"),
    ("Scheduling", "Shifts · Open · Blocked · Unconfirmed", "Shift, site, time, person", "Assign / Swap", "Week · Day · List"),
    ("CRM", "Leads · Quoted · Won · Lost", "Company, contact, value, stage", "Send quote / Call", "Pipeline · List · Insights"),
    ("Assets", "All · In service · Inspection due · Out of service", "Asset, site, next inspection", "Book inspection / Move", "List · Map · Calendar"),
    ("Expenses", "Claims · To approve · Sent back · Paid", "Person, amount, category, date", "Approve / Send back", "List · Insights"),
    ("Documents", "All · To review · To sign · Expiring", "Document, owner, version, review date", "Sign / New version", "Folders · List"),
]

CSS = """
:root { --head: "Google Sans", "Helvetica Neue", Arial, sans-serif; color-scheme: light; }
* { box-sizing: border-box; }
body { margin: 0; background: #E9E9EB; font-family: var(--head); color: #1C1C1E; padding: 32px 16px 64px; -webkit-font-smoothing: antialiased; }
.wrap { max-width: 1440px; margin: 0 auto; }
h1 { font-weight: 500; font-size: 30px; letter-spacing: -1px; margin: 0 0 6px; }
h2 { font-weight: 500; font-size: 22px; letter-spacing: -.6px; margin: 48px 0 6px; }
.lead { color: #5E5E63; font-size: 15px; line-height: 1.5; margin: 0 0 22px; max-width: 760px; }
.frame { border-radius: 22px; overflow: hidden; box-shadow: 0 30px 60px -30px rgba(0,0,0,.35); background: #fff; }
.fit { position: relative; width: 100%; aspect-ratio: 1280 / 800; overflow: hidden; }
.m-page { position: absolute; left: 0; top: 0; width: 1280px; height: 800px; transform-origin: 0 0; transform: scale(var(--s, 1)); display: grid; grid-template-columns: 68px 1fr; gap: 10px; padding: 10px; background: #fff; letter-spacing: -.2px; }
.i { width: 16px; height: 16px; fill: none; stroke: currentColor; stroke-width: 1.7; stroke-linecap: round; stroke-linejoin: round; flex: none; }

/* numbered markers explaining each region */
.mk { position: absolute; z-index: 30; width: 26px; height: 26px; border-radius: 50%; background: #2F5FC2; color: #fff; font-size: 13px; font-weight: 500; display: grid; place-items: center; box-shadow: 0 0 0 3px #fff, 0 4px 10px rgba(47,95,194,.4); letter-spacing: 0; }
.m-page > .mk { left: 62px; top: 150px; }
.m-title .mk { left: auto; right: -40px; top: 30px; }
.tiles > .mk { left: -12px; top: -10px; }
.mw-h .mk { position: static; margin-right: 4px; }
.dw > .mk { right: 92px; top: 18px; left: auto; }
.tabbar span.mk, .tabbar.bulk span.mk { position: absolute; left: -14px; top: -14px; width: 26px; height: 26px; padding: 0; justify-content: center; border-radius: 50%; background: #2F5FC2; color: #fff; font-size: 13px; }
.si > .mk { left: -12px; top: 18px; }

/* rail */
.m-rail { background: #F1F1F2; border-radius: 18px; display: flex; flex-direction: column; align-items: center; padding: 18px 0 14px; gap: 14px; }
.dz-lg { position: relative; width: 26px; height: 24px; }
.dz-lg i { position: absolute; width: 11px; height: 11px; border-radius: 2.5px; background: #1C1C1E; }
.dz-lg i:nth-child(1) { left: 0; top: 2px; } .dz-lg i:nth-child(2) { left: 7px; top: 11px; width: 12px; height: 12px; } .dz-lg i:nth-child(3) { left: 14px; top: 0; background: #CFB783; transform: rotate(14deg); }
.exp { width: 22px; height: 22px; border-radius: 50%; background: #fff; display: grid; place-items: center; color: #6B6B70; box-shadow: 0 1px 2px rgba(0,0,0,.08); }
.exp .i { width: 12px; height: 12px; }
.m-rail nav { display: flex; flex-direction: column; align-items: center; gap: 4px; margin-top: 6px; }
.nv { position: relative; width: 40px; height: 40px; border-radius: 12px; display: grid; place-items: center; color: #6B6B70; }
.nv.on { background: #1C1C1E; color: #fff; }
.bd { position: absolute; top: 2px; right: 0; min-width: 16px; height: 16px; padding: 0 4px; border-radius: 99px; background: #fff; color: #1C1C1E; font-size: 9.5px; font-style: normal; font-weight: 500; display: grid; place-items: center; box-shadow: 0 1px 3px rgba(0,0,0,.18); }
.nv-sep { width: 14px; height: 1px; background: #D9D9DC; margin: 4px 0; }
.dz-me, .av { width: 36px; height: 36px; border-radius: 50%; background: #1C1C1E; color: #fff; display: grid; place-items: center; font-size: 12px; font-weight: 500; letter-spacing: 0; flex: none; }
.dz-me { margin-top: auto; }
.av.sm { width: 26px; height: 26px; font-size: 9.5px; }

/* main column */
.m-main { position: relative; display: grid; grid-template-rows: 54px 86px 1fr; gap: 10px; min-width: 0; min-height: 0; }
.m-hd { display: flex; align-items: center; justify-content: space-between; padding: 0 2px 0 6px; }
.m-title { position: relative; }
.m-title small { font-size: 11px; color: #8A8A90; } .m-title small i { font-style: normal; margin: 0 3px; }
.tl { display: flex; align-items: center; gap: 12px; margin-top: 2px; }
.tl h4 { margin: 0; font-size: 24px; font-weight: 500; letter-spacing: -.8px; }
.m-act { display: flex; align-items: center; gap: 8px; }
.pill { display: inline-flex; align-items: center; gap: 6px; height: 32px; padding: 0 12px; border-radius: 99px; background: #fff; box-shadow: inset 0 0 0 1px #E6E6E8; font-size: 12px; color: #3A3A3E; white-space: nowrap; }
.pill .i { width: 13px; height: 13px; }
.pill.ghost { background: transparent; }
.srch { width: 240px; color: #8A8A90; background: #F4F4F5; box-shadow: none; height: 38px; }
.srch kbd { margin-left: auto; font-family: inherit; font-size: 10px; padding: 2px 6px; border-radius: 6px; background: #fff; color: #8A8A90; }
.rnd { position: relative; width: 38px; height: 38px; border-radius: 50%; background: #F4F4F5; display: grid; place-items: center; color: #1C1C1E; flex: none; }
.rnd.dark { background: #1C1C1E; color: #fff; }
.rnd.sm { width: 30px; height: 30px; background: #fff; box-shadow: inset 0 0 0 1px #E6E6E8; }
.rnd.sm .i { width: 14px; height: 14px; }
.cnt { position: absolute; top: -3px; right: -3px; min-width: 17px; height: 17px; padding: 0 4px; border-radius: 99px; background: #1C1C1E; color: #fff; font-size: 9.5px; font-style: normal; display: grid; place-items: center; box-shadow: 0 0 0 2px #fff; }
.dotr { position: absolute; top: 9px; right: 10px; width: 7px; height: 7px; border-radius: 50%; background: #E5484D; box-shadow: 0 0 0 2px #F4F4F5; }
.user { display: flex; align-items: center; gap: 9px; padding: 4px 12px 4px 4px; border-radius: 99px; background: #F4F4F5; }
.user .av { width: 30px; height: 30px; font-size: 10.5px; }
.user b { display: block; font-size: 12px; font-weight: 500; } .user small { font-size: 10px; color: #8A8A90; }

/* status tiles */
.tiles { position: relative; display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; }
.tile { all: unset; box-sizing: border-box; position: relative; background: #F1F1F2; border-radius: 18px; padding: 12px 16px; display: grid; grid-template-columns: auto 1fr; grid-template-rows: auto 1fr; column-gap: 12px; cursor: pointer; }
.t-top { grid-column: 1 / -1; display: flex; align-items: center; gap: 8px; font-size: 12px; color: #5E5E63; }
.t-top .i { margin-left: auto; width: 13px; height: 13px; color: #9A9AA0; }
.sdot { width: 8px; height: 8px; border-radius: 50%; background: var(--c); flex: none; }
.tile b { font-size: 30px; font-weight: 500; letter-spacing: -1.2px; align-self: end; line-height: 1; }
.tile small { font-size: 11px; color: #8A8A90; align-self: end; padding-bottom: 3px; }
.tile.sel { background: #fff; box-shadow: inset 0 0 0 2px var(--c), 0 8px 18px -10px var(--c); }

/* body: records window + detail window */
.m-body { position: relative; display: grid; grid-template-columns: 1fr 372px; gap: 10px; min-height: 0; }
.mw { position: relative; background: #F1F1F2; border-radius: 20px; padding: 16px 16px 72px; display: flex; flex-direction: column; min-width: 0; min-height: 0; overflow: hidden; }
.mw-top { display: flex; flex-direction: column; gap: 12px; }
.mw-h { display: flex; align-items: center; gap: 10px; } .mw-h b { font-size: 16px; font-weight: 500; } .mw-h span:last-child { font-size: 12px; color: #8A8A90; }
.mw-tools { display: flex; align-items: center; gap: 8px; }
.srch2 { width: 200px; color: #8A8A90; }
.seg { margin-left: auto; display: flex; gap: 2px; padding: 3px; border-radius: 99px; background: #E4E4E7; }
.seg span { width: 30px; height: 26px; border-radius: 99px; display: grid; place-items: center; color: #6B6B70; }
.seg .on { background: #fff; color: #1C1C1E; box-shadow: 0 1px 2px rgba(0,0,0,.08); }
.cards { margin-top: 14px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; align-content: start; }
.rc { position: relative; background: #fff; border-radius: 16px; padding: 14px; display: flex; flex-direction: column; gap: 3px; min-height: 148px; }
.rc.open { box-shadow: 0 0 0 2px #1C1C1E, 0 12px 24px -14px rgba(0,0,0,.4); }
.rc-top { display: flex; justify-content: space-between; align-items: start; margin-bottom: 8px; }
.ci { width: 34px; height: 34px; border-radius: 50%; background: #F1F1F2; display: grid; place-items: center; color: #1C1C1E; flex: none; }
.ci.sm { width: 30px; height: 30px; } .ci.sm .i { width: 14px; height: 14px; }
.rc b { font-size: 14px; font-weight: 500; } .rc small { font-size: 11px; color: #8A8A90; }
.rc-ft { margin-top: auto; display: flex; justify-content: space-between; font-size: 11px; color: #5E5E63; padding-top: 10px; }
.rc-ft em { font-style: normal; color: var(--c); font-weight: 500; }
.bar { height: 4px; border-radius: 99px; background: #EDEDEF; overflow: hidden; margin-top: 7px; }
.bar i { display: block; height: 100%; background: var(--c); border-radius: 99px; }
.tabbar { position: absolute; left: 50%; bottom: 14px; translate: -50% 0; display: flex; align-items: center; gap: 4px; padding: 5px; border-radius: 99px; background: #fff; box-shadow: 0 10px 26px -10px rgba(0,0,0,.3), inset 0 0 0 1px #E6E6E8; white-space: nowrap; }
.tabbar span { display: inline-flex; align-items: center; gap: 6px; height: 34px; padding: 0 14px; border-radius: 99px; font-size: 12px; color: #5E5E63; }
.tabbar .on { background: #F1F1F2; color: #1C1C1E; }
.tabbar .add { width: 34px; padding: 0; justify-content: center; background: #1C1C1E; color: #fff; }
.tabbar.bulk { background: #1C1C1E; box-shadow: 0 10px 26px -10px rgba(0,0,0,.5); }
.tabbar.bulk b { color: #fff; font-weight: 500; font-size: 12px; padding: 0 12px 0 14px; }
.tabbar.bulk span { color: #fff; background: rgba(255,255,255,.1); }
.tabbar.bulk .x { width: 34px; padding: 0; justify-content: center; background: transparent; }

/* list view */
.lhead, .lr { display: grid; grid-template-columns: 26px 34px 1.6fr 1fr 1fr 120px; gap: 10px; align-items: center; }
.lhead { margin-top: 14px; padding: 0 12px 8px; font-size: 10.5px; color: #8A8A90; text-transform: uppercase; letter-spacing: .4px; }
.lrows { display: grid; gap: 6px; }
.lr { background: #fff; border-radius: 14px; padding: 8px 12px; font-size: 12px; color: #3A3A3E; }
.lr.sel { background: #E9E9EC; box-shadow: inset 0 0 0 1px #D2D2D6; }
.tk { width: 20px; height: 20px; border-radius: 50%; box-shadow: inset 0 0 0 1.5px #C9C9CE; display: grid; place-items: center; }
.lr.sel .tk { background: #1C1C1E; box-shadow: none; color: #fff; } .tk .i { width: 12px; height: 12px; stroke-width: 2.4; }
.tk.all { background: #1C1C1E; box-shadow: none; position: relative; } .tk.all::after { content: ""; width: 9px; height: 2px; background: #fff; border-radius: 2px; }
.lr-n b { display: block; font-size: 13px; font-weight: 500; color: #1C1C1E; } .lr-n small { font-size: 10.5px; color: #8A8A90; }
.st-pill { justify-self: start; display: inline-flex; align-items: center; gap: 6px; height: 24px; padding: 0 10px; border-radius: 99px; background: #F4F4F5; font-size: 11px; color: #1C1C1E; }

/* detail window */
.dw { position: relative; background: #F1F1F2; border-radius: 20px; padding: 16px; display: flex; flex-direction: column; min-height: 0; overflow: hidden; }
.dw-hd { display: flex; align-items: center; gap: 6px; }
.chip { display: inline-flex; align-items: center; gap: 6px; height: 26px; padding: 0 10px; border-radius: 99px; background: #fff; font-size: 11px; color: #3A3A3E; }
.chip .i { width: 12px; height: 12px; }
.dw-r { margin-left: auto; display: flex; gap: 6px; }
.dw h5 { margin: 14px 0 0; font-size: 24px; font-weight: 500; letter-spacing: -.8px; }
.dw-sub { margin: 6px 0 0; display: flex; align-items: center; gap: 8px; font-size: 12.5px; color: #5E5E63; } .dw-sub i { font-style: normal; }
.key { margin-top: 14px; background: #fff; border-radius: 16px; padding: 14px; display: flex; gap: 14px; align-items: center; }
.mini-ring { position: relative; width: 80px; height: 80px; flex: none; }
.mini-ring svg { width: 100%; height: 100%; transform: rotate(-90deg); }
.mini-ring .tr { fill: none; stroke: #EDEDEF; stroke-width: 7; }
.mini-ring .pr { fill: none; stroke: #C98A1B; stroke-width: 7; stroke-linecap: round; stroke-dasharray: 201; stroke-dashoffset: calc(201 - 201 * var(--p) / 100); }
.mini-ring span { position: absolute; inset: 0; display: grid; place-content: center; text-align: center; }
.mini-ring b { font-size: 22px; font-weight: 500; line-height: 1; } .mini-ring small { font-size: 9.5px; color: #8A8A90; }
.key-r p { margin: 0; font-size: 12px; line-height: 1.45; color: #3A3A3E; font-weight: 400; } .key-r p b { font-weight: 500; color: #1C1C1E; }
.key-b { display: flex; gap: 6px; margin-top: 10px; }
.btn-d, .btn-l { display: inline-flex; align-items: center; justify-content: center; gap: 6px; height: 32px; padding: 0 14px; border-radius: 99px; font-size: 12px; }
.btn-d { background: #1C1C1E; color: #fff; } .btn-l { background: #F1F1F2; color: #1C1C1E; }
.btn-d .i, .btn-l .i { width: 13px; height: 13px; }
.facts { margin-top: 10px; display: grid; grid-template-columns: 1fr 1fr; gap: 8px; }
.facts div { background: #fff; border-radius: 12px; padding: 9px 12px; }
.facts small { display: block; font-size: 10px; color: #8A8A90; } .facts b { font-size: 12.5px; font-weight: 500; }
.dtabs { margin-top: 14px; display: flex; gap: 4px; padding: 3px; border-radius: 99px; background: #E4E4E7; }
.dtabs span { flex: 1; text-align: center; height: 28px; line-height: 28px; border-radius: 99px; font-size: 11.5px; color: #5E5E63; }
.dtabs .on { background: #fff; color: #1C1C1E; box-shadow: 0 1px 2px rgba(0,0,0,.08); }
.dtabs em { font-style: normal; font-size: 10px; color: #8A8A90; margin-left: 2px; }
.acts { margin-top: 10px; display: grid; gap: 10px; }
.act { display: flex; gap: 10px; align-items: start; }
.act p { margin: 0; font-size: 12px; color: #3A3A3E; font-weight: 400; line-height: 1.35; } .act p b { font-weight: 500; color: #1C1C1E; }
.act small { display: block; font-size: 10.5px; color: #8A8A90; margin-top: 1px; }
.cmt { margin-top: auto; display: flex; align-items: center; justify-content: space-between; height: 38px; padding: 0 6px 0 14px; border-radius: 99px; background: #fff; font-size: 12px; color: #8A8A90; }
.cmt .i { width: 26px; height: 26px; padding: 6px; border-radius: 50%; background: #1C1C1E; color: #fff; }

/* slide-in edit panel */
.scrim { position: absolute; inset: 0; border-radius: 20px; background: rgba(28,28,30,.18); z-index: 10; }
.si { position: absolute; z-index: 20; top: 0; right: 0; bottom: 0; width: 420px; background: #fff; border-radius: 20px; box-shadow: -20px 0 50px -20px rgba(0,0,0,.35); padding: 16px 18px; display: flex; flex-direction: column; }
.si-hd { display: flex; align-items: center; gap: 10px; } .si-hd b { font-size: 17px; font-weight: 500; }
.draft { margin-left: auto; font-size: 11px; color: #2F8F5B; display: inline-flex; align-items: center; gap: 5px; }
.draft::before { content: ""; width: 6px; height: 6px; border-radius: 50%; background: #2F8F5B; }
.fields { margin-top: 16px; display: grid; gap: 12px; }
.fields label { display: grid; gap: 5px; } .fields small { font-size: 11px; color: #5E5E63; }
.inp { display: flex; align-items: center; gap: 8px; height: 40px; padding: 0 12px; border-radius: 12px; background: #F4F4F5; font-size: 13px; }
.inp .i:last-child { margin-left: auto; color: #8A8A90; }
.inp.area { height: 58px; align-items: start; padding-top: 10px; }
.two { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
.bad .inp { box-shadow: inset 0 0 0 1.5px #C2413A; background: #FDF3F2; }
.bad em { font-style: normal; font-size: 10.5px; color: #C2413A; }
.drop { display: flex; align-items: center; gap: 10px; height: 58px; padding: 0 14px; border-radius: 12px; border: 1.5px dashed #CFCFD3; font-size: 12px; color: #5E5E63; }
.si-ft { margin-top: auto; display: flex; justify-content: flex-end; gap: 8px; padding-top: 12px; border-top: 1px solid #EDEDEF; }
.si-ft .btn-d, .si-ft .btn-l { height: 38px; padding: 0 18px; font-size: 13px; }

/* explanation below */
.legend { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; margin-top: 18px; }
.lg-i { display: flex; gap: 12px; background: #fff; border-radius: 16px; padding: 14px 16px; }
.lg-i .mk { position: static; flex: none; box-shadow: none; }
.lg-i b { display: block; font-weight: 500; font-size: 15px; } .lg-i p { margin: 3px 0 0; font-size: 13.5px; line-height: 1.5; color: #4A4A4F; }
.tbl-wrap { overflow-x: auto; background: #fff; border-radius: 16px; margin-top: 14px; }
table { width: 100%; border-collapse: collapse; font-size: 13.5px; min-width: 860px; }
th, td { text-align: left; padding: 11px 14px; border-bottom: 1px solid #EDEDEF; vertical-align: top; }
th { font-weight: 500; font-size: 12px; color: #6B6B70; background: #F7F7F8; }
tr:last-child td { border-bottom: 0; } td:first-child { font-weight: 500; }
.rules { margin: 14px 0 0; padding: 0; list-style: none; display: grid; gap: 8px; }
.rules li { background: #fff; border-radius: 14px; padding: 12px 16px; font-size: 14px; line-height: 1.5; color: #3A3A3E; }
.rules b { font-weight: 500; color: #1C1C1E; }
@media (max-width: 760px) { .legend { grid-template-columns: 1fr; } h1 { font-size: 24px; } body { padding: 20px 12px 48px; } }
"""

JS = """
document.querySelectorAll('.fit').forEach(f => {
  const p = f.firstElementChild;
  const set = () => p.style.setProperty('--s', f.clientWidth / 1280);
  set(); addEventListener('resize', set);
  if ('ResizeObserver' in window) new ResizeObserver(set).observe(f);
});
"""

html = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Luex Module Template</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500&display=swap">
<style>{CSS}</style></head><body>
<div class="wrap">
  <h1>Luex module template</h1>
  <p class="lead">One page layout for every module except the Dashboard. Modules only change what goes in the boxes, never the boxes themselves. Shown with Compliance as the example. Colours come later; status colours (green, amber, red) only ever mean status.</p>

  <h2>1. A record open</h2>
  <p class="lead">Tap a status tile to filter. Tap a card and its details open on the right, with the one thing to do next at the top.</p>
  <div class="frame">{frame("open")}</div>
  <div class="legend">{"".join(f'<div class="lg-i"><span class="mk">{n}</span><div><b>{h}</b><p>{t}</p></div></div>' for n, h, t in LEGEND)}</div>

  <h2>2. Editing or adding</h2>
  <p class="lead">Edit (the pencil) or the + opens the form as a panel from the right, over the detail window. Mistakes show next to the field as you type. A draft saves automatically.</p>
  <div class="frame">{frame("edit")}</div>

  <h2>3. List view with bulk select</h2>
  <p class="lead">The same records as a compact list. Tick a few and the tab bar turns into the bulk bar.</p>
  <div class="frame">{frame("list")}</div>

  <h2>How each module fills the boxes</h2>
  <p class="lead">Every module provides these five things and nothing else changes.</p>
  <div class="tbl-wrap"><table><thead><tr><th>Module</th><th>Status tiles</th><th>Each card shows</th><th>Main action in detail</th><th>View tabs</th></tr></thead>
  <tbody>{"".join(f'<tr><td>{a}</td><td>{b}</td><td>{c}</td><td>{d}</td><td>{e}</td></tr>' for a, b, c, d, e in MODULES)}</tbody></table></div>

  <h2>Rules that keep every module the same</h2>
  <ul class="rules">
    <li><b>Nothing is ever empty.</b> No records shows a short line and a button to add the first one; nothing selected shows a summary of the current filter in the detail window.</li>
    <li><b>Buttons only appear if you can use them.</b> Someone who can't approve never sees Approve.</li>
    <li><b>Everything has its own link.</b> The chosen tile, filters, view and open record are in the address, so Back, bookmarks and notification links land in the exact spot.</li>
    <li><b>Open and selected look different.</b> The open record has a dark outline; ticked records are shaded with a tick.</li>
    <li><b>Tablet:</b> the detail window slides over from the right. <b>Phone:</b> tiles become a 2 by 2 grid, the records fill the screen, and a record opens full screen with a back button.</li>
  </ul>
</div>
<script>{JS}</script>
</body></html>"""

out = pathlib.Path(__file__).with_name("app-module.html")
out.write_text(html)
print("wrote", out, len(html))

# =============================================================== AI panel options (second page)
P["spark"] = '<path d="M12 3.5l1.8 4.9 4.9 1.8-4.9 1.8L12 16.9l-1.8-4.9-4.9-1.8 4.9-1.8z"/><path d="M18.5 15.5l.8 2 2 .8-2 .8-.8 2-.8-2-2-.8 2-.8z"/>'
P["min"] = '<path d="M6 12h12"/>'
P["send"] = '<path d="M5 12l14-7-5 14-2.5-5.5z"/>'
P["arrow"] = '<path d="M5 12h13M13 7l5 5-5 5"/>'

def header_ai(ask_pill):
    pill = f'<span class="ask">{ic("spark")}Ask Luex</span>' if ask_pill else ""
    return f'''<header class="m-hd">
      <div class="m-title"><small>Safety and quality <i>·</i> Compliance</small>
        <div class="tl"><h4>Compliance</h4><span class="pill">{ic("cal")}All sites {ic("down")}</span></div></div>
      <div class="m-act">
        <span class="pill srch">{ic("search")}Search everything<kbd>Ctrl K</kbd></span>
        {pill}
        <span class="rnd dark">{ic("plus")}</span>
        <span class="rnd">{ic("inbox")}<em class="cnt">5</em></span>
        <span class="rnd">{ic("bell")}<i class="dotr"></i></span>
        <span class="user"><span class="av">CM</span><span><b>Ciara Murphy</b><small>Operations manager</small></span>{ic("down")}</span>
      </div></header>'''

def detail_glow():
    return detail(False).replace('<span class="btn-d">', '<span class="btn-d glow">', 1)

def ai_panel(closable):
    btns = f'<span class="rnd sm">{ic("min")}</span>' if closable else '<span class="pin">Always on</span>'
    return f'''<aside class="ai">
      <div class="ai-hd"><span class="ai-logo">{ic("spark")}</span><span><b>Ask Luex</b><small>Help and how-to</small></span>{btns}</div>
      <div class="ai-msgs">
        <div class="q">How do I renew Seán's CSCS card?</div>
        <div class="a"><p>You're already in the right place. Renewing takes three steps:</p>
          <ol><li class="done"><span>Open <b>Compliance</b> and find Seán's CSCS card.</span></li>
              <li class="now"><span>Press <b>Renew</b> at the top of the details. I've highlighted it.</span></li>
              <li><span>Add the new expiry date and a photo of the card, then <b>Save</b>.</span></li></ol>
          <span class="go">{ic("arrow")}Compliance › CSCS card, Seán Byrne</span>
          <small class="src">From the help article "Renewing a certificate"</small></div>
        <div class="q">Will it stop him being booked on shifts?</div>
        <div class="a"><p>Yes. Once it expires, Seán can't be put on a shift until it's renewed. You'll see a red "blocked" mark in <b>Scheduling</b>.</p>
          <span class="go">{ic("arrow")}Scheduling › Week of 2 Feb</span></div>
      </div>
      <div class="sugg"><span>Where do I add a new site?</span><span>Who can see medical certificates?</span></div>
      <div class="ai-in"><span>Ask anything about Luex</span><span class="snd">{ic("send")}</span></div>
    </aside>'''

def guide_bar():
    return f'''<div class="guide">
      <span class="ai-logo sm">{ic("spark")}</span>
      <span class="g-step">Step 2 of 3</span>
      <span class="g-dots"><i class="d"></i><i class="n"></i><i></i></span>
      <p>Press <b>Renew</b> at the top of the details. It's glowing.</p>
      <span class="btn-l">{ic("back")}Back</span><span class="btn-d">Next {ic("chev")}</span><span class="btn-l">{ic("spark")}Open chat</span><span class="rnd sm">{ic("x")}</span>
    </div>'''

def ai_frame(kind):
    if kind == "always":
        main = f'''<div class="m-main ai-on">{header_ai(False)}{tiles(2, False)}
          <div class="m-body narrow">{main_window("listplain", False)}{detail_glow()}</div>{ai_panel(False)}</div>'''
    elif kind == "closed":
        main = f'''<div class="m-main">{header_ai(True)}{tiles(2, False)}<div class="m-body">{main_window("listplain", False)}{detail(False)}</div></div>'''
    else:
        main = f'''<div class="m-main guide-on">{header_ai(True)}{guide_bar()}{tiles(2, False)}<div class="m-body">{main_window("listplain", False)}{detail_glow()}</div></div>'''
    return f'<div class="fit"><div class="m-page">{rail()}{main}</div></div>'

AI_CSS = """
.m-main.ai-on { grid-template-columns: 1fr 318px; grid-template-rows: 54px 86px 1fr; column-gap: 10px; }
.m-main.ai-on > .m-hd { grid-column: 1 / -1; }
.m-main.ai-on > .tiles { grid-column: 1; grid-row: 2; }
.m-main.ai-on > .m-body { grid-column: 1; grid-row: 3; }
.m-main.ai-on > .ai { grid-column: 2; grid-row: 2 / 4; }
.m-main.ai-on .tile small { display: none; }
.m-main.ai-on .tile b { font-size: 26px; }
.m-body.narrow { grid-template-columns: 1fr 330px; }
.cards.two { grid-template-columns: repeat(2, 1fr); }
.lr.open { box-shadow: 0 0 0 2px #1C1C1E; }
.m-body.narrow .lhead, .m-body.narrow .lr { grid-template-columns: 22px 30px 1.5fr 1fr 104px; }
.m-body.narrow .lr-s, .m-body.narrow .lhead span:nth-child(4) { display: none; }
.m-body.narrow .mw-tools .pill:nth-of-type(n+3) { display: none; }
.m-body.narrow .srch2 { width: 150px; }
.m-main.guide-on { grid-template-rows: 54px 46px 86px 1fr; }
.ask { display: inline-flex; align-items: center; gap: 7px; height: 38px; padding: 0 14px 0 12px; border-radius: 99px; background: #fff; box-shadow: inset 0 0 0 1.5px #1C1C1E; font-size: 12.5px; font-weight: 500; }
.ask .i { width: 15px; height: 15px; }
.ai { background: #fff; border-radius: 20px; box-shadow: inset 0 0 0 1px #E6E6E8; padding: 14px; display: flex; flex-direction: column; min-height: 0; overflow: hidden; }
.ai-hd { display: flex; align-items: center; gap: 10px; padding-bottom: 12px; border-bottom: 1px solid #EDEDEF; }
.ai-hd b { display: block; font-size: 14px; font-weight: 500; } .ai-hd small { font-size: 10.5px; color: #8A8A90; }
.ai-hd > :last-child { margin-left: auto; }
.pin { font-size: 10.5px; padding: 4px 9px; border-radius: 99px; background: #F1F1F2; color: #5E5E63; }
.ai-logo { width: 34px; height: 34px; border-radius: 11px; background: #1C1C1E; color: #CFB783; display: grid; place-items: center; flex: none; }
.ai-logo.sm { width: 28px; height: 28px; border-radius: 9px; } .ai-logo .i { width: 16px; height: 16px; }
.ai-msgs { flex: 1; min-height: 0; overflow: hidden; display: flex; flex-direction: column; gap: 10px; padding-top: 12px; }
.q { align-self: flex-end; max-width: 86%; background: #1C1C1E; color: #fff; padding: 9px 12px; border-radius: 14px 14px 4px 14px; font-size: 12px; line-height: 1.4; }
.a { align-self: flex-start; max-width: 96%; background: #F1F1F2; padding: 10px 12px; border-radius: 14px 14px 14px 4px; font-size: 12px; line-height: 1.45; color: #2A2A2E; }
.a p { margin: 0; font-weight: 400; } .a b { font-weight: 500; }
.a ol { margin: 8px 0 0; padding-left: 0; list-style: none; counter-reset: s; display: grid; gap: 6px; }
.a li { counter-increment: s; display: grid; grid-template-columns: 20px 1fr; gap: 8px; align-items: start; }
.a li::before { content: counter(s); width: 20px; height: 20px; border-radius: 50%; background: #fff; display: grid; place-items: center; font-size: 10.5px; box-shadow: inset 0 0 0 1px #D9D9DC; }
.a li.done::before { content: "✓"; background: #2F8F5B; color: #fff; box-shadow: none; }
.a li.now::before { background: #1C1C1E; color: #fff; box-shadow: none; }
.go { margin-top: 9px; display: inline-flex; align-items: center; gap: 6px; padding: 6px 10px; border-radius: 99px; background: #fff; font-size: 11px; font-weight: 500; box-shadow: inset 0 0 0 1px #E2E2E5; }
.go .i { width: 13px; height: 13px; }
.src { display: block; margin-top: 7px; font-size: 10px; color: #8A8A90; }
.sugg { display: flex; flex-wrap: wrap; gap: 6px; padding: 10px 0; }
.sugg span { font-size: 10.5px; padding: 6px 10px; border-radius: 99px; background: #F1F1F2; color: #3A3A3E; }
.ai-in { display: flex; align-items: center; justify-content: space-between; height: 42px; padding: 0 5px 0 14px; border-radius: 99px; background: #F1F1F2; font-size: 12px; color: #8A8A90; }
.snd { width: 32px; height: 32px; border-radius: 50%; background: #1C1C1E; color: #fff; display: grid; place-items: center; }
.snd .i { width: 14px; height: 14px; }
.glow { position: relative; box-shadow: 0 0 0 3px #fff, 0 0 0 6px #CFB783, 0 0 22px 6px rgba(207,183,131,.75); animation: pulse 1.6s ease-in-out infinite; }
@keyframes pulse { 50% { box-shadow: 0 0 0 3px #fff, 0 0 0 6px #CFB783, 0 0 34px 12px rgba(207,183,131,.45); } }
.guide { display: flex; align-items: center; gap: 10px; padding: 0 6px 0 7px; border-radius: 99px; background: #1C1C1E; color: #fff; }
.guide .g-step { font-size: 11px; color: #CFB783; letter-spacing: .3px; text-transform: uppercase; }
.g-dots { display: flex; gap: 4px; } .g-dots i { width: 7px; height: 7px; border-radius: 50%; background: rgba(255,255,255,.25); }
.g-dots .d { background: #2F8F5B; } .g-dots .n { background: #fff; width: 18px; border-radius: 99px; }
.guide p { margin: 0 auto 0 6px; font-size: 13px; font-weight: 400; } .guide p b { font-weight: 500; }
.guide .btn-l { background: rgba(255,255,255,.12); color: #fff; height: 32px; }
.guide .btn-d { background: #fff; color: #1C1C1E; height: 32px; }
.guide .rnd.sm { background: transparent; box-shadow: none; color: #fff; }
.cmp { width: 100%; border-collapse: collapse; font-size: 14px; background: #fff; border-radius: 16px; overflow: hidden; }
.cmp th, .cmp td { padding: 12px 16px; border-bottom: 1px solid #EDEDEF; text-align: left; vertical-align: top; }
.cmp th { background: #F7F7F8; font-weight: 500; font-size: 12.5px; color: #5E5E63; }
.cmp tr:last-child td { border-bottom: 0; } .cmp td:first-child { font-weight: 500; width: 22%; }
"""

page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Ask Luex Options</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500&display=swap">
<style>{CSS}{AI_CSS}</style></head><body>
<div class="wrap">
  <h1>Where the AI help lives: two options</h1>
  <p class="lead">In both, the AI is part of the frame like the nav and header. It never reloads, keeps the conversation as you move between modules, and never covers the records or the detail window. The thing it's pointing at glows.</p>

  <h2>Option A: a dedicated spot, always on</h2>
  <p class="lead">A fixed column on the right, always showing. The records list gives up the space: the Site column and some filters hide to make room.</p>
  <div class="frame">{ai_frame("always")}</div>

  <h2>Option B: there when you want it</h2>
  <p class="lead">Closed, the page uses the full width and an "Ask Luex" button sits in the header. Open, it looks exactly like Option A. When you follow its steps, it folds into this guide bar:</p>
  <div class="frame">{ai_frame("closed")}</div>
  <p class="lead" style="margin-top:22px">Following steps: a one-line guide under the header, with Back, Next and "Open chat" to unfold the conversation again.</p>
  <div class="frame">{ai_frame("guide")}</div>

  <h2>Side by side</h2>
  <table class="cmp"><thead><tr><th></th><th>A: always on</th><th>B: open when needed</th></tr></thead><tbody>
    <tr><td>Always visible</td><td>Yes, all the time</td><td>Chat or guide bar while in use; a button when closed</td></tr>
    <tr><td>Space for records</td><td>Always about a quarter narrower</td><td>Full width most of the day</td></tr>
    <tr><td>Following instructions</td><td>Chat and glowing button side by side</td><td>Guide bar plus glowing button, with the full page visible</td></tr>
    <tr><td>Smaller laptops</td><td>Tight: records drop to list view</td><td>Fine when closed</td></tr>
    <tr><td>Phone</td><td>Can't be always on; becomes a sheet</td><td>Sheet, then the guide bar</td></tr>
  </tbody></table>
</div>
<script>{JS}</script>
</body></html>"""
pathlib.Path(__file__).with_name("app-ai-options.html").write_text(page)
print("wrote app-ai-options.html", len(page))
