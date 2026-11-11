#!/usr/bin/env python3
"""Generate the games' legal pages: /<slug>/, /<slug>/privacy/, /<slug>/terms/, /<slug>/delete-account/.

Single source of truth for every game's Privacy Policy, Terms of Use and account-deletion page. Edit the
GAMES table or the shared text below, then run `python3 tools/build_game_legal.py` and commit the output.
The apps link to https://hungryemon.github.io/<slug>/privacy and /terms (PRIVACY_URL / TERMS_URL).
"""
from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://hungryemon.github.io"
OPERATOR = "Md Shahed Uddin Emon"
CONTACT = "shahedemon.pro@gmail.com"
EFFECTIVE = "11 November 2026"
COUNTRY = "Bangladesh"

# Per-game facts. Keep them in step with each game's docs/OWNER_SETUP.md ("Store and privacy answers").
GAMES = [
    {
        "slug": "type-detective",
        "name": "Type Detective",
        "tagline": "A daily typography mystery: name the typeface from the clues.",
        "delete_path": "Settings → Account → Delete account",
        "notifications": True,
        "location": None,
        "camera": None,
        "sensors": None,
    },
    {
        "slug": "script-rogue",
        "name": "Script Rogue",
        "tagline": "A roguelike that teaches you to read new writing systems.",
        "delete_path": "Settings → Account → Delete account and cloud copy",
        "notifications": True,
        "location": None,
        "camera": None,
        "sensors": None,
    },
    {
        "slug": "rainbloom",
        "name": "Rainbloom",
        "tagline": "A garden that grows with your real local weather.",
        "delete_path": "Settings (the bench) → Account → Delete my cloud data",
        "notifications": True,
        "location": (
            "Rainbloom asks for <strong>approximate</strong> location only (iOS reduced accuracy; Android "
            "coarse location). On your device it is snapped to a grid cell about 25–30 km wide, and only that "
            "cell's centre is sent to the Norwegian Meteorological Institute (MET Norway, api.met.no) to get "
            "the forecast. Your location is not stored, logged, synced, or shared with analytics or "
            "advertising. You can deny the permission and pick a climate by hand instead."
        ),
        "camera": None,
        "sensors": None,
    },
    {
        "slug": "sky-hunt",
        "name": "Sky Hunt",
        "tagline": "Find real stars, planets and sky events above you.",
        "delete_path": "Settings → Account → Delete my cloud data",
        "notifications": False,
        "location": (
            "Sky Hunt asks for <strong>approximate</strong> location only (iOS reduced accuracy; Android "
            "coarse location) to compute the sky above you on your device. For the cloud forecast, "
            "coordinates rounded to one decimal place (about 10 km) are sent to the Norwegian Meteorological "
            "Institute (MET Norway, api.met.no). Your location is not synced, and never goes to analytics or "
            "advertising. You can deny the permission and choose a place by hand instead."
        ),
        "camera": None,
        "sensors": (
            "The compass and motion sensors are used on your device to show where your phone is pointing. "
            "Sensor readings never leave the device."
        ),
    },
    {
        "slug": "photo-bestiary",
        "name": "Photo Bestiary",
        "tagline": "Photograph everyday objects and discover the creatures living in them.",
        "delete_path": "Settings → Account → Delete account",
        "notifications": False,
        "location": None,
        "camera": (
            "Photo Bestiary uses the camera to take still photos. Each photo is analysed <strong>on your "
            "device</strong> (Google ML Kit, on-device models) to choose a creature; the photo is deleted "
            "after the reveal unless you choose to keep it. Kept photos stay in the app's private storage, "
            "are re-encoded to strip location and other metadata, and are excluded from iCloud and Android "
            "backups. <strong>Photos are never uploaded, synced or shared with us or anyone else.</strong> "
            "If the on-device check finds a person in a photo, no creature is made from it. The app does not "
            "read your photo library."
        ),
        "sensors": None,
    },
]


def esc(s: str) -> str:
    return html.escape(s, quote=True)


