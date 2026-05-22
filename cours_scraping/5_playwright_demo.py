# ============================================================
# 5_playwright_demo.py — Quand requests ne suffit plus
# ============================================================
# Certains sites chargent leur contenu APRES la page (en JS).
# Avec requests, tu recuperes une page presque vide.
# Solution : un vrai navigateur pilote en code = Playwright.
#
# PREREQUIS :
#   pip install playwright
#   playwright install chromium
#
# (Le 2eme telecharge un Chrome headless de ~150 Mo)
# ============================================================

from playwright.sync_api import sync_playwright


# ============================================================
# 1. Demo basique : aller sur une page et lire le titre
# ============================================================
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    # headless=True : pas de fenetre visible (mode serveur)
    # headless=False : ouvre une vraie fenetre (utile pour debug)

    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/js/", timeout=10000)

    # ATTENDRE que les citations apparaissent
    # Sans ce wait, on lirait la page avant le rendu JS
    page.wait_for_selector(".quote")

    # Extraire les citations
    citations = page.locator(".quote").all()
    print(f"{len(citations)} citations trouvees\n")

    for c in citations[:5]:
        texte = c.locator(".text").inner_text()
        auteur = c.locator(".author").inner_text()
        print(f"- {texte}")
        print(f"  ({auteur})\n")

    input('test')
    browser.close()


# ============================================================
# 2. Difference cle avec requests
# ============================================================
# Essaie ca en parallele :
#
#   import requests
#   from bs4 import BeautifulSoup
#   r = requests.get("https://quotes.toscrape.com/js/")
#   soup = BeautifulSoup(r.text, "html.parser")
#   print(len(soup.select(".quote")))   # -> 0 !
#
# La page renvoyee par requests est presque vide : le contenu
# est genere par du JavaScript apres le chargement.


# ============================================================
# 3. Cas d'usage typiques de Playwright
# ============================================================
# - Single Page Applications (React, Vue, Angular)
# - Sites qui demandent un login / cookies complexes
# - Sites avec scroll infini
# - Captures d'ecran automatiques
#
# Cout : 10-50x plus lent que requests, et plus lourd a
# deployer. A utiliser EN DERNIER RECOURS.


# ============================================================
# 4. Bonus : screenshot de la page
# ============================================================
with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://example.com")
    page.screenshot(path="screenshot.png", full_page=True)
    print("Screenshot enregistre dans screenshot.png")
    browser.close()
