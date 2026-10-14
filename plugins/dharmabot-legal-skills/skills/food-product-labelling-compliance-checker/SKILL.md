---
name: food-product-labelling-compliance-checker
description: Checks food and consumer product compliance in India under the Food Safety and Standards Act, 2006 and FSSAI regulations on licensing, product standards, labelling and display, and advertising and claims, the Legal Metrology (Packaged Commodities) Rules, 2011, and BIS registration and Quality Control Orders, producing a label markup and licence list. Use when a client shares a product label, pack artwork or product list and asks if it complies before launch. Do not use for advertising campaigns beyond the pack; use advertising-claims-reviewer instead.
---

# Food and Product Labelling Compliance Checker

Every output is a draft review for an advocate enrolled in India and the client's regulatory team to check before printing.

## Purpose

Find every label and licensing defect before the product is printed and sold, and flag claims that need approval or evidence.

## Jurisdiction gate

- Confirm the product is sold in India (domestic manufacture or import). Imported food also needs FSSAI import clearance; note it.
- Classify the product first: general food, standardised food, proprietary food, health supplement or nutraceutical, food for special dietary use, or something regulated as a drug or cosmetic. Classification decides the rules. If it may be a drug, hand to `drugs-devices-regulatory-analyst`.

## Temporal gate

FSSAI amends labelling rules often, with compliance dates. Record the print date and launch date, and check each amendment's effective date. Mark draft notifications (for example on front-of-pack nutrition labelling) as not yet law.

## Required inputs

**Blocking**:
- the full label or artwork for every face of the pack, at actual size if possible;
- the ingredient list with quantities, and nutrition data with its source (lab report or calculation);
- the claims the client wants to make, on pack and online;
- the manufacturer, packer, marketer or importer, and their licence numbers.

Also useful: pack sizes, sales channels (retail, e-commerce, export), and target consumers.

## Method

1. Retrieve the current official text of the FSS Act, the FSSAI regulations on licensing, product standards, labelling and display, advertising and claims, and supplements where relevant, the Legal Metrology (Packaged Commodities) Rules, and any BIS Quality Control Order for the product. Record version and date.
2. Licensing: check the right licence or registration category for each operator in the chain, and that the licence covers this product category.
3. Product standards: compare composition with the standard or permitted ingredient and additive lists, and any limits for supplements.
4. FSSAI label check: name of food, ingredients in descending order, allergens, nutrition information, veg or non-veg symbol, additives declared correctly, FSSAI logo and licence number, date marking, storage and usage instructions, and any mandatory warnings.
5. Legal Metrology check: manufacturer, packer or importer name and address, net quantity in standard units, MRP inclusive of taxes, date of manufacture or import, consumer care details, country of origin for imports, unit sale price where required, and font and panel requirements.
6. Claims: classify each (nutrient content, nutrient comparative, health, reduction of disease risk, or other). Check the threshold or conditions in the regulations, and whether prior approval is needed. Flag disease-related claims.
7. BIS: check whether any component or packaging falls under a Quality Control Order.
8. E-commerce: the same mandatory information must be shown on the product page. Hand platform issues to `ecommerce-platform-terms-checker`.
9. Mark up the label with numbered comments and a fix for each.

## Output

1. Label markup: item · rule (to confirm) · issue · fix.
2. Licence and registration list for each operator.
3. Claims table: claim · type · condition · evidence needed · approval needed.
4. Pre-launch checklist.

## Guardrails and hand-offs

- Never approve a health or disease claim without the regulation and evidence.
- Never fill in nutrition values or test results not supplied.
- Advertising beyond the pack goes to `advertising-claims-reviewer`; applications to `licence-application-drafter`.