def page(game: dict, kind: str, title: str, description: str, body: str) -> str:
    slug, name = game["slug"], game["name"]
    url = f"{SITE}/{slug}/" + ("" if kind == "home" else f"{kind}/")
    crumbs = (
        f'<a href="/">hungryemon</a> / <a href="/{slug}/">{esc(name)}</a>'
        + ("" if kind == "home" else f" / {esc(title)}")
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(name) if kind == "home" else f"{esc(title)} · {esc(name)}"}</title>
  <meta name="description" content="{esc(description)}" />
  <meta name="theme-color" content="#16161a" />
  <link rel="canonical" href="{url}" />
  <link rel="icon" href="/assets/favicon.svg" type="image/svg+xml" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/css/legal.css?v=1" />
</head>
<body>
  <main class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb">{crumbs}</nav>
{body}
    <footer class="doc">
      <p>{esc(name)} is made by {esc(OPERATOR)}, an independent developer in {COUNTRY}.
      Questions: <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
      <p><a href="/{slug}/privacy/">Privacy Policy</a> · <a href="/{slug}/terms/">Terms of Use</a> ·
      <a href="/{slug}/delete-account/">Delete your account</a></p>
    </footer>
  </main>
</body>
</html>
"""


def home(g: dict) -> str:
    n = esc(g["name"])
    body = f"""    <header class="doc">
      <span class="eyebrow">Game</span>
      <h1>{n}</h1>
      <p class="meta">{esc(g["tagline"])}</p>
    </header>
    <p>{n} is a game for iPhone, iPad and Android by {esc(OPERATOR)}. It plays fully offline; an optional
    account keeps your progress in step across devices.</p>
    <div class="cards">
      <a class="card" href="/{g["slug"]}/privacy/"><strong>Privacy Policy</strong>What the game collects, why, and your choices.</a>
      <a class="card" href="/{g["slug"]}/terms/"><strong>Terms of Use</strong>The rules for playing, purchases and subscriptions.</a>
      <a class="card" href="/{g["slug"]}/delete-account/"><strong>Delete your account</strong>Remove your account and cloud data, in the app or by email.</a>
    </div>
    <h2>Support</h2>
    <p>Found a bug, lost progress, or have a question about a purchase? Email
    <a href="mailto:{CONTACT}?subject={esc(g["name"]).replace(" ", "%20")}%20support">{CONTACT}</a>.</p>
