/* =====================================================================
   Portfolio — Md Shahed Uddin Emon
   ===================================================================== */
'use strict';

const REDUCE_MOTION = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ----------------------------- DATA ----------------------------- */
const ASSET = (slug, file) => `assets/projects/${slug}/${file}`;

const PROJECTS = [
  {
    slug: 'sds-manager', name: 'SDS Manager', type: 'apps', featured: true,
    cat: 'Productivity · Enterprise', rating: '5.0', reviews: 5,
    tagline: 'Offline-first SDS access for field teams',
    desc: 'Mobile companion for SDS Manager. Gives field teams full offline access to their Safety Data Sheet library — barcode/QR scanning, instant first-aid & hazard info — even with zero connectivity.',
    tech: ['Flutter', 'Dart', 'Riverpod', 'Offline Sync', 'QR / Barcode'],
    shots: ['shot-1.webp','shot-2.webp','shot-3.webp','shot-4.webp','shot-5.webp','shot-6.webp','play-shot-1.webp','play-shot-2.webp','play-shot-3.webp','play-shot-4.webp','play-shot-5.webp','play-shot-6.webp'],
    primary: 'play-shot-2.webp',
    links: { appstore: 'https://apps.apple.com/us/app/sds-manager/id6754279703', play: 'https://play.google.com/store/apps/details?id=com.sdsmanager.mainapp' },
  },
  {
    slug: 'invoice-matrix', name: 'Invoice Matrix', type: 'apps', featured: true,
    cat: 'Business · Finance', rating: '4.4', reviews: 14,
    tagline: 'Professional PDF invoices in minutes',
    desc: 'Invoicing & billing app for freelancers and small businesses — create polished PDF invoices, track billing history, automate recurring invoices, get overdue alerts, with secure cloud storage.',
    tech: ['Flutter', 'Dart', 'Firebase', 'PDF Gen', 'RevenueCat'],
    shots: ['shot-1.webp','shot-2.webp','shot-3.webp','shot-4.webp','shot-5.webp','shot-6.webp'],
    links: { appstore: 'https://apps.apple.com/us/app/invoice-matrix-pdf-invoices/id6742684220' },
  },
  {
    slug: 'paraphrase-ai', name: 'Paraphrase AI', type: 'apps', featured: true,
    cat: 'Productivity · AI', rating: '4.3', reviews: 29,
    tagline: 'AI rewriter & humanizer, 185+ languages',
    desc: 'AI-powered paraphrasing app: reword, rewrite and humanize text with 25+ modes across 185+ languages, plus grammar correction and history. Fast, natural-sounding results.',
    tech: ['React Native', 'TypeScript', 'LLM API', 'Firebase', 'RevenueCat'],
    shots: ['shot-1.webp','shot-2.webp','shot-3.webp','shot-4.webp','shot-5.webp','shot-6.webp'],
    links: { appstore: 'https://apps.apple.com/us/app/paraphrase-ai-smart-humanizer/id6746731727' },
  },
  {
    slug: 'note-genie', name: 'Note Genie', type: 'apps', featured: true,
    cat: 'Education · AI', rating: '5.0', reviews: 1,
    tagline: 'AI note taker: audio, video & text → notes',
    desc: 'Turns lectures, meetings, PDFs and YouTube videos into organized notes, summaries, quizzes and flashcards — with an AI chat that answers questions over your own notes.',
    tech: ['React Native', 'TypeScript', 'AI Transcription', 'Firebase', 'RevenueCat'],
    shots: ['shot-1.webp','shot-2.webp','shot-3.webp','shot-4.webp','shot-5.webp','shot-6.webp'],
    links: { appstore: 'https://apps.apple.com/us/app/lecture-note-taker-note-genie/id6748276655' },
  },
  {
    slug: 'ostad', name: 'Ostad', type: 'apps',
    cat: 'Education · Live Learning', rating: '4.7', reviews: 450,
    tagline: 'Live skill-development bootcamp platform',
    desc: "Multi-platform live-learning app for Bangladesh's leading ed-tech bootcamp — real-time streamed classes, a task-based curriculum, mentor feedback and job-placement tools. Built from scratch, serving 20,000+ learners across iOS, Android, macOS, Windows & Linux.",
    tech: ['Flutter', 'Dart', 'Live Streaming', 'GetX', 'Mixpanel', 'Sentry'],
    shots: ['shot-1.webp','shot-2.webp','shot-3.webp','shot-4.webp','shot-5.webp','shot-6.webp'],
    links: { appstore: 'https://apps.apple.com/us/app/ostad-app/id6446163017', play: 'https://play.google.com/store/apps/details?id=com.ostad.app', web: 'https://ostad.app', windows: 'https://cutt.ly/Fr3QsjFo' },
  },
  {
    slug: 'quran-shikkha', name: 'Quran Shikkha', type: 'apps',
    cat: 'Education',
    tagline: 'Learn the Quran online, in Bengali',
    desc: 'Ed-tech app for learning proper Quran reading and recitation (Tajweed) online, with structured Bengali courses and in-app enrollment & payment. Built with Flutter.',
    tech: ['Flutter', 'Dart', 'SSLCommerz', 'REST'],
    shots: ['play-shot-1.webp','play-shot-2.webp','play-shot-3.webp','play-shot-4.webp','play-shot-5.webp','play-shot-6.webp','play-shot-7.webp'],
    links: { play: 'https://play.google.com/store/apps/details?id=com.quranshikkha.app' },
  },
  {
    slug: 'capito-basic', name: 'Capito Basic', type: 'apps',
    cat: 'Clinical · Cognitive',
    tagline: 'Cognitive & attention testing',
    desc: 'Clinical cognitive-assessment tool — CAPITO stands for Cognitive & Psychophysiological Test Operations — measuring attention, reaction time and impulse control for neurofeedback clinicians. Built for IFEN, Germany.',
    tech: ['Flutter', 'Dart', 'Precise Timing', 'Charts', 'EN / DE'],
    shots: ['shot-1.webp','shot-2.webp','shot-3.webp','shot-4.webp','shot-5.webp','shot-6.webp'],
    links: { appstore: 'https://apps.apple.com/us/app/capito-basic-by-ifen/id1550991580' },
  },
  {
    slug: 'capito-xpert', name: 'Capito Xpert', type: 'apps',
    cat: 'Clinical · Cognitive',
    tagline: 'Advanced assessment + Stroop tests',
    desc: 'The advanced Capito edition — Stroop tests (arrow & colour-word), trend graphs for timing/errors/SD, adjustable difficulty and ~2-minute sessions clinicians use to document treatment progress.',
    tech: ['Flutter', 'Dart', 'Data Viz', 'Stroop Test', 'EN / DE'],
    shots: ['shot-1.webp','shot-2.webp','shot-3.webp','shot-4.webp','shot-5.webp','shot-6.webp'],
    links: { appstore: 'https://apps.apple.com/us/app/capito-xpert-by-ifen/id1550994819', play: 'https://play.google.com/store/apps/details?id=com.ifen.capitoxpert' },
  },
  {
    slug: 'ifen-learning-portal', name: 'IFEN Learning Portal', type: 'apps',
    cat: 'Education',
    tagline: 'Neurofeedback training & certification',
    desc: "Course-delivery app bringing IFEN's neurofeedback training and certification materials to clinicians and trainees worldwide.",
    tech: ['Flutter', 'Dart', 'Content Delivery', 'Auth'],
    shots: ['shot-1.webp','shot-2.webp','shot-3.webp','shot-4.webp','shot-5.webp','shot-6.webp'],
    links: { appstore: 'https://apps.apple.com/us/app/ifen-learning-portal/id1547252500', play: 'https://play.google.com/store/apps/details?id=com.ifen.neurofeedback_academy' },
  },
  {
    slug: 'ifen-symptom-tracker', name: 'IFEN Symptom Tracker', type: 'apps',
    cat: 'Health & Fitness',
    tagline: 'Track symptoms across categories',
    desc: 'Patient & clinician tool for logging and monitoring symptoms across cognitive, emotional, physical, behavioural and nutritional categories — bilingual EN/DE — complementing neurofeedback treatment.',
    tech: ['Flutter', 'Dart', 'Charts', 'EN / DE'],
    shots: ['shot-1.webp','shot-2.webp','shot-3.webp','shot-4.webp','shot-5.webp','shot-6.webp'],
    links: { appstore: 'https://apps.apple.com/us/app/ifen-symptom-tracker/id6503682705', play: 'https://play.google.com/store/apps/details?id=com.ifen.symptom_tracker' },
  },
  {
    slug: 'watcher', name: 'Watcher', type: 'oss',
    cat: 'Open Source · Flutter',
    tagline: 'Cross-platform movie & TV browser',
    desc: 'A Flutter app for discovering movies & TV series via the TMDB API — showcasing GetX for state, routing and DI across mobile, tablet and web, with light/dark themes and onboarding.',
    tech: ['Flutter', 'Dart', 'GetX', 'TMDB API', 'Responsive'],
    shots: ['shot-1.webp', 'shot-2.webp', 'shot-3.webp', 'shot-4.webp', 'shot-5.webp'],
    primary: 'shot-1.webp',
    links: { github: 'https://github.com/hungryemon/watcher' },
  },
  {
    slug: 'todo', name: 'Todo App', type: 'oss',
    cat: 'Open Source · Flutter',
    tagline: 'Flutter + GetX task manager',
    desc: 'A clean cross-platform to-do app built with Flutter and the GetX framework — add tasks, toggle completion — with integration tests covering the core flows.',
    tech: ['Flutter', 'Dart', 'GetX', 'Integration Tests'],
    cover: 'cover.webp',
    links: { github: 'https://github.com/hungryemon/todo_app' },
  },
  {
    slug: 'django', name: 'Django Weather', type: 'oss',
    cat: 'Open Source · Python',
    tagline: 'Air-quality lookup by US zip code',
    desc: 'A Django web app that looks up real-time air quality by US zip code via the AirNow API, mapping AQI categories to human-readable labels and colour codes.',
    tech: ['Python', 'Django', 'AirNow API', 'requests'],
    cover: 'cover.webp',
    links: { github: 'https://github.com/hungryemon/djangoweather' },
  },
];

