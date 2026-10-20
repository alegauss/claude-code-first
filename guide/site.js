// What every page of the site runs after it loads (CCF77): the theme toggle, and Google
// Analytics behind the visitor's consent, the flow the hub (its AG1) and claude-tray run.
// Nothing reaches googletagmanager.com before a choice: the tag is not in the HTML, and
// this adds it only for "granted". A refusal is remembered as firmly as a consent, and
// the footer's "Analytics settings" asks again.
//
// The key and the measurement id are the hub's on purpose. This site is served from the
// same origin (alegauss.github.io/claude-code-first/), so the two share one localStorage
// and one property, and a visitor who has answered on either has answered for both.
(function () {
  var THEME_KEY = "ccf-theme";
  var KEY = "alegauss-consent";
  var MEASUREMENT_ID = "G-6HG45Q9BHP";

  var toggle = document.getElementById("theme");
  if (toggle) {
    var label = function () {
      var next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
      toggle.setAttribute("aria-label", "Switch to " + next + " theme");
      toggle.title = "Switch to " + next + " theme";
    };
    label();
    toggle.addEventListener("click", function () {
      var root = document.documentElement;
      root.dataset.theme = root.dataset.theme === "dark" ? "light" : "dark";
      try { localStorage.setItem(THEME_KEY, root.dataset.theme); } catch (e) { /* blocked storage: the choice lasts this visit */ }
      label();
    });
  }

  function readChoice() {
    try {
      var v = localStorage.getItem(KEY);
      return v === "granted" || v === "denied" ? v : null;
    } catch (e) {
      return null;
    }
  }

  var loaded = false;
  function loadAnalytics() {
    if (loaded) return;
    loaded = true;
    window.dataLayer = window.dataLayer || [];
    // gtag.js reads the arguments object itself, not an array
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag("js", new Date());
    window.gtag("config", MEASUREMENT_ID);
    var s = document.createElement("script");
    s.async = true;
    s.src = "https://www.googletagmanager.com/gtag/js?id=" + MEASUREMENT_ID;
    document.head.appendChild(s);
  }

  var banner = null;
  function choose(choice) {
    try { localStorage.setItem(KEY, choice); } catch (e) { /* private mode: the choice lasts this page */ }
    if (choice === "granted") loadAnalytics();
    // the tag cannot be unloaded from a running page; the next one will not load it
    else if (loaded) window["ga-disable-" + MEASUREMENT_ID] = true;
    if (banner) { banner.remove(); banner = null; }
  }

  function ask() {
    if (banner) return;
    banner = document.createElement("section");
    banner.className = "consent";
    banner.setAttribute("aria-label", "Analytics consent");
    banner.innerHTML =
      "<p>This site counts visits with Google Analytics only if you allow it. Nothing is " +
      "loaded until you choose, and the specification itself collects nothing either way.</p>" +
      '<div class="consent-actions">' +
      '<button type="button" class="vg-site-btn vg-site-btn-ghost" data-choice="denied">Decline</button>' +
      '<button type="button" class="vg-site-btn vg-site-btn-primary" data-choice="granted">Allow analytics</button>' +
      "</div>";
    banner.addEventListener("click", function (event) {
      var choice = event.target.getAttribute && event.target.getAttribute("data-choice");
      if (choice) choose(choice);
    });
    document.body.appendChild(banner);
  }

  var choice = readChoice();
  if (choice === "granted") loadAnalytics();
  if (choice === null) ask();
  var settings = document.querySelectorAll(".consent-settings");
  for (var i = 0; i < settings.length; i++) settings[i].addEventListener("click", ask);
})();