"""
    return page(g, "home", g["name"], f"{g['name']}: {g['tagline']}", body)


def privacy(g: dict) -> str:
    n = esc(g["name"])
    device_items = []
    if g["location"]:
        device_items.append(f"<h3>Location</h3>\n    <p>{g['location']}</p>")
    if g["camera"]:
        device_items.append(f"<h3>Camera and photos</h3>\n    <p>{g['camera']}</p>")
    if g["sensors"]:
        device_items.append(f"<h3>Motion sensors</h3>\n    <p>{g['sensors']}</p>")
    if g["notifications"]:
        device_items.append(
            "<h3>Notifications</h3>\n    <p>Reminders are optional, scheduled on your device, and you can turn "
            "them off in the game or in your device settings. We don't use push-notification servers.</p>"
        )
    not_used = ["precise location" if g["location"] else "location"]
    if not g["camera"]:
        not_used.append("camera")
    not_used += ["microphone", "contacts", "photo library"]
    device_items.append(
        f"<h3>What the game never accesses</h3>\n    <p>{n} does not access your {', '.join(not_used[:-1])} "
        f"or {not_used[-1]}.</p>"
    )
    device_html = "\n    ".join(device_items)

    photo_line = (
        "<li><strong>Your photos are never collected.</strong> They are processed on your device only.</li>"
        if g["camera"]
        else ""
    )
    loc_line = (
        "<li>Approximate location is used for the weather or sky only and is never stored, synced, or used for "
        "ads or analytics.</li>"
        if g["location"]
        else ""
    )

    body = f"""    <header class="doc">
      <span class="eyebrow">Privacy Policy</span>
      <h1>{n} Privacy Policy</h1>
      <p class="meta">Effective {EFFECTIVE}</p>
    </header>

    <div class="summary">
      <ul>
        <li>You can play without giving us your name or email. The game starts with an anonymous account.</li>
        <li>If you choose to link Google or Apple, we receive the email address that provider shares, so your
        progress can follow you to other devices.</li>
        {photo_line}
        {loc_line}
        <li>We use Google Firebase (accounts, cloud save, analytics, crash reports), RevenueCat (purchases) and
        Google AdMob (ads in the free version). We don't sell your data.</li>
        <li>You can delete your account and cloud data in the app at any time: {esc(g["delete_path"])}.</li>
      </ul>
    </div>

    <h2>1. Who we are</h2>
    <p>{n} ("the game", "we", "us") is developed and operated by {esc(OPERATOR)}, an independent developer
    based in {COUNTRY}, who is the data controller for the personal data described here. Contact:
    <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>

    <h2>2. What we collect and why</h2>
    <div class="table-wrap"><table>
      <thead><tr><th>Data</th><th>Why</th><th>Service</th></tr></thead>
      <tbody>
        <tr><td>Account ID (a random user ID created when you first open the game)</td><td>To keep your
        progress, purchases and settings together and sync them between your devices</td><td>Firebase
        Authentication</td></tr>
        <tr><td>Email address and display name, <em>only if</em> you link a Google or Apple account</td><td>To
        let you sign in on another device and recover your progress</td><td>Firebase Authentication, Google
        Sign-In, Sign in with Apple</td></tr>
        <tr><td>Game progress: levels, collection, streaks, in-game currency balances, settings</td><td>Cloud
        save and cross-device sync</td><td>Cloud Firestore (Firebase)</td></tr>
        <tr><td>Purchase records: product, price, store transaction IDs, subscription status</td><td>To unlock
        what you bought on every device and restore purchases</td><td>RevenueCat, Apple App Store, Google
        Play</td></tr>
        <tr><td>Gameplay events (for example "level finished"), device model, OS version, app version,
        approximate country derived from IP</td><td>To understand which parts of the game work and fix what
        doesn't</td><td>Google Analytics for Firebase</td></tr>
        <tr><td>Crash reports and diagnostics</td><td>To find and fix crashes</td><td>Firebase
        Crashlytics</td></tr>
        <tr><td>Advertising identifier, IP address, device information, ad interactions</td><td>To show ads in
        the free version, limit how often they appear, and measure them</td><td>Google AdMob</td></tr>
      </tbody>
    </table></div>
    <p>Analytics events never include your email, your photos, your location or free text you type.</p>

    <h2>3. Device permissions</h2>
    {device_html}

    <h2>4. Advertising and your consent</h2>
    <p>The free version of {n} can show ads from Google AdMob. Players can remove them with a purchase.</p>
    <ul>
      <li><strong>EEA, UK and Switzerland:</strong> before any ad loads, the game shows Google's consent
      message (Google User Messaging Platform). Ads are personalised only if you agree, and you can change
      your choice later from the game's settings.</li>
      <li><strong>iPhone and iPad:</strong> the game doesn't ask to track you across other companies' apps
      and websites (App Tracking Transparency), so it never accesses your device's advertising
      identifier.</li>
      <li><strong>Android:</strong> you can reset or delete your advertising ID in your device's Google
      settings.</li>
      <li>US state privacy laws: we don't sell personal information for money. Where personalised advertising
      counts as "sharing", you can opt out with the consent controls above or by limiting ad tracking on
      your device.</li>
    </ul>
    <p>Google's use of data is described at
    <a href="https://policies.google.com/technologies/partner-sites">policies.google.com/technologies/partner-sites</a>.</p>

    <h2>5. Legal bases (EEA and UK players)</h2>
    <ul>
      <li><strong>Contract:</strong> your account, cloud save, sync and purchases, which you need to play as
      you chose.</li>
      <li><strong>Legitimate interests:</strong> crash reports, basic analytics and non-personalised ads, to
      keep the game working and free to play.</li>
      <li><strong>Consent:</strong> personalised advertising, and linking a Google or Apple account. You can
      withdraw consent at any time.</li>
    </ul>

    <h2>6. Who we share data with</h2>
    <p>Only the service providers named above, who process data for us under their own terms and data
    protection agreements: Google (Firebase, AdMob), RevenueCat, Apple and Google Play (payments),
    {"MET Norway (forecast requests with approximate coordinates only), " if g["location"] else ""}and
    authorities when the law requires it. These providers may store data in the United States and other
    countries; transfers out of the EEA and UK rely on the providers' Standard Contractual Clauses or
    equivalent safeguards.</p>

    <h2>7. How long we keep data</h2>
    <ul>
      <li>Account and cloud progress: until you delete your account. If you want inactive data removed, email
      us.</li>
      <li>Analytics: no longer than 14 months (the Google Analytics retention setting).</li>
      <li>Crash reports: about 90 days.</li>
      <li>Purchase records: as long as needed to give you what you paid for and to meet tax and accounting
      law; the stores keep their own records.</li>
    </ul>

    <h2>8. Your rights and choices</h2>
    <ul>
      <li><strong>Delete:</strong> in the app, {esc(g["delete_path"])} deletes your account and cloud copy
      straight away. You can also <a href="/{g["slug"]}/delete-account/">ask by email</a>.</li>
      <li><strong>Access, correct, export or object:</strong> email us and we'll answer within 30 days.</li>
      <li><strong>Ads:</strong> change your ad consent in the game's settings or your device settings, or buy
      the ad-free option.</li>
      <li><strong>Complain:</strong> you may contact your local data protection authority.</li>
    </ul>
    <p>Deleting the game from your device does not delete your cloud account; use the in-app option or email
    us. Subscriptions are managed by Apple or Google; deleting your account doesn't cancel them (see the
    <a href="/{g["slug"]}/terms/">Terms</a>).</p>

    <h2>9. Children</h2>
    <p>{n} is made for a general audience and is not directed at children under 13 (or the minimum age in
    your country). We don't knowingly collect personal data from children. If you believe a child has given
    us personal data, email us and we'll delete it.</p>

    <h2>10. Security</h2>
    <p>Data is sent over encrypted connections, and each player's cloud data can be read or written only by
    that player's own account. No method is perfectly secure, but we take reasonable measures to protect
    your data.</p>

    <h2>11. Changes</h2>
    <p>If this policy changes, we'll update the date above and, for significant changes, tell you in the
    game.</p>

    <h2>12. Contact</h2>
    <p>{esc(OPERATOR)} · <a href="mailto:{CONTACT}">{CONTACT}</a></p>
