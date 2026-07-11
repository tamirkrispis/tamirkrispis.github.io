#!/usr/bin/env python3
"""Generate Hebrew cruise guide day pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DAYS = ROOT / "days"
IMG = "../assets"

FONTS = ""

DAY_IDS = [
    "14-09", "15-09", "16-09", "17-09", "18-09", "19-09",
    "20-09", "21-09", "22-09", "23-09", "24-09", "25-09",
]

# Rome land days = warm yellow; cruise block (embark→last port) = sea blue
ROME_DAYS = {"14-09", "15-09", "16-09", "24-09", "25-09"}


def day_theme(day_id):
    return "theme-rome" if day_id in ROME_DAYS else "theme-sea"


def nav_days(current=None, prefix="../"):
    links = []
    for d in DAY_IDS:
        cur = ' aria-current="page"' if d == current else ""
        links.append(f'<a href="{prefix}days/{d}.html"{cur}>{d[:2]}</a>')
    return "\n      ".join(links)


def header(current=None, depth=0):
    p = "../" if depth else ""
    home = f"{p}index.html"
    return f"""  <header class="site-header">
    <p class="brand"><a href="{home}" style="color:#fff;text-decoration:none">משפחת קריספיס</a></p>
    <p class="tagline">מדריך החופשה · רומא · Legend of the Seas · 14–25 בספטמבר 2026</p>
    <nav class="nav-days" aria-label="ימי הטיול">
      {nav_days(current, p)}
    </nav>
    <nav class="nav-links">
      <a href="{home}">בית</a>
      <a href="{p}hotels.html">מלונות</a>
      <a href="{p}prebook.html">להזמין מראש</a>
      <a href="{p}taxis.html">מוניות בטוחות</a>
      <a href="{p}packing.html">אריזה</a>
      <a href="{p}cruise-info.html">הספינה</a>
      <a href="{p}excursions.html">סיורי חוף</a>
    </nav>
  </header>"""


def footer(depth=0):
    p = "../" if depth else ""
    return f"""  <footer class="site-footer">
    מחירים משוערים — לעדכון לפני הנסיעה · <a href="{p}index.html">חזרה לבית</a>
  </footer>
  <script src="{p}js/app.js"></script>"""


def day_nav(prev_id, next_id):
    prev = f'<a class="btn btn-secondary" href="{prev_id}.html">← יום קודם</a>' if prev_id else "<span></span>"
    nxt = f'<a class="btn" href="{next_id}.html">יום הבא →</a>' if next_id else "<span></span>"
    return f'<nav class="day-nav">{prev}{nxt}</nav>'


def place_card(img, title, blurb, travel, tip=""):
    tip_html = f'<p class="note">{tip}</p>' if tip else ""
    return f"""
        <article class="place-card">
          <img src="{IMG}/{img}" alt="{title}" loading="lazy" />
          <div class="place-body">
            <span class="travel">⏱ {travel}</span>
            <h3>{title}</h3>
            <p>{blurb}</p>
            {tip_html}
          </div>
        </article>"""


def taxi_box(city_key):
    data = {
        "rome": (
            "רומא",
            "<strong>מומלץ:</strong> אפליקציות <strong>FreeNow</strong> או <strong>itTaxi</strong> (מוניות מורשות עם מעקב).<br />"
            "בשדה FCO — רק מוניות לבנות רשמיות מתור המוניות (תעריף קבוע למרכז ~€50–55).<br />"
            "<strong>לא:</strong> אנשים שמציעים נסיעה בתוך האולם.",
        ),
        "civitavecchia": (
            "צ׳יוויטווקיה / נמל",
            "<strong>מומלץ:</strong> העברה פרטית מראש (הכי בטוח עם מזוודות).<br />"
            "גיבוי: מונית רשמית מתחנת הרכבת/נמל · או FreeNow אם זמין.<br />"
            "אל תעלו על רכב בלי מונה/רישוי ברור.",
        ),
        "naples": (
            "נאפולי",
            "<strong>מומלץ:</strong> <strong>FreeNow</strong> / <strong>itTaxi</strong> · או מונית לבנה עם מונה מהנמל.<br />"
            "לפומפיי — עדיף רכב פרטי/סיור עם חזרה מובטחת לספינה.<br />"
            "שמרו על תיקים צמודים; העיר תוססת וצפופה.",
        ),
        "barcelona": (
            "ברצלונה",
            "<strong>מומלץ:</strong> <strong>FreeNow</strong> (הכי נפוץ) · גיבוי <strong>Cabify</strong>.<br />"
            "מוניות שחור־צהוב רשמיות עם ירוק דולק.<br />"
            "מטרו גם מצוין בין Sagrada / מרכז — אבל עם ילדים עייפים מונית נוחה יותר.",
        ),
        "palma": (
            "פלמה",
            "<strong>מומלץ:</strong> מונית רשמית מתור הנמל · אפליקציית <strong>FreeNow</strong> אם זמינה.<br />"
            "נסיעות קצרות — ודאו שהמונה דולק.",
        ),
        "marseille": (
            "מרסיי",
            "<strong>מומלץ:</strong> <strong>FreeNow</strong> · מוניות רשמיות מתור הנמל.<br />"
            "לאקס־אן־פרובאנס — סיור ספינה או העברה פרטית עדיפים על מונית ספונטנית הלוך־חזור.",
        ),
        "laspezia": (
            "לה ספציה / צ׳ינקווה טרה",
            "בין הכפרים — <strong>רכבת</strong> (לא מונית).<br />"
            "מהנמל לתחנה: שאטל ספינה / מונית רשמית קצרה.<br />"
            "גיבוי מונית: תור רשמי ליד התחנה אם פספסתם רכבת אחרונה.",
        ),
    }
    title, body = data[city_key]
    return f"""
    <section class="section">
      <h2>מוניות בטוחות — {title}</h2>
      <div class="taxi-box">{body}
        <p class="note" style="margin-top:0.5rem">פירוט לכל היעדים: <a href="../taxis.html">עמוד מוניות בטוחות</a></p>
      </div>
    </section>"""


OPTION_REGISTRY = {}


def _slug_action(day_id, letter, i, label):
    import re
    base = re.sub(r"\W+", "-", f"{day_id}-{letter}-{i}-{label}")[:48]
    return base.strip("-")


def build_plan(day_id, letter, title, grade, why, pros, cons, cost, time, when, family, recommended):
    """Build extended plan content + checklists for an option page."""
    book = [
        ("decide", f"מחליטים סופית על אפשרות {letter} ליום זה"),
        ("weather", "בודקים תחזית מזג אוויר בבוקר / ערב לפני"),
    ]
    transport = [
        ("taxi-app", "מוודאים ש־FreeNow / itTaxi / Cabify מותקנים ופעילים"),
    ]
    bring = [
        ("water", "בקבוקי מים"),
        ("hats", "כובעים לכל המשפחה"),
        ("spf", "קרם הגנה"),
        ("powerbank", "מטען נייד"),
        ("snack", "חטיף לדרך"),
        ("headphones", "אוזניות / טאבלט לדרך"),
        ("cash", "קצת מזומן יורו + כרטיס"),
        ("docs", "צילום דרכונים בטלפון + אישורי הזמנות"),
    ]
    timeline = [
        f"לפני היציאה: סימון צ׳ק־ליסט + בדיקת שעות פתיחה/כל־אבורד",
        f"משך משוער לפעילות: {time}",
        "הפסקת צל / מזגן / גלידה באמצע",
        "סיום עם באפר זמן לפני החזרה (מלון / ספינה / טיסה)",
    ]
    t = title
    tl = title.lower()

    if day_id == "14-09":
        transport.append(("fco-transfer", "שיריינו העברה FCO→מלון / מונית רשמית בשדה"))
        if letter == "A":
            book.append(("rest-reserve", "שיריינו מסעדה ליד המלון (Armando / Emma וכו׳)"))
            timeline = [
                "12:45 נחיתה → דרכונים → איסוף מזוודות",
                "העברה למלון (~45–60 דק׳) → צ׳ק־אין / השארת מזוודות",
                "מקלחת קצרה + מים",
                "הליכה לטרווי לצילום קצר (~10–15 דק׳ במקום)",
                "גלידה → ארוחה מוקדמת → שינה",
            ]
        if letter == "C":
            book.append(("colo-skip", "לא להזמין קולוסיאום להיום — לשמור ל־15/9"))

    if day_id == "15-09":
        book.append(("colo-tickets", "הזמנת כרטיסי קולוסיאום רשמיים (~30 יום מראש) — כולל ילדים חינם"))
        transport.append(("taxi-colo", "לתכנן מונית למלון↔קולוסיאום או הליכה 25–35 דק׳"))
        bring.append(("comfy-shoes", "נעלי הליכה נוחות"))
        if letter == "B":
            book.append(("full-exp", "לנסות Full Experience Underground+Arena בחלון השחרור — או סיור צד ג׳ אם אזל"))
            timeline = [
                "הגעה 30 דק׳ לפני השעה בכרטיס",
                "ביקור מודרך בהיפוגאום → רצפת הזירה → יציעים",
                "החלטה במקום: פורום או יציאה לגלידה/מזגן",
                "אחה״צ קניות קלות / מנוחה",
            ]
        elif letter == "A":
            timeline = [
                "בוקר: כניסה מתוזמנת לקולוסיאום",
                "סיבוב ביציעים + הסברים קצרים לילדים",
                "פורום רק אם האנרגיה גבוהה — אחרת יציאה",
                "צהריים מזגן/אוכל → Via del Corso",
            ]

    if day_id == "16-09":
        if letter in ("A", "B", "C"):
            book.append(("food-tour", f"הזמנת הסיור אונליין + בקשת התאמות: בלי חזיר / בלי פירות ים"))
            book.append(("meeting-point", "לשמור את נקודת המפגש והשעה מהאישור"))
            transport.append(("to-tour", "לתכנן הגעה לנקודת המפגש (הליכה/מונית) 15 דק׳ לפני"))
        if letter == "A":
            book.append(("eating-europe", "Eating Europe — Trastevere/Family: eatingeurope.com"))
        if letter == "B":
            book.append(("devour", "Devour Testaccio — לתאם תזונה מראש (הרבה בשרי/חזיר באזור)"))
        if letter == "C":
            book.append(("private", "Eating Europe Private — לשריין ל־4 ולציין קצב גמיש למשפחה"))
        if letter == "E":
            book.append(("skip-outlet", "לא להזמין אאוטלט — האפשרות לא רלוונטית"))
        bring.append(("appetite", "לבוא רעבים יחסית לסיור האוכל"))
        timeline = [
            "בוקר: סיור אוכל / תוכנית שנבחרה",
            "אחה״צ קל: פנתיאון/נבונה קצר או מנוחה",
            "ערב: אריזה לשייט — מסמכים ותרופות בטרולי",
        ]

    if day_id == "17-09":
        book.append(("royal-checkin", "צ׳ק־אין דיגיטלי באפליקציית Royal + חלון עלייה"))
        book.append(("dining", "הזמנת My Time Dining 17:30–18:30"))
        if letter == "A":
            book.append(("van", "הזמנת ואן פרטי מלון→צ׳יוויטווקיה עם מקום ל־4 מזוודות"))
            transport = [
                ("confirm-driver", "אישור נהג/שעת איסוף יום לפני"),
                ("luggage", "מזוודות מוכנות בלובי בשעת האיסוף"),
            ]
            timeline = [
                "בוקר: ארוחת בוקר + צ׳ק־אאוט",
                "נסיעה לנמל (~1–1.5 שע׳)",
                "בידוק ביטחוני + עלייה לספינה",
                "חדר 7680 → חקר קצר / בריכה → ארוחת ערב My Time",
            ]
        if letter == "B":
            book.append(("train", "כרטיסי רכבת Termini→Civitavecchia + מונית לנמל"))

    if day_id == "18-09":
        bring.append(("ship-card", "כרטיס הספינה / טלפון עם אפליקציה"))
        bring.append(("all-aboard", "לרשום שעת all-aboard מהאפליקציה"))
        if letter == "A":
            book.append(("pizza-spot", "לבחור פיצריה מראש (או לשאול על הספינה)"))
            transport.append(("port-taxi", "FreeNow/itTaxi מהנמל למרכז"))
            timeline = [
                "ארוחת בוקר בספינה",
                "מונית למרכז → פיצה",
                "הליכה קצרה Spaccanapoli",
                "חזרה לספינה עם באפר שעתיים",
            ]
        if letter in ("E", "B"):
            book.append(("pompeii-tickets", "כרטיסי פומפיי / סיור עם העברה מהנמל"))
            book.append(("private-car", "רכב פרטי עם חזרה מובטחת — חובה לקומבו E"))
            timeline = [
                "יציאה מהספינה ~08:00",
                "פומפיי ~08:45–11:00 (ביקור ממוקד)",
                "חזרה לנאפולי ~12:00 — שוק/פיצה" if letter == "E" else "חזרה ישירה לנמל / מנוחה בספינה",
                "על הספינה עד ~16:00 לפחות",
            ]
        if letter == "C":
            book.append(("capri", "סירות/סיור קאפרי רק עם חזרה מובטחת לספינה"))

    if day_id == "19-09":
        book.append(("show", "הזמנת מופע באפליקציה אם נדרש (אחה״צ/ערב)"))
        book.append(("confirm-crown", "אישור באפליקציה: Crown Edge Experience · 09:00 — כבר הוזמן"))
        book.append(("confirm-izumi", "אישור באפליקציה: Izumi Hibachi · 12:30 — כבר הוזמן · לבקש בלי חזיר/פירות ים"))
        if letter == "B":
            book.append(("evening-light", "ארוחת ערב קלה בלבד (אחרי Izumi בצהריים) — לא Specialty נוספת"))
        bring = [b for b in bring if b[0] not in ("docs",)]
        bring.extend([
            ("swimsuit", "בגדי ים + מגבת אם צריך (אחרי הפעילויות)"),
            ("spf-deck", "קרם הגנה לסיפון"),
            ("closed-shoes", "נעליים סגורות ל־Crown Edge (לפי הנחיות האפליקציה)"),
            ("nice-casual", "לבוש נעים ל־Izumi (casual)"),
        ])
        timeline = [
            "ארוחת בוקר קלה מוקדם (לפני Crown Edge)",
            "09:00 — Crown Edge Experience (כבר הוזמן) · להגיע ~08:40–08:50",
            "אחרי החוויה — מנוחה קצרה / סיפון",
            "12:30 — Izumi Hibachi (כבר הוזמן) · להגיע ~12:15 · תפריט בלי חזיר/פירות ים",
            "אחה״צ — בריכות / פארק מים / מנוחה בחדר (בטן מלאה)",
            "ערב — מופע · ארוחת ערב קלה בלבד (Windjammer / My Time קל) — לא Specialty נוספת",
        ]

    if day_id == "20-09":
        bring.append(("all-aboard", "שעת all-aboard — יעד חזרה לנמל ~14:30–15:00"))
        if letter in ("A", "B"):
            book.append(("sagrada", "כרטיסי Sagrada Família מתוזמנים ל־4 (בוקר)"))
            transport.append(("to-sagrada", "מונית FreeNow מהנמל ל־Sagrada (~20–30 דק׳)"))
            transport.append(("to-ramblas", "מונית/מטרו מ־Sagrada לרמבלס (~15–25 דק׳)"))
            timeline = [
                "ארוחת בוקר בספינה (לא לצאת ב־05:30)",
                "Sagrada — ביקור מתוזמן (ביום ראשון לרוב אחרי ~10:30)",
                "מעבר לרמבלס + אוכל ברובע הגותי / טאפאס",
                "גלידה / קניות קצרות",
                "חזרה לנמל עם באפר",
            ]
        if letter == "B":
            book.append(("guell", "כרטיסי Park Güell מתוזמנים — רק אם A מסתיים מוקדם"))
            timeline.append("אופציונלי: Park Güell רק אם כולם בשיא — אחרת לדלג")
        if letter == "C":
            transport.append(("to-ramblas", "מונית/שאטל לנמל→רמבלס"))

    if day_id == "21-09":
        bring.append(("all-aboard", "חלון קצר — באפר 90 דק׳ לפני יציאה"))
        transport.append(("port-taxi", "מונית רשמית מהנמל למרכז/חוף"))
        if letter == "A":
            timeline = ["נמל→קתדרלה", "עיר עתיקה קצרה", "גלידה", "חזרה"]
        if letter == "B":
            bring.append(("swim", "בגדי ים + מגבת קטנה"))
            timeline = ["נמל→חוף", "שחייה/משחק", "מקלחת/מגבת", "חזרה"]

    if day_id == "22-09":
        bring.append(("all-aboard", "לרשום all-aboard"))
        if letter == "A":
            transport.append(("vieux", "שאטל/מונית לנמל הישן"))
            timeline = ["Vieux Port", "תצפית Notre-Dame (או מבט מרחוק)", "אוכל קל", "חזרה"]
        if letter == "B":
            book.append(("aix-tour", "סיור/העברה לאקס עם חזרה מובטחת"))
            transport.append(("aix-time", "נסיעה ~30–45 דק׳ לכל כיוון — לשבץ בלו״ז"))
        if letter == "C":
            book.append(("calanques-boat", "סירת קלנקים — לבדוק מזג אוויר וביטולים"))

    if day_id == "23-09":
        bring.extend([
            ("train-pass", "כרטיס רכבת / Cinque Terre day pass"),
            ("all-aboard", "באפר שעתיים לפני all-aboard"),
            ("shoes", "נעליים עם אחידה למדרגות"),
        ])
        if letter in ("A", "B"):
            book.append(("ct-tickets", "לבדוק כרטיסי רכבת/כרטיס יומי בתחנה או אונליין"))
            transport.append(("to-station", "שאטל/מונית מהנמל ל־La Spezia Centrale"))
            timeline = [
                "נמל → תחנה → רכבת לריומג׳ורה",
                "כפר 1: מעגן + אוכל + צילום (45–90 דק׳)",
                "רכבת למנרולה — כפר 2",
                "אם אפשרות B ואנרגיה: ורנאצה קצר — אחרת חזרה",
                "רכבת ללה ספציה → ספינה עם באפר",
            ]
        if letter == "C":
            book.append(("boat", "כרטיסי סירה בין כפרים + תוכנית גיבוי ברכבת"))
        if letter == "D":
            book.append(("guided-ct", "הזמנת סיור מודרך Royal/פרטי עם חזרה לספינה"))
        if letter == "F":
            book.append(("pisa", "העברה/רכבת לפיזה — רק כגיבוי"))

    if day_id == "24-09":
        book.append(("hotel-last", "אישור מלון לילה אחרון + בקשת early luggage storage"))
        book.append(("fco-next", "שיריינו העברה למחר ל־FCO ל־07:00–07:15"))
        if letter == "A":
            book.append(("civ-rome", "העברה פרטית צ׳יוויטווקיה→מלון"))
            timeline = [
                "ירידה מהספינה ~07:00",
                "נסיעה לרומא (~1–1.5 שע׳)",
                "צ׳ק־אין / השארת מזוודות + מנוחה",
                "ערב קל: טרווי/ספניש סטפס",
                "שינה מוקדמת",
            ]

    if day_id == "25-09":
        book.extend([
            ("alarm", "שעון מעורר + באפר"),
            ("fco-transfer", "אישור נהג להעברה ~07:00–07:15"),
            ("boarding-pass", "כרטיסי עלייה לטיסה / אפליקציית אל על"),
            ("harel", "פרטי ביטוח הראל נגישים"),
        ])
        timeline = [
            "יציאה מהמלון בזמן",
            "הגעה ל־FCO ~08:00",
            "צ׳ק־אין + בידוק",
            "זמן המתנה עם חטיפים ואוזניות",
            "טיסה ~11:00",
        ]
        bring = [
            ("passports", "דרכונים"),
            ("tickets", "כרטיסי טיסה"),
            ("chargers", "מטענים מהחדר"),
            ("meds", "תרופות בתיק יד"),
            ("snack", "חטיפים לדרך"),
        ]

    # Generic enrichments
    if any(k in t for k in ("כרטיס", "Sagrada", "Full Experience", "קולוסיאום", "פומפיי", "סיור")):
        book.append(("screenshots", "צילומי מסך של כל הכרטיסים אופליין בטלפון"))

    return {
        "overview": why,
        "when": when,
        "cost": cost,
        "time": time,
        "grade": grade,
        "recommended": recommended,
        "pros": pros,
        "cons": cons,
        "family": family,
        "timeline": timeline,
        "book": book,
        "transport": transport,
        "bring": bring,
        "food": "כללי משפחה: בלי חזיר, בלי פירות ים; דגים בסדר. לבקש בכל הזמנה/מסעדה.",
        "super_tip": "בלוקים של 60–90 דק׳, יציאת חירום מוכנה, פרס גלידה/חטיף, לא להעמיס אטרקציה שנייה כבדה.",
    }


def option_card(day_id, letter, title, grade, why, pros, cons, cost, time, when, family, recommended=False, plan=None):
    key = f"{day_id}-{letter}"
    href = f"{key}.html"
    plan_data = build_plan(day_id, letter, title, grade, why, pros, cons, cost, time, when, family, recommended)
    if plan:
        plan_data.update(plan)
    OPTION_REGISTRY[key] = {
        "day_id": day_id,
        "letter": letter,
        "title": title,
        "grade": grade,
        "why": why,
        "pros": pros,
        "cons": cons,
        "cost": cost,
        "time": time,
        "when": when,
        "family": family,
        "recommended": recommended,
        "plan": plan_data,
        "href": href,
    }

    rec = " recommended" if recommended else ""
    badge = ' <span class="note">(המלצת ברירת מחדל)</span>' if recommended else ""
    pros_li = "".join(f"<li>{x}</li>" for x in pros)
    cons_li = "".join(f"<li>{x}</li>" for x in cons)
    return f"""
        <article class="option-card{rec}">
          <div class="option-head">
            <h3><a class="option-title-link" href="{href}">{letter}. {title}</a>{badge}</h3>
            <span class="grade" data-grade="{grade}">{grade}</span>
          </div>
          <p class="option-cost"><strong>עלות משוערת ליום (משפחה ×4):</strong> {cost}</p>
          <p><strong>למה הציון:</strong> {why}</p>
          <div class="pros-cons">
            <div class="pros"><strong>יתרונות</strong><ul>{pros_li}</ul></div>
            <div class="cons"><strong>חסרונות</strong><ul>{cons_li}</ul></div>
          </div>
          <div class="option-meta">
            <span><strong>זמן / הליכה:</strong> {time}</span>
            <span><strong>מתי לבחור:</strong> {when}</span>
          </div>
          <div class="family-notes">{family}</div>
          <p style="margin:0.75rem 0 0"><a class="btn btn-secondary" href="{href}">תוכנית מפורטת וצ׳ק־ליסט ←</a></p>
        </article>"""


def checklist_html(items, prefix):
    lis = []
    for i, item in enumerate(items):
        if isinstance(item, tuple):
            aid, label = item
        else:
            aid, label = f"{prefix}-{i}", item
        data_id = f"{prefix}-{aid}"
        lis.append(f'<li><input type="checkbox" data-id="{data_id}" /> {label}</li>')
    return "<ul class=\"checklist\">" + "".join(lis) + "</ul>"


def write_option_page(opt, day_title, day_subtitle, meeting, exit_ramp, taxi_key):
    plan = opt["plan"]
    day_id = opt["day_id"]
    letter = opt["letter"]
    rec_banner = (
        '<div class="default-pick"><strong>זו המלצת ברירת המחדל ליום זה</strong> — עדיין אפשר לבחור אחרת.</div>'
        if opt["recommended"]
        else ""
    )
    pros_li = "".join(f"<li>{x}</li>" for x in plan["pros"])
    cons_li = "".join(f"<li>{x}</li>" for x in plan["cons"])
    timeline_li = "".join(f"<li>{x}</li>" for x in plan["timeline"])
    taxi_html = taxi_box(taxi_key) if taxi_key else ""

    body = f"""
    <p class="note"><a href="{day_id}.html">← חזרה ליום {day_id[:2]}/{day_id[3:]}</a></p>
    <section class="hero">
      <h1>אפשרות {letter} · {opt["title"]}</h1>
      <p>{day_title}<br />{day_subtitle}</p>
      <div class="meta-grid">
        <div class="meta-item"><strong>ציון למשפחה</strong><span class="grade" data-grade="{opt["grade"]}">{opt["grade"]}</span></div>
        <div class="meta-item"><strong>עלות משוערת ליום (משפחה ×4)</strong>{plan["cost"]}</div>
        <div class="meta-item"><strong>משך</strong>{plan["time"]}</div>
        <div class="meta-item"><strong>מתי לבחור</strong>{plan["when"]}</div>
      </div>
    </section>
    {rec_banner}
    <div class="super-tip"><strong>Super-Tips:</strong> {plan["super_tip"]}</div>

    <section class="section">
      <h2>סקירה</h2>
      <p>{plan["overview"]}</p>
      <div class="family-notes">{plan["family"]}</div>
      <div class="pros-cons">
        <div class="pros"><strong>יתרונות</strong><ul>{pros_li}</ul></div>
        <div class="cons"><strong>חסרונות / סיכונים</strong><ul>{cons_li}</ul></div>
      </div>
    </section>

    <section class="section">
      <h2>לו״ז מוצע</h2>
      <ol>{timeline_li}</ol>
    </section>

    <section class="section">
      <h2>להזמין / לסדר מראש</h2>
      {checklist_html(plan["book"], f"{day_id}-{letter}-book")}
    </section>

    <section class="section">
      <h2>תחבורה</h2>
      {checklist_html(plan["transport"], f"{day_id}-{letter}-tr")}
    </section>

    <section class="section">
      <h2>מה לקחת</h2>
      {checklist_html(plan["bring"], f"{day_id}-{letter}-br")}
    </section>

    <section class="section">
      <h2>אוכל</h2>
      <p>{plan["food"]}</p>
    </section>