const SKILLS = {
  lang:   ['Dart', 'Flutter', 'React Native', 'TypeScript', 'Swift', 'Java', 'Python'],
  mobile: ['Riverpod', 'GetX', 'BLoC', 'Provider', 'Redux'],
  data:   ['Firebase', 'Supabase', 'SQLite', 'Drift', 'Hive', 'MongoDB'],
  tools:  ['VS Code', 'Cursor', 'Trae', 'Android Studio', 'Xcode', 'Postman', 'Figma', 'Burp Suite', 'Git'],
};

const TECH = [
  { img: 'assets/tech/flutter.png',          name: 'Flutter',      d: 'Primary toolkit' },
  { img: 'assets/tech/dart.png',             name: 'Dart',         d: 'Core language' },
  { i: 'fa-solid fa-fire',      c: '#ffca28', name: 'Firebase',     d: 'Backend & auth' },
  { i: 'fa-brands fa-react',    c: '#61dafb', name: 'React Native', d: 'Cross-platform' },
  { i: 'fa-brands fa-swift',    c: '#f05138', name: 'Swift',        d: 'Native iOS' },
  { i: 'fa-brands fa-js',       c: '#f7df1e', name: 'TypeScript',   d: 'Web & tooling' },
  { i: 'fa-brands fa-react',    c: '#61dafb', name: 'ReactJS',      d: 'Web frontends' },
  { i: 'fa-brands fa-python',   c: '#3776ab', name: 'Python',       d: 'Django & scripts' },
  { i: 'fa-brands fa-java',     c: '#e76f00', name: 'Java',         d: 'Android / JVM' },
  { i: 'fa-brands fa-git-alt',  c: '#f1502f', name: 'Git',          d: 'Version control' },
];

