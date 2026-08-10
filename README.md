# Kleos — Serbia contractor guide

Country landing page for the Eastern European cluster. Fixed-width (1440px) Figma export with an interactive calculator, a nine-criterion misclassification checklist and an eight-item FAQ.

Live preview runs on Streamlit. The page itself is plain HTML and CSS, so it can be lifted straight into Webflow or a static host without Streamlit.

---

## Run it

**Locally**

```bash
pip install -r requirements.txt
streamlit run app.py
```

**Streamlit Community Cloud**

1. Push this folder to a GitHub repo.
2. On share.streamlit.io, pick the repo, branch, and `app.py` as the entry point.
3. Deploy. No secrets or environment variables are needed.

---

## Files

| File | What it is |
|---|---|
| `index.html` | The page. Markup, the untouched Figma CSS, and one `<script>` block at the end that adds interactivity. |
| `app.py` | Streamlit wrapper. Reads `index.html` and renders it in a component iframe. Contains no page content. |
| `requirements.txt` | `streamlit` only. |
| `.streamlit/config.toml` | Light theme, headless server, usage stats off. |

**To change the page, edit `index.html`.** `app.py` only sets the iframe height and hides Streamlit's chrome.

If the page gets taller or shorter, adjust `PAGE_HEIGHT` in `app.py`. It is currently 8300px against a measured page height of about 8113px.

---

## How the interactive layer works

Everything sits in one `<script id="kleos-calc">` at the end of `index.html`.

- **The `<style>` block is byte-identical to the Figma export.** The script sets a few inline styles (cursor, the injected input) and toggles existing classes. It adds no CSS rules and no new markup patterns.
- **All rates are constants** at the top of the script. Update them there, in one place.
- Keyboard access: tabs, the direction toggle, checklist rows and FAQ questions are focusable and respond to Enter and Space.

### Calculator

Four regimes as tabs, gross-to-net or net-to-gross. Net-to-gross is solved numerically, so it stays correct for the freelancer model where the relationship is piecewise-linear.

### Checklist

Clicking a row toggles it and the note underneath recomputes the score. Below five it says so explicitly.

### FAQ

All eight answers ship expanded, which is what you want for indexing. Clicking a question collapses it.

---

## What is verified and what is not

This matters more than the code. Numbers here were checked against 2026 sources; two of the four regimes rest on an assumption that a Serbian adviser still needs to confirm.

### Verified against 2026 sources

| Figure | Source |
|---|---|
| Employee 19.9% / employer 15.15% contributions (PIO 24%, health 10.3%, unemployment 0.75%) | PwC Worldwide Tax Summaries, Feb 2026 |
| Non-taxable monthly salary amount 34,221 RSD | Official Gazette 109/2025; KPMG, Karanović, PR Legal |
| Minimum wage 371 RSD net per hour from 1 Jan 2026 | Official Gazette 78/2025 |
| Flat-rate ceiling 6,000,000 RSD, calendar year, on invoice date | attorney.rs, Solar Staff |
| VAT threshold 8,000,000 RSD, rolling 12 months | attorney.rs, TaxRavens |
| Freelancer deductions 110,647 and 66,733 RSD per quarter, taxed at 20% and 10% | PlatniListić, Biznis.rs, pitajknjigovodju.rs — all 2026 |
| Nine criteria, five-of-nine threshold, per client, in force since 1 Mar 2020 | NCR Lawyers, Creative Finance, PR Legal |
| A day counts if any part of it is worked; 70% is "at least" | Creative Finance, quoting the statute |
| A d.o.o. sits outside the independence test | Creative Finance |
| Personal-salary mechanics; entrepreneur contributions 35.05%; minimum base 51,297 and cap 732,820 RSD a month | Biznis.rs (Dec 2025), Biro Vision (Jun 2026), knjigovodstvena.rs — checked against two worked examples that reconcile to the dinar |
| Corporate tax 15%, dividends 15%, VAT 20% / 10% | PwC, TaxRavens |

### Assumptions in the calculator — confirm before publishing

**Flat-rate (paušal).** The monthly amount comes from an individual Tax Administration decision and cannot be derived from income. The calculator uses `state.pausalMonthly = 443` USD, roughly 45,000 RSD, the middle of a published 30,000–60,000 RSD range for a Belgrade IT or consulting activity code. That range comes from one relocation-advisory source. Treat it as a placeholder and let the user enter their contractor's actual figure.

