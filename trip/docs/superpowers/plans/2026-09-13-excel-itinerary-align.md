# Excel Itinerary Align Implementation Plan

> **For agentic workers:** Execute inline or via subagent-driven-development. Steps use checkbox syntax.

**Goal:** Align the Hebrew Cruise Guide to `assets/תוכנית מסע.xlsx`, link the Rome PDF, rename family to לנון, regenerate day pages.

**Architecture:** Update content in `generate_days.py` (source of truth for day/option HTML), regenerate `days/*.html`, then hand-update shared pages (`index`, hotels, prebook, cruise-info, etc.) and `CONTEXT.md`.

**Tech Stack:** Static HTML/CSS/JS · Python3 generator · no build server

## Global Constraints

- All user-facing copy Hebrew RTL; father name **טמיר**
- Family name **לנון** (not קריספיס)
- Excel is source of truth for flights/hotels/activities/shows
- Vatican visit still excluded; pasta workshop near Vatican area OK
- 23/9 = Cinque Terre 3 villages
- Option A = Excel plan (10); 1–2 backups only
- Super-Tips must not name ADHD/Roni
- No git commits unless user asks (repo may lack `.git`)

---

### Task 1: Generator brand + Rome PDF helper + rewrite day data

**Files:**
- Modify: `generate_days.py`

- [ ] Replace brand `קריספיס` → `לנון` in `header()`
- [ ] Add `rome_guide_html(depth=1)` linking `../assets/Michal_Milrad_Rome_2026.pdf`
- [ ] Rewrite `days["14-09"]` … `days["25-09"]` per design spec (A + 1–2 backups; Excel facts)
- [ ] Run: `python3 generate_days.py` — expect wrote 12 days + option pages; stale option files removed

### Task 2: Home summary table + PDF + rename

**Files:**
- Modify: `index.html`

- [ ] Rename לנון; flights LY285/11:45 and LY386/10:00; Accademia in meta
- [ ] Add morning/noon/evening summary table for 14–25
- [ ] Align mini-cards to Option A
- [ ] Add Rome PDF under important links

### Task 3: Shared pages + CONTEXT

**Files:**
- Modify: `hotels.html`, `prebook.html`, `cruise-info.html`, `excursions.html`, `taxis.html`, `packing.html`, `CONTEXT.md`

- [ ] Global rename לנון
- [ ] hotels: Accademia as booked/recommended last night
- [ ] prebook: workshop, Provence tour, Accademia, flights, Crown Edge 09:15, Charlie; drop Eating Europe as primary
- [ ] cruise-info: show times + Crown Edge 09:15
- [ ] CONTEXT sync open items

### Task 4: Verify

- [ ] `rg 'קריספיס' .` → no hits in html/py/md (except maybe this plan/spec historical)
- [ ] Spot-check day 16/18/19/22/24 HTML for Excel plan
- [ ] Confirm PDF path resolves from `index.html` and a Rome day page
