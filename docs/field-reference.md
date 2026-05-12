# Field reference

This chapter walks through the fields that appear on a standard small-business invoice, in roughly the order they appear from top to bottom on the page. Each entry explains the purpose of the field, what to put in it, and the most common mistake to avoid.

## Header fields

### Document title

The word "Invoice" should appear clearly near the top of the document. This sounds trivial but it matters: many corporate accounts-payable systems route documents based on this word. Avoid alternatives like "Bill", "Statement" or "Charges Summary" unless you have a specific reason.

### Invoice number

A unique identifier for this invoice in your own records. See {doc}`workflow` for a numbering scheme. The number should appear near the top, labelled clearly. **Common mistake**: reusing or skipping numbers when redrafting a cancelled invoice. Issue a credit note instead.

### Issue date

The date you are sending the invoice. Use an unambiguous format such as "15 March 2026" or "2026-03-15". **Common mistake**: writing "03/15/26", which is ambiguous to international clients.

### Due date

The date by which payment is expected. Compute it from the issue date plus the agreed payment terms. **Common mistake**: writing "net 30" without an absolute date; non-accountants often do not know what that means.

## Party blocks

### From block (your business)

Include:

- Legal business name (and trading name if different).
- Full postal address.
- Email address used for billing queries.
- Tax identifier if your jurisdiction issues one (VAT number, EIN, GST number).
- Logo or wordmark, optional but recommended.

### Bill to block (your client)

Include:

- Client's legal name as they prefer to be invoiced. For corporate clients this is rarely the same as the trading name on the storefront.
- Their full billing address.
- The name of an individual contact, if you have one, after the company name. Many AP systems route invoices internally based on this.
- Their tax identifier if they have asked you to include it.

## Body fields

### Line items

Each line should contain:

- A short, specific **description**. "Consulting services" is too vague; "Strategy workshop, 14 March 2026" is clear.
- The **quantity** (hours, days, units).
- The **unit price**.
- The **line total** (quantity multiplied by unit price).

If you bill for time, include the date range covered. If you bill for products, include a SKU or model identifier when possible.

### Subtotal

The sum of all line totals before tax. State it explicitly so the client can verify the arithmetic.

### Tax

If you charge tax, show the tax rate, the tax amount, and the type of tax ("VAT 20 percent", "Sales tax 8.875 percent"). Where multiple lines are taxed at different rates, show a tax subtotal per rate. See {doc}`jurisdictions` for an overview of where this gets complicated.

### Total

The final amount the client owes. Display it more prominently than other figures, since this is the number both parties care about most.

### Currency

State the currency explicitly with a three-letter ISO code (USD, EUR, GBP, CNY) next to the total at minimum, and ideally next to every monetary figure on the invoice. **Common mistake**: a bare dollar sign on an invoice sent between a US client and a Canadian or Australian supplier.

## Payment fields

### Payment instructions

Provide at least one clear, complete way to pay. For bank transfers, this means bank name, account holder, account number and routing or IBAN. For payment platforms, include a clickable link and a fallback option. For checks, include the payee name and the address.

### Payment reference

Ask the client to include your invoice number as the reference for the payment. This makes reconciliation on your side trivial.

## Footer fields

### Notes

A short, free-form text field. Useful for thanking the client, repeating the payment terms in plain language, noting any agreed discount, or pointing out attachments. Keep it to one short paragraph.

### Terms

If you have generic terms ("Payment is due 30 days from the invoice date. Late payments are subject to 1.5 percent interest per month."), include them in a small font at the bottom or attach a separate Terms document. Do not pad the invoice with paragraphs of legalese; it makes the document harder to scan.