{taxi_html}

    <section class="section">
      <h2>נקודת מפגש ויציאת חירום</h2>
      <div class="meeting">{meeting}</div>
      <div class="exit-ramp"><strong>יציאת חירום:</strong> {exit_ramp}</div>
    </section>

    <nav class="day-nav">
      <a class="btn btn-secondary" href="{day_id}.html">← חזרה ליום</a>
      <a class="btn" href="../prebook.html">רשימת הזמנות כלליות</a>
    </nav>
"""
    html = page_shell(
        f"אפשרות {letter} · {opt['title']}",
        body,
        current=day_id,
        depth=1,
        theme=day_theme(day_id),
    )
    (DAYS / opt["href"]).write_text(html, encoding="utf-8")


def page_shell(title, body, current=None, depth=0, theme=None):
    css = "../css/styles.css" if depth else "css/styles.css"
    theme_cls = f' class="{theme}"' if theme else ""
    return f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
{FONTS}
  <link rel="stylesheet" href="{css}" />
</head>
<body{theme_cls}>
{header(current, depth)}
  <main class="wrap">
{body}
  </main>
{footer(depth)}
</body>
</html>
"""


def day_page(day_id, title, subtitle, weather, super_tip, default_text, places_html, options_html, extra, taxi_html, meeting, exit_ramp, costs_table, prev_id, next_id):
    places_section = f"""
    <section class="section">
      <h2>הכרת היעד והמקומות</h2>
      <div class="place-grid">
{places_html}
      </div>
    </section>""" if places_html else ""

    body = f"""
    <section class="hero">
      <h1>{title}</h1>
      <p>{subtitle}</p>
    </section>

    <div class="weather">
      <span class="temp">{weather['temp']}</span>
      <div>
        <strong>מזג אוויר טיפוסי לאמצע ספטמבר</strong><br />
        {weather['note']}
        <div class="note"><a href="{weather.get('link', 'https://www.accuweather.com/')}" target="_blank" rel="noopener">עדכון תחזית לפני היציאה</a></div>
      </div>
    </div>

    <div class="super-tip"><strong>Super-Tips:</strong> {super_tip}</div>
    <div class="default-pick"><strong>המלצת ברירת מחדל:</strong> {default_text}</div>

{places_section}

    <section class="section">
      <h2>אפשרויות מדורגות</h2>
      <div class="options">
{options_html}
      </div>
    </section>

{extra}
{taxi_html}

    <section class="section">
      <h2>עלות משוערת לפי אפשרות (משפחה ×4 ליום)</h2>
      {costs_table}
      <p class="note">מחירים משוערים באירו ליום שלם למשפחה — לא כוללים טיסות/מלון/חבילת השייט עצמה, אלא מה שמשלמים באותו יום לפי האפשרות. לעדכון לפני הנסיעה.</p>
    </section>

    <section class="section">
      <h2>נקודת מפגש אם נפרדים</h2>
      <div class="meeting">{meeting}</div>
      <div class="exit-ramp"><strong>יציאת חירום (Super-Tips):</strong> {exit_ramp}</div>
    </section>

    {day_nav(prev_id, next_id)}
"""
    return page_shell(title, body, current=day_id, depth=1, theme=day_theme(day_id))


