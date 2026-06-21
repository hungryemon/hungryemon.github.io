# CLAUDE.md — hungryemon.github.io

Personal portfolio of **Md Shahed Uddin Emon** (Flutter developer / software engineer), live at
**https://hungryemon.github.io**. Static site (plain HTML/CSS/JS, no build step) on GitHub Pages.

## Structure
```
index.html              # markup, meta/SEO, all section content
css/style.css           # design system (dark + amber theme)
js/script.js            # PROJECTS / SKILLS / EXPERIENCE data + interactions (cards, lightbox, particles)
assets/
  profile/              # headshot, og-card
  projects/<slug>/      # app icons + screenshots
  resume/
    Md_Shahed_Uddin_Emon_Resume.pdf      # GLOBAL resume — committed
    Md_Shahed_Uddin_Emon_Resume_BD.pdf   # LOCAL (Dhaka/hybrid) resume — GITIGNORED, never commit/push
tools/build_resume.py   # single source of truth that generates BOTH resume PDFs
```

## Conventions
- **Cache-busting:** when `css/style.css` or `js/script.js` change, bump the `?v=N` query in `index.html`
  (both tags) so visitors don't get a stale cached copy.
- **Deploy:** commit + push to `main`; GitHub Pages rebuilds automatically (≈1 min).
- **Resumes:** never hand-edit the PDFs. Edit `tools/build_resume.py` and run `python3 tools/build_resume.py`
  (needs Google Chrome; override with `CHROME=/path/to/chrome`). It rebuilds both the global and local PDFs.
- **Local resume privacy:** `assets/resume/Md_Shahed_Uddin_Emon_Resume_BD.pdf` is gitignored and must
  NEVER be committed or pushed. Only the global resume is public.

## Portfolio ↔ Resume sync rule (IMPORTANT)
The portfolio (`index.html` + `js/script.js`) and the résumés (`tools/build_resume.py`) describe the
**same person and the same facts** — experience, job titles, dates, employers, projects, tech stacks,
skills, education, certifications, and headline stats. They must stay consistent.

Therefore:
1. **When the portfolio changes**, check whether the résumés need the same change, and vice versa
   (a résumé edit may need to be reflected on the site). Flag anything that has drifted out of sync.
2. **Before applying any cross-update, show a draft first and get the user's explicit consent.**
   - Present the proposed change as a clear diff/draft (what will change, in which file, old → new).
   - Do **not** auto-apply the synced change. Wait for the user to approve (and let them edit/decline).
   - Only after approval: make the edit, rebuild the resume PDF(s) if affected, bump the cache version
     if site files changed, and deploy.
3. Apply the same fact to **both** résumé variants (global + local) — they differ only in the SDS Manager
   location/work-mode line and one summary sentence.
4. Never push the local (`_BD`) résumé.

Examples of fields that should stay in sync: years of experience, current role/title, employer & dates,
project names/tech/links, skills lists, education, certifications, and the About stats (Years / Apps / Users).