const EXPERIENCE = [
  { date: 'Oct 2025 — Present', role: 'Software Engineer II', company: 'SDS Manager · Oslo, Norway', tag: 'Remote',
    points: ['Lead a team of 2 Flutter developers, owning mobile delivery end-to-end (requirements to release) across SDS Manager\'s EHS product suite.', 'Build the SDS Manager app with Flutter — offline-first Safety Data Sheet access and chemical-safety workflows for field teams on iOS & Android.', 'Develop additional EHS apps with the team — Workplace Safety (audits, inspections, incidents & asset management) and an EHS Incident Manager — on a shared Riverpod architecture.', 'Built and maintain Axis UI, a shared Flutter component library and design system used across the apps.'] },
  { date: 'Jan 2024 — Sep 2025', role: 'Senior Software Engineer', company: 'AlgoSoft Technologies Ltd.', tag: 'Remote',
    points: ['Owned 3 App Store apps end-to-end — Invoice Matrix (Flutter), Paraphrase AI & Note Genie (React Native) — from requirements through release, backed by Firebase.', 'Integrated in-app purchases & subscriptions across all apps with RevenueCat.', 'Implemented a custom ad network in client apps with a ReactJS + Supabase admin panel.'] },
  { date: 'Apr 2022 — Dec 2024', role: 'Flutter Developer', company: 'Ostad Ltd.',
    points: ['Owned the build of 2 ed-tech apps from scratch (Ostad & Quran Shikkha), serving 20,000+ learners.', 'Cut Ostad app load time by 30% via performance optimization.', 'Integrated 5+ analytics tools (Firebase, Mixpanel, Sentry, Mux, Smartlook) → +20% engagement.'] },
  { date: 'Apr 2021 — Mar 2022', role: 'Flutter Developer', company: 'TechAByte Solutions',
    points: ['Gathered client requirements and translated Figma designs into pixel-accurate, user-friendly interfaces.', 'Customized 10+ projects and templates to spec, always on deadline.'] },
  { date: 'Sep 2020 — Nov 2020', role: 'Flutter Developer', company: 'DeepSight AI', tag: 'Remote',
    points: ['Contributed to 2 e-commerce apps and 5+ feature/maintenance projects.', 'Coordinated a 3-developer team using an agile process.'] },
  { date: 'Apr 2020 — Jun 2020', role: 'Software Engineer Intern', company: 'Tech5Soft Ltd.',
    points: ['Verified technical documentation across 3 products and helped trace 100+ bugs.'] },
];

