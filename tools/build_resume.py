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
@page { size: Letter; margin: 0.5in 0.62in; }
* { box-sizing: border-box; }
body { font-family: 'Calibri','Carlito','Helvetica Neue',Arial,sans-serif; font-size: 10.5pt; line-height: 1.33; color: #1b1b1b; margin: 0; font-variant-ligatures: none; -webkit-font-feature-settings: "liga" 0, "clig" 0; font-feature-settings: "liga" 0, "clig" 0; }
a { color: #1b1b1b; text-decoration: none; }
h1 { font-size: 20pt; margin: 0; letter-spacing: 0.3px; }
.subtitle { font-size: 11pt; font-weight: 600; color: #333; margin: 1px 0 5px; }
.contact { font-size: 9.5pt; color: #2a2a2a; }
.contact span { white-space: nowrap; }
.sep { color: #999; padding: 0 5px; }
.hdr { display: flex; justify-content: space-between; align-items: flex-start; gap: 18px; }
.hdr-text { flex: 1 1 auto; }
.photo { flex: 0 0 auto; width: 96px; height: 96px; border-radius: 50%; object-fit: cover; border: 1.5px solid #9a9a9a; }
h2 { font-size: 10.5pt; font-weight: 700; text-transform: uppercase; letter-spacing: 1px; border-bottom: 1.1px solid #444; padding-bottom: 2px; margin: 13px 0 6px; }
p { margin: 2px 0; }
.summary { margin: 2px 0 0; text-align: justify; }
.skills div { margin: 2.5px 0; }
.skills b { color: #111; }
.job { margin-bottom: 8px; }
.role { font-weight: 700; font-size: 10.8pt; }
.org { font-weight: 600; color: #222; }
.when { color: #555; }
.orgline { margin: 0 0 1px; }
ul { margin: 3px 0 0; padding-left: 17px; }
li { margin-bottom: 1.5px; }
.proj { margin: 2.7px 0; }
.proj b { color: #111; }
.plinks a { color: #1f57b6; text-decoration: none; }
.plinks { color: #1f57b6; font-size: 9.3pt; }
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
        "Flutter developer and software engineer with 7+ years of experience building high-performance, "
        "cross-platform applications across iOS, Android, macOS, Windows, Linux, and Web. Shipped 10+ production apps "
        "to the App Store and Google Play reaching 500K+ combined users across ed-tech, AI productivity, healthcare, "
        "and enterprise chemical-safety domains. Strong in Dart/Flutter and React Native, state management "
        "(Riverpod, BLoC, GetX), offline-first architecture, REST APIs, Firebase, in-app purchases, and CI/CD. "
        + summary_tail
    )

    skills = [
        ("Languages &amp; Frameworks", "Dart, Flutter, React Native, TypeScript, Swift, Java, Python"),
        ("State Management", "Riverpod, BLoC, GetX, Provider, Redux"),
        ("Databases &amp; Storage", "Firebase, Supabase, SQLite, Drift, Hive, MongoDB"),
        ("Mobile &amp; Architecture", "Cross-platform development, Offline-first sync, REST APIs, Clean Architecture / MVVM, In-app purchases (RevenueCat), Push notifications"),
        ("Tools &amp; Practices", "Git, CI/CD, Agile/Scrum, Android Studio, Xcode, VS Code, Cursor, Postman, Figma, Firebase Analytics, Mixpanel, Sentry"),
        ("Platforms", "iOS, Android, macOS, Windows, Linux, Web"),
    ]

    experience = [
        ("Software Engineer II", sds_line, "Oct 2025 &ndash; Present", [
            "Develop the SDS Manager cross-platform mobile app (iOS &amp; Android) in Flutter, delivering offline-first access to Safety Data Sheet (SDS) libraries for field teams in connectivity-free environments.",
            "Implement first-aid and hazard lookup and chemical-safety compliance workflows; manage application state with Riverpod.",
            "Port the web platform&rsquo;s SDS management capabilities to mobile and ship cross-platform feature releases to the App Store and Google Play.",
        ]),
        ("Senior Software Engineer", "AlgoSoft Technologies Ltd. &mdash; Remote", "Jan 2024 &ndash; Sep 2025", [
            "Built and shipped 3 AI productivity and invoicing apps to the App Store: Invoice Matrix (Flutter), Paraphrase AI and Note Genie (React Native), backed by Firebase.",
            "Integrated in-app purchases and subscriptions across all apps using RevenueCat.",
            "Developed a custom ad network for client apps with a ReactJS + Supabase admin panel.",
        ]),
        ("Flutter Developer", "Ostad Ltd. &mdash; Dhaka, Bangladesh", "Apr 2022 &ndash; Dec 2024", [
            "Built two ed-tech apps from scratch (Ostad live-learning platform and Quran Shikkha) in Flutter, serving 20,000+ learners across iOS, Android, macOS, Windows, and Linux.",
            "Reduced Ostad app load time by 30% through performance optimization and profiling.",
            "Integrated 5+ analytics tools (Firebase Analytics, Mixpanel, Sentry, Mux, Smartlook), improving user engagement by 20%.",
            "Built and maintained 50+ reusable packages and plugins.",
        ]),
        ("Flutter Developer", "TechAByte Solutions &mdash; Dhaka, Bangladesh", "Apr 2021 &ndash; Mar 2022", [
            "Converted Figma designs into pixel-accurate, responsive Flutter user interfaces.",
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
        ("SDS Manager", "Flutter, Riverpod, offline-first", "Enterprise chemical-safety (EHS) Safety Data Sheet app.",
         [("App Store","https://apps.apple.com/us/app/sds-manager/id6754279703"),("Google Play","https://play.google.com/store/apps/details?id=com.sdsmanager.mainapp")]),
        ("Invoice Matrix", "Flutter, Firebase, RevenueCat", "PDF invoicing &amp; billing app.",
         [("App Store","https://apps.apple.com/us/app/invoice-matrix-pdf-invoices/id6742684220")]),
        ("Paraphrase AI", "React Native, TypeScript, LLM APIs", "AI rewriting/humanizing app supporting 185+ languages.",
         [("App Store","https://apps.apple.com/us/app/paraphrase-ai-smart-humanizer/id6746731727")]),
        ("Note Genie", "React Native, AI transcription", "AI note-taker converting audio, video and text into organized notes.",
         [("App Store","https://apps.apple.com/us/app/lecture-note-taker-note-genie/id6748276655")]),
        ("Ostad", "Flutter, GetX, live streaming", "Multi-platform live-learning bootcamp; 20,000+ learners, 4.7&#9733;.",
         [("App Store","https://apps.apple.com/us/app/ostad-app/id6446163017"),("Google Play","https://play.google.com/store/apps/details?id=com.ostad.app"),("Web","https://ostad.app"),("Windows","https://cutt.ly/Fr3QsjFo")]),
        ("Quran Shikkha", "Flutter, SSLCommerz", "Online Quran-learning ed-tech app (Bengali).",
         [("Google Play","https://play.google.com/store/apps/details?id=com.quranshikkha.app")]),
        ("Capito Basic by IFEN", "Flutter, EN/DE", "Clinical cognitive &amp; attention testing tool.",
         [("App Store","https://apps.apple.com/us/app/capito-basic-by-ifen/id1550991580")]),
        ("Capito Xpert by IFEN", "Flutter, data visualization", "Advanced cognitive assessment with Stroop tests.",
         [("App Store","https://apps.apple.com/us/app/capito-xpert-by-ifen/id1550994819"),("Google Play","https://play.google.com/store/apps/details?id=com.ifen.capitoxpert")]),
        ("IFEN Learning Portal", "Flutter", "Neurofeedback training &amp; certification delivery.",
         [("App Store","https://apps.apple.com/us/app/ifen-learning-portal/id1547252500"),("Google Play","https://play.google.com/store/apps/details?id=com.ifen.neurofeedback_academy")]),
        ("IFEN Symptom Tracker", "Flutter, charts", "Patient symptom logging &amp; monitoring (EN/DE).",
         [("App Store","https://apps.apple.com/us/app/ifen-symptom-tracker/id6503682705"),("Google Play","https://play.google.com/store/apps/details?id=com.ifen.symptom_tracker")]),
        ("Watcher", "Flutter, GetX, TMDB API", "Cross-platform movie &amp; TV browser (open source).",
         [("GitHub","https://github.com/hungryemon/watcher")]),
        ("Todo App", "Flutter, GetX", "Cross-platform task manager with integration tests (open source).",
         [("GitHub","https://github.com/hungryemon/todo_app")]),
        ("Django Weather", "Python, Django, AirNow API", "Air-quality lookup by US zip code (open source).",
         [("GitHub","https://github.com/hungryemon/djangoweather")]),
    ]

    p = []
    p.append(
        '<header class="hdr"><div class="hdr-text">'
        '<h1>Md Shahed Uddin Emon</h1>'
        '<div class="subtitle">Flutter Developer &nbsp;|&nbsp; Software Engineer</div>'
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
    p.append('<div class="edu-item"><b>Higher Secondary Certificate (H.S.C.), Science</b> &mdash; Bir Shrestha Munshi Abdur Rouf Public College, Dhaka <span class="when">&nbsp;|&nbsp; 2014</span></div>')
    p.append('<div class="edu-item"><b>Secondary School Certificate (S.S.C.), Science</b> &mdash; Motijheel Model High School &amp; College, Dhaka <span class="when">&nbsp;|&nbsp; 2012</span></div>')
    p.append('<h2>Certifications</h2>')
    p.append('<div class="edu-item">Full-Stack Web Development (Python, Django &amp; React JS) &mdash; Skill Jobs <span class="when">&nbsp;|&nbsp; 2021</span></div>')
    p.append('<div class="edu-item">Student Prefect &mdash; Daffodil International University <span class="when">&nbsp;|&nbsp; 2016</span></div>')
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