**Bookkeeping (knjigaš).** Now verified. Modelled as the personal-salary election under article 33a: the salary is declared at the statutory minimum base (51,297 RSD a month), contributions of 35.05% and 10% salary tax sit on it, the salary is a deductible business expense, and the remaining profit is taxed at 10% and not taxed again on withdrawal. The calculator also reports what the alternative costs — without the election, contributions fall on the whole profit, which is roughly 45% effective at $36,000.

Two things this corrected: the entrepreneur's own contribution rate is **35.05%**, not 34.3%, because they pay the 0.75% unemployment contribution too; and the personal-salary election must be filed by 15 December for the following year.

The remaining assumption is that the entrepreneur declares exactly the minimum base. Anyone declaring more will see different numbers.

**Company (d.o.o.).** Assumes the whole profit is distributed and no deductible costs, so the effective rate is the maximum. Real cases will be lower.

> The entrepreneur's 35.05% and the 34.3% used elsewhere on the page are both correct in their own context. An entrepreneur pays pension, health and unemployment on their own income. A reclassified engagement under article 85 attracts pension and health only.

### Not verified at all

- The 12%–40% effective-burden range in the first case card. Single source, Tax Advisor Serbia.
- "A one-person company is the recognised way out" — an adviser recommendation, not a statutory safe harbour.
- Permanent-establishment risk. Sources disagree on how easily a foreign client triggers a PE in Serbia on facts that overlap the nine criteria. Not mentioned on the page; worth a decision before publishing.
- Employer-side statutory notice period. Deliberately not stated as a number.
- Related-party aggregation: several companies in one group hiring the same contractor are assessed together for the 70% and 130-day tests. Confirmed once, not on the page.

### Legal review list

The independence-test consequences, the nine criteria as reworded buyer-side, the claim that a foreign client is not assessed, the Contractor of Record and Employer of Record statements, and the section headline "Nine criteria decide if this is employment" — that last one is loose, because the Serbian test is a tax test and does not create employment under labour law.

---

## Currency

Every amount on the page is shown in US dollars, converted from dinars at **101.5 RSD/$ (August 2026)** and rounded, with "about" or "roughly" in front so the figures do not read as exact.

The underlying thresholds are set in dinars by Serbian law. A contractor crosses the flat-rate ceiling at 6,000,000 RSD, not at $59,000. Anyone near a threshold should work in dinars.

Update `RSD_PER_USD` in `index.html` when you refresh the rate. Use the National Bank of Serbia middle rate — it is the rate Serbian accounting uses under the Law on Foreign Exchange Operations.

---

## January review

Several figures are indexed every January, so the page needs an annual pass. All of them live in `index.html`; the calculator constants are at the top of the script.

- [ ] Non-taxable monthly salary amount — 34,221 RSD for 2026, up from 28,423
- [ ] Freelancer standardised deductions — 110,647 and 66,733 RSD; these have changed every year since 2023 and took effect 1 February in 2026
- [ ] Minimum wage — 371 RSD net per hour for 2026
- [ ] Minimum and maximum contribution bases — 51,297 and 732,820 RSD a month
- [ ] `RSD_PER_USD` and the date in the footer disclaimer
- [ ] Status of the draft package that would abolish several incentives from 1 January 2027 (public consultation closed 21 June 2026)

---

## Known gaps for design and development

- **Section order differs from the template.** `screen` now follows `employee` rather than preceding it, so the Kleos block lands after the checklist. Figma needs the same move.
- **22 elements have no `data-node-id`** — the expanded FAQ answer blocks, three checklist rows, one calculator tab, the hero disclaimer and the CTA button in `screen`. They have no Figma counterpart yet.
- **`hero__buttons` is reused outside the hero** to wrap the CTA button in `screen`. There is no button-wrapper class for that section in the template; worth renaming in a cleanup pass.
- **Dead CSS.** Rules for `.rates`, `.sanctions`, `.screen__*` variants and `.btn--secondary` remain from deleted or changed blocks. Safe to strip.
- **Nine `href="#"` remain** — Login, EN, Book a demo, the hero button, both Check your setup buttons and the two social links. The four nav items resolve to real anchors.
- **`.footer__disclaimer` is absolutely positioned**, so it can only hold one paragraph. Removing `position: absolute` would let it flow and allow the disclaimer to be split up again.
- **Fixed-height containers.** `.calc__card` (485px), `.yearlife` (1299px), `.screen` (650px), `.case` (360px) and `.footer` (511px) all clip. Any copy change needs measuring against those budgets.