/* ----------------------------- RENDER ----------------------------- */
function el(html) { const t = document.createElement('template'); t.innerHTML = html.trim(); return t.content.firstElementChild; }
function chips(arr) { return arr.map(s => `<span class="chip">${s}</span>`).join(''); }

function linkButtons(links) {
  const out = [];
  if (links.appstore) out.push(`<a href="${links.appstore}" target="_blank" rel="noopener"><i aria-hidden="true" class="fa-brands fa-app-store-ios"></i> App Store</a>`);
  if (links.play) out.push(`<a href="${links.play}" target="_blank" rel="noopener"><i aria-hidden="true" class="fa-brands fa-google-play"></i> Google Play</a>`);
  if (links.web) out.push(`<a href="${links.web}" target="_blank" rel="noopener"><i aria-hidden="true" class="fa-solid fa-globe"></i> Web</a>`);
  if (links.windows) out.push(`<a href="${links.windows}" target="_blank" rel="noopener"><i aria-hidden="true" class="fa-brands fa-windows"></i> Windows</a>`);
  if (links.github) out.push(`<a class="primary" href="${links.github}" target="_blank" rel="noopener"><i aria-hidden="true" class="fa-brands fa-github"></i> Source</a>`);
  return out.join('');
}

function renderProjects() {
  const grid = document.getElementById('projectsGrid');
  grid.innerHTML = '';
  PROJECTS.forEach(p => {
    const primary = p.primary || (p.shots && p.shots[0]);
    let media;
    if (p.shots) {
      media = `<div class="card-media" data-slug="${p.slug}" role="button" tabindex="0" aria-label="Open ${p.name} gallery">
           ${p.type === 'apps' ? `<img class="card-icon" src="${ASSET(p.slug, 'icon.png')}" alt="${p.name} icon" loading="lazy" width="46" height="46" />` : `<span class="card-badge"><i aria-hidden="true" class="fa-brands fa-github"></i></span>`}
           ${p.rating ? `<span class="card-rating"><i aria-hidden="true" class="fa-solid fa-star"></i> ${p.rating}</span>` : ''}
           <img class="shot" src="${ASSET(p.slug, primary)}" alt="${p.name} screenshot" loading="lazy" />
           <div class="card-gallery-hint"><span><i aria-hidden="true" class="fa-solid fa-images"></i> View Gallery</span></div>
         </div>`;
    } else {
      media = `<div class="card-cover">
           <img src="${ASSET(p.slug, p.cover)}" alt="${p.name} cover" loading="lazy" />
         </div>`;
    }
    const card = el(`
      <article class="project-card" data-type="${p.type}" data-featured="${!!p.featured}">
        ${media}
        <div class="card-body">
          <span class="card-cat">${p.cat}</span>
          <h3>${p.name}</h3>
          <p class="card-tagline">${p.tagline}</p>
          <p class="card-desc">${p.desc}</p>
          <div class="card-tech">${p.tech.map(t => `<span>${t}</span>`).join('')}</div>
          <div class="card-links">${linkButtons(p.links)}</div>
        </div>
      </article>`);
    grid.appendChild(card);
  });
  // gallery openers
  grid.querySelectorAll('.card-media').forEach(m => {
    const open = () => openLightbox(m.dataset.slug, m);
    m.addEventListener('click', open);
    m.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); } });
  });
}