days = {}

# ---------- 14 ----------
days["14-09"] = dict(
    title="14 בספטמבר · הגעה לרומא",
    subtitle="שני · נחיתה FCO 12:45 · Colonna Collection",
    weather={"temp": "27°", "note": "חם ונעים · שמש · כובעים ומים.", "link": "https://www.accuweather.com/en/it/rome/213633/weather-forecast/213633"},
    super_tip="אחרי טיסה — הליכה קצרה וגלידה בלבד.",
    default_text="אפשרות A — מלון, טרווי מבחוץ, גלידה וארוחה מוקדמת ליד המלון.",
    places="".join([
        place_card("trevi.jpg", "מזרקת טרווי",
                   "מזרקת הבארוק המפורסמת ביותר ברומא (המאה ה־18). זורקים מטבע עם הגב למזרקה — מסורת ל״חזרה לרומא״. בערב מוארת ויפה במיוחד.",
                   "מהמלון ~8–12 דק׳ הליכה", "עמוס בתיירים — עצירה קצרה לצילום מספיקה."),
        place_card("pantheon.jpg", "הפנתיאון / אזור המלון",
                   "מקדש רומי עתיק שהפך לכנסייה, עם כיפה מרהיבה ו״אוקולוס״ פתוח לשמיים. המלון שלכם במרחק דקות הליכה.",
                   "מהמלון ~3–5 דק׳ הליכה", "הכניסה חינמית בדרך כלל — תור קצר אפשרי."),
        place_card("gelato.jpg", "גלידה רומית",
                   "גלידה איטלקית (gelato) — חלק מחוויית רומא. ליד המלון: Giolitti או Della Palma.",
                   "מהמלון ~5–10 דק׳ הליכה", "אפשר לקחת לדרך אם יש תור."),
    ]),
    options=[
        option_card("14-09", "A", "מלון → טרווי (מבחוץ) → גלידה → ארוחה מוקדמת ליד המלון", 9,
            "מתאים לג׳ט־לג + must-see קל.",
            ["קרוב", "שליטה באורך", "מסעדות טובות באזור"],
            ["עומס ליד המזרקה"],
            "€100–180 (ארוחה + גלידה)", "הליכה 20–40 דק׳", "ברירת מחדל",
            "<strong>Super-Tips:</strong> קצר ומתוק", True),
        option_card("14-09", "B", "מלון → קניות קלות ב-Via del Corso → שינה מוקדמת", 8,
            "טוב אם עייפים מהטיסה.",
            ["מיזוג בחנויות", "גמיש"],
            ["פחות וואו"],
            "€40–120 (קניות/חטיפים לפי בחירה)", "30–60 דק׳", "אם כולם מותשים",
            "<strong>יובל:</strong> חנויות"),
        option_card("14-09", "C", "לדחוף לקולוסיאום באותו יום", 4,
            "יותר מדי אחרי נחיתה ומזוודות.",
            ["וי מוקדם"],
            ["תורים וחום"],
            "€120–200 (מונית + כרטיסים + אוכל קל)", "3+ שעות", "לא מומלץ",
            "<strong>Super-Tips:</strong> סיכון גבוה"),
    ],
    extra="""
    <section class="section">
      <h2>מסעדות מומלצות ליד המלון (Colonna / פנתיאון)</h2>
      <p class="note">לבקש תמיד: בלי חזיר / בלי פירות ים · דגים בסדר. מומלץ לשריין בטלפון/אפליקציה.</p>
      <ul class="restaurant-list">
        <li><strong>Armando al Pantheon</strong> — טרטוריה רומית קלאסית ליד הפנתיאון. פסטות מצוינות (למשל cacio e pepe / gricia — לבדוק שאין חזיר בגרסאות מסוימות). שריון מומלץ מאוד. הליכה ~5 דק׳.</li>
        <li><strong>Emma Pizzeria</strong> (ליד Campo de' Fiori) — פיצה דקה רומית, משפחתית, אווירה טובה לילדים. הליכה ~10–12 דק׳ או מונית קצרה.</li>
        <li><strong>Osteria dell'Ingegno</strong> — כיכר נחמדה, תפריט מגוון, נוח למשפחה. הליכה ~5–7 דק׳.</li>
        <li><strong>Ginger Sapori e Salute</strong> — אופציה קלילה יותר (סלטים/בריאות) אם כבדים אחרי הטיסה. ליד הפנתיאון.</li>
        <li><strong>גלידה:</strong> Giolitti או Della Palma — תור אפשרי; אפשר לקחת לדרך.</li>
      </ul>
      <h2>תחבורה מהשדה</h2>
      <table>
        <tr><th>אפשרות</th><th>זמן משוער</th><th>עלות</th></tr>
        <tr><td>העברה פרטית מראש</td><td>45–60 דק׳</td><td>€55–80</td></tr>
        <tr><td>מונית רשמית FCO (תעריף קבוע)</td><td>45–60 דק׳</td><td>~€50–55</td></tr>
        <tr><td>Leonardo Express + מונית</td><td>70–90 דק׳</td><td>~€60+</td></tr>
      </table>
      <h2>חיסכון ברומא (תזכורת)</h2>
      <ul>
        <li>מים ממזרקות (nasoni) + בקבוק רב־פעמי · סופר ליד המלון למים/חטיפים</li>
        <li>צהריים קלים (pizza al taglio) · ארוחה יושבת אחת ביום · לא מסעדות צמודות לטרווי</li>
        <li>כרטיסי קולוסיאום רק מהאתר הרשמי · ילדים לרוב חינם + עמלה</li>
        <li>פירוט מלא: <a href="../prebook.html">איך לחסוך — רומא והספינה</a></li>
      </ul>
      <iframe class="map-frame" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=12.475%2C41.898%2C12.485%2C41.904&amp;layer=mapnik&amp;marker=41.901%2C12.480"></iframe>
    </section>
    """,
    taxi="rome",
    meeting="<strong>ראשי:</strong> לובי המלון.<br /><strong>משני:</strong> Piazza Colonna (עמודת מרקוס אורליוס).",
    exit_ramp="חזרה למלון, מקלחת, חטיף בחדר.",
    costs="<table><tr><th>סעיף</th><th>משוער</th></tr><tr><td>העברה FCO</td><td>€55–80</td></tr><tr><td>ערב אוכל+גלידה</td><td>€90–150</td></tr></table>",
    prev=None, next="15-09",
)

