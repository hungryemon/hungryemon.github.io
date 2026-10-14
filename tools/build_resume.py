#!/usr/bin/env python3
"""
Build Md Shahed Uddin Emon's ATS-friendly resumes (PDF) from a single source of truth.

Outputs (into assets/resume/):
  - Md_Shahed_Uddin_Emon_Resume.pdf       (GLOBAL: SDS Manager - Oslo, Norway / Remote)  -> committed
  - Md_Shahed_Uddin_Emon_Resume_BD.pdf    (LOCAL:  SDS Manager - Gulshan-1, Dhaka / Hybrid) -> GITIGNORED, never push

Usage:  python3 tools/build_resume.py
Requires: Google Chrome (for headless print-to-PDF). Override path with env CHROME=...

Keep this file in sync with the portfolio (index.html + js/script.js). See CLAUDE.md.
"""
import os, base64, subprocess, tempfile, shutil

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTDIR = os.path.join(REPO, "assets", "resume")
PHOTO_FILE = os.path.join(REPO, "assets", "profile", "headshot-760.jpg")

def chrome_path():
    env = os.environ.get("CHROME")
    if env and os.path.exists(env):
        return env
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        shutil.which("google-chrome"), shutil.which("chromium"), shutil.which("chrome"),
    ]
    for c in candidates:
        if c and os.path.exists(c):
            return c
    raise SystemExit("Chrome not found. Set CHROME=/path/to/chrome")

PHOTO = "data:image/jpeg;base64," + base64.b64encode(open(PHOTO_FILE, "rb").read()).decode()

CSS = """
@page { size: Letter; margin: 0.4in 0.55in; }
* { box-sizing: border-box; }
body { font-family: Arial,'Helvetica Neue',Helvetica,sans-serif; font-size: 9.5pt; line-height: 1.25; color: #1b1b1b; margin: 0; font-variant-ligatures: none; -webkit-font-feature-settings: "liga" 0, "clig" 0; font-feature-settings: "liga" 0, "clig" 0; }
a { color: #1b1b1b; text-decoration: none; }
h1 { font-size: 22pt; margin: 0; letter-spacing: 0.3px; }
.subtitle { font-size: 12pt; font-weight: 600; color: #333; margin: 1px 0 5px; }
.contact { font-size: 9.5pt; color: #2a2a2a; }
.contact span { white-space: nowrap; }
.sep { color: #999; padding: 0 5px; }
.hdr { display: flex; justify-content: space-between; align-items: flex-start; gap: 18px; }
.hdr-text { flex: 1 1 auto; }
.photo { flex: 0 0 auto; width: 96px; height: 96px; border-radius: 50%; object-fit: cover; border: 1.5px solid #9a9a9a; }
h2 { font-size: 10.5pt; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; border-bottom: 1.1px solid #444; padding-bottom: 2px; margin: 8px 0 3px; }
p { margin: 2px 0; }
.summary { margin: 2px 0 0; text-align: justify; }
.skills div { margin: 1.5px 0; }
.skills b { color: #111; }
.job { margin-bottom: 5px; }
.role { font-weight: 700; font-size: 10.5pt; }
.org { font-weight: 600; color: #222; }
.when { color: #555; }
.orgline { margin: 0 0 1px; }
ul { margin: 3px 0 0; padding-left: 17px; }
li { margin-bottom: 1px; }
.proj { margin: 2.7px 0; }
.proj b { color: #111; }
.plinks a { color: #1f57b6; text-decoration: none; }
.plinks { color: #1f57b6; }
.ilink { color: #1f57b6; }
.edu-item { margin: 2px 0; }
.muted { color: #555; }
"""

