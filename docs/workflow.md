# Invoicing workflow

This chapter covers the steady-state habits around invoicing once you have produced your first invoice using {doc}`quickstart`: how to number invoices so the sequence still makes sense in five years, how to set payment terms that protect your cash flow, and what to do when an invoice is not paid on time.

## Numbering

A good invoice number is:

- **Unique** across all invoices you have ever issued.
- **Sequential** within a given year, with no gaps.
- **Predictable** enough that you can guess the next number without looking.
- **Short enough** to be readable as a payment reference.

A scheme that works well for most small businesses is *YEAR-SEQUENCE* with zero-padded sequence numbers, for example `2026-0001`, `2026-0002`. Reset the sequence at the start of each year. Avoid embedding the client name in the number; this makes the scheme harder to maintain and can create privacy concerns if the invoice number is used as a payment reference.

If you need to cancel an invoice that has already been sent, do **not** delete it or reuse the number. Issue a credit note that explicitly references the original invoice. This keeps the audit trail clean.

## Payment terms

The most common terms in B2B services are:

- **Due on receipt**: payment is expected immediately. Useful for small clients or projects.
- **Net 7** or **Net 14**: payment is due 7 or 14 calendar days after the invoice date. Suitable for short-cycle work.
- **Net 30**: payment is due 30 days after the invoice date. The default for many corporate clients.
- **Net 45** or **Net 60**: payment is due 45 or 60 days after the invoice date. Larger corporates and government clients sometimes insist on these terms.

The shorter your terms, the better for your cash flow, but unrealistic terms create friction and disputes. Match the term to what the client's accounting department can actually process; if they pay monthly on the last Friday, "Net 14" simply means "paid at the next monthly cycle anyway".

Always state the **exact due date** on the invoice in addition to the terms.

## Sending

A few small habits make invoices easier to process and faster to be paid:

- Send the invoice as a PDF attachment, with the invoice number in the file name. `invoice-2026-0042.pdf` is much easier for the client to file than `document.pdf`.
- Use a subject line that includes both your name and the invoice number, for example "Invoice 2026-0042 from Acme Consulting Ltd".
- Keep the email body short and factual: who you are, what the invoice is for in one sentence, the amount, the due date, the payment method, and your willingness to answer questions.
- Send to a billing email address if the client has one, and CC your day-to-day contact.

## Recording

Maintain a single ledger of all invoices with at least:

- Invoice number.
- Date issued.
- Client name.
- Amount.
- Due date.
- Status ("sent", "paid", "overdue", "written off").
- Date of payment, once received.

A spreadsheet is fine for under fifty invoices a year. Beyond that, move to a small-business accounting tool that imports your bank feed and reconciles automatically.

## Chasing late payments

If the due date passes and the invoice is unpaid:

1. **Day 1 after due date**: a polite reminder email. Restate the invoice number, the amount, the date issued, and offer help with any issue. Many late payments are simply administrative oversights and resolve at this step.
2. **Day 7 after due date**: a firmer email referencing the original invoice and the first reminder. State explicitly that the payment is now overdue.
3. **Day 14 after due date**: a phone call. The single most effective collection step. Ask whether they have received the invoice, whether it has been approved, and when payment is expected.
4. **Day 21 after due date**: a final notice in writing, mentioning any late-payment interest you are entitled to charge under your agreed terms or the applicable law.
5. **Day 30 onward**: consider whether to keep working with this client, whether to involve a collections agency, or whether to write off the invoice and learn from it.

Keep the tone professional throughout. Most late payments arrive in the first two steps; very few clients are genuinely unwilling to pay.

## Reconciliation

Once a payment arrives, match it to the invoice using the payment reference. Update the ledger to "paid" with the date received. If the amount differs from the invoice (for instance, a wire-transfer fee was deducted), record the discrepancy and decide whether to absorb it, invoice for the difference, or note it for future reference. Consistency matters more than perfection here.