# ---------- 15 ----------
days["15-09"] = dict(
    title="15 בספטמבר · קולוסיאום",
    subtitle="שלישי · יום must-see ברומא",
    weather={"temp": "28°", "note": "חם · בוקר עדיף לאתרים פתוחים.", "link": "https://www.accuweather.com/en/it/rome/213633/weather-forecast/213633"},
    super_tip="כרטיס מוקדם + הפסקת מזגן חובה אחרי האתר.",
    default_text="אפשרות A — קולוסיאום בבוקר; Full Experience רק אם השגתם כרטיסים והאנרגיה גבוהה.",
    places="".join([
        place_card("colosseum.jpg", "הקולוסיאום",
                   "האמפיתיאטרון הרומי הגדול בעולם (~80 לספירה). כאן התקיימו קרבות גלדיאטורים ומשחקים. היום זה אתר מורשת עולמית — והכרטיס כולל גם גישה לפורום/פלאטין לפי סוג הכרטיס.",
                   "מהמלון ~25–35 דק׳ הליכה · או מונית 10–15 דק׳ (~€10–15)", "ילדים מתחת ל־18 חינם — חייבים הזמנת מקום."),
        place_card("forum.jpg", "מה זה Full Experience?",
                   "כרטיס מורחב רשמי: בנוסף ליציעים הרגילים נכנסים ל<strong>היפוגאום</strong> (מנהרות מתחת לזירה שבהן חיכו גלדיאטורים וחיות) ול<strong>רצפת הזירה (Arena)</strong> — המקום שבו נלחמו בפועל. הביקור במנהרות מודרך ובקבוצות קטנות, ואז עולים לזירה. כולל גם פורום/פלאטין ליומיים. נמכר מהר מאוד (~30 יום מראש).",
                   "תוספת ~30–60 דק׳ לעומת כרטיס רגיל", "יותר עמידה ומדרגות — מעקב צמוד אחרי הקצב של כולם. אם אין כרטיסים: כרטיס רגיל/Arena בלבד מצוין גם כן."),
    ]),
    options=[
        option_card("15-09", "A", "קולוסיאום בבוקר (+ פורום רק אם יש אנרגיה) → מזגן → Corso", 9,
            "הליבה עם יציאת חירום.",
            ["בוקר פחות חם", "גמישות"],
            ["עמידה בכניסה"],
            "€150–230 (כרטיסים 2 מבוגרים + מונית + אוכל; ילדים לרוב חינם באתר)", "2–3 שעות באתר", "ברירת מחדל",
            "<strong>Super-Tips:</strong> סיפורי גלדיאטורים קצרים", True),
        option_card("15-09", "B", "Full Experience (Underground + Arena) אם יש כרטיסים", 8,
            "הכי וואו — היפוגאום + רצפת זירה; יותר זמן עמידה.",
            ["חוויה בלתי נשכחת", "רואים ״מאחורי הקלעים״ של הזירה"],
            ["קשה להשיג", "ארוך יותר", "מדרגות/תנאים לא אחידים במנהרות"],
            "€170–260 (Full Experience למבוגרים + מונית + אוכל)", "כ־90 דק׳ בתוך הקולוסיאום לפי הרגולציה + זמן כניסה", "אם השגתם כרטיסים רשמיים והאנרגיה גבוהה",
            "<strong>Super-Tips:</strong> להכין ״עוד קטע ואז גלידה״ · אפשר לדלג על פורום אחרי"),
        option_card("15-09", "C", "רק קולוסיאום — בלי פורום/פלאטין", 8,
            "יציאה מוקדמת חכמה — Super-Tips.",
            ["קצר", "פחות חום"],
            ["מפספסים חלק מהכרטיס"],
            "€150–230 (כמו A — אותם כרטיסים, פחות זמן באתר)", "90–120 דק׳", "אם מישהו מתעייף",
            "<strong>כולם:</strong> עדיף פחות וטוב"),
        option_card("15-09", "D", "מעגל מלא פורום + פלאטין", 5,
            "חום וסבלנות — מסוכן לנו.",
            ["שלמות"],
            ["שמש והליכה ארוכה"],
            "€160–250 (כרטיסים כמו A + יותר אוכל/מים ביום ארוך)", "3–4 שעות נוספות", "רק אם כולם בשיא",
            "<strong>Super-Tips:</strong> לא מומלץ"),
    ],
    extra="""
    <section class="section">
      <h2>Full Experience — פירוט קצר</h2>
      <div class="info-callout">
        <ul>
          <li><strong>Underground (היפוגאום):</strong> מנהרות מתחת לזירה — כלובים, מסדרונות ומנגנוני הרמה עתיקים.</li>
          <li><strong>Arena:</strong> עמידה על רצפת הזירה המשוחזרת חלקית — תחושת קנה מידה של הקרבות.</li>
          <li><strong>גם כלול:</strong> יציעים 1–2, מוזיאון הקולוסיאום, פורום רומי + פלאטין (תוקף ליומיים).</li>
          <li><strong>לא חובה בשביל יום מוצלח:</strong> כרטיס רגיל/Arena בלבד עדיין חוויה גדולה למשפחה.</li>
        </ul>
        <p>הזמנה: <a href="https://ticketing.colosseo.it" target="_blank" rel="noopener">ticketing.colosseo.it</a></p>
      </div>
      <iframe class="map-frame" loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=12.488%2C41.888%2C12.498%2C41.894&amp;layer=mapnik&amp;marker=41.8902%2C12.4922"></iframe>
    </section>
    """,
    taxi="rome",
    meeting="<strong>ראשי:</strong> שער הכניסה לקולוסיאום.<br /><strong>משני:</strong> קשת קונסטנטינוס.",
    exit_ramp="גלידה/מונית חזרה למלון — בלי פורום.",
    costs="<table><tr><th>סעיף</th><th>משוער</th></tr><tr><td>כרטיסים (2 מבוגרים)</td><td>€40–56</td></tr><tr><td>מונית הלוך־חזור</td><td>€20–30</td></tr><tr><td>אוכל</td><td>€90–130</td></tr></table>",
    prev="14-09", next="16-09",
)

