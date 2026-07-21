# Kleos — Serbia contractor-taxation page

A self-contained landing page explaining what a contractor in Serbia actually
keeps, with a live gross-to-net calculator across the three realistic setups and
an interactive version of Serbia's nine-criterion **independence test**
(*test samostalnosti*). EN / SR (Serbian, Latin) toggle. Same design system as the
Romania and Spain pages in this series.

## Files
- `index.html` — the entire page (HTML + CSS + JS, no build step, no dependencies)
- `app.py` — thin Streamlit wrapper that renders `index.html` full-bleed
- `requirements.txt` — Streamlit dependency for cloud deploy
- `README.md` — this file

## Run it

**Just open it.** `index.html` is standalone — double-click it, or open in any
browser. Nothing to install.

**As a Streamlit app (local):**
```bash
pip install streamlit
streamlit run app.py
```
`app.py` and `index.html` must sit in the same folder.

**On Streamlit Community Cloud:** push all four files to a GitHub repo (root),
then deploy `app.py` at share.streamlit.io. `requirements.txt` must be in the
repo or the build fails with `ModuleNotFoundError`.

## What the calculator models

Currency: shown in **euros** for comparability with the other country pages and
because foreign hiring is priced in EUR — but **Serbian tax is legally assessed in
dinars (RSD)**. Amounts convert at an indicative `RSD_PER_EUR = 117.5`; the rate
moves. Say the word and this can be rebuilt dinar-native.

Three regimes (tabs):

1. **Paušalac (flat-rate entrepreneur)** — a *fixed* monthly amount covering tax +
   all contributions, independent of income. `net = invoiced − 12 × monthly`.
   The monthly figure is a user input (default €300) because the real one is set
   by activity code, municipality, age and gender — it is *not* derivable from
   revenue. Valid only up to **6,000,000 RSD/yr (~€51k)**; over that, a cap
   warning appears. Effective rate *falls* as invoicing rises — the whole appeal.
2. **Freelancer (self-tax, Model A / B)** — for individuals via the Tax
   Administration portal. The engine computes both models and shows the cheaper:
   - Model A: fixed standardized deduction, 20% tax
   - Model B: fixed deduction + 34% of gross, 10% tax
   - both + 24% pension (PIO) and 10.3% health on the base
3. **DOO (company)** — 15% corporate tax on profit, then 15% on distributed
   dividends. `profit = invoiced − expenses`.

Both directions work: enter an invoice to see the net, or a target net to solve
for the invoice (60-step binary search).

The **independence test** section is interactive: tick the criteria true for a
client relationship; five or more of nine flips the verdict to "dependent",
where income is taxed as other income at 20% + full contributions.

## Updating the numbers each year

All tax parameters live in one `TAX` object and the `RSD_PER_EUR` constant near
the top of the `<script>` in `index.html`. To refresh for a new year, edit only:

- `RSD_PER_EUR` — indicative exchange rate (also re-derives the €-shown ceilings)
- `pausalCeilingEUR` / `vatThresholdEUR` — from the 6,000,000 / 8,000,000 RSD lines
- `freelancer.modelA_deductionEUR`, `modelB_fixedDeductionEUR` — from that year's
  quarterly standardized-cost figures (currently 107,738 and 64,979 RSD/quarter)
- `freelancer` tax rates (20% / 10%) and `contribRate` (0.343 = 24% + 10.3%)
- `doo.corpRate` / `dividendRate` (both 0.15)

You should not need to touch the engine, the layout, or the copy to do a yearly
figures refresh. If the default paušal monthly estimate drifts, update the
`value="300"` on the `#pausal` input and the hint text.

## Honest caveats (these are real, keep them in mind)

- **The paušal figure is entered, not computed.** The genuine amount depends on
  activity code, municipality, age and gender. Two contractors billing the same
  can owe very different fixed sums. The default is a plausible IT-in-Belgrade
  midpoint, nothing more.
- **Freelancer minimum contribution bases are simplified out.** At typical
  foreign-client incomes they rarely bind, but at low income the real bill can be
  higher than shown.
- **The DOO route excludes a director's salary and contributions and accounting
  fees.** A real company's take-home burden is higher than the 15% + 15% shown.
- **The lična zarada (personal-salary) optimization is not modelled** in the DOO
  or a bookkeeping-entrepreneur tab — it's described only in the "special cases"
  section. Properly structured, it can beat everything at higher income.
- **EUR is indicative.** Serbian tax is assessed in RSD; the exchange rate moves.
- **The independence test is applied per client relationship, on the facts** — the
  checklist is an orientation, not a ruling.
- This is general information, **not tax, legal or accounting advice.** Every real
  decision should go past a qualified Serbian accountant (*knjigovođa*) or tax
  adviser.

Figures reflect the 2026 Serbian rules.
