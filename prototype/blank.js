const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

/* menu + launch countdown */
const menuBtn = document.getElementById('menuBtn');
menuBtn.onclick = () => { const o = document.body.classList.toggle('open'); menuBtn.setAttribute('aria-expanded', o); };
document.querySelectorAll('#drop a').forEach(a => a.onclick = () => document.body.classList.remove('open'));
const launch = new Date('2027-01-15T09:00:00Z');
function tick() {
  let s = Math.max(0, Math.floor((launch - Date.now()) / 1000));
  const v = [Math.floor(s / 86400), Math.floor(s % 86400 / 3600), Math.floor(s % 3600 / 60), s % 60];
  document.querySelectorAll('#cd b').forEach((b, i) => b.textContent = String(v[i]).padStart(2, '0'));
}
tick(); setInterval(tick, 1000);

/* word-by-word heading reveal */
document.querySelectorAll('.split').forEach(el => {
  const walk = n => [...n.childNodes].forEach(c => {
    if (c.nodeType === 3) {
      const f = document.createDocumentFragment();
      c.textContent.split(/(\s+)/).forEach(t => { if (!t) return; if (/^\s+$/.test(t)) f.append(t); else { const s = document.createElement('span'); s.className = 'w'; s.textContent = t; f.append(s); } });
      c.replaceWith(f);
    } else if (c.nodeType === 1 && !c.classList.contains('w')) { if (c.matches('em, .dot')) c.classList.add('w'); else walk(c); }
  });
  walk(el);
  el.querySelectorAll('.w').forEach((w, i) => w.style.transitionDelay = (i * 70) + 'ms');
});

/* odometers roll to their value when seen */
function setOdo(el, on) {
  el.querySelectorAll('.d').forEach((d, i) => {
    const v = on ? +d.dataset.v : 0;
    d.firstElementChild.style.transitionDelay = (i * 90) + 'ms';
    d.firstElementChild.style.transform = `translateY(${-v * 10}%)`;
  });
}
document.querySelectorAll('.odo').forEach(o => setOdo(o, reduce));

const io = new IntersectionObserver(es => es.forEach(e => {
  if (!e.isIntersecting) return;
  if (e.target.classList.contains('odo')) setOdo(e.target, true); else e.target.classList.add('shown');
  io.unobserve(e.target);
}), { threshold: .3 });
document.querySelectorAll('.split, .odo').forEach(el => io.observe(el));

/* parallax: hero content drifts up, Hello heading drifts down */
const heroBg = document.getElementById('heroBg'), heroIn = document.getElementById('heroIn'), helloH = document.getElementById('helloH'), hello = document.getElementById('hello');
function onScroll() {
  if (reduce || !heroIn) return;
  heroIn.style.transform = `translateY(${-0.36 * Math.min(scrollY, 1200)}px)`;
  if (heroBg) heroBg.style.opacity = Math.max(0, 1 - scrollY / 450);
  if (!hello) return;
  const r = hello.getBoundingClientRect();
  helloH.style.transform = `translateY(${0.3 * Math.max(0, Math.min(innerHeight, -r.top))}px)`;
}
addEventListener('scroll', onScroll, { passive: true }); onScroll();

/* capabilities carousel: centred slide, auto-advance every 5s */
const rail = document.getElementById('rail'), dots = document.getElementById('dots'), caps = document.querySelector('.caps');
const N = rail.children.length;
for (let i = 0; i < N; i++) { const b = document.createElement('button'); b.type = 'button'; b.setAttribute('aria-label', 'Slide ' + (i + 1)); b.onclick = () => { go(i); restart(); }; dots.appendChild(b); }
let cur = 0, timer, playing = !reduce;
function go(i) {
  cur = (i + N) % N;
  const sw = rail.children[0].offsetWidth, gap = parseFloat(getComputedStyle(rail).gap);
  rail.style.transform = `translateX(${innerWidth / 2 - sw / 2 - cur * (sw + gap)}px)`;
  [...dots.children].forEach((d, k) => d.classList.toggle('on', k === cur));
  const on = dots.children[cur]; on.classList.remove('on'); void on.offsetWidth; on.classList.add('on');
}
function restart() { clearInterval(timer); if (playing) timer = setInterval(() => go(cur + 1), 5000); }
document.getElementById('pause').onclick = () => {
  playing = !playing; caps.classList.toggle('paused', !playing);
  document.getElementById('pauseIcon').innerHTML = playing ? '<rect x="6" y="5" width="3" height="11" rx="1"/><rect x="12" y="5" width="3" height="11" rx="1"/>' : '<path d="M7 5l9 5.5L7 16z"/>';
  restart();
};
if (!playing) caps.classList.add('paused');
go(0); restart(); addEventListener('resize', () => go(cur));

/* accordions: one open at a time per list */
document.querySelectorAll('.acc').forEach(list => list.addEventListener('click', e => {
  const q = e.target.closest('.acc-q'); if (!q) return;
  const item = q.parentElement, was = item.classList.contains('open');
  list.querySelectorAll('.acc-i').forEach(i => i.classList.remove('open'));
  if (!was) item.classList.add('open');
}));

/* material thumbnails */
document.querySelectorAll('.th').forEach(t => t.onclick = () => { document.querySelectorAll('.th').forEach(x => x.classList.remove('on')); t.classList.add('on'); });
