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


def rome_guide_html(depth=1):
    """Link to Michal Milrad Rome PDF (Rome land days)."""
    p = "../" if depth else ""
    return f"""
    <section class="section">
      <h2>מדריך רומא (מיכל מילרד)</h2>
      <p><a class="btn" href="{p}assets/Michal_Milrad_Rome_2026.pdf" target="_blank" rel="noopener">פתחו את מדריך רומא 2026 (PDF)</a></p>
      <p class="note">מדריך משפחתי לרומא — לשמירה במכשיר לשימוש אופליין.</p>
    </section>"""


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
    <p class="brand"><a href="{home}" style="color:#fff;text-decoration:none">משפחת לנון</a></p>
    <p class="tagline">מדריך החופשה · רומא · Legend of the Seas · 14–25 בספטמבר 2026</p>
    <nav class="nav-days" aria-label="ימי הטיול">
      {nav_days(current, p)}
    </nav>
    <nav class="nav-links">
      <a href="{home}">בית</a>
      <a href="{p}emergency.html">חירום והעברות</a>
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
            "בשדה FCO — Romio הוזמן (14/9 ~11:45). גיבוי: מוניות לבנות רשמיות מתור המוניות (תעריף קבוע למרכז ~€50–55).<br />"
            "<strong>לא:</strong> אנשים שמציעים נסיעה בתוך האולם.",
        ),
        "civitavecchia": (
            "צ׳יוויטווקיה / נמל",
            "<strong>מומלץ:</strong> העברה Romio שהוזמנה (17/9 איסוף 10:30 · 24/9 איסוף 09:00).<br />"
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
        <p class="note" style="margin-top:0.5rem">פירוט לכל היעדים: <a href="../taxis.html">עמוד מוניות בטוחות</a> · <a href="../emergency.html">חירום והעברות</a></p>
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
        transport.append(("fco-transfer", 'Romio FCO→Colonna ~11:45 — <a href="../emergency.html#transfers">פרטי ההעברה</a>'))
        if letter == "A":
            book.append(("rest-reserve", "שיריינו מסעדה ליד המלון (Armando / Emma וכו׳)"))
            timeline = [
                "~11:45 נחיתה LY285 → דרכונים → איסוף מזוודות",
                "Romio FCO→Colonna (~45–60 דק׳) → צ׳ק־אין / השארת מזוודות",
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
            book.append(("van", 'Romio מלון→נמל · איסוף 10:30 — <a href="../emergency.html#transfers">פרטים</a>'))
            transport = [
                ("confirm-driver", "אישור נהג Romio / וואטסאפ יום לפני"),
                ("luggage", "מזוודות מוכנות בלובי לפני 10:30"),
            ]
            timeline = [
                "בוקר: ארוחת בוקר + צ׳ק־אאוט",
                "Romio 10:30 · נסיעה לנמל (~1–1.5 שע׳)",
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
        book.append(("hotel-last", "אישור מלון Accademia + בקשת early luggage storage"))
        book.append(("fco-next", 'Romio Accademia→FCO מחר 06:30 — <a href="../emergency.html#transfers">פרטים</a>'))
        if letter == "A":
            book.append(("civ-rome", 'Romio נמל→Accademia · איסוף 09:00 — <a href="../emergency.html#transfers">פרטים</a>'))
            timeline = [
                "ירידה מהספינה ~07:30",
                "המתנה בנמל עם מזוודות עד Romio 09:00",
                "נסיעה לרומא (~1–1.5 שע׳) → Hotel Accademia, Piazza Accademia di San Luca 75",
                "צ׳ק־אין / השארת מזוודות + מנוחה",
                "ערב קל ליד המלון · שינה מוקדמת (מחר איסוף 06:30)",
            ]

    if day_id == "25-09":
        book.extend([
            ("alarm", "שעון מעורר + באפר"),
            ("fco-transfer", 'Romio Accademia→FCO · איסוף 06:30 — <a href="../emergency.html#transfers">פרטים</a>'),
            ("boarding-pass", "כרטיסי עלייה לטיסה / אפליקציית אל על"),
            ("harel", 'פרטי ביטוח הראל — <a href="../emergency.html">עמוד חירום</a>'),
        ])
        timeline = [
            "יציאה מהמלון 06:30 עם Romio",
            "הגעה ל־FCO ~07:15–07:40",
            "צ׳ק־אין + בידוק",
            "זמן המתנה עם חטיפים ואוזניות",
            "טיסה LY386 ~10:00",
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
    icon = "../assets/favicon.png" if depth else "assets/favicon.png"
    theme_cls = f' class="{theme}"' if theme else ""
    return f"""<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
{FONTS}
  <link rel="icon" href="{icon}" type="image/png" />
  <link rel="apple-touch-icon" href="{icon}" />
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

ROME_PDF = rome_guide_html(1)

# ---------- 14 ----------
days["14-09"] = dict(
    title="14 בספטמבר · הגעה לרומא",
    subtitle="שני · טיסת LY285 · נחיתה FCO ~11:45 · Colonna Collection",
    weather={"temp": "27°", "note": "חם ונעים · שמש · כובעים ומים.", "link": "https://www.accuweather.com/en/it/rome/213633/weather-forecast/213633"},
    super_tip="אחרי טיסה — מלון, מקלחת, ואז הליכה קצרה לטרווי בלבד.",
    default_text="אפשרות A — LY285 → Colonna Collection → ערב באזור טרווי.",
    places="".join([
        place_card("trevi.jpg", "מזרקת טרווי",
                   "מזרקת הבארוק המפורסמת ביותר ברומא. בערב מוארת ויפה — עצירה קצרה לצילום מספיקה.",
                   "מהמלון ~8–12 דק׳ הליכה", "עמוס בתיירים — לא להישאר ארוך ביום הגעה."),
        place_card("pantheon.jpg", "הפנתיאון / אזור המלון",
                   "המלון במרחק דקות הליכה מהפנתיאון ו־Via del Corso.",
                   "מהמלון ~3–5 דק׳ הליכה", "הכניסה חינמית בדרך כלל."),
        place_card("gelato.jpg", "גלידה רומית",
                   "Giolitti או Della Palma ליד המלון — פרס מושלם אחרי הטיסה.",
                   "מהמלון ~5–10 דק׳ הליכה", "אפשר לקחת לדרך אם יש תור."),
    ]),
    options=[
        option_card("14-09", "A", "LY285 → Colonna → ערב בטרווי והאזור", 10,
            "תוכנית האקסל: טיסה, מלון, ואז להסתובב בטרווי.",
            ["תואם לתוכנית המשפחה", "קרוב למלון", "שליטה באורך"],
            ["עומס ליד המזרקה", "ג׳ט־לג"],
            "€100–180 (ארוחה + גלידה; העברה בנפרד)", "הליכה 20–40 דק׳ בערב", "ברירת מחדל",
            "<strong>Super-Tips:</strong> קצר ומתוק אחרי טיסה", True,
            plan={
                "timeline": [
                    "09:00 — המראה LY285 (אל על) · כ־3:40 שעות",
                    "~11:45 — נחיתה FCO → דרכונים → מזוודות",
                    "Romio FCO→Colonna Collection (~45–60 דק׳) → צ׳ק־אין",
                    "צהריים — מקלחת, מים, ארוחה קלה ליד המלון",
                    "ערב — הליכה קצרה לטרווי והאזור + גלידה → שינה מוקדמת",
                ],
                "book": [
                    ("ly285", "אישור טיסת LY285 + כרטיסי עלייה"),
                    ("fco-transfer", 'Romio FCO→Colonna ~11:45 — <a href="../emergency.html#transfers">פרטי ההעברה</a>'),
                    ("rest-reserve", "מסעדה ליד המלון לערב אם רוצים לשריין"),
                ],
            }),
        option_card("14-09", "B", "מלון בלבד + ערב קצר מאוד (בלי טרווי)", 8,
            "אם כולם מותשים מהטיסה — רק מקלחת, אוכל ליד המלון, שינה.",
            ["מינימום הליכה", "התאוששות"],
            ["פחות ״וואו״ ביום הראשון"],
            "€40–120", "ערב קצר", "אם עייפים מאוד",
            "<strong>כולם:</strong> שינה = הצלחה"),
    ],
    extra=ROME_PDF + """
    <section class="section">
      <h2>מסעדות מומלצות ליד המלון (Colonna / פנתיאון)</h2>
      <p class="note">לבקש תמיד: בלי חזיר / בלי פירות ים · דגים בסדר.</p>
      <ul class="restaurant-list">
        <li><strong>Armando al Pantheon</strong> — טרטוריה קלאסית · שריון מומלץ · ~5 דק׳.</li>
        <li><strong>Emma Pizzeria</strong> — פיצה משפחתית · ~10–12 דק׳.</li>
        <li><strong>Osteria dell'Ingegno</strong> — כיכר נחמדה · ~5–7 דק׳.</li>
        <li><strong>גלידה:</strong> Giolitti או Della Palma.</li>
      </ul>
      <h2>תחבורה מהשדה</h2>
      <table>
        <tr><th>אפשרות</th><th>זמן משוער</th><th>עלות</th></tr>
        <tr><td>Romio FCO→Colonna (הוזמן)</td><td>45–60 דק׳</td><td>€85</td></tr>
        <tr><td>מונית רשמית FCO (גיבוי, תעריף קבוע)</td><td>45–60 דק׳</td><td>~€50–55</td></tr>
      </table>
      <p>פרטי נהג ווואטסאפ: <a href="../emergency.html#transfers">חירום והעברות · Romio</a></p>
      <p>מדריך רומא PDF: <a href="../assets/Michal_Milrad_Rome_2026.pdf" target="_blank" rel="noopener">Michal Milrad Rome 2026</a></p>
    </section>
    """,
    taxi="rome",
    meeting="<strong>ראשי:</strong> לובי המלון.<br /><strong>משני:</strong> Piazza Colonna.",
    exit_ramp="חזרה למלון, מקלחת, חטיף בחדר.",
    costs="",
    prev=None, next="15-09",
)

# ---------- 15 ----------
days["15-09"] = dict(
    title="15 בספטמבר · קולוסיאום",
    subtitle="שלישי · יום must-see · לפי התוכנית: קולוסיאום (ערב)",
    weather={"temp": "28°", "note": "חם · בוקר עדיף לאתרים פתוחים; אפשר גם כניסה אחה״צ/ערב לפי כרטיס.", "link": "https://www.accuweather.com/en/it/rome/213633/weather-forecast/213633"},
    super_tip="כרטיס מתוזמן + הפסקת מזגן אחרי האתר. לפי האקסל הדגש הוא קולוסיאום ביום זה.",
    default_text="אפשרות A — יום קולוסיאום (כרטיס מתוזמן; האקסל מציין ערב — בחרו סלוט שמתאים לאנרגיה).",
    places="".join([
        place_card("colosseum.jpg", "הקולוסיאום",
                   "האמפיתיאטרון הרומי הגדול בעולם. כרטיס מתוזמן חובה; ילדים מתחת ל־18 לרוב חינם + עמלה.",
                   "מהמלון ~25–35 דק׳ הליכה · או מונית 10–15 דק׳", "לא לדחוס פורום מלא אם האנרגיה יורדת."),
        place_card("forum.jpg", "פורום / Full Experience (גיבוי)",
                   "פורום או Full Experience רק אם יש כרטיסים ואנרגיה — לא חובה להצלחת היום.",
                   "תוספת זמן לפי כרטיס", "יציאת חירום: גלידה + חזרה למלון."),
    ]),
    options=[
        option_card("15-09", "A", "קולוסיאום (מתוזמן) · דגש יום לפי התוכנית", 10,
            "התוכנית המשפחתית ליום זה: קולוסיאום.",
            ["must-see", "ברור וממוקד", "גמישות אחרי"],
            ["עמידה ותורים", "חום"],
            "€150–230 (כרטיסים 2 מבוגרים + מונית + אוכל)", "2–3 שעות באתר", "ברירת מחדל",
            "<strong>Super-Tips:</strong> סיפורי גלדיאטורים קצרים", True,
            plan={
                "timeline": [
                    "בוקר — ארוחת בוקר + מנוחה / קניות קלות באזור המלון (לפי אנרגיה)",
                    "צהריים — ארוחה קלה במזגן",
                    "אחה״צ/ערב — כניסה מתוזמנת לקולוסיאום (לפי שעת הכרטיס באקסל: ערב)",
                    "אחרי — גלידה או מונית חזרה למלון · בלי פורום מלא אם עייפים",
                ],
                "book": [
                    ("colo-tickets", "כרטיסי קולוסיאום רשמיים מתוזמנים (~30 יום מראש)"),
                    ("screenshots", "צילומי מסך של הכרטיסים אופליין"),
                ],
            }),
        option_card("15-09", "B", "קולוסיאום בוקר + מנוחה אחה״צ", 8,
            "אם מעדיפים פחות חום בערב — סלוט בוקר מוקדם ואז איפוס.",
            ["פחות חום", "ערב חופשי"],
            ["קימה מוקדמת"],
            "€150–230", "בוקר באתר", "אם יש כרטיס בוקר",
            "<strong>Super-Tips:</strong> אחה״צ מזגן בלבד"),
        option_card("15-09", "C", "רק קולוסיאום קצר — בלי פורום", 8,
            "יציאה מוקדמת מהאתר ברגע שהאנרגיה יורדת.",
            ["קצר", "פחות סבלנות נדרשת"],
            ["פחות מהכרטיס"],
            "€150–230", "90–120 דק׳", "אם מישהו מתעייף",
            "<strong>כולם:</strong> עדיף פחות וטוב"),
    ],
    extra=ROME_PDF + """
    <section class="section">
      <h2>הזמנה</h2>
      <p>אתר רשמי: <a href="https://ticketing.colosseo.it" target="_blank" rel="noopener">ticketing.colosseo.it</a></p>
    </section>
    """,
    taxi="rome",
    meeting="<strong>ראשי:</strong> שער הכניסה לקולוסיאום.<br /><strong>משני:</strong> קשת קונסטנטינוס.",
    exit_ramp="גלידה/מונית חזרה למלון — בלי פורום.",
    costs="",
    prev="14-09", next="16-09",
)

# ---------- 16 ----------
days["16-09"] = dict(
    title="16 בספטמבר · סדנת פסטה וטירמיסו",
    subtitle="רביעי · סדנת פסטה וטירמיסו (GetYourGuide) · אריזה לשייט",
    weather={"temp": "28°", "note": "חם · סדנה במקום מקורה = יתרון.", "link": "https://www.accuweather.com/en/it/rome/213633/weather-forecast/213633"},
    super_tip="סדנה מודרכת = פחות החלטות. לבקש מראש: בלי חזיר/פירות ים.",
    default_text="אפשרות A — סדנת פסטה וטירמיסו (GetYourGuide).",
    places="".join([
        place_card("food-tour.jpg", "סדנת בישול",
                   "סדנת פסטה וטירמיסו מ־GetYourGuide — חוויה מעשית למשפחה.",
                   "מהמלון במונית ~15–25 דק׳ (תלוי תנועה)", "לבדוק שעת מפגש באישור ההזמנה."),
        place_card("pantheon.jpg", "אחה״צ במלון / מרכז",
                   "אחרי הסדנה — מנוחה ואריזה לשייט. אופציה קלה: הליכה קצרה ליד המלון.",
                   "באזור המלון", "מסמכים ותרופות בטרולי לשייט."),
    ]),
    options=[
        option_card("16-09", "A", "סדנת פסטה וטירמיסו (GetYourGuide) · בוקר", 10,
            "תוכנית האקסל ליום זה — סדנת בישול משפחתית.",
            ["כבר בתוכנית", "כיף לילדים", "מקורה"],
            ["נסיעה לנקודת המפגש", "עלות סדנה"],
            "€200–350 (סדנה למשפחה — לפי GetYourGuide) + מונית", "בוקר / חצי יום", "ברירת מחדל",
            "<strong>לבקש:</strong> בלי חזיר/פירות ים", True,
            plan={
                "timeline": [
                    "בוקר — מונית לנקודת המפגש של הסדנה (GetYourGuide) · להגיע 10–15 דק׳ לפני",
                    "סדנת פסטה וטירמיסו + ארוחה מהמה שהכנתם (לפי הפורמט בהזמנה)",
                    "צהריים/אחה״צ — חזרה למלון · מנוחה",
                    "ערב — אריזה לשייט (מסמכים, תרופות, בגדי ים בטרולי)",
                ],
                "book": [
                    ("gyg-pasta", "הזמנת סדנת פסטה+טירמיסו ב־GetYourGuide"),
                    ("diet", "בקשת התאמות: בלי חזיר / בלי פירות ים"),
                    ("meeting-point", "לשמור נקודת מפגש ושעה מהאישור"),
                ],
                "food": "הסדנה כוללת טעימות — עדיין לבקש בלי חזיר/פירות ים. דגים בסדר אם מופיעים.",
            }),
        option_card("16-09", "B", "הליכה קלה בפנתיאון/נבונה + אריזה (בלי סדנה)", 7,
            "גיבוי אם הסדנה מתבטלת או אם רוצים יום רגוע לפני השייט.",
            ["קרוב למלון", "זול"],
            ["מפספסים את הסדנה שתוכננה"],
            "€40–100", "2–3 שעות", "גיבוי",
            "<strong>Super-Tips:</strong> אריזה מוקדמת"),
    ],
    extra=ROME_PDF,
    taxi="rome",
    meeting="<strong>ראשי:</strong> נקודת המפגש באישור הסדנה.<br /><strong>משני:</strong> לובי המלון.",
    exit_ramp="מונית חזרה למלון ואריזה — בלי אטרקציה נוספת.",
    costs="",
    prev="15-09", next="17-09",
)

# ---------- 17 ----------
days["17-09"] = dict(
    title="17 בספטמבר · עלייה לספינה",
    subtitle="חמישי · Romio 10:30 לנמל · Legend of the Seas · תא 7680 · AGT 19:00",
    weather={"temp": "27°", "note": "נעים · באונייה מיזוג — שכבה קלה.", "link": "https://www.accuweather.com/en/it/civitavecchia/213198/weather-forecast/213198"},
    super_tip="יום לוגיסטיקה — Romio 10:30 מהמלון לנמל, בלי אטרקציות בדרך. ערב: America's Got Talent 19:00.",
    default_text="אפשרות A — Romio 10:30 לנמל · עלייה · מופע AGT 19:00.",
    places="".join([
        place_card("cruise-port.jpg", "צ׳יוויטווקיה",
                   "נמל השייט של רומא — כ־70–80 ק״מ מרומא.",
                   "מרומא בואן: כ־1–1.5 שעות", "להגיע לפי חלון הצ׳ק־אין באפליקציה."),
        place_card("ship.jpg", "Legend of the Seas · תא 7680",
                   "סיפון 7 · קטגוריה F1 · My Time 17:30–18:30.",
                   "בתוך הנמל לפי הוראות", "ערב: America's Got Talent 19:00."),
    ]),
    options=[
        option_card("17-09", "A", "Romio 10:30 לנמל → עלייה → AGT 19:00", 10,
            "תוכנית האקסל: יציאה לקרוז בבוקר + מופע בערב.",
            ["תואם תוכנית", "דלת לדלת עם מזוודות", "מופע משפחתי"],
            ["יום לוגיסטי", "המתנה בעלייה"],
            "€199 (Romio €170 + €29 PayPal)", "נסיעה 1–1.5 שע׳ + עלייה", "ברירת מחדל",
            "<strong>כולם:</strong> ראש שקט", True,
            plan={
                "timeline": [
                    "בוקר — ארוחת בוקר + צ׳ק־אאוט · Romio איסוף 10:30 ב־Colonna",
                    "עלייה לספינה לפי החלון באפליקציה → תא 7680",
                    "צהריים/אחה״צ — חקר קצר / בריכה / ארוחת צהריים בספינה",
                    "17:30–18:30 — My Time (אם רעבים לפני המופע; אחרת קל)",
                    "19:00 — America's Got Talent (לשריין באפליקציה אם נדרש)",
                ],
                "book": [
                    ("van", 'Romio מלון→נמל 10:30 — <a href="../emergency.html#transfers">פרטים</a>'),
                    ("royal-checkin", "צ׳ק־אין דיגיטלי + חלון עלייה"),
                    ("dining", "My Time Dining 17:30–18:30"),
                    ("agt", "America's Got Talent 19:00 — הזמנה באפליקציה"),
                ],
            }),
        option_card("17-09", "B", "רכבת Termini→Civitavecchia + מונית לנמל", 6,
            "זול יותר, קשה עם 4 מזוודות.",
            ["זול"],
            ["החלפות ולחץ"],
            "€50–90", "2+ שעות", "רק אם נוחים עם רכבות",
            "<strong>Super-Tips:</strong> המתנות קשות"),
    ],
    extra="""
    <section class="section">
      <h2>פרטי עלייה</h2>
      <table>
        <tr><th>תא</th><td>7680 · סיפון 7 · F1</td></tr>
        <tr><th>יציאה משוערת</th><td>~20:00</td></tr>
        <tr><th>ערב</th><td>America's Got Talent 19:00</td></tr>
        <tr><th>ארוחות</th><td>My Time · 17:30–18:30</td></tr>
      </table>
      <p><a href="../cruise-info.html">עמוד הספינה המלא</a></p>
    </section>
    """,
    taxi="civitavecchia",
    meeting="<strong>על הספינה:</strong> חנות הפיצה (Pizza Shop).<br /><strong>בעלייה:</strong> דלפק הצ׳ק־אין / כבש העלייה.",
    exit_ramp="ישר לחדר + מקלחת + אוכל בספינה.",
    costs="",
    prev="16-09", next="18-09",
)

# ---------- 18 ----------
days["18-09"] = dict(
    title="18 בספטמבר · נאפולי / סורנטו",
    subtitle="שישי · עגינה ~07:30 · סורנטו בוקר · פיצה בשוק אחה״צ",
    weather={"temp": "29°", "note": "חם מאוד · מים וכובע · באפר לחזרה לספינה.", "link": "https://www.accuweather.com/en/it/naples/212986/weather-forecast/212986"},
    super_tip="בוקר סורנטו, צהריים פיצה בשוק בנאפולי, באפר גדול לכל־אבורד.",
    default_text="אפשרות A — סורנטו בבוקר + פיצה בשוק בנאפולי אחה״צ (רכב פרטי מומלץ).",
    places="".join([
        place_card("naples.jpg", "נאפולי · שוק ופיצה",
                   "בית הפיצה בעולם. לפי התוכנית: פיצה בשוק אחרי סורנטו.",
                   "מהנמל למרכז: 10–20 דק׳ במונית", "תיקי רוכסן צמודים."),
        place_card("pompeii.jpg", "סורנטו",
                   "עיירת חוף מקסימה על המפרץ — נוף, גלידה, סמטאות. בוקר ממוקד ואז חזרה לנאפולי לפיצה.",
                   "מהנמל בפרטי: ~45–60 דק׳ לכל כיוון (תנועה!)", "בלי לדחוס גם פומפיי באותו יום."),
    ]),
    options=[
        option_card("18-09", "A", "סורנטו בוקר + פיצה בשוק נאפולי", 10,
            "תוכנית האקסל ליום נאפולי.",
            ["שתי חוויות ממוקדות", "פיצה בלתי נשכחת", "תואם תוכנית"],
            ["נסיעות ארוכות", "חום", "חובה באפר"],
            "€280–450 (רכב פרטי + אוכל)", "יום מלא עם באפר", "ברירת מחדל",
            "<strong>לו״ז:</strong> סורנטו → שוק/פיצה → ספינה", True,
            plan={
                "timeline": [
                    "ארוחת בוקר בספינה · יציאה מוקדמת (~08:00)",
                    "בוקר — סורנטו (הליכה קצרה, גלידה/קפה, תצפית) עם נהג ממתין או סיור מסודר",
                    "צהריים — חזרה לנאפולי · פיצה בשוק / דוכנים",
                    "חזרה לנמל עם באפר שעתיים לפני all-aboard (~18:30)",
                ],
                "book": [
                    ("private-car", "רכב פרטי נמל→סורנטו→נאפולי→נמל עם חזרה מובטחת"),
                    ("pizza-spot", "יעד פיצה/שוק מראש (או המלצת הנהג)"),
                    ("all-aboard", "לרשום שעת all-aboard מהאפליקציה"),
                ],
            }),
        option_card("18-09", "B", "רק פיצה + מרכז נאפולי (בלי סורנטו)", 8,
            "קצר וזול יותר אם רוצים פחות נסיעות.",
            ["פחות לחץ", "פיצה"],
            ["בלי סורנטו שתוכנן"],
            "€100–180", "3–5 שעות", "אם עייפים / תנועה כבדה",
            "<strong>Super-Tips:</strong> פיצה = מוטיבציה"),
        option_card("18-09", "C", "פומפיי קצר + פיצה (גיבוי)", 7,
            "רק אם מחליטים לוותר על סורנטו לטובת עתיקות.",
            ["היסטוריה חזקה"],
            ["לא תוכנית האקסל"],
            "€280–450", "יום מלא", "גיבוי בלבד",
            "<strong>Super-Tips:</strong> באפר חובה"),
    ],
    extra="""
    <section class="section">
      <h2>הערת לוגיסטיקה</h2>
      <p>בלי רכב פרטי / סיור עם חזרה מובטחת — לא ממליצים על סורנטו+נאפולי באותו יום.</p>
    </section>
    """,
    taxi="naples",
    meeting="<strong>ראשי:</strong> כבש הספינה.<br /><strong>משני:</strong> נקודת מפגש עם הנהג.",
    exit_ramp="חזרה לספינה ל־Windjammer + בריכה.",
    costs="",
    prev="17-09", next="19-09",
)

# ---------- 19 ----------
days["19-09"] = dict(
    title="19 בספטמבר · יום בים",
    subtitle="שבת · Crown Edge 09:15 · Izumi 12:30 · צ׳ארלי שוקולד 15:30",
    weather={"temp": "—", "note": "שמש חזקה על הסיפון · קרם הגנה.", "link": "https://www.royalcaribbean.com/"},
    super_tip="שלושה סלוטים קבועים — אחרי 15:30 רק איפוס קל, בלי לדחוס עוד.",
    default_text="<strong>כבר נקבע:</strong> Crown Edge 09:15 → Izumi 12:30 → צ׳ארלי בממלכת השוקולד 15:30.",
    places=place_card("ship.jpg", "יום בים",
                      "אין נמל — כל היום על Legend of the Seas עם שלוש הזמנות קבועות.",
                      "0 — כבר על הספינה", "ערב קל בלבד אחרי השוקולד."),
    options=[
        option_card("19-09", "A", "לו״ז קבוע: Crown Edge → Izumi → Charlie Chocolate", 10,
            "תוכנית האקסל ליום הים — כל ההזמנות.",
            ["הכל כבר משוריין", "כיף לילדים", "ברור"],
            ["יום עמוס עד אחה״צ", "ערב חייב להיות קל"],
            "€0–40 תוספת (רוב שולם מראש)", "כל היום", "ברירת מחדל",
            "<strong>טיילר ו־ליי-ליי:</strong> שלוש חוויות · ערב רגוע", True,
            plan={
                "timeline": [
                    "ארוחת בוקר קלה מוקדם",
                    "09:15 — Crown Edge Experience · להגיע ~08:55–09:05",
                    "12:30 — Izumi Hibachi · להגיע ~12:15 · בלי חזיר/פירות ים",
                    "15:30 — צ׳ארלי בממלכת השוקולד (Charlie Chocolate)",
                    "אחרי — בריכה/חדר · ערב מופע או Windjammer קל בלבד",
                ],
                "book": [
                    ("confirm-crown", "Crown Edge 09:15 — כבר הוזמן · לאשר באפליקציה"),
                    ("confirm-izumi", "Izumi Hibachi 12:30 — כבר הוזמן"),
                    ("charlie", "צ׳ארלי בממלכת השוקולד 15:30 — לאשר באפליקציה"),
                    ("show", "מופע ערב אופציונלי (קליל)"),
                ],
            }),
        option_card("19-09", "B", "כמו A בלי Charlie — מנוחה מ־14:00", 8,
            "אם אחרי Izumi כולם מלאים/עייפים — מדלגים על השוקולד.",
            ["פחות עומס", "איפוס"],
            ["מפספסים חוויה שתוכננה"],
            "€0–40", "עד צהריים + מנוחה", "אם צריך יציאת חירום",
            "<strong>Super-Tips:</strong> בלי Specialty בערב"),
    ],
    extra="""
    <section class="section">
      <h2>כבר הוזמן — 19/9</h2>
      <div class="default-pick"><strong>09:15 — Crown Edge Experience</strong></div>
      <div class="default-pick"><strong>12:30 — Izumi Hibachi</strong> · בלי חזיר · בלי פירות ים</div>
      <div class="default-pick"><strong>15:30 — צ׳ארלי בממלכת השוקולד</strong></div>
    </section>
    """,
    taxi=None,
    meeting="<strong>על הספינה:</strong> חנות הפיצה (Pizza Shop).<br /><strong>משני לפעילות:</strong> נקודת המפגש באפליקציה.",
    exit_ramp="חדר + טאבלט + חטיף קל.",
    costs="",
    prev="18-09", next="20-09",
)

# ---------- 20 ----------
days["20-09"] = dict(
    title="20 בספטמבר · ברצלונה",
    subtitle="ראשון · Sagrada · לה רמבלה · Shockwave 20:00",
    weather={"temp": "26°", "note": "נעים · Sagrada ביום ראשון לרוב מ־~10:30.", "link": "https://www.accuweather.com/en/es/barcelona/307297/weather-forecast/307297"},
    super_tip="Sagrada מתוזמן → רמבלס → חזרה לספינה עם באפר · ערב Shockwave 20:00.",
    default_text="אפשרות A — סגרדה דה פמיליה → לה רמבלה → Shockwave 20:00 בספינה.",
    places="".join([
        place_card("sagrada.jpg", "סגרדה פמיליה",
                   "כנסיית גאודי — כרטיס מתוזמן חובה.",
                   "מהנמל במונית ~20–30 דק׳", "בימי ראשון לרוב מ־~10:30."),
        place_card("ramblas.jpg", "לה רמבלה",
                   "שדרה מפורסמת — אווירה, דוכנים, טאפאס ברובע. כייסים — ערנות.",
                   "מ־Sagrada במונית ~15–20 דק׳", "לא חייבים את כל השדרה."),
    ]),
    options=[
        option_card("20-09", "A", "Sagrada + לה רמבלה + Shockwave 20:00", 10,
            "תוכנית האקסל לברצלונה + מופע ערב.",
            ["must-see", "אוכל ברובע", "מופע בספינה"],
            ["חלון נמל עד ~16:30", "כייסים"],
            "€240–350", "6–7 שעות בחוף + ערב בספינה", "ברירת מחדל",
            "<strong>לו״ז:</strong> Sagrada → רמבלס → ספינה → Shockwave", True,
            plan={
                "timeline": [
                    "ארוחת בוקר בספינה",
                    "בוקר — Sagrada Família (כרטיס מתוזמן)",
                    "צהריים — לה רמבלה + טאפאס/גלידה ברובע",
                    "חזרה לנמל עם באפר (יעד ~14:30–15:00)",
                    "20:00 — Shockwave בספינה",
                ],
                "book": [
                    ("sagrada", "כרטיסי Sagrada ל־4 (אחרי ~10:30 ביום ראשון)"),
                    ("shockwave", "Shockwave 20:00 — הזמנה באפליקציה"),
                    ("all-aboard", "שעת all-aboard — באפר חזרה"),
                ],
            }),
        option_card("20-09", "B", "רק רמבלס + רובע (בלי Sagrada) + Shockwave", 6,
            "אם אין כרטיסים ל־Sagrada.",
            ["גמיש", "זול"],
            ["בלי החוויה המרכזית"],
            "€80–140", "3–4 שעות + ערב", "גיבוי",
            "—"),
    ],
    extra="""
    <section class="section">
      <h2>ערב בספינה</h2>
      <div class="default-pick"><strong>20:00 — Shockwave</strong> · לשריין באפליקציה</div>
    </section>
    """,
    taxi="barcelona",
    meeting="<strong>על הספינה:</strong> חנות הפיצה (Pizza Shop).<br /><strong>בנמל:</strong> כבש הספינה · <strong>משני בחוף:</strong> כניסת Sagrada.",
    exit_ramp="מונית ישר לנמל.",
    costs="",
    prev="19-09", next="21-09",
)

# ---------- 21 ----------
days["21-09"] = dict(
    title="21 בספטמבר · פלמה דה מיורקה",
    subtitle="שני · ~08:30–15:30 · קתדרלה + עיר עתיקה (ברירת מחדל משפחתית)",
    weather={"temp": "27°", "note": "שמשי · חלון קצר.", "link": "https://www.accuweather.com/en/es/palma/355667/weather-forecast/355667"},
    super_tip="האקסל ריק לפרטים — נשארים עם תוכנית אחת: קתדרלה/עיר או חוף.",
    default_text="אפשרות A — קתדרלה (פתוחה בשני לתיירים מ~10:00) + עיר עתיקה.",
    places="".join([
        place_card("palma.jpg", "פלמה · הקתדרלה (La Seu)",
                      "קתדרלה גותית מול הים. ב־21/9 (שני) פתוחה לתיירים לרוב מ־~10:00.",
                      "מהנמל למרכז: 10–20 דק׳ במונית", "באפר חזרה 90 דק׳."),
        place_card("beach.jpg", "חוף (גיבוי)",
                      "יום קל אם רוצים איפוס באמצע השייט.",
                      "מהנמל ~15–25 דק׳", "בדקו מזג אוויר."),
    ]),
    options=[
        option_card("21-09", "A", "קתדרלה + עיר עתיקה + גלידה", 9,
            "ברירת מחדל משפחתית (האקסל לא פירט את היום).",
            ["יפה", "קצר", "פתוח ב־21/9"],
            ["חם באבנים"],
            "€60–120", "3–4 שעות", "עיר",
            "<strong>כולם:</strong> מאוזן", True),
        option_card("21-09", "B", "זמן חוף / שחייה", 9,
            "איפוס סבלנות.",
            ["כיף לילדים"],
            ["פחות אטרקציה עירונית"],
            "€40–80", "3–4 שעות", "ים",
            "<strong>טיילר ו־ליי-ליי:</strong> מעולה"),
    ],
    extra="",
    taxi="palma",
    meeting="<strong>ראשי:</strong> כבש הספינה.<br /><strong>משני:</strong> ליד הקתדרלה.",
    exit_ramp="גלידה וחזרה לספינה.",
    costs="",
    prev="20-09", next="22-09",
)

# ---------- 22 ----------
days["22-09"] = dict(
    title="22 בספטמבר · פרובנס / מרסיי",
    subtitle="שלישי · סיור נורית גאון · מונית 09:30 → חזרה 15:30",
    weather={"temp": "26°", "note": "נעים.", "link": "https://www.accuweather.com/en/fr/marseille/227246/weather-forecast/227246"},
    super_tip="סיור פרטי עם נורית גאון — להגיע לנקודת האיסוף בזמן. בלי לתכנן אטרקציה נוספת אחרי.",
    default_text="אפשרות A — סיור פרובנס עם נורית גאון (איסוף 09:30 · חזרה 15:30).",
    places=place_card("marseille.jpg", "פרובנס / מרסיי",
                      "סיור מאורגן בפרובנס עם מדריכה נורית גאון — מונית תאסוף ב־09:30 ותחזיר ב־15:30.",
                      "איסוף לפי תיאום עם המדריכה / ליד הנמל", "לא מאחרים לאיסוף."),
    options=[
        option_card("22-09", "A", "סיור נורית גאון פרובנס (09:30–15:30)", 10,
            "תוכנית האקסל — סיור משוריין.",
            ["מדריכה בעברית", "לוגיסטיקה סגורה", "תואם תוכנית"],
            ["תלוי בתיאום", "פחות גמישות עצמאית"],
            "לפי מחיר הסיור שנקבע עם נורית", "09:30–15:30", "ברירת מחדל",
            "<strong>להגיע מוקדם לאיסוף</strong>", True,
            plan={
                "timeline": [
                    "ארוחת בוקר בספינה",
                    "09:30 — מונית/איסוף עם נורית גאון לסיור פרובנס",
                    "סיור מאורגן (כפרים/נוף/עצירות לפי המסלול שלה)",
                    "15:30 — חזרה לנמל/ספינה",
                    "אחה״צ־ערב — מנוחה בספינה",
                ],
                "book": [
                    ("nurit", "אישור סופי עם נורית גאון — נקודת איסוף + טלפון"),
                    ("all-aboard", "וידוא ש־15:30 משאיר באפר לפני all-aboard"),
                    ("cash-tip", "מזומן לטיפ/עצירות קטנות לפי הצורך"),
                ],
                "transport": [
                    ("meet-taxi", "להיות בנקודת האיסוף ב־09:20"),
                    ("whatsapp", "וואטסאפ פתוח עם המדריכה/נהג"),
                ],
            }),
        option_card("22-09", "B", "Vieux Port בלבד (גיבוי אם הסיור מתבטל)", 7,
            "נשארים במרסיי הקרובה לספינה.",
            ["קרוב", "גמיש"],
            ["לא תוכנית האקסל"],
            "€80–140", "4–5 שעות", "גיבוי",
            "<strong>Super-Tips:</strong> אזור תיירותי מרכזי"),
    ],
    extra="""
    <section class="section">
      <h2>פרטי הסיור</h2>
      <div class="default-pick"><strong>נורית גאון · פרובנס</strong><br />מונית תפגוש ב־09:30 · חזרה 15:30</div>
    </section>
    """,
    taxi="marseille",
    meeting="<strong>על הספינה:</strong> חנות הפיצה (Pizza Shop).<br /><strong>בנמל:</strong> כבש הספינה · <strong>משני בחוף:</strong> נקודת האיסוף עם נורית.",
    exit_ramp="חזרה מוקדמת לספינה אם הסיור מתקצר.",
    costs="",
    prev="21-09", next="23-09",
)

# ---------- 23 ----------
days["23-09"] = dict(
    title="23 בספטמבר · צ׳ינקווה טרה",
    subtitle="רביעי · לה ספציה · מאנרולה · ורנאצה · מונטרוסו",
    weather={"temp": "25°", "note": "נעים · רכבות עמוסות.", "link": "https://www.accuweather.com/en/it/la-spezia/214748/weather-forecast/214748"},
    super_tip="שלושה כפרים לפי התוכנית — קצב נעים, בלי שביל הליכה בין כפרים, באפר שעתיים.",
    default_text="אפשרות A — מאנרולה, ורנאצה, מונטרוסו (רכבת).",
    places="".join([
        place_card("cinqueterre.jpg", "צ׳ינקווה טרה",
                   "כפרי דייגים צבעוניים — מורשת עולמית. לפי התוכנית: מאנרולה, ורנאצה, מונטרוסו.",
                   "לה ספציה → כפר ברכבת: ~10–20 דק׳", "כרטיס יומי / רכבות תכופות."),
        place_card("vernazza.jpg", "בכל כפר",
                   "פוקאצ׳ה/גלידה, מעגן, צילום, חנות אחת — 45–75 דק׳ לכפר.",
                   "בתוך כפר", "אם האנרגיה יורדת — מדלגים על כפר שלישי."),
    ]),
    options=[
        option_card("23-09", "A", "מאנרולה + ורנאצה + מונטרוסו", 10,
            "תוכנית האקסל — שלושה כפרים.",
            ["תואם תוכנית", "נוף+אוכל", "רכבת בין כפרים"],
            ["מדרגות", "רכבות צפופות", "יום ארוך"],
            "€140–220 (רכבת + אוכל)", "יום מלא עם באפר", "ברירת מחדל",
            "<strong>בכל כפר:</strong> אוכל קל · מעגן · צילום", True,
            plan={
                "timeline": [
                    "נמל → La Spezia Centrale → רכבת למאנרולה",
                    "מאנרולה — כפר 1",
                    "רכבת לוורנאצה — כפר 2",
                    "רכבת למונטרוסו — כפר 3 (אם נשאר כוח וזמן)",
                    "רכבת חזרה ללה ספציה → ספינה עם באפר שעתיים",
                ],
                "book": [
                    ("ct-tickets", "כרטיס רכבת / Cinque Terre day pass"),
                    ("all-aboard", "באפר שעתיים לפני all-aboard (~19:30)"),
                ],
            }),
        option_card("23-09", "B", "שני כפרים בלבד (מאנרולה + ורנאצה)", 8,
            "אם רוצים פחות לחץ — עדיין חוויה מצוינת.",
            ["פחות עומס", "יותר זמן בכל כפר"],
            ["בלי מונטרוסו"],
            "€120–200", "6–7 שעות", "אם עייפים",
            "<strong>Super-Tips:</strong> איכות על כמות"),
        option_card("23-09", "C", "יום בספינה (גיבוי מזג אוויר)", 5,
            "רק אם רכבות/מזג אוויר משבשים.",
            ["מנוחה"],
            ["מפספסים CT"],
            "€0", "—", "חירום",
            "—"),
    ],
    extra="""
    <section class="section">
      <h2>סדר מוצע</h2>
      <p><strong>מאנרולה → ורנאצה → מונטרוסו</strong> · רכבת בלבד בין הכפרים · בלי שביל טיול ארוך.</p>
    </section>
    """,
    taxi="laspezia",
    meeting="<strong>על הספינה:</strong> חנות הפיצה (Pizza Shop).<br /><strong>בנמל:</strong> כבש הספינה · <strong>משני בחוף:</strong> תחנת La Spezia Centrale.",
    exit_ramp="אחרי כפר אחד — חזרה ללה ספציה.",
    costs="",
    prev="22-09", next="24-09",
)

# ---------- 24 ----------
days["24-09"] = dict(
    title="24 בספטמבר · חזרה לרומא",
    subtitle="חמישי · עגינה ~07:30 · Hotel Accademia",
    weather={"temp": "26°", "note": "נעים · אנרגיה נמוכה אחרי שייט.", "link": "https://www.accuweather.com/en/it/rome/213633/weather-forecast/213633"},
    super_tip="מנוחה במלון Accademia. מחר Romio 06:30 לטיסת LY386 בשעה 10:00 — שינה מוקדמת.",
    default_text="אפשרות A — ירידה ~07:30 · Romio 09:00 → Hotel Accademia → ערב קל.",
    places=place_card("spanish-steps.jpg", "Hotel Accademia · לילה אחרון",
                      "יורדים מהספינה ~07:30, Romio אוסף ב־09:00 ל־Hotel Accademia, Piazza Accademia di San Luca 75. ערב קל בלבד — מחר איסוף 06:30.",
                      "צ׳יוויטווקיה→רומא: ~1–1.5 שעות", "Romio Accademia→FCO מחר 06:30."),
    options=[
        option_card("24-09", "A", "העברה → Hotel Accademia → מנוחה", 10,
            "תוכנית האקסל: עגינה 07:30 ומלון Accademia.",
            ["מלון משוריין", "רגוע לפני טיסה"],
            ["צ׳ק־אין מוקדם לא תמיד אפשרי — לבקש שמירת מזוודות"],
            "€199 (Romio €170 + €29 PayPal) + ערב קל", "יום רגוע", "ברירת מחדל",
            "<strong>כולם:</strong> מנוחה = הצלחה", True,
            plan={
                "timeline": [
                    "עגינה / ירידה ~07:30",
                    "המתנה בנמל עד Romio 09:00 → Hotel Accademia",
                    "צהריים — צ׳ק־אין / שמירת מזוודות + מנוחה",
                    "ערב קל ליד המלון (אופציונלי טרווי קצר) → שינה מוקדמת",
                ],
                "book": [
                    ("accademia", "אישור Hotel Accademia"),
                    ("civ-rome", 'Romio נמל→Accademia 09:00 — <a href="../emergency.html#transfers">פרטים</a>'),
                    ("fco-next", 'Romio Accademia→FCO מחר 06:30 — <a href="../emergency.html#transfers">פרטים</a>'),
                ],
            }),
        option_card("24-09", "B", "כמו A + הליכה קלה לטרווי", 8,
            "רק אם יש אנרגיה אחרי הנסיעה.",
            ["סגירת מעגל ברומא"],
            ["עייפות לפני טיסה"],
            "€220–320", "תוספת 1 שע׳", "אופציונלי",
            "<strong>Super-Tips:</strong> קצר בלבד"),
    ],
    extra=ROME_PDF + """
    <section class="section">
      <h2>מלון</h2>
      <p><strong>Hotel Accademia</strong> — Piazza Accademia di San Luca 75 · לילה 24→25. העברה: <a href="../emergency.html#transfers">Romio</a></p>
    </section>
    """,
    taxi="rome",
    meeting="<strong>ראשי:</strong> לובי Hotel Accademia.",
    exit_ramp="פיצה ליד המלון ושינה מוקדמת.",
    costs="",
    prev="23-09", next="25-09",
)

# ---------- 25 ----------
days["25-09"] = dict(
    title="25 בספטמבר · טיסה לישראל",
    subtitle="שישי · אל על LY386 · המראה ~10:00 מ־FCO",
    weather={"temp": "—", "note": "בדקו תנועה בבוקר.", "link": "https://www.accuweather.com/en/it/rome/213633/weather-forecast/213633"},
    super_tip="בלי עצירות — Romio 06:30 מהמלון, יעד בשדה ~07:15–07:40 לטיסת 10:00.",
    default_text="אפשרות A — Romio 06:30 Accademia→FCO · LY386 בשעה 10:00.",
    places=place_card("airport.jpg", "FCO · לאונרדו דה וינצ׳י",
                      "טיסת אל על LY386 בשעה 10:00. Romio אוסף ב־06:30 מ־Hotel Accademia.",
                      "ממרכז רומא בואן: ~45–70 דק׳", "רק Romio / מוניות רשמיות."),
    options=[
        option_card("25-09", "A", "העברה ל־FCO · LY386 10:00", 10,
            "תוכנית האקסל לחזרה.",
            ["אמין", "מזוודות"],
            ["קימה מוקדמת"],
            "€85 (Romio Accademia→FCO)", "45–70 דק׳", "חובה",
            "<strong>Super-Tips:</strong> טאבלט/חטיף ברכב", True,
            plan={
                "timeline": [
                    "יציאה מהמלון 06:30 עם Romio",
                    "הגעה ל־FCO ~07:15–07:40",
                    "צ׳ק־אין אל על + בידוק",
                    "10:00 — המראה LY386 לישראל",
                ],
                "book": [
                    ("ly386", "אישור טיסת LY386 + כרטיסי עלייה"),
                    ("fco-transfer", 'Romio Accademia→FCO 06:30 — <a href="../emergency.html#transfers">פרטים</a>'),
                    ("harel", 'פרטי ביטוח הראל — <a href="../emergency.html">עמוד חירום</a>'),
                ],
            }),
        option_card("25-09", "B", "יציאה מוקדמת יותר מהמלון (באפר גדול)", 9,
            "אם חוששים מתנועה או תורים בשדה.",
            ["יותר ראש שקט"],
            ["יותר המתנה בשדה"],
            "€85", "—", "אם רוצים באפר",
            "—"),
    ],
    extra="""
    <section class="section">
      <h2>צ׳ק־ליסט בוקר</h2>
      <ul class="checklist">
        <li><input type="checkbox" data-id="dep-passports" /> דרכונים + כרטיסי טיסה LY386</li>
        <li><input type="checkbox" data-id="dep-harel" /> פרטי ביטוח הראל (<a href="../emergency.html">עמוד חירום</a>)</li>
        <li><input type="checkbox" data-id="dep-chargers" /> מטענים</li>
        <li><input type="checkbox" data-id="dep-keys" /> החזרת מפתח מלון Accademia</li>
      </ul>
    </section>
    """,
    taxi="rome",
    meeting="<strong>ראשי:</strong> דלפק אל על ב־FCO.",
    exit_ramp="אין גמישות — וואטסאפ Romio אם איחור.",
    costs="",
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
