# CONTEXT.md — Cruise Guide (Hebrew Family Vacation)

## What this project is

Offline-friendly **Hebrew RTL static website** for a family vacation:

- **Who:** Family Lennon (לנון) — ולנטינו (48), ג'ולייט (49), טיילר (13), ליי-ליי (10, ADHD — limited patience for long waits, heat, staying in one place)
- **When:** 14–25 September 2026
- **Where:** Rome (pre) → Royal Caribbean *Legend of the Seas* (Civitavecchia round-trip) → Rome (1 night, Hotel Accademia) → FCO → Israel (El Al)

## Key trip facts

| Item | Detail |
|------|--------|
| Arrival | FCO 14 Sep ~**11:45** · El Al **LY285** (depart ~09:00) |
| Departure | FCO 25 Sep ~**10:00** · El Al **LY386** |
| Luggage | 2 suitcases + 2 trolleys |
| First hotel | Colonna Collection, Via della Colonna Antonina 41, Rome |
| Last hotel | **Hotel Accademia**, Piazza Accademia di San Luca 75 (24→25 Sep) — booked |
| Ship | Legend of the Seas, cabin **7680**, deck 7, category F1 |
| Dining | My Time, prefer 17:30–18:30 |
| Diet | No pork, no shellfish/seafood; **fish OK**; not kosher |
| Insurance | Harel — 24/7 **+972-3-7547030** · WhatsApp **052-7544589** (no full policy number in the repo) |
| Transfers | **Romio Transportation Services**, voucher **Sharon Krispis**, 4 pax — see `emergency.html#transfers` |
| Source plan | `assets/תוכנית מסע.xlsx` + Rome guide `assets/Michal_Milrad_Rome_2026.pdf` |

## Romio transfers (booked)

Coordination WhatsApp: `+972-50-955-6074` · Emergency WA: `+972-58-691-1946` and `+39 340 909 8285` · Hebrew tours (not medical): `052-8018872`

| Date | Pickup | Route | Cost |
|------|--------|-------|------|
| 14/9 | 11:45 | FCO → Colonna Collection | €85 |
| 17/9 | 10:30 | Colonna → Legend of the Seas | €170 + €29 PayPal |
| 24/9 | 09:00 | Ship (~07:30 disembark, wait at port) → Hotel Accademia | €170 + €29 PayPal |
| 25/9 | 06:30 | Accademia → FCO for LY386 ~10:00 | €85 |

## Cruise ports (app times) + locked plans

1. 17 Sep — Embark Civitavecchia (~20:00 sail) · **Romio 10:30** · **AGT 19:00**
2. 18 Sep — Naples ~07:30–18:30 · **Sorrento AM + Naples market pizza PM**
3. 19 Sep — Sea day — **Crown Edge 09:15**, **Izumi Hibachi 12:30**, **Charlie Chocolate 15:30**
4. 20 Sep — Barcelona ~05:30–16:30 · **Sagrada + Ramblas** · **Shockwave 20:00**
5. 21 Sep — Palma ~08:30–15:30 · cathedral/old town default (Excel had no detail) · **Yom Kippur** — Israeli missions closed
6. 22 Sep — Marseille ~09:30–17:30 · **נורית גאון Provence tour 09:30–15:30**
7. 23 Sep — La Spezia ~09:00–19:30 · **Cinque Terre: Manarola, Vernazza, Monterosso**
8. 24 Sep — Disembark ~**07:30** · **Romio 09:00** → Hotel Accademia

## Site structure

```
index.html          Home + Excel-style morning/noon/evening summary table
emergency.html      Panic-first: 112, local numbers, MFA, embassies, Harel, Romio transfers
prebook.html        Booking checklist aligned to Excel
taxis.html          Safe taxi apps by city (Romio for FCO/port)
packing.html        Packing lists (localStorage checkboxes)
cruise-info.html    Ship, cabin, dining, ports, booked shows
excursions.html     Typical RC shore excursions (reference)
days/14-09.html …   Day overview pages (Option A = Excel plan)
days/14-09-A.html … Dedicated option plan pages
assets/             Photos + favicon.png (rubber duck) + Michal_Milrad_Rome_2026.pdf + תוכנית מסע.xlsx
css/styles.css
js/app.js
generate_days.py    Regenerates day + option pages
docs/superpowers/   Design specs + implementation plans
```

## Content conventions

- All user-facing copy in **Hebrew**, `dir="rtl"`.
- Family name in UI: **לנון** (not קריספיס). Romio voucher name **Sharon Krispis** is shown only on transfer cards so the driver can match.
- Each day: **Option A (score 10) = Excel plan**; 1–2 lighter backups only.
- Every day includes: weather strip, **Super-Tips** (kid-safe ADHD pacing — never say ADHD/ליי-ליי in those tips on the website), default pick, place intro cards, cost comparison, meeting point, exit ramp, taxi tips.
- Option titles link to `days/DD-MM-X.html` with timeline + checklists.
- Names in UI: **ולנטינו**, **ג'ולייט**, **טיילר**, **ליי-ליי**.
- Rome days link to Michal Milrad PDF.
- Do not mention the Vatican / St. Peter’s in user-facing copy (not planned).
- Prices marked as estimates (משוער) except booked Romio amounts which are actual.
- Emergency numbers: EU **112** + local police/ambulance/fire + Israeli missions + MFA Situation Room (+972-2-530-3155 / WA +972-50-507-3969).

## How to edit

1. Small copy tweaks: edit the HTML file directly.
2. Day options / scores: edit `generate_days.py` then run `python3 generate_days.py`.
3. Do not put secrets (passport numbers, full insurance policy) in the repo; use placeholders.
4. Keep `CONTEXT.md` in sync when trip facts change.

## Design notes

- Fonts: Arial site-wide
- **Rome days** (14–16, 24–25): `theme-rome`
- **Cruise / sea days** (17–23): `theme-sea`
- Print CSS hides nav chrome; `.call-btn` on `emergency.html` still prints
- Tap-to-call: `.call-row` / `.call-btn` (min 44px)
- Favicon: rubber duck at `assets/favicon.png`

## Open items for the family

- [x] Harel emergency phone / WhatsApp (policy number stays off the site)
- [x] Book FCO/hotel/port transfers (Romio)
- [x] Hotel Accademia — last night (per Excel)
- [ ] Book Colosseum timed tickets
- [ ] Book GetYourGuide pasta + tiramisu workshop (16/9)
- [ ] Confirm Nurit Gaon Provence pickup details (22/9)
- [ ] Book private car Sorrento + Naples (18/9)
- [ ] Book Sagrada timed tickets (20/9)
- [ ] Set My Time dining in Royal app
- [ ] Reserve AGT 19:00 (17/9), Shockwave 20:00 (20/9), Charlie 15:30 (19/9) in app
- [x] Crown Edge Experience — 19 Sep **09:15**
- [x] Izumi Hibachi — 19 Sep 12:30 (request no pork/shellfish)
- [ ] Install FreeNow + itTaxi (+ Cabify)
- [ ] WhatsApp group + meeting-point habit
- [ ] Install TravIL (MFA) + Harel travel app

## Super-Tips (kid-facing)

On the website, ADHD pacing tips are labeled **Super-Tips** only — do not mention ADHD or ליי-ליי by name in those boxes, exit ramps, or checklists she might read.