function applyFilter(filter) {
  document.querySelectorAll('.project-card').forEach(c => {
    const show = filter === 'all'
      || (filter === 'featured' && c.dataset.featured === 'true')
      || (filter === 'apps' && c.dataset.type === 'apps')
      || (filter === 'oss' && c.dataset.type === 'oss');
    c.classList.toggle('hide', !show);
  });
}

function renderSkills() {
  document.getElementById('chipsLang').innerHTML = chips(SKILLS.lang);
  document.getElementById('chipsMobile').innerHTML = chips(SKILLS.mobile);
  document.getElementById('chipsData').innerHTML = chips(SKILLS.data);
  document.getElementById('chipsTools').innerHTML = chips(SKILLS.tools);
  const car = document.getElementById('techCarousel');
  const cardHtml = (t, dup) => {
    const visual = t.img
      ? `<img class="tech-img" src="${t.img}" alt="${t.name} logo" width="44" height="44" loading="lazy" />`
      : `<i aria-hidden="true" class="${t.i}" style="color:${t.c}"></i>`;
    return `<div class="tech-card"${dup ? ' aria-hidden="true"' : ''}><div class="tech-icon">${visual}</div><h4>${t.name}</h4><p>${t.d}</p></div>`;
  };
  // render twice (flat) for a seamless autoplay loop; duplicates hidden from AT
  car.innerHTML = TECH.map(t => cardHtml(t, false)).join('') + TECH.map(t => cardHtml(t, true)).join('');
}

function renderTimeline() {
  document.getElementById('timeline').innerHTML = EXPERIENCE.map(e => `
    <div class="tl-item reveal">
      <div class="tl-date">${e.date}</div>
      <div class="tl-role">${e.role}</div>
      <div class="tl-company">${e.company}${e.tag ? `<span class="tag">${e.tag}</span>` : ''}</div>
      <ul class="tl-list">${e.points.map(p => `<li>${p}</li>`).join('')}</ul>
    </div>`).join('');
}

/* ----------------------------- LIGHTBOX ----------------------------- */
const lb = document.getElementById('lightbox');
const lbContent = document.getElementById('lbContent');
const lbClose = document.getElementById('lbClose');
let lbTrigger = null;