# ---------- 16 ----------
days["16-09"] = dict(
    title="16 בספטמבר · סיור אוכל",
    subtitle="רביעי · סיורים מומלצים מהרשת · אריזה לשייט",
    weather={"temp": "28°", "note": "חם · סיור בוקר/צהריים עדיף.", "link": "https://www.accuweather.com/en/it/rome/213633/weather-forecast/213633"},
    super_tip="סיור עם מדריך = פחות החלטות. לבקש מראש התאמות בלי חזיר/פירות ים.",
    default_text="Eating Europe — Twilight Trastevere או סיור משפחתי שלהם (ציון 9). Devour Testaccio אם רוצים שוק אותנטי (לשים לב לאוכל בשרי/חזיר).",
    places="".join([
        place_card("trastevere.jpg", "טרסטוורה",
                   "שכונה ציורית מעבר לטיבר — סמטאות, כנסיות, ואוכל מקומי. רוב סיורי האוכל הערב־לילה מתרחשים כאן.",
                   "מהמלון ~20–30 דק׳ הליכה · או מונית 10–15 דק׳", "בערב תוססת — מתאים לסיור מונחה."),
        place_card("food-tour.jpg", "טסטאצ׳ו (Testaccio)",
                   "שכונת אוכל ״אמיתית״ של רומאים — שוק מקורה, דוכנים, טרטוריות משפחתיות. פחות תיירותית מטרווי.",
                   "מהמלון ~20–25 דק׳ במונית / ~35–45 בתחבורה", "הרבה מנות בשריות מסורתיות — לבקש חלופות בלי חזיר."),
    ]),
    options=[
        option_card("16-09", "A", "Eating Europe — Twilight Trastevere / Family food tour", 9,
            "מהמפעילים המדורגים ביותר ברומא; ביקורות משפחתיות חזקות; הנחות לילדים.",
            ["מדריכים מעולים לפי ביקורות", "עצירות מגוונות", "מתאים למשפחות (גילאי ילדים מוזלים)"],
            ["ערב יכול להיות מאוחר לילדים — לבחור סלוט מוקדם אם יש", "עלות"],
            "€280–400 (סיור משפחתי — תלוי הנחות ילדים)", "כ־3–3.5 שעות", "ברירת מחדל לפי המלצות ברשת",
            "<strong>לבקש:</strong> בלי חזיר/פירות ים · <a href='https://www.eatingeurope.com/rome-family-tours/' target='_blank' rel='noopener'>eatingeurope.com</a>", True),
        option_card("16-09", "B", "Devour Tours — Ultimate Testaccio Market Tour", 8,
            "ביקורות מעולות, קבוצות קטנות (עד 12), שוק + טעימות + גלידה — קצב טוב לילדים סקרנים.",
            ["אותנטי", "שוק חי", "שביעים לגמרי"],
            ["טסטאצ׳ו = הרבה בשרי/חזיר מסורתי — חובה לתאם מראש", "בוקר מוקדם לפעמים"],
            "€320–450 (סיור משפחתי)", "כ־3.5–4 שעות", "אם רוצים שוק מקומי ולא רק מרכז תיירים",
            "<a href='https://devourtours.com/tours/rome-testaccio-food-market-tour/' target='_blank' rel='noopener'>devourtours.com</a>"),
        option_card("16-09", "C", "Eating Europe — Private Testaccio (פרטי)", 9,
            "אותו מותג חזק + קצב שלכם — אידיאלי לקצב גמיש ולדרישות תזונה.",
            ["גמישות מלאה", "רק המשפחה", "התאמות קלות יותר"],
            ["יקר משמעותית"],
            "€500–700 (סיור פרטי למשפחה)", "כ־3.5 שעות", "אם התקציב מאפשר חוויה מותאמת",
            "<strong>Super-Tips:</strong> אפשר לקצר עצירות"),
        option_card("16-09", "D", "טיול אוכל עצמאי בטרסטוורה", 6,
            "זול יותר, יותר החלטות והליכה.",
            ["גמיש", "זול"],
            ["קל ללכת לאיבוד בבחירות"],
            "€100–180 (אוכל + תחבורה קלה)", "3–4 שעות", "אם לא מצאתם סיור",
            "<strong>Super-Tips:</strong> 3 עצירות מקסימום מראש"),
        option_card("16-09", "E", "יום אאוטלט Castel Romano", 3,
            "הוסר כמעט מהתוכנית — לא מתאים ליעד שלכם.",
            ["קניות"],
            ["נסיעה ארוכה", "מפספסים רומא", "עייפות לפני שייט"],
            "€150–350 (העברה + קניות לפי בחירה)", "חצי יום+", "לא מתכננים",
            "דלגו"),
    ],
    extra="""
    <section class="section">
      <h2>איך לבחור סיור אוכל</h2>
      <table>
        <tr><th>סיור</th><th>ציון לנו</th><th>למה</th></tr>
        <tr><td>Eating Europe Trastevere / Family</td><td><strong>9</strong></td><td>ביקורות משפחתיות מצוינות, מותג ותיק</td></tr>
        <tr><td>Eating Europe Private</td><td><strong>9</strong></td><td>שליטה מלאה בקצב ותזונה</td></tr>
        <tr><td>Devour Testaccio</td><td><strong>8</strong></td><td>שוק אותנטי; לתאם תזונה</td></tr>
        <tr><td>DIY</td><td><strong>6</strong></td><td>רק אם אין מקום בסיורים</td></tr>
      </table>
      <p>אחה״צ: פנתיאון/נבונה קצר + <strong>אריזה לשייט</strong>.</p>
    </section>
    """,
    taxi="rome",
    meeting="<strong>ראשי:</strong> נקודת המפגש באישור הסיור.<br /><strong>משני:</strong> לובי המלון.",
    exit_ramp="גלידה וחזרה לארוז — בלי אטרקציה נוספת.",
    costs="<table><tr><th>סעיף</th><th>משוער למשפחה</th></tr><tr><td>סיור אוכל</td><td>€250–450 (תלוי סיור/פרטי)</td></tr><tr><td>ערב קל אם צריך</td><td>€40–80</td></tr></table>",
    prev="15-09", next="17-09",
)

# ---------- 17 ----------
days["17-09"] = dict(
    title="17 בספטמבר · עלייה לספינה",
    subtitle="חמישי · צ׳יוויטווקיה · Legend of the Seas · תא 7680",
    weather={"temp": "27°", "note": "נעים · באונייה מיזוג — שכבה קלה.", "link": "https://www.accuweather.com/en/it/civitavecchia/213198/weather-forecast/213198"},
    super_tip="יום לוגיסטיקה — בלי אטרקציות בדרך.",
    default_text="העברה פרטית מהמלון לנמל.",
    places="".join([
        place_card("cruise-port.jpg", "צ׳יוויטווקיה",
                   "נמל השייט של רומא — עיירת חוף כ־70–80 ק״מ צפון־מערב לרומא. מכאן יוצאות רוב ספינות הים התיכון של רומא.",
                   "מרומא בואן פרטי: כ־1–1.5 שעות (תלוי תנועה)", "להגיע לפי חלון הצ׳ק־אין באפליקציה."),
        place_card("ship.jpg", "Legend of the Seas · תא 7680",
                   "ספינת Royal Caribbean חדשה/גדולה עם בריכות, פעילויות משפחתיות והרבה מסעדות. התא בסיפון 7, קטגוריה F1.",
                   "בתוך הנמל: שאטלים/הליכה לפי הוראות הנמל", "My Time Dining 17:30–18:30."),
    ]),
    options=[
        option_card("17-09", "A", "העברה פרטית מלון→נמל → עלייה → חקר הספינה", 9,
            "הכי בטוח עם 4 מזוודות.",
            ["דלת לדלת", "פחות לחץ"],
            ["יקר מרכבת"],
            "€120–180 (ואן פרטי לנמל)", "נסיעה 1–1.5 שע׳ + עלייה", "ברירת מחדל",
            "<strong>כולם:</strong> ראש שקט", True),
        option_card("17-09", "B", "רכבת Termini→Civitavecchia + מונית", 6,
            "זול יותר, קשה עם מזוודות.",
            ["זול"],
            ["החלפות ולחץ"],
            "€50–90 (רכבת ×4 + מונית/שאטל לנמל)", "2+ שעות", "רק אם נוחים עם רכבות+מזוודות",
            "<strong>Super-Tips:</strong> המתנות קשות"),
        option_card("17-09", "C", "אטרקציות בדרך", 3,
            "סיכון לפספס ספינה.",
            [],
            ["איחור = אסון"],
            "€0–80 (+ סיכון לפספס שייט)", "מסוכן", "לא",
            "לא"),
    ],
    extra="""
    <section class="section">
      <h2>פרטי עלייה</h2>
      <table>
        <tr><th>תא</th><td>7680 · סיפון 7 · F1</td></tr>
        <tr><th>יציאה משוערת</th><td>~20:00</td></tr>
        <tr><th>ארוחות</th><td>My Time · 17:30–18:30</td></tr>
      </table>
      <p><a href="../cruise-info.html">עמוד הספינה המלא</a></p>
    </section>
    """,
    taxi="civitavecchia",
    meeting="<strong>ראשי:</strong> דלפק הצ׳ק־אין / כבש העלייה.<br /><strong>משני:</strong> לובי ליד התא אחרי עלייה.",
    exit_ramp="ישר לחדר + מקלחת + אוכל בספינה.",
    costs="<table><tr><th>סעיף</th><th>משוער</th></tr><tr><td>העברה לנמל</td><td>€120–180</td></tr></table>",
    prev="16-09", next="18-09",
)

# ---------- 18 ----------
days["18-09"] = dict(
    title="18 בספטמבר · נאפולי",
    subtitle="שישי · ~07:30–18:30 · פיצה / פומפיי / שוק",
    weather={"temp": "29°", "note": "חם מאוד באתרים פתוחים · מים וכובע.", "link": "https://www.accuweather.com/en/it/naples/212986/weather-forecast/212986"},
    super_tip="בוקר פעילות, צהריים בצל, באפר גדול לחזרה לספינה.",
    default_text="A לפיצה בעיר, או E לפומפיי קצר + שוק/פיצה בנאפולי עם רכב פרטי.",
    places="".join([
        place_card("naples.jpg", "נאפולי",
                   "עיר תוססת, בית הפיצה בעולם, נופים למפרץ ולוזוב. צפופה, רועשת ומלאת טעם — שווה טעימה קצרה וממוקדת.",
                   "מהנמל למרכז: 10–20 דק׳ במונית", "תיקי רוכסן צמודים."),
        place_card("pompeii.jpg", "פומפיי",
                   "עיר רומית שנקברה בהתפרצות וזוב בשנת 79 לספירה. רחובות, בתים ועיצובים שנשמרו בצורה מדהימה — חוויה היסטורית חזקה לילדים.",
                   "מהנמל בפרטי: ~30–45 דק׳ לכל כיוון", "חצי יום באתר מספיק; בלי וזוב באותו יום."),
    ]),
    options=[
        option_card("18-09", "A", "פיצת נאפולי + Spaccanapoli קצר", 9,
            "וואו אוכל, אורך בשליטה.",
            ["פיצה בלתי נשכחת", "גמיש"],
            ["רחובות צפופים"],
            "€100–180 (פיצה + מוניות + שתייה)", "3–5 שעות", "ברירת מחדל לאוכל",
            "<strong>Super-Tips:</strong> פיצה = מוטיבציה", True),
        option_card("18-09", "E", "פומפיי חצי בוקר + שוק/פיצה בנאפולי אחה״צ", 8,
            "אפשרי בחלון ~07:30–18:30 עם רכב פרטי ומשמעת זמנים — פומפיי קצר (כשעתיים) ואז נאפולי.",
            ["שתי חוויות ביום אחד", "שוק+פיצה אחרי ההיסטוריה", "זיכרון חזק"],
            ["יום עמוס", "חום בפומפיי", "תנועה בנאפולי — חובה באפר"],
            "€280–450 (רכב פרטי + כרטיסים/מדריך + אוכל)", "יום מלא עם באפר", "אם רוצים גם עתיקות וגם טעם העיר",
            "<strong>לו״ז מוצע:</strong> יציאה מהספינה ~08:00 → פומפיי 08:45–11:00 → חזרה לעיר ~12:00 → Pignasecca/פיצה → חזרה לנמל עד ~16:00"),
        option_card("18-09", "B", "פומפיי חצי יום בלבד (בלי חזרה לשוק)", 8,
            "פחות עומס מ־E, יותר זמן באתר או מנוחה בספינה.",
            ["מיקוד", "פחות לחץ"],
            ["בלי טעם נאפולי"],
            "€200–400 (רכב/סיור + כרטיסים + אוכל קל)", "5–6 שעות", "אם מעדיפים רק פומפיי",
            "<strong>Super-Tips:</strong> הפסקות צל"),
        option_card("18-09", "C", "קאפרי", 6,
            "יפה אך תורים ועלות.",
            ["נוף"],
            ["סירות ולחץ זמן"],
            "€300–500+ (סירות/מעבורת + אוכל + מוניות)", "יום מלא", "רק אם מתים על אי",
            "<strong>Super-Tips:</strong> תורים קשים"),
        option_card("18-09", "D", "פומפיי + וזוב מלא", 3,
            "ארוך וחם מדי.",
            [],
            ["קריסה"],
            "€350–550 (סיור מלא + אוכל)", "8+ שעות", "לא",
            "לא"),
    ],
    extra="""
    <section class="section">
      <h2>תוכנית E — פומפיי + שוק נאפולי (פירוט)</h2>
      <div class="info-callout">
        <p><strong>למה זה אפשרי:</strong> הנמל עד ~18:30 נותן חלון ארוך. עם נהג פרטי: ~35 דק׳ לכל כיוון לפומפיי. ביקור ממוקד של ~2 שעות באתר משאיר זמן ל־Pignasecca / אזור העיר העתיקה + פיצה.</p>
        <ol>
          <li>יציאה מוקדמת מהספינה אחרי ארוחת בוקר קלה</li>
          <li>פומפיי: פורום, רחוב ראשי, בית אחד־שניים — ואז יוצאים (לא לכסות את כל האתר)</li>
          <li>נאפולי: שוק Pignasecca או דוכני רחוב + פיצריה טובה</li>
          <li>חזרה לנמל עם באפר של שעתיים לפני הכל־אבורד</li>
        </ol>
        <p class="note">בלי רכב פרטי / סיור עם חזרה מובטחת — לא ממליצים על הקומבו (רכבות+תנועה = סיכון לאיחור).</p>
      </div>
    </section>
    """,
    taxi="naples",
    meeting="<strong>ראשי:</strong> כבש הספינה.<br /><strong>משני:</strong> Piazza del Plebiscito.",
    exit_ramp="חזרה לספינה ל־Windjammer + בריכה.",
    costs="<table><tr><th>אפשרות</th><th>משוער</th></tr><tr><td>A עיר</td><td>€100–180</td></tr><tr><td>E פומפיי+שוק</td><td>€280–450</td></tr><tr><td>B פומפיי בלבד</td><td>€200–400</td></tr></table>",
    prev="17-09", next="19-09",
)

