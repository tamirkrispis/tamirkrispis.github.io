# CONTEXT.md — Cruise Guide (Hebrew Family Vacation)

## What this project is

Offline-friendly **Hebrew RTL static website** for a family vacation:

- **Who:** Family Krispis (קריספיס) — טמיר (48), Sharon (49), Yuval (13), Roni (10, ADHD — limited patience for long waits, heat, staying in one place)
- **When:** 14–25 September 2026
- **Where:** Rome (pre) → Royal Caribbean *Legend of the Seas* (Civitavecchia round-trip) → Rome (1 night) → FCO → Israel (El Al)

## Key trip facts

| Item | Detail |
|------|--------|
| Arrival | FCO 14 Sep ~12:45 |
| Departure | FCO 25 Sep ~11:00 El Al |
| Luggage | 2 suitcases + 2 trolleys |
| First hotel | Colonna Collection, Via della Colonna Antonina 41, Rome |
| Last hotel | TBD — see `hotels.html` (default recommend: Repubblica / Via Nazionale with elevator; avoid south Termini) |
| Ship | Legend of the Seas, cabin **7680**, deck 7, category F1 |
| Dining | My Time, prefer 17:30–18:30 |
| Diet | No pork, no shellfish/seafood; **fish OK**; not kosher |
| Insurance | Harel (Israel) — emergency contacts TBD |
| Out of scope | Vatican / St. Peter’s (explicitly excluded) |

## Cruise ports (app times)

1. 17 Sep — Embark Civitavecchia (~20:00 sail)
2. 18 Sep — Naples ~07:30–18:30
3. 19 Sep — Sea day — **booked:** Crown Edge Experience **09:00**, Izumi Hibachi **12:30** (diet: no pork/shellfish); light evening only
4. 20 Sep — Barcelona ~05:30–16:30
5. 21 Sep — Palma ~08:30–15:30
6. 22 Sep — Marseille ~09:30–17:30
7. 23 Sep — La Spezia ~09:00–19:30 (priority: **Cinque Terre 2–3 villages**)
8. 24 Sep — Disembark Civitavecchia ~07:00

## Site structure

```
index.html          Home overview
hotels.html         Last-night hotel comparison + safety zones
prebook.html        Booking checklist + costs
taxis.html          Safe taxi apps by city (FreeNow, itTaxi, Cabify)
packing.html        Packing lists (localStorage checkboxes)
cruise-info.html    Ship, cabin, dining, port table
excursions.html     Typical RC shore excursions by port (est. prices + popularity + family grades)
days/14-09.html … days/25-09.html   Day overview pages
days/14-09-A.html …                 Dedicated option plan pages (45 total)
assets/             Destination photos
css/styles.css
js/app.js
generate_days.py    Regenerates day + option pages from embedded content
```
## Content conventions

- All user-facing copy in **Hebrew**, `dir="rtl"`.
- Each day has **multiple graded options (1–10)** for *this* family, not generic tourism scores.
- Every day includes: weather strip, **Super-Tips** (kid-safe label for ADHD pacing — never say ADHD/Roni in those tips on the website), default pick, **place intro cards** (what/why + travel time + image), cost table, meeting point, exit ramp, taxi tips.
- **Each option title is clickable** → dedicated plan page `days/DD-MM-X.html` with timeline + checklists (book / transport / bring).
- Father’s Hebrew name in UI: **טמיר** (not תמיר).
- Each day option shows **עלות משוערת ליום (משפחה ×4)** plus an auto-built comparison table of all options for that day.
- Prices marked as estimates (משוער) — update closer to travel.
- **Savings tips:** `prebook.html` sections «איך לחסוך — רומא» and «איך לחסוך — הספינה»; short recap on `cruise-info.html` and day 14 / day 19.
- **Shore excursions:** `excursions.html` lists *typical* Royal Caribbean Western Med shore tours (not a live Cruise Planner dump — verify in the Royal app). Dual grades: popularity + family suitability. Prefer DIY day-page options unless ship guarantee is needed.
- Maps: OpenStreetMap embeds + Google Maps links.

## Itinerary preferences (locked updates)

- Barcelona **Sunday 20 Sep**: plan Sagrada + Ramblas + Gothic food only (La Boqueria closed Sundays — **removed from day plan**); Sagrada tourist entry often from ~10:30
- Palma **Monday 21 Sep**: Cathedral open for tourists (~10:00–17:15 in season)
- Correct weekdays 2026: 14 Mon … 25 Fri

- Naples: pizza city **or** Pompeii morning + market/pizza combo with private car
- Cinque Terre: **2–3 villages** with activities (food, harbor, photos) — not scenery-only
- Outlets: not planned
- Food tours: Eating Europe (9), Devour Testaccio (8), private Eating Europe (9)

## How to edit

1. Small copy tweaks: edit the HTML file directly.
2. Day options / scores: edit `generate_days.py` then run `python3 generate_days.py`.
3. Do not put secrets (passport numbers, full insurance policy) in the repo; use placeholders.

## Design notes

- Fonts: Arial site-wide
- **Rome days** (14–16, 24–25): `theme-rome` — warm yellow / gold header + sand background
- **Cruise / sea days** (17–23): `theme-sea` — blue sea-like background + ocean header
- Home mini-cards use the same `theme-rome` / `theme-sea` classes
- Print CSS hides nav chrome

## Open items for the family

- [ ] Confirm last-night hotel booking
- [ ] Fill Harel emergency phone / policy number
- [ ] Book transfers and Colosseum when windows open
- [ ] Book Sagrada timed tickets (Barcelona)
- [ ] Book Rome food tour (Eating Europe / Devour)
- [ ] Set My Time dining in Royal app
- [x] Crown Edge Experience — 19 Sep 09:00
- [x] Izumi Hibachi — 19 Sep 12:30 (request no pork/shellfish)
- [ ] Install FreeNow + itTaxi (+ Cabify)
- [ ] WhatsApp group + meeting-point habit


## Super-Tips (kid-facing)
On the website, ADHD pacing tips are labeled **Super-Tips** only — do not mention ADHD or Roni by name in those boxes, exit ramps, or checklists she might read.