function openLightbox(slug, trigger) {
  const p = PROJECTS.find(x => x.slug === slug);
  if (!p || !p.shots) return;
  lbTrigger = trigger || document.activeElement;
  const head = p.type === 'apps'
    ? `<img src="${ASSET(p.slug, 'icon.png')}" alt="${p.name} icon" />`
    : `<span class="lb-glyph"><i aria-hidden="true" class="fa-brands fa-github"></i></span>`;
  lbContent.innerHTML = `
    <div class="lb-head">
      ${head}
      <div>
        <span class="lb-cat">${p.cat}</span>
        <h3>${p.name}</h3>
      </div>
    </div>
    <p class="lb-desc">${p.desc}</p>
    <div class="lb-shots-wrap">
      <div class="lb-shots">
        ${p.shots.map(s => `<img src="${ASSET(p.slug, s)}" alt="${p.name} screenshot" loading="lazy" />`).join('')}
      </div>
    </div>
    <div class="lb-links card-links">${linkButtons(p.links)}</div>`;
  lb.classList.add('open');
  lb.setAttribute('aria-hidden', 'false');
  document.body.style.overflow = 'hidden';
  ['main', 'header', 'footer'].forEach(sel => document.querySelector(sel)?.setAttribute('inert', ''));
  lbClose.focus();
}
function closeLightbox() {
  lb.classList.remove('open');
  lb.setAttribute('aria-hidden', 'true');
  document.body.style.overflow = '';
  ['main', 'header', 'footer'].forEach(sel => document.querySelector(sel)?.removeAttribute('inert'));
  if (lbTrigger && typeof lbTrigger.focus === 'function') lbTrigger.focus();
  lbTrigger = null;
}
lbClose.addEventListener('click', closeLightbox);
lb.addEventListener('click', e => { if (e.target === lb) closeLightbox(); });
document.addEventListener('keydown', e => {
  if (!lb.classList.contains('open')) return;
  if (e.key === 'Escape') { closeLightbox(); return; }
  if (e.key === 'Tab') {
    const f = [lbClose, ...lbContent.querySelectorAll('a[href], button')];
    if (!f.length) return;
    const first = f[0], last = f[f.length - 1];
    if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
    else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
  }
});

/* ----------------------------- HERO NAME letters ----------------------------- */
function splitName() {
  const node = document.getElementById('heroName');
  const text = node.textContent;
  node.textContent = '';
  [...text].forEach(ch => {
    if (ch === ' ') { node.appendChild(el('<span class="ch sp"> </span>')); return; }
    const s = document.createElement('span');
    s.className = 'ch'; s.textContent = ch;
    node.appendChild(s);
  });
}

/* ----------------------------- INTERACTIONS ----------------------------- */
function initNav() {
  const nav = document.getElementById('nav');
  const links = document.getElementById('navLinks');
  const burger = document.getElementById('hamburger');
  const scrim = document.getElementById('navScrim');
  const navAs = [...links.querySelectorAll('a')];

  const setMenu = open => {
    links.classList.toggle('open', open);
    burger.classList.toggle('open', open);
    scrim.classList.toggle('open', open);
    burger.setAttribute('aria-expanded', String(open));
  };
  burger.addEventListener('click', () => setMenu(!links.classList.contains('open')));
  scrim.addEventListener('click', () => setMenu(false));
  navAs.forEach(a => a.addEventListener('click', () => setMenu(false)));

  const onScroll = () => {
    nav.classList.toggle('scrolled', window.scrollY > 40);
    document.getElementById('toTop').classList.toggle('show', window.scrollY > 600);
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // scroll-spy
  const sections = [...document.querySelectorAll('section[id]')];
  const spy = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (en.isIntersecting) {
        const id = en.target.id;
        navAs.forEach(a => a.classList.toggle('active', a.getAttribute('href') === `#${id}`));
      }
    });
  }, { rootMargin: '-45% 0px -50% 0px' });
  sections.forEach(s => spy.observe(s));
}

function initReveal() {
  if (!('IntersectionObserver' in window)) {
    document.querySelectorAll('.reveal').forEach(r => r.classList.add('in'));
    return;
  }
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { threshold: 0.12 });
  document.querySelectorAll('.reveal').forEach(r => io.observe(r));
  // safety net: never leave content stuck hidden
  window.addEventListener('load', () => setTimeout(() => {
    document.querySelectorAll('.reveal:not(.in)').forEach(r => {
      const top = r.getBoundingClientRect().top;
      if (top < window.innerHeight * 1.1) r.classList.add('in');
    });
  }, 2500));
}