"""
    return page(g, "privacy", "Privacy Policy", f"How {g['name']} handles your data.", body)


def terms(g: dict) -> str:
    n = esc(g["name"])
    body = f"""    <header class="doc">
      <span class="eyebrow">Terms of Use</span>
      <h1>{n} Terms of Use</h1>
      <p class="meta">Effective {EFFECTIVE}</p>
    </header>

    <p>These terms are an agreement between you and {esc(OPERATOR)} ("we", "us"), the developer of {n}. By
    downloading or playing the game you accept them. If you don't agree, please don't use the game. Our
    <a href="/{g["slug"]}/privacy/">Privacy Policy</a> explains how we handle your data.</p>

    <h2>1. Licence to play</h2>
    <p>We give you a personal, non-exclusive, non-transferable, revocable licence to install and play {n} on
    devices you own or control, for your own non-commercial use. You may not copy, modify, resell, reverse
    engineer or exploit the game or its content except where the law allows it.</p>

    <h2>2. Your account</h2>
    <p>The game creates an anonymous account automatically. You can link a Google or Apple account to keep
    your progress across devices. If you never link one, losing or resetting your device may lose your
    progress. You're responsible for activity on your account. You can delete your account at any time
    ({esc(g["delete_path"])}).</p>

    <h2>3. Purchases and subscriptions</h2>
    <ul>
      <li>{n} is free to download. It offers optional in-app purchases, which may include a subscription,
      a one-time lifetime unlock, ad removal and cosmetic items. Prices are shown in the app before you buy
      and include any taxes the store applies.</li>
      <li>Payments are processed by Apple (App Store) or Google (Google Play) under their terms. We never see
      your card details.</li>
      <li><strong>Subscriptions renew automatically</strong> at the end of each period unless you cancel at
      least 24 hours before it ends. You can cancel or manage them in your App Store or Google Play account
      settings; cancelling stops the next renewal, and access continues until the paid period ends.</li>
      <li><strong>Free trials:</strong> if a trial is offered, the subscription starts and you are charged when
      the trial ends unless you cancel before then.</li>
      <li><strong>Refunds</strong> are handled by Apple or Google under their policies; we can't issue them
      directly. Nothing in these terms limits your statutory consumer rights.</li>
      <li>Purchases are tied to your store account and game account. Use "Restore purchases" in the game to
      get them back on a new device.</li>
    </ul>

    <h2>4. Virtual items and currencies</h2>
    <p>In-game currencies, items, unlocks and progress are a limited licence to use them inside the game.
    They have no cash value, can't be exchanged for money or transferred to other players, and may change as
    the game is balanced or updated. We don't sell randomised items for real money.</p>

    <h2>5. Ads</h2>
    <p>The free version may show ads, including optional ads you choose to watch for a reward. Rewards are
    given only after the ad completes. Buying ad removal stops ads that play automatically; optional reward
    ads may stay available if you want them.</p>

    <h2>6. Fair play</h2>
    <p>Don't cheat, use bots or exploits, tamper with the game or its servers, interfere with other players,
    or use the game to break the law. We may reset progress gained unfairly, or suspend accounts that break
    these rules.</p>

    <h2>7. Our content</h2>
    <p>The game, its code, art, text, music and characters are owned by us or our licensors and are
    protected by copyright and other laws. Third-party licences are listed in the app's settings.</p>

    <h2>8. Changes and availability</h2>
    <p>We may update, change or stop parts of the game, for example to fix bugs, rebalance or add content.
    We'll try to give notice before ending the game; if we stop it while a paid subscription is active, you
    can ask the store for a pro-rata refund. Features that need the internet (sync, purchases, ads,
    forecasts) may sometimes be unavailable.</p>

    <h2>9. Disclaimer</h2>
    <p>The game is provided "as is" and "as available". To the extent the law allows, we disclaim implied
    warranties, including fitness for a particular purpose and non-infringement. Play safely and be aware
    of your surroundings{", especially outdoors at night" if g["slug"] == "sky-hunt" else ""}.</p>

    <h2>10. Limitation of liability</h2>
    <p>To the extent the law allows, we aren't liable for indirect, incidental or consequential damages, or
    for lost data or progress, and our total liability is limited to the amount you paid for the game in the
    12 months before the claim. Some places don't allow these limits, so they may not apply to you.</p>

    <h2>11. Ending this agreement</h2>
    <p>You can stop at any time by deleting your account and the game. We may end your licence if you
    seriously break these terms. Sections 4, 7, 9, 10 and 13 continue after it ends.</p>

    <h2>12. Apple App Store</h2>
    <p>If you got the game from the App Store: these terms are between you and us, not Apple. Apple has no
    obligation to provide maintenance or support. If the game fails to meet any applicable warranty, you may
    notify Apple for a refund of the purchase price (if any); Apple has no other warranty obligation. Apple
    isn't responsible for claims relating to the game (product liability, legal or regulatory compliance,
    consumer protection or intellectual property); we are, as these terms describe. You confirm you aren't
    in a country subject to a U.S. Government embargo and aren't on a U.S. Government restricted-party list.
    Apple and its subsidiaries are third-party beneficiaries of these terms and may enforce them against
    you. Apple's standard Licensed Application End User License Agreement also applies where these terms
    don't cover something.</p>

    <h2>13. Law and disputes</h2>
    <p>These terms are governed by the laws of {COUNTRY}. If you are a consumer living elsewhere, you also
    keep the protection of the mandatory laws of your country, and you can bring claims in your local
    courts. Please email us first; most problems can be solved quickly.</p>

    <h2>14. Changes to these terms</h2>
    <p>We may update these terms. We'll change the date above and, for significant changes, tell you in the
    game. Continuing to play after changes take effect means you accept them.</p>

    <h2>15. Contact</h2>
    <p>{esc(OPERATOR)} · <a href="mailto:{CONTACT}">{CONTACT}</a></p>
