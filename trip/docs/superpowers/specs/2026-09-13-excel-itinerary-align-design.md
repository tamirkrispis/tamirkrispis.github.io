# Design: Align Cruise Guide to Excel itinerary + Rome PDF + rename לנון

Date: 2026-09-13  
Project: Cruise-Guide (Hebrew RTL static family vacation site)

## Goal

Rewrite the site so the family’s locked plan matches `assets/תוכנית מסע.xlsx`, add a link to `assets/Michal_Milrad_Rome_2026.pdf`, replace the family name **קריספיס → לנון**, and keep a small set of backup options per day.

## Decisions (locked)

| Topic | Decision |
|-------|----------|
| Scope depth | Full rewrite: day pages + home summary aligned to Excel as primary plan |
| Source of truth | Excel wins for flights, hotels, activities, show times |
| Vatican | Pasta/tiramisu workshop near Vatican area on 16/9 is kept; **no** Vatican / St. Peter’s visit |
| 23/9 | Cinque Terre (Manarola, Vernazza, Monterosso) — ignore Florence/Pisa header in Excel |
| Options model | Option A = Excel plan (score 10); keep 1–2 lighter backups where useful |
| Family name | **לנון** everywhere (UI + CONTEXT) |
| Implementation approach | Update `generate_days.py`, regenerate day HTML, hand-update shared pages |

## Excel → site facts

| Item | New value |
|------|-----------|
| Outbound | El Al **LY285**, depart ~09:00, land FCO **11:45** (14/9) |
| Return | El Al **LY386**, depart ~**10:00** (25/9) |
| First hotel | Colonna Collection (unchanged) |
| Last hotel | **Hotel Accademia** (24/9) |
| 14/9 | Arrival → hotel check-in → Trevi area evening |
| 15/9 | Colosseum (Excel places it in evening; plan A centers Colosseum that day) |
| 16/9 | GetYourGuide pasta + tiramisu workshop near Vatican area |
| 17/9 | Taxi to embarkation port; evening **America’s Got Talent 19:00** |
| 18/9 | Sorrento morning + Naples market pizza afternoon |
| 19/9 | Crown Edge **09:15** · Izumi Hibachi **12:30** · Charlie Chocolate Kingdom **15:30** |
| 20/9 | Sagrada · La Rambla · **Shockwave 20:00** |
| 21/9 | Palma (Excel cells empty → keep cathedral / old town as A; beach as backup) |
| 22/9 | **נורית גאון** Provence tour; taxi pickup **09:30**, return **15:30** |
| 23/9 | Cinque Terre: Manarola, Vernazza, Monterosso |
| 24/9 | Disembark ~07:30 → Hotel Accademia |
| 25/9 | Transfer to FCO for LY386 ~10:00 |

## Content model

### Home (`index.html`)

1. Brand / titles / meta: משפחת **לנון**
2. **Summary table** modeled on the Excel (morning / noon / evening per date), with links to `days/DD-MM.html`
3. Mini-cards text aligned to Option A for each day
4. Important links: add Rome guide PDF (`assets/Michal_Milrad_Rome_2026.pdf`, open in new tab)
5. Flight / hotel meta lines updated to Excel facts

### Day pages (via `generate_days.py`)

For each day 14–25:

- **Option A (10):** Excel morning → noon → evening as timeline on dedicated plan page
- **1–2 backups:** shorter / weather / lower-energy variants only (not the old full option set)
- Default pick copy points at A
- Place intro cards, costs, meeting point, Super-Tips, taxi box retained in existing patterns
- Rome days (14–16, 24–25): visible link to Michal Milrad Rome PDF
- Regenerate removes obsolete option letters (e.g. old 18-E, 23-F) that are no longer defined

Suggested backups (non-exhaustive):

| Day | A | Backups |
|-----|---|---------|
| 14 | Flight + Colonna + Trevi | Short evening only |
| 15 | Colosseum day | Lighter ruins / rest afternoon |
| 16 | Pasta workshop | Pantheon stroll / rest |
| 17 | Port taxi + AGT | Train transfer |
| 18 | Sorrento + pizza | Pizza-only city OR short Pompeii |
| 19 | Booked ship day | Skip Charlie / rest-only |
| 20 | Sagrada + Ramblas + Shockwave | Ramblas-only shorter |
| 21 | Cathedral + old town | Beach / light |
| 22 | Nurit Gaon Provence | Vieux Port only |
| 23 | CT 3 villages | 2 villages / stay on ship |
| 24 | Accademia + light evening | Rest-only after transfer |
| 25 | LY386 transfer | Earlier buffer leave |

### Shared pages

- `hotels.html` — recommend / document **Hotel Accademia** as last-night choice; rename לנון
- `prebook.html` — flights LY285/LY386; Accademia; pasta workshop; Provence tour; ship shows/experiences; still **no Vatican visit** bookings; rename
- `cruise-info.html` — Crown Edge 09:15, Charlie 15:30, AGT, Shockwave; rename
- `excursions.html`, `taxis.html`, `packing.html` — rename only unless copy contradicts Excel
- `CONTEXT.md` — full fact sync + rename + open items refresh

## Out of scope

- Parsing the `.xlsx` at build time
- Live Royal Caribbean Cruise Planner sync
- Designing a new visual theme (keep existing CSS / Rome vs sea themes)
- Translating or extracting text from the Rome PDF (link only)

## Risks / notes

- Repo may not be a git repository yet; design/plan docs are still saved under `docs/superpowers/`
- Excel spelling quirks (colonna colection, Amricas got talent) should be corrected in Hebrew UI copy
- “Near Vatican” workshop must not reintroduce Vatican Museums / St. Peter’s as a plan
- Palma lacks Excel detail — A is a reasonable fill, marked as family default not Excel-verbatim

## Success criteria

1. Home shows Excel-style morning/noon/evening table for 14–25/9
2. Every day’s default Option A matches the locked Excel plan (with Palma filled as above)
3. PDF guide linked from home + Rome days
4. No remaining user-facing **קריספיס**; all **לנון**
5. Flights, Accademia, booked ship items, Provence tour, workshop reflected in prebook/cruise-info/CONTEXT
6. `python3 generate_days.py` regenerates days consistently with the new content