function initCounters() {
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (!en.isIntersecting) return;
      const node = en.target;
      const target = +node.dataset.target;
      const suffix = node.dataset.suffix || '';
      if (REDUCE_MOTION) { node.textContent = target + suffix; io.unobserve(node); return; }
      const start = performance.now(), dur = 1400;
      const step = now => {
        const t = Math.min((now - start) / dur, 1);
        const eased = 1 - Math.pow(1 - t, 3);
        node.textContent = Math.round(eased * target) + suffix;
        if (t < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
      io.unobserve(node);
    });
  }, { threshold: 0.5 });
  document.querySelectorAll('.stat-num').forEach(n => io.observe(n));
}

function initTyped() {
  const node = document.getElementById('typed');
  if (REDUCE_MOTION || typeof Typed === 'undefined') { node.textContent = 'Flutter Developer.'; return; }
  // headline: Flutter-Developer-led
  new Typed('#typed', {
    strings: ['Flutter Developer.', 'Software Engineer.', 'Cross-Platform App Developer.', 'Mobile App Specialist.', 'Problem Solver.'],
    typeSpeed: 70, backSpeed: 38, backDelay: 1600, startDelay: 400, loop: true, smartBackspace: true,
  });
}

function initParticles() {
  if (REDUCE_MOTION || typeof particlesJS === 'undefined') return;
  particlesJS('particles', {
    particles: {
      number: { value: 180, density: { enable: true, value_area: 800 } },
      color: { value: ['#f5b301', '#ffcb45', '#ffffff'] },
      shape: { type: 'circle' },
      opacity: { value: 0.5, random: true, anim: { enable: true, speed: 0.6, opacity_min: 0.1 } },
      size: { value: 2.6, random: true },
      line_linked: { enable: true, distance: 120, color: '#f5b301', opacity: 0.22, width: 1 },
      move: { enable: true, speed: 1.2, direction: 'none', random: true, out_mode: 'out' },
    },
    interactivity: {
      detect_on: 'window',
      events: { onhover: { enable: true, mode: 'grab' }, onclick: { enable: true, mode: 'push' }, resize: true },
      modes: { grab: { distance: 200, line_linked: { opacity: 0.6 } }, push: { particles_nb: 4 } },
    },
    retina_detect: false,
  });
}

function initTechAutoplay() {
  const car = document.getElementById('techCarousel');
  if (!car || REDUCE_MOTION) return;
  let paused = false, last = 0;
  const half = () => car.scrollWidth / 2;
  ['pointerenter', 'focusin', 'touchstart'].forEach(e => car.addEventListener(e, () => { paused = true; }, { passive: true }));
  ['pointerleave', 'focusout', 'touchend'].forEach(e => car.addEventListener(e, () => { paused = false; }, { passive: true }));
  const step = now => {
    const dt = last ? now - last : 16; last = now;
    if (!paused) {
      car.scrollLeft += dt * 0.045; // ~45px/s
      if (car.scrollLeft >= half()) car.scrollLeft -= half();
    }
    requestAnimationFrame(step);
  };
  requestAnimationFrame(step);
}

function initLogoEmoji() {
  const e = document.getElementById('logoEmoji');
  if (!e) return;
  const fun = ['/', '⚡', '✦', '★', '◆', '※', '∞', '☂'];
  let i = 0;
  e.addEventListener('click', ev => {
    ev.preventDefault();
    i = (i + 1) % fun.length; e.textContent = fun[i];
    setTimeout(() => { e.textContent = '/'; }, 700);
  });
}

/* ----------------------------- INIT ----------------------------- */
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('year').textContent = new Date().getFullYear();
  splitName();
  renderProjects();
  renderSkills();
  renderTimeline();
  initNav();
  initReveal();
  initCounters();
  initTechAutoplay();
  initLogoEmoji();

  document.getElementById('filterBar').addEventListener('click', e => {
    const btn = e.target.closest('.filter-btn'); if (!btn) return;
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    applyFilter(btn.dataset.filter);
  });
  document.getElementById('toTop').addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  // libs may still be loading (defer) — try now and shortly after
  initTyped(); initParticles();
  setTimeout(() => { if (typeof particlesJS !== 'undefined' && !document.querySelector('#particles canvas')) initParticles(); }, 400);
});
