(function () {
  "use strict";

  function gradeClass(n) {
    if (n >= 8) return "grade-high";
    if (n >= 6) return "grade-mid";
    return "grade-low";
  }

  document.querySelectorAll("[data-grade]").forEach(function (el) {
    var n = parseInt(el.getAttribute("data-grade"), 10);
    if (!isNaN(n)) {
      el.classList.add("grade", gradeClass(n));
      if (!el.textContent.trim()) el.textContent = String(n);
    }
  });

  var key = "cruise-guide-checks";
  var saved = {};
  try {
    saved = JSON.parse(localStorage.getItem(key) || "{}");
  } catch (e) {
    saved = {};
  }

  document.querySelectorAll(".checklist input[type=checkbox][data-id]").forEach(function (box) {
    var id = box.getAttribute("data-id");
    if (saved[id]) box.checked = true;
    box.addEventListener("change", function () {
      saved[id] = box.checked;
      try {
        localStorage.setItem(key, JSON.stringify(saved));
      } catch (err) {
        /* ignore */
      }
    });
  });
})();