def doc(variant):
    if variant == "global":
        loc = "Dhaka, Bangladesh (Open to Remote)"
        sds_line = "SDS Manager &mdash; Oslo, Norway (Remote)"
        summary_tail = "Experienced delivering production software in remote, distributed international teams."
    else:
        loc = "Dhaka, Bangladesh"
        sds_line = "SDS Manager &mdash; Gulshan-1, Dhaka, Bangladesh (Hybrid)"
        summary_tail = "Comfortable in hybrid and on-site teams, with strong remote collaboration experience."

    contact = (
        '<span><a href="mailto:shahedemon.pro@gmail.com">shahedemon.pro@gmail.com</a></span>'
        '<span class="sep">|</span><span>+880 1861-992088</span>'
        f'<span class="sep">|</span><span>{loc}</span><br/>'
        '<span><a href="https://github.com/hungryemon">github.com/hungryemon</a></span>'
        '<span class="sep">|</span><span><a href="https://www.linkedin.com/in/shahed-emon">linkedin.com/in/shahed-emon</a></span>'
        '<span class="sep">|</span><span><a href="https://hungryemon.github.io">hungryemon.github.io</a></span>'
    )

    summary = (
        "Software engineer with 6+ years of experience building cross-platform products for mobile, desktop "
        "and web. Shipped 10+ production apps to the App Store and Google Play reaching 500K+ combined users across "
        "ed-tech, AI productivity, healthcare, and enterprise EHS / chemical-safety domains. Mobile-first (Flutter, "
        "React Native) with full-stack delivery in React/Next.js and Django. Owns products end-to-end &mdash; from "
        "requirements and architecture through testing, store review, release, and production monitoring &mdash; "
        "working independently or leading small teams. "
        + summary_tail
    )

    skills = [
        ("Languages", "Dart, TypeScript, JavaScript, Python, Swift, Java"),
        ("Cross-Platform", "Flutter, React Native &mdash; iOS, Android, macOS, Windows, Linux, Web"),
        ("Native &amp; Integrations", "Platform channels (MethodChannel), In-app purchases (RevenueCat), Push notifications"),
        ("State Management", "Riverpod, BLoC, Provider, GetX, Redux"),
        ("Web &amp; Backend", "React, Next.js, Vite, Tailwind CSS, Django / DRF, Express, Celery, REST APIs, PWA &amp; Web Push"),
        ("Databases &amp; Storage", "PostgreSQL, MongoDB, Redis, SQLite / Drift, Hive, Firebase, Supabase"),
        ("Architecture", "Clean Architecture / MVVM, Offline-first sync, Monorepos (melos), Design systems &amp; tokens, RBAC, i18n"),
        ("Testing", "Unit, widget &amp; integration testing (Flutter), Playwright, Vitest"),
        ("CI/CD &amp; Release", "GitHub Actions, Codemagic, Docker, App Store Connect, Play Console, Inno Setup (Windows installers)"),
        ("Monitoring &amp; Analytics", "Sentry, Firebase Analytics, Mixpanel"),
        ("Tools &amp; Workflow", "Git, VS Code, Xcode, Android Studio, Figma, Postman, Agile/Scrum"),
        ("AI-Assisted Development", "Claude Code, OpenCode, Hermes Agent, Cursor, Trae, Grok, Ollama (local LLMs)"),
    ]

    experience = [
        ("Software Engineer II", sds_line, "Oct 2025 &ndash; Present", [
            "Built the SDS Manager iOS/Android app (<a class=\"ilink\" href=\"https://apps.apple.com/us/app/sds-manager/id6754279703\">App Store</a> &middot; <a class=\"ilink\" href=\"https://play.google.com/store/apps/details?id=com.sdsmanager.mainapp\">Google Play</a>) from scratch and own it end-to-end &mdash; architecture, features, CI/CD releases to the App Store and Google Play, and production monitoring. Lead a team of 2 Flutter developers through task planning, code reviews, and mentoring.",
            "Delivered the full inventory product: SSO login, offline-first SDS library with Drift sync and search, barcode/QR scanning, stock and kit-lot management with change logs and CSV export, Risk Assessment with AI-suggested hazards and exposure data, Substitution, QR employee access, user management, subscription and permission gating at web parity, in-app update and review prompts, and analytics with an offline queue.",
            "Built most of the EHS module on a multi-package Riverpod / melos architecture &mdash; Investigations (5-Why, Fishbone, OSHA/RIDDOR compliance), CAPA, Training (courses, quizzes, certificates), Assets with QR scan-to-inspect, and dynamic capture forms with 17 field types.",
            "Kept production stable through Sentry monitoring, crash triage, and defensive JSON parsing across every feature model; grew the automated test suite (unit, widget, and integration tests) to 1,000+ test files running in CI.",
            "Unified theming into a design-token palette matched to the web app (WCAG AA) and localized the app into 40 languages.",
            "Took the Hub One Flutter app multi-platform &mdash; shipped iPhone and Mac App Store builds, added macOS and Windows support, made the UI responsive across phone, tablet and desktop, and set up release monitoring with Sentry (symbol and obfuscation-map upload).",
            "Rebuilt 9 EHS product pages on sdsmanager.com (Next.js, Tailwind, 30+ locales) and made the EHS Incident Manager web app (React, Express, PostgreSQL) an installable PWA with Web Push.",
            "Built document management, push notifications, and auth token refresh in the Workplace Safety Flutter app; built Axis UI, a shared Flutter design system.",
        ]),
        ("Senior Software Engineer", "AlgoSoft Technologies Ltd. &mdash; Remote", "Jan 2025 &ndash; Sep 2025", [
            "Owned 3 AI productivity and invoicing apps end-to-end &mdash; from requirements and architecture through App Store release &mdash; backed by Firebase, with RevenueCat in-app purchases and subscriptions across all apps.",
            "Built Invoice Matrix in Flutter, a PDF invoicing and billing app (<a class=\"ilink\" href=\"https://apps.apple.com/us/app/invoice-matrix-pdf-invoices/id6742684220\">App Store</a>).",
            "Built Paraphrase AI in React Native and TypeScript, an AI rewriting and humanizing app powered by LLM APIs and supporting 185+ languages (<a class=\"ilink\" href=\"https://apps.apple.com/us/app/paraphrase-ai-smart-humanizer/id6746731727\">App Store</a>).",
            "Built Note Genie in React Native, an AI note-taker that uses AI transcription to turn audio, video and text into organized notes (<a class=\"ilink\" href=\"https://apps.apple.com/us/app/lecture-note-taker-note-genie/id6748276655\">App Store</a>).",
            "Developed a custom ad network for client apps with a ReactJS + Supabase admin panel.",
        ]),
        ("Flutter Developer", "Ostad Ltd. &mdash; Dhaka, Bangladesh", "Apr 2022 &ndash; Dec 2024", [
            "Owned the end-to-end build of two ed-tech apps from scratch (Ostad live-learning platform and Quran Shikkha) in Flutter, serving 20,000+ learners across iOS, Android, macOS, Windows, and Linux.",
            "Implemented live-streaming classes in the Ostad bootcamp app using GetX state management.",
            "Integrated SSLCommerz payments into Quran Shikkha, a Bengali-language Quran-learning app (<a class=\"ilink\" href=\"https://play.google.com/store/apps/details?id=com.quranshikkha.app\">Google Play</a>).",
            "Reduced Ostad app load time by 30% through performance optimization and profiling.",
            "Integrated 5+ analytics tools (Firebase Analytics, Mixpanel, Sentry, Mux, Smartlook), improving user engagement by 20%.",
            "Built <a class=\"ilink\" href=\"https://pub.dev/packages/video_player_mux\">video_player_mux</a>, a native Android Flutter plugin using MethodChannel (ExoPlayer + Mux Data video monitoring), and published it to pub.dev.",
        ]),
        ("Flutter Developer", "TechAByte Solutions &mdash; Dhaka, Bangladesh", "Apr 2021 &ndash; Mar 2022", [
            "Gathered client requirements and converted Figma designs into pixel-accurate, responsive Flutter user interfaces.",
            "Customized and delivered 10+ client projects and templates, consistently meeting deadlines.",
        ]),
        ("Flutter Developer", "DeepSight AI &mdash; Remote, Dhaka", "Sep 2020 &ndash; Nov 2020", [
            "Contributed to 2 e-commerce applications and 5+ feature and maintenance projects.",
            "Led a 3-developer team using an Agile workflow.",
        ]),
        ("Software Engineer Intern", "Tech5Soft Ltd. &mdash; Dhaka, Bangladesh", "Apr 2020 &ndash; Jun 2020", [
            "Reviewed and verified technical documentation for 3 products; helped trace and resolve 100+ bugs.",
        ]),
    ]

    projects = [
        ("SDS Manager", "Flutter, Riverpod, offline-first", "Chemical-safety (EHS) app: offline SDS library, QR scanning, inventory &amp; EHS workflows.",
         [("App Store","https://apps.apple.com/us/app/sds-manager/id6754279703"),("Google Play","https://play.google.com/store/apps/details?id=com.sdsmanager.mainapp")]),
        ("Hub One", "Flutter, iOS, macOS, Windows", "Multi-product business app (tasks, sales, support, ledger) for iPhone, iPad &amp; Mac.",
         [("App Store","https://apps.apple.com/us/app/hubone-sds/id6814464975")]),
        ("MaintainOne", "Django, React, TypeScript, PostgreSQL, Celery, Docker", "CMMS built end-to-end for a US client &mdash; work requests and orders, preventive maintenance, asset/location hierarchy, inventory and purchasing, role-based access, and reporting.",
         []),
        ("AI Productivity Apps", "Flutter, React Native, TypeScript, LLM APIs, Firebase, RevenueCat", 'Invoice Matrix (<a class="ilink" href="https://apps.apple.com/us/app/invoice-matrix-pdf-invoices/id6742684220">App Store</a>), a PDF invoicing &amp; billing app; Paraphrase AI (<a class="ilink" href="https://apps.apple.com/us/app/paraphrase-ai-smart-humanizer/id6746731727">App Store</a>), an AI rewriter &amp; humanizer in 185+ languages; Note Genie (<a class="ilink" href="https://apps.apple.com/us/app/lecture-note-taker-note-genie/id6748276655">App Store</a>), an AI note-taker for audio, video &amp; text.',
         []),
        ("Ostad", "Flutter, GetX, live streaming", "Multi-platform live-learning bootcamp; 20,000+ learners, 4.7&#9733;.",
         [("App Store","https://apps.apple.com/us/app/ostad-app/id6446163017"),("Google Play","https://play.google.com/store/apps/details?id=com.ostad.app"),("Web","https://ostad.app"),("Windows","https://cutt.ly/Fr3QsjFo")]),
        ("Quran Shikkha", "Flutter, SSLCommerz", "Online Quran-learning ed-tech app (Bengali).",
         [("Google Play","https://play.google.com/store/apps/details?id=com.quranshikkha.app")]),
        ("IFEN Clinical Apps", "Flutter, data visualization, EN/DE", 'Healthcare app suite: Capito Basic (<a class="ilink" href="https://apps.apple.com/us/app/capito-basic-by-ifen/id1550991580">App Store</a>) and Capito Xpert (<a class="ilink" href="https://apps.apple.com/us/app/capito-xpert-by-ifen/id1550994819">App Store</a> &middot; <a class="ilink" href="https://play.google.com/store/apps/details?id=com.ifen.capitoxpert">Google Play</a>) for clinical cognitive &amp; attention testing (Stroop tests); IFEN Learning Portal (<a class="ilink" href="https://apps.apple.com/us/app/ifen-learning-portal/id1547252500">App Store</a> &middot; <a class="ilink" href="https://play.google.com/store/apps/details?id=com.ifen.neurofeedback_academy">Google Play</a>) for neurofeedback training &amp; certification; IFEN Symptom Tracker (<a class="ilink" href="https://apps.apple.com/us/app/ifen-symptom-tracker/id6503682705">App Store</a> &middot; <a class="ilink" href="https://play.google.com/store/apps/details?id=com.ifen.symptom_tracker">Google Play</a>) for patient symptom logging &amp; monitoring.',
         []),
        ("Watcher", "Flutter, GetX, TMDB API", "Cross-platform movie &amp; TV browser (open source).",
         [("GitHub","https://github.com/hungryemon/watcher")]),
    ]

    p = []
    p.append(
        '<header class="hdr"><div class="hdr-text">'
        '<h1>Md Shahed Uddin Emon</h1>'
        '<div class="subtitle">Software Engineer</div>'
        f'<div class="contact">{contact}</div>'
        f'</div><img class="photo" src="{PHOTO}" alt="Md Shahed Uddin Emon" /></header>'
    )
    p.append('<h2>Professional Summary</h2>')
    p.append(f'<p class="summary">{summary}</p>')
    p.append('<h2>Technical Skills</h2><div class="skills">')
    for k, v in skills:
        p.append(f'<div><b>{k}:</b> {v}</div>')
    p.append('</div>')
    p.append('<h2>Professional Experience</h2>')
    for role, org, when, bullets in experience:
        p.append('<div class="job">')
        p.append(f'<div class="role">{role}</div>')
        p.append(f'<div class="orgline"><span class="org">{org}</span> <span class="when">&nbsp;|&nbsp; {when}</span></div>')
        p.append('<ul>')
        for b in bullets:
            p.append(f'<li>{b}</li>')
        p.append('</ul></div>')
    p.append('<h2>Projects</h2>')
    for name, tech, desc, links in projects:
        lk = ' &middot; '.join(f'<a href="{u}">{t}</a>' for t, u in links)
        lk = f' <span class="plinks">{lk}</span>' if links else ''
        p.append(f'<div class="proj"><b>{name}</b> <span class="muted">({tech})</span> &mdash; {desc}{lk}</div>')
    p.append('<h2>Education</h2>')
    p.append('<div class="edu-item"><b>B.Sc. in Computer Science &amp; Engineering</b> &mdash; Daffodil International University, Dhaka, Bangladesh <span class="when">&nbsp;|&nbsp; 2019</span></div>')
    p.append('<div class="edu-item muted" style="padding-left:12px">Activities: Student Prefect (2016)</div>')
    p.append('<div class="edu-item"><b>Higher Secondary Certificate (H.S.C.), Science</b> &mdash; Bir Shrestha Munshi Abdur Rouf Public College, Dhaka <span class="when">&nbsp;|&nbsp; 2014</span></div>')
    p.append('<div class="edu-item"><b>Secondary School Certificate (S.S.C.), Science</b> &mdash; Motijheel Model High School &amp; College, Dhaka <span class="when">&nbsp;|&nbsp; 2012</span></div>')
    p.append('<h2>Certifications</h2>')
    p.append('<div class="edu-item">Full-Stack Web Development (Python, Django &amp; React JS) &mdash; Skill Jobs <span class="when">&nbsp;|&nbsp; 2021</span></div>')
    p.append('<h2>Languages</h2>')
    p.append('<div class="edu-item">Bengali (Native) &nbsp;&middot;&nbsp; English (Professional / Advanced)</div>')

    return f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Md Shahed Uddin Emon &mdash; Resume</title><style>{CSS}</style></head><body>{"".join(p)}</body></html>'

def render(html, out_pdf):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False) as f:
        f.write(html); tmp = f.name
    try:
        subprocess.run([chrome_path(), "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={out_pdf}", "file://" + tmp],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    finally:
        os.unlink(tmp)

if __name__ == "__main__":
    os.makedirs(OUTDIR, exist_ok=True)
    targets = {"global": "Md_Shahed_Uddin_Emon_Resume.pdf", "local": "Md_Shahed_Uddin_Emon_Resume_BD.pdf"}
    for variant, fname in targets.items():
        render(doc(variant), os.path.join(OUTDIR, fname))
        print(f"built {fname} ({variant})")
    print("\nNote: the LOCAL (_BD) resume is gitignored - never commit/push it.")