# ---------- 19 ----------
days["19-09"] = dict(
    title="19 בספטמבר · יום בים",
    subtitle="שבת · יום 3 בשייט · איפוס + הזמנות קבועות",
    weather={"temp": "—", "note": "שמש חזקה על הסיפון · קרם הגנה.", "link": "https://www.royalcaribbean.com/"},
    super_tip="בוקר וצהריים תפוסים (Crown Edge + Izumi) — אחה״צ רגוע בלבד, בלי לדחוס עוד.",
    default_text="<strong>כבר נקבע:</strong> Crown Edge 09:00 → Izumi Hibachi 12:30. אחה״צ בריכות/מנוחה · ערב מופע + ארוחה קלה בלבד.",
    places=place_card("ship.jpg", "יום בים",
                      "אין נמל — כל היום על Legend of the Seas. הזדמנות למנוחה, מים, מופעים ואוכל בלי תורים בחוף.",
                      "0 — כבר על הספינה", "יום זהב לאיפוס אנרגיה — עם שני סלוטים קבועים בבוקר/צהריים."),
    options=[
        option_card("19-09", "A", "לו״ז קבוע + בריכות/מופע אחה״צ", 10,
            "משלב את ההזמנות שכבר יש + איפוס אחרי הצהריים.",
            ["Crown Edge + Izumi כבר סגורים", "כיף לילדים אחה״צ", "גמיש אחרי 14:00"],
            ["שמש על הסיפון", "צהריים כבד — ערב קל"],
            "€0–40 תוספת ביום (Crown Edge + Izumi שולמו מראש · אחה״צ כלול)", "כל היום", "ברירת מחדל — כבר הוזמן",
            "<strong>יובל והילדים:</strong> כוכבות ב־Crown Edge / Hibachi · אחה״צ מים", True),
        option_card("19-09", "B", "כמו A + ערב מופע מוקדם / מנוחה בחדר", 9,
            "אותו בוקר/צהריים קבוע — דגש על ערב רגוע אחרי ארוחת צהריים גדולה.",
            ["לא עומסים על הקיבה", "מופע חינם"],
            ["פחות זמן בריכה בערב"],
            "€0–40 תוספת ביום (כמו A · מופע כלול)", "ערב", "אם עייפים אחרי Izumi",
            "<strong>Super-Tips:</strong> בלי Specialty נוספת בערב"),
        option_card("19-09", "C", "ספא למבוגרים אחרי Izumi (ילדים במועדון/חדר)", 5,
            "רק אם יש פתרון לילדים — הבוקר כבר תפוס.",
            ["שקט להורים"],
            ["פיצול", "עלות נוספת", "יום כבר עמוס עד 14:00"],
            "€80–250 תוספת ספא (מעבר ל־Crown Edge + Izumi ששולמו)", "אחה״צ", "רק עם פתרון לילדים",
            "—"),
    ],
    extra="""
    <section class="section">
      <h2>כבר הוזמן — יום 3 בשייט (19/9)</h2>
      <div class="default-pick">
        <strong>09:00 — Crown Edge Experience</strong><br />
        להגיע ~08:40–08:50 · בדקו באפליקציה מגבלות גיל/גובה ונעליים · אחרי החוויה מנוחה קצרה לפני הארוחה.
      </div>
      <div class="default-pick">
        <strong>12:30 — Izumi Hibachi</strong> (Specialty)<br />
        להגיע ~12:15 · לבקש מהמלצר: <strong>בלי חזיר · בלי פירות ים</strong> (דגים/עוף/בקר/ירקות לפי התפריט) · זו הארוחה החגיגית של היום — בערב רק משהו קל.
      </div>
      <h2>לו״ז מוצע ליום</h2>
      <ol>
        <li>בוקר מוקדם — ארוחת בוקר קלה (לא להתמלא לפני Hibachi)</li>
        <li>09:00 Crown Edge</li>
        <li>12:30 Izumi Hibachi</li>
        <li>אחה״צ — בריכות / פארק מים / חדר</li>
        <li>ערב — מופע · Windjammer קל או My Time קל (לא Specialty שנייה)</li>
      </ol>
      <h2>טיפים</h2>
      <ul>
        <li>הזמינו מופע ערב באפליקציה (חינם)</li>
        <li>אחרי Izumi אין צורך ב־Specialty נוספת בטיול הזה</li>
        <li>פירוט חבילות: <a href="../prebook.html">איך לחסוך על הספינה</a></li>
      </ul>
    </section>
    """,
    taxi=None,
    meeting="<strong>ראשי:</strong> תא 7680.<br /><strong>משני:</strong> דלפק אורחים / נקודת המפגש של הפעילות באפליקציה.",
    exit_ramp="חדר + טאבלט + חטיף קל (לא אחרי Izumi מיד).",
    costs="<table><tr><th>סעיף</th><th>סטטוס</th></tr><tr><td>Crown Edge 09:00</td><td><strong>הוזמן</strong></td></tr><tr><td>Izumi Hibachi 12:30</td><td><strong>הוזמן</strong></td></tr><tr><td>בריכות / מופע</td><td>כלול</td></tr></table>",
    prev="18-09", next="20-09",
)

# ---------- 20 ----------
days["20-09"] = dict(
    title="20 בספטמבר · ברצלונה",
    subtitle="ראשון · ~05:30–16:30 · Sagrada · רמבלס · אוכל ברובע",
    weather={"temp": "26°", "note": "נעים · לא לצאת ב־05:30 עם ילדים — אחרי ארוחת בוקר. Sagrada בימי ראשון נפתחת לרוב מאוחר יותר (~10:30) — לשריין סלוט בהתאם.", "link": "https://www.accuweather.com/en/es/barcelona/307297/weather-forecast/307297"},
    super_tip="כרטיס Sagrada מתוזמן (לא לפני ~10:30 ביום ראשון) + מסלול אחד: רמבלס/רובע גותי.",
    default_text="Sagrada Família (כרטיס מראש) → רמבלס + רובע גותי/טאפאס → גלידה.",
    places="".join([
        place_card("sagrada.jpg", "סגרדה פמיליה",
                   "כנסיית העל של גאודי בברצלונה — בבנייה יותר ממאה שנה. בפנים אור צבעוני מדהים דרך ויטראז׳ים. חובה כרטיס מתוזמן.",
                   "מהנמל במונית ~20–30 דק׳ · במטרו ~35–45 דק׳", "בימי ראשון נפתחת לתיירים לרוב מ־~10:30 — בדקו שעת הכרטיס."),
        place_card("ramblas.jpg", "לאס רמבלס (La Rambla)",
                   "שדרה רחבה ומפורסמת מהפלסה לקטלוניה עד לנמל — אמני רחוב, דוכנים, אווירה. כייסים — ערנות.",
                   "מ־Sagrada במונית ~15–20 דק׳ / מטרו ~20–25 דק׳", "ללכת בחלק מהשדרה, לא חייבים את כולה."),
        place_card("parkguell.jpg", "פארק גואל (אופציונלי)",
                   "פארק מעוצב של גאודי על גבעה — ספסל פסיפס, בתים צבעוניים, תצפית. יפה אך דורש כרטיס מתוזמן + עלייה/תחבורה.",
                   "מהרמבלס במונית ~20–25 דק׳ · בתחבורה ~35–45 דק׳", "פתוח גם בימי ראשון — רק אם נשאר זמן ואנרגיה."),
    ]),
    options=[
        option_card("20-09", "A", "Sagrada (מתוזמן) + רמבלס + אוכל ברובע הגותי", 10,
            "Sagrada + רמבלס + טאפאס ברובע — מתאים לחלון הקצר של יום ראשון.",
            ["וואו של Sagrada", "אוכל ברובע", "מסלול ברור"],
            ["עמידה ב־Sagrada", "כייסים ברמבלס", "חלון נמל עד ~16:30"],
            "€240–350 (Sagrada ×4 + מוניות + אוכל/טאפאס)", "6–7 שעות כולל באפר", "ברירת מחדל ל־20/9 (ראשון)",
            "<strong>לו״ז מוצע:</strong> Sagrada (אחרי פתיחה) → מונית לרמבלס → טאפאס/גלידה ברובע → חזרה לנמל עד ~14:30–15:00", True),
        option_card("20-09", "B", "כמו A + Park Güell בסוף (אם נשאר כוח)", 7,
            "תוספת יפה אך לוחצת על הזמן — במיוחד אחרי פתיחה מאוחרת של Sagrada ביום ראשון.",
            ["עוד גאודי", "תצפית", "פתוח בימי ראשון"],
            ["גבעה/חום", "כרטיס נוסף", "סיכון לאיחור לספינה"],
            "€300–420 (A + Park Güell + העברה נוספת)", "יום מלא בלחץ", "רק אם Sagrada מוקדם יחסית והילדים בשיא",
            "<strong>Super-Tips:</strong> לשקול לדלג — לא must"),
        option_card("20-09", "C", "רק רמבלס + רובע גותי (בלי Sagrada)", 6,
            "קל יותר אם אין כרטיסים ל־Sagrada.",
            ["גמיש", "זול"],
            ["בלי החוויה המרכזית שרציתם"],
            "€80–140 (מוניות + אוכל)", "3–4 שעות", "רק אם אין כרטיסים ל־Sagrada",
            "—"),
        option_card("20-09", "D", "יום חוף Barceloneta", 5,
            "קל, אבל מפספסים Sagrada/רמבלס.",
            ["קל לילדים"],
            ["מפספסים את היעד העיקרי"],
            "€40–80 (תחבורה + שתייה/חטיפים)", "חצי יום", "רק כתוכנית חירום",
            "—"),
    ],
    extra="""
    <section class="section">
      <h2>פתוח היום (ראשון 20/9)</h2>
      <table>
        <tr><th>מקום</th><th>סטטוס</th></tr>
        <tr><td>Sagrada Família</td><td>פתוח לתיירים לרוב מ־~10:30</td></tr>
        <tr><td>La Rambla / רובע גותי</td><td>פתוח</td></tr>
        <tr><td>Park Güell</td><td>פתוח עם כרטיס מתוזמן</td></tr>
      </table>
      <h2>אוכל מומלץ ביום</h2>
      <ul>
        <li>טאפאס בשר/ירקות או טורטיה ברובע הגותי / ליד הרמבלס</li>
        <li>דגים פשוטים בסדר אם בא לכם (לא פירות ים)</li>
        <li>Churros / גלידה להפסקה</li>
      </ul>
    </section>
    """,
    taxi="barcelona",
    meeting="<strong>ראשי:</strong> כבש הספינה.<br /><strong>משני:</strong> כניסת Sagrada / קצה הרמבלס ליד הים (קולומבוס).",
    exit_ramp="מונית ישר לנמל — מדלגים על המשך הרמבלס.",
    costs="<table><tr><th>אפשרות</th><th>משוער</th></tr><tr><td>A Sagrada+רמבלס+אוכל</td><td>€240–350</td></tr><tr><td>B + Park Güell</td><td>€300–420</td></tr></table>",
    prev="19-09", next="21-09",
)

