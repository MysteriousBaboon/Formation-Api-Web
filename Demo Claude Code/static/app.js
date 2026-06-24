// ============================================================
// app.js — Front générique de la démo
// ============================================================
// Pour chaque <form class="demo"> :
//   - lit les champs (input/textarea)
//   - GET  => construit une query string
//   - POST => construit un corps JSON
//   - attache le Bearer token si data-auth="true"
//   - affiche le résultat (JSON, image PNG, ou téléchargement)
// Pas de framework : vanilla JS.
// ============================================================

(function () {
  "use strict";

  // --- Gestion du token (mémorisé dans le navigateur) ---
  const tokenInput = document.getElementById("token");
  if (tokenInput) {
    tokenInput.value = localStorage.getItem("ladinguerie_token") || "";
    tokenInput.addEventListener("input", () => {
      localStorage.setItem("ladinguerie_token", tokenInput.value.trim());
    });
  }

  function getToken() {
    return (localStorage.getItem("ladinguerie_token") || "").trim();
  }

  // --- Récupère la valeur d'un champ, en parsant le JSON si besoin ---
  function lireChamp(el) {
    const type = el.dataset.type;
    let valeur = el.value;
    if (type === "json") {
      valeur = JSON.parse(valeur === "" ? "null" : valeur); // peut lever une erreur
    } else if (type === "number") {
      valeur = valeur === "" ? null : Number(valeur);
    }
    return valeur;
  }

  // --- Affiche un résultat JSON / image / erreur ---
  function afficherJSON(zone, data) {
    zone.innerHTML = "<pre></pre>";
    zone.querySelector("pre").textContent = JSON.stringify(data, null, 2);
  }
  function afficherImage(zone, url) {
    zone.innerHTML = "";
    const img = new Image();
    img.src = url;
    zone.appendChild(img);
  }
  function afficherErreur(zone, message) {
    zone.innerHTML = '<div class="err"></div>';
    zone.querySelector(".err").textContent = message;
  }

  // --- Soumission d'une démo ---
  async function soumettre(form) {
    const method = (form.dataset.method || "GET").toUpperCase();
    const rendu = form.dataset.rendu || "json";
    const auth = form.dataset.auth === "true";
    const zone = form.querySelector(".resultat");
    const bouton = form.querySelector("button");

    zone.hidden = false;

    // Construire les données depuis les champs
    const champs = form.querySelectorAll("input[name], textarea[name]");
    const data = {};
    try {
      champs.forEach((el) => {
        if (el === tokenInput) return;
        data[el.name] = lireChamp(el);
      });
    } catch (e) {
      afficherErreur(zone, "Champ JSON invalide : " + e.message);
      return;
    }

    // En-têtes
    const headers = {};
    if (auth) {
      const t = getToken();
      if (!t) {
        afficherErreur(zone, "Token requis : renseigne le Bearer token en haut de page.");
        return;
      }
      headers["Authorization"] = "Bearer " + t;
    }

    // URL + corps selon la méthode
    let url = form.dataset.url;
    const options = { method, headers };
    if (method === "GET") {
      const qs = new URLSearchParams();
      Object.entries(data).forEach(([k, v]) => {
        if (v !== null && v !== "") qs.append(k, v);
      });
      const s = qs.toString();
      if (s) url += "?" + s;
    } else {
      headers["Content-Type"] = "application/json";
      options.body = JSON.stringify(data);
    }

    bouton.disabled = true;
    bouton.dataset.label = bouton.textContent;
    bouton.textContent = "… en cours";

    try {
      // Cas image : on laisse le navigateur charger l'URL (GET) directement.
      if (rendu === "image" && method === "GET") {
        afficherImage(zone, url);
        return;
      }

      const reponse = await fetch(url, options);

      if (rendu === "image" && reponse.ok) {
        const blob = await reponse.blob();
        afficherImage(zone, URL.createObjectURL(blob));
        return;
      }
      if (rendu === "download" && reponse.ok) {
        const blob = await reponse.blob();
        const dispo = reponse.headers.get("Content-Disposition") || "";
        const m = dispo.match(/filename="?([^"]+)"?/);
        const nom = m ? m[1] : "rapport.xlsx";
        const a = document.createElement("a");
        a.href = URL.createObjectURL(blob);
        a.download = nom;
        a.textContent = "⬇️ Télécharger " + nom;
        zone.innerHTML = "";
        zone.appendChild(a);
        a.click();
        return;
      }

      const payload = await reponse.json().catch(() => ({
        error: "réponse non-JSON (" + reponse.status + ")",
      }));
      if (!reponse.ok) {
        afficherErreur(zone, "HTTP " + reponse.status + " — " +
          (payload.error || JSON.stringify(payload)));
      } else {
        afficherJSON(zone, payload);
      }
    } catch (e) {
      afficherErreur(zone, "Échec de la requête : " + e.message);
    } finally {
      bouton.disabled = false;
      if (bouton.dataset.label) bouton.textContent = bouton.dataset.label;
    }
  }

  document.querySelectorAll("form.demo").forEach((form) => {
    form.addEventListener("submit", (e) => {
      e.preventDefault();
      soumettre(form);
    });
  });
})();