"""
    return page(g, "terms", "Terms of Use", f"The terms for playing {g['name']}.", body)


def delete_account(g: dict) -> str:
    n = esc(g["name"])
    subject = f"Delete my {g['name']} account".replace(" ", "%20")
    body = f"""    <header class="doc">
      <span class="eyebrow">Account deletion</span>
      <h1>Delete your {n} account</h1>
      <p class="meta">Developer: {esc(OPERATOR)}</p>
    </header>

    <h2>In the app (fastest)</h2>
    <p>Open {n} and go to <strong>{esc(g["delete_path"])}</strong>, then confirm. Your account and its cloud
    copy are deleted straight away, and the device starts fresh.</p>

    <h2>By email</h2>
    <p>If you no longer have the game installed, email
    <a href="mailto:{CONTACT}?subject={subject}">{CONTACT}</a> with the subject "Delete my {n} account".
    Include the email of the Google or Apple account you linked. We'll confirm and delete within 30 days.</p>
    <p>If you never linked Google or Apple, your account is anonymous and we can't find it from an email
    address. Reinstall the game on the same device and use the in-app option, or send us the approximate
    date you last played and your device model and we'll do our best to locate it.</p>

    <h2>What is deleted</h2>
    <ul>
      <li>Your sign-in account (anonymous ID and any linked Google or Apple email).</li>
      <li>Your cloud save: progress, collection, streaks, in-game currency balances and settings.</li>
    </ul>

    <h2>What is kept, and for how long</h2>
    <ul>
      <li>Purchase records kept by Apple, Google and RevenueCat, for as long as tax and accounting law
      requires. Deleting your account does <strong>not</strong> cancel a subscription; cancel it in your App
      Store or Google Play settings.</li>
      <li>Analytics and crash data, which isn't linked to your email, expires on its own (up to 14 months for
      analytics, about 90 days for crash reports).</li>
    </ul>
    <p>Progress saved only on your device is removed when you uninstall the game.</p>
"""
    return page(g, "delete-account", "Delete your account", f"How to delete your {g['name']} account and data.", body)


def main() -> None:
    urls = []
    for g in GAMES:
        for kind, fn in (("", home), ("privacy", privacy), ("terms", terms), ("delete-account", delete_account)):
            out = ROOT / g["slug"] / kind / "index.html" if kind else ROOT / g["slug"] / "index.html"
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(fn(g), encoding="utf-8")
            urls.append(f"{SITE}/{g['slug']}/" + (f"{kind}/" if kind else ""))
            print("wrote", out.relative_to(ROOT))
    sitemap = ROOT / "sitemap.xml"
    entries = "".join(
        f"  <url>\n    <loc>{u}</loc>\n    <changefreq>yearly</changefreq>\n    <priority>0.3</priority>\n  </url>\n"
        for u in urls
    )
    sitemap.write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"  <url>\n    <loc>{SITE}/</loc>\n    <changefreq>monthly</changefreq>\n    <priority>1.0</priority>\n  </url>\n"
        f"{entries}</urlset>\n",
        encoding="utf-8",
    )
    print("wrote sitemap.xml")


if __name__ == "__main__":
    main()