# ---------- 21 ----------
days["21-09"] = dict(
    title="21 בספטמבר · פלמה דה מיורקה",
    subtitle="שני · ~08:30–15:30",
    weather={"temp": "27°", "note": "שמשי · חלון קצר.", "link": "https://www.accuweather.com/en/es/palma/355667/weather-forecast/355667"},
    super_tip="תוכנית אחת — עיר או חוף.",
    default_text="קתדרלה (פתוחה בימי שני לתיירים, לרוב מ־10:00) + עיר עתיקה, או חוף — שניהם ציון 9.",
    places="".join([
        place_card("palma.jpg", "פלמה דה מיורקה · הקתדרלה (La Seu)",
                      "קתדרלה גותית מול הים. ב־21/9 (שני) פתוחה לתיירים לרוב מ־~10:00 עד ~17:15.",
                      "מהנמל למרכז: 10–20 דק׳ במונית", "חלון קצר — באפר חזרה 90 דק׳. מבחוץ יפה גם בלי כרטיס."),
        place_card("beach.jpg", "חופי מיורקה",
                      "אופציה ליום קל: שחייה וחול במקום סיור עירוני. מתאים כשרוצים איפוס אנרגיה באמצע השייט.",
                      "מהנמל לחוף קרוב: לרוב 15–25 דק׳ במונית", "בדקו מזג אוויר וזמן חזרה לספינה."),
    ]),
    options=[
        option_card("21-09", "A", "קתדרלה (מבפנים או מבחוץ) + עיר עתיקה + גלידה", 9,
            "יום שני — הקתדרלה פתוחה לתיירים (מ~10:00). אפשר גם רק מבחוץ אם אין זמן/רצון לתור.",
            ["יפה", "קצר", "פתוח ב־21/9"],
            ["חם באבנים", "שעת פתיחה 10:00 — לא להגיע מוקדם מדי לפנים"],
            "€60–120 (קתדרלה אם נכנסים + גלידה/אוכל קל + מונית)", "3–4 שעות", "עיר",
            "<strong>כולם:</strong> מאוזן", True),
        option_card("21-09", "B", "זמן חוף / שחייה", 9,
            "איפוס סבלנות.",
            ["כיף לילדים"],
            ["פחות אטרקציה"],
            "€40–80 (מונית + שתייה/חטיפים בחוף)", "3–4 שעות", "ים",
            "<strong>יובל והילדים:</strong> מעולה"),
        option_card("21-09", "C", "סיור רחוק יותר", 6,
            "יותר העברות.",
            ["נוף"],
            ["לחץ זמן"],
            "€100–180 (סיור/העברות + אוכל קל)", "רוב היום", "רק מאורגן",
            "<strong>Super-Tips:</strong> נסיעות = בינוני"),
        option_card("21-09", "D", "קניון בלבד", 5,
            "מפספס את האי.",
            ["מיזוג"],
            ["גנרי"],
            "€50–150 (תחבורה + קניות לפי בחירה)", "2–3 שעות", "גשם/עייפות",
            "<strong>יובל:</strong> אוקיי"),
    ],
    extra="",
    taxi="palma",
    meeting="<strong>ראשי:</strong> כבש הספינה.<br /><strong>משני:</strong> ליד הקתדרלה / Plaça de la Reina.",
    exit_ramp="גלידה וחזרה לספינה.",
    costs="<table><tr><th>אפשרות</th><th>משוער</th></tr><tr><td>A/B</td><td>€40–100</td></tr></table>",
    prev="20-09", next="22-09",
)

# ---------- 22 ----------
days["22-09"] = dict(
    title="22 בספטמבר · מרסיי / פרובאנס",
    subtitle="שלישי · ~09:30–17:30",
    weather={"temp": "26°", "note": "נעים · לא טיולי קלנקים ארוכים.", "link": "https://www.accuweather.com/en/fr/marseille/227246/weather-forecast/227246"},
    super_tip="אזור תיירותי מרכזי או סיור לאקס.",
    default_text="Vieux Port או אקס־אן־פרובאנס — שניהם 8.",
    places=place_card("marseille.jpg", "מרסיי · Vieux Port",
                      "עיר הנמל העתיקה של צרפת על הים התיכון. הנמל הישן (Vieux Port) הוא הלב התיירותי — סירות, בתי קפה, ותצפית ל־Notre-Dame de la Garde על הגבעה.",
                      "מהנמל ל־Vieux Port: לרוב 15–30 דק׳ (שאטל/מונית)", "הישארו באזור התיירותי המרכזי."),
    options=[
        option_card("22-09", "A", "Vieux Port + תצפית Notre-Dame + הליכה קצרה", 8,
            "שליטה באורך.",
            ["נוף", "אוכל"],
            ["חלקים מהעיר פחות נעימים"],
            "€80–140 (מוניות + אוכל קל + כרטיס תצפית אם יש)", "4–5 שעות", "קרוב לספינה",
            "<strong>Super-Tips:</strong> טוב עם הפסקות", True),
        option_card("22-09", "B", "אקס־אן־פרובאנס", 8,
            "כפר־עיר מקסים.",
            ["אווירה", "קניות"],
            ["נסיעה ~30–45 דק׳ לכל כיוון"],
            "€200–350 (סיור/העברה הלוך־חזור + אוכל)", "רוב היום", "פרובאנס קלאסי",
            "<strong>יובל/שרון:</strong> קניות"),
        option_card("22-09", "C", "סירת קלנקים (בלי טיול רגלי)", 7,
            "נוף; שמש וים.",
            ["נופים"],
            ["תורים"],
            "€150–300 (סירה ×4 + אוכל קל)", "חצי יום", "אם הים שקט",
            "<strong>Super-Tips:</strong> תלוי בתנודת הסירה"),
        option_card("22-09", "D", "טיול רגלי ארוך בקלנקים", 3,
            "חום ומרחק.",
            [],
            ["עייפות"],
            "€40–100 (תחבורה + מים; לא מומלץ)", "ארוך", "לא",
            "<strong>Super-Tips:</strong> לא"),
    ],
    extra="",
    taxi="marseille",
    meeting="<strong>ראשי:</strong> כבש הספינה.<br /><strong>משני:</strong> מרכז Vieux Port.",
    exit_ramp="חזרה מוקדמת לספינה.",
    costs="<table><tr><th>אפשרות</th><th>משוער</th></tr><tr><td>A</td><td>€80–140</td></tr><tr><td>B</td><td>€200–350</td></tr></table>",
    prev="21-09", next="23-09",
)

# ---------- 23 ----------
days["23-09"] = dict(
    title="23 בספטמבר · צ׳ינקווה טרה",
    subtitle="רביעי · לה ספציה · 2–3 כפרים",
    weather={"temp": "25°", "note": "נעים · רכבות עמוסות.", "link": "https://www.accuweather.com/en/it/la-spezia/214748/weather-forecast/214748"},
    super_tip="2 כפרים אידיאלי; כפר שלישי רק אם כולם בשיא. בלי שביל טיול ארוך.",
    default_text="ריומג׳ורה + מנרולה (+ ורנאצה אם נשאר כוח) — לא רק נוף: אוכל, נמל, חנויות קטנות, צילומים.",
    places="".join([
        place_card("cinqueterre.jpg", "צ׳ינקווה טרה",
                   "חמישה כפרי דייגים צבעוניים על צוקי ליגוריה — מורשת עולמית. מגיעים בעיקר ברכבת מלה ספציה. הכפרים קטנים ותלולים (מדרגות).",
                   "לה ספציה → כפר ראשון ברכבת: ~10–20 דק׳", "כרטיס יומי Cinque Terre / רכבות תכופות."),
        place_card("vernazza.jpg", "מה עושים בכפר (לא רק להסתכל)",
                   "זה לא רק נוף: פוקאצ׳ה/גלידה, הליכה קצרה במעגן, חנויות מזכרות קטנות, טעימת פסטו/יין להורים, צילומי משפחה במדרגות הצבעוניות, ובכפרים עם חוף קטן — מים עד הברכיים אם חם.",
                   "בתוך כפר: 45–90 דק׳ מספיקים", "עדיף איכות בשני כפרים מאשר ריצה בחמישה."),
    ]),
    options=[
        option_card("23-09", "A", "2 כפרים ברכבת (ריומג׳ורה + מנרולה) + אוכל/נמל", 9,
            "מממש כפרים בלי להעמיס.",
            ["נוף+אוכל+קצב", "שליטה"],
            ["מדרגות", "רכבות צפופות"],
            "€120–200 (רכבת Cinque Terre + אוכל/גלידה)", "6–7 שעות עם באפר", "ברירת מחדל",
            "<strong>בכל כפר:</strong> פוקאצ׳ה/גלידה · 10 דק׳ במעגן · צילום · חנות אחת", True),
        option_card("23-09", "B", "2 כפרים + כפר שלישי קצר (ורנאצה) אם יש אנרגיה", 8,
            "תואם את הרצון ל־2–3 כפרים — רק עם משמעת יציאה.",
            ["עוד כפר אייקוני", "עדיין בלי הליכה בין כפרים"],
            ["יותר רכבות", "סיכון לעייפות/איחור"],
            "€140–220 (רכבת + אוכל ל־3 כפרים)", "יום מלא", "אם אחרי כפר 2 כולם עדיין שמחים",
            "<strong>כלל:</strong> אם האנרגיה יורדת בכפר 2 — חוזרים בלי 3"),
        option_card("23-09", "C", "דילוג בסירה בין 2 כפרים", 8,
            "וואו מהים; תורים.",
            ["נוף מהים"],
            ["תורים/מזג אוויר"],
            "€200–350 (סירה + אוכל + רכבת גיבוי)", "רוב היום", "ים שקט",
            "<strong>Super-Tips:</strong> תור לסירה = האתגר"),
        option_card("23-09", "D", "סיור מודרך חצי יום", 8,
            "פחות ניווט.",
            ["ראש שקט"],
            ["פחות חופש"],
            "€250–450 (סיור מודרך למשפחה)", "חצי יום", "אם לא בא רכבות",
            "<strong>הורים:</strong> ראש שקט"),
        option_card("23-09", "E", "3+ כפרים או שביל הליכה", 4,
            "overreach.",
            [],
            ["עייפות ואיחור"],
            "€150–250 (לא מומלץ — סיכון לאיחור)", "לחץ", "לא",
            "<strong>Super-Tips:</strong> לא"),
        option_card("23-09", "F", "פיזה בלבד", 6,
            "קל יותר, לא הכפרים שרציתם.",
            ["לוגיסטיקה קלה"],
            ["לא CT"],
            "€100–180 (העברה/רכבת + אוכל)", "5–6 שעות", "גיבוי למזג אוויר",
            "<strong>Super-Tips:</strong> צילום קצר + גלידה"),
    ],
    extra="""
    <section class="section">
      <h2>רעיונות לפעילות בכל כפר (15–40 דק׳ לרעיון)</h2>
      <table>
        <tr><th>פעילות</th><th>למי מתאים</th><th>הערה</th></tr>
        <tr><td>פוקאצ׳ה / גלידה / מיץ</td><td>כולם — במיוחד אוהבי מתוק</td><td>״פרס״ בין הליכות</td></tr>
        <tr><td>הליכה במעגן / מזח</td><td>צילום · יובל</td><td>שטוח יחסית, פחות מדרגות</td></tr>
        <tr><td>סמטאות צבעוניות לצילום משפחתי</td><td>כולם</td><td>5–10 דק׳ — לא לטפס עד סוף הכפר</td></tr>
        <tr><td>חנות מזכרות קטנה / קרמיקה</td><td>יובל/שרון</td><td>אחת לכל כפר מספיק</td></tr>
        <tr><td>טעימת פסטו / יין (הורים)</td><td>טמיר/שרון</td><td>הילדים עם גלידה במקביל</td></tr>
        <tr><td>רגליים במים (אם יש גישה נוחה)</td><td>יובל והילדים</td><td>רק בכפר עם חוף/סלעים נוחים — לא חובה</td></tr>
      </table>
      <p><strong>מסלול מוצע ל־2 כפרים:</strong> ריומג׳ורה (נמל+סמטאות+אוכל) → רכבת → מנרולה (תצפית קצרה+גלידה) → חזרה ללה ספציה עם שעתיים באפר.</p>
      <p><strong>ל־3 כפרים:</strong> הוסיפו ורנאצה רק אם השעה מאפשרת (פלאצה מרכזית + גלידה) — ואז ישר חזרה.</p>
    </section>
    """,
    taxi="laspezia",
    meeting="<strong>ראשי:</strong> כבש הספינה.<br /><strong>משני:</strong> תחנת La Spezia Centrale.",
    exit_ramp="אחרי כפר אחד — חזרה ללה ספציה וגלידה.",
    costs="<table><tr><th>אפשרות</th><th>משוער</th></tr><tr><td>A שני כפרים</td><td>€120–200</td></tr><tr><td>B שלושה כפרים</td><td>€140–220</td></tr><tr><td>C/D</td><td>€200–450</td></tr></table>",
    prev="22-09", next="24-09",
)

# ---------- 24 ----------
days["24-09"] = dict(
    title="24 בספטמבר · חזרה לרומא",
    subtitle="חמישי · ירידה ~07:00 · לילה אחרון",
    weather={"temp": "26°", "note": "נעים · אנרגיה נמוכה אחרי שייט.", "link": "https://www.accuweather.com/en/it/rome/213633/weather-forecast/213633"},
    super_tip="מנוחה + ערב קל. מחר טיסה מוקדמת.",
    default_text="העברה פרטית → מלון → מנוחה → טרווי קל.",
    places=place_card("spanish-steps.jpg", "רומא — לילה אחרון",
                      "חוזרים מהנמל למלון (ראו השוואת מלונות). ערב קל במרכז — בלי אטרקציות כבדות.",
                      "צ׳יוויטווקיה→רומא בואן: ~1–1.5 שעות", "הזמינו העברה ל־FCO למחר ל־07:00–07:15."),
    options=[
        option_card("24-09", "A", "העברה פרטית → מלון → מנוחה → טרווי/ספניש סטפס קל", 9,
            "איזון נכון.",
            ["רגוע"],
            ["צ׳ק־אין מוקדם לא תמיד אפשרי"],
            "€200–300 (העברה מהנמל €120–180 + ערב אוכל קל €80–120)", "יום רגוע", "ברירת מחדל",
            "<strong>כולם:</strong> מנוחה = הצלחה", True),
        option_card("24-09", "B", "כמו A + קניות אחרונות", 8,
            "אם יש אנרגיה.",
            ["קניות"],
            ["עייפות"],
            "€220–380 (A + קניות לפי בחירה)", "תוספת 1–2 שע׳", "אם רוצים",
            "<strong>Super-Tips:</strong> חנות אחת–שתיים"),
        option_card("24-09", "C", "טיול יום למקום אחר", 2,
            "מתיש לפני הטיסה.",
            [],
            ["קריסה"],
            "€250–450 (לא מומלץ לפני טיסה)", "לא", "לא",
            "<strong>Super-Tips:</strong> לא"),
    ],
    extra="""
    <section class="section">
      <h2>מלון</h2>
      <p><a href="../hotels.html">השוואת מלונות לילה אחרון</a> — המלצה: Repubblica / Via Nazionale עם מעלית.</p>
    </section>
    """,
    taxi="rome",
    meeting="<strong>ראשי:</strong> לובי המלון.",
    exit_ramp="פיצה ליד המלון ושינה מוקדמת.",
    costs="<table><tr><th>סעיף</th><th>משוער</th></tr><tr><td>העברה מהנמל</td><td>€120–180</td></tr><tr><td>ערב</td><td>€80–120</td></tr></table>",
    prev="23-09", next="25-09",
)

# ---------- 25 ----------
days["25-09"] = dict(
    title="25 בספטמבר · טיסה לישראל",
    subtitle="שישי · אל על ~11:00 מ־FCO",
    weather={"temp": "—", "note": "בדקו תנועה בבוקר.", "link": "https://www.accuweather.com/en/it/rome/213633/weather-forecast/213633"},
    super_tip="בלי עצירות — חטיפים ואוזניות לדרך.",
    default_text="העברה פרטית, יעד בשדה ~08:00.",
    places=place_card("airport.jpg", "FCO · נמל התעופה לאונרדו דה וינצ׳י",
                      "שדה התעופה הבינלאומי של רומא. לטיסת אל על ב־11:00 מומלץ להיות בשדה סביב 08:00 (בידוק+דרכונים).",
                      "ממרכז רומא בואן פרטי: ~45–70 דק׳", "רק מוניות/העברות רשמיות."),
    options=[
        option_card("25-09", "A", "העברה פרטית מלון→FCO · יעד ~08:00", 10,
            "האפשרות ההגיונית היחידה.",
            ["אמין", "מזוודות"],
            ["עלות"],
            "€55–80 (העברה פרטית למלון→FCO)", "45–70 דק׳", "חובה",
            "<strong>Super-Tips:</strong> טאבלט/חטיף ברכב", True),
    ],
    extra="""
    <section class="section">
      <h2>צ׳ק־ליסט בוקר</h2>
      <ul class="checklist">
        <li><input type="checkbox" data-id="dep-passports" /> דרכונים + כרטיסי טיסה</li>
        <li><input type="checkbox" data-id="dep-harel" /> פרטי ביטוח הראל</li>
        <li><input type="checkbox" data-id="dep-chargers" /> מטענים</li>
        <li><input type="checkbox" data-id="dep-keys" /> החזרת מפתח מלון</li>
      </ul>
    </section>
    """,
    taxi="rome",
    meeting="<strong>ראשי:</strong> דלפק אל על ב־FCO.",
    exit_ramp="אין גמישות — להתקשר להעברה/חברה אם איחור.",
    costs="<table><tr><th>סעיף</th><th>משוער</th></tr><tr><td>העברה FCO</td><td>€55–80</td></tr></table>",
    prev="24-09", next=None,
)


def costs_table_for_day(day_id):
    """Build a comparison table from registered options for this day."""
    rows = []
    for letter in "ABCDEF":
        key = f"{day_id}-{letter}"
        opt = OPTION_REGISTRY.get(key)
        if not opt:
            continue
        rec = " ★" if opt.get("recommended") else ""
        rows.append(
            f"<tr><td><strong>{letter}</strong>{rec}</td>"
            f"<td>{opt['title']}</td>"
            f"<td class=\"cost-cell\">{opt['cost']}</td></tr>"
        )
    if not rows:
        return "<p class=\"note\">אין אפשרויות עם עלות ליום זה.</p>"
    return (
        "<table>"
        "<tr><th>אפשרות</th><th>מה כולל</th><th>עלות משוערת ליום (משפחה ×4)</th></tr>"
        + "".join(rows)
        + "</table>"
    )


def write_day(day_id, data):
    options_html = "\n".join(data["options"])
    places = data.get("places") or ""
    taxi_key = data.get("taxi")
    taxi_html = taxi_box(taxi_key) if taxi_key else ""
    costs = costs_table_for_day(day_id)
    html = day_page(
        day_id,
        data["title"],
        data["subtitle"],
        data["weather"],
        data["super_tip"],
        data["default_text"],
        places,
        options_html,
        data.get("extra") or "",
        taxi_html,
        data["meeting"],
        data["exit_ramp"],
        costs,
        data["prev"],
        data["next"],
    )
    (DAYS / f"{day_id}.html").write_text(html, encoding="utf-8")
    n = 0
    for key, opt in OPTION_REGISTRY.items():
        if opt["day_id"] == day_id:
            write_option_page(
                opt,
                data["title"],
                data["subtitle"],
                data["meeting"],
                data["exit_ramp"],
                taxi_key,
            )
            n += 1
    print(f"wrote {day_id} (+{n} option plans)")


def main():
    DAYS.mkdir(exist_ok=True)
    # Clear stale option HTML files
    for p in DAYS.glob("*-*.html"):
        if p.name.count("-") >= 2:  # e.g. 14-09-A.html
            p.unlink()
    for day_id, data in days.items():
        write_day(day_id, data)
    print("done", len(OPTION_REGISTRY), "option pages")


if __name__ == "__main__":
    main()
