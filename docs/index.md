# open-invoice-docs

Welcome to **open-invoice-docs**, an open documentation project that explains how to structure, store and send invoices in a small business or freelance context.

The focus is on the *content* of the invoice rather than on a particular tool. A clean invoice that follows the conventions in this guide should be acceptable whether you produce it in a word processor, a spreadsheet, a dedicated accounting application, or an online generator such as [invoicegenerator.run](https://invoicegenerator.run/).

This site is aimed at:

- **Freelancers and contractors** who need to issue a handful of invoices per month and do not want to learn full accounting software.
- **Small business owners** who are setting up an invoicing process for the first time.
- **Developers** who are building a billing or invoicing feature into their own product and want a starting point for the data model and field semantics.

## How the documentation is organised

- {doc}`quickstart` walks you from a blank page to a complete invoice you can send today.
- {doc}`field-reference` explains every standard line on an invoice and why it is there.
- {doc}`schema` gives a JSON schema you can reuse as the data model behind your own system.
- {doc}`jurisdictions` summarises how invoice requirements differ across the US, the EU and the UK.
- {doc}`workflow` covers numbering, payment terms and politely chasing late payments.
- {doc}`faq` answers the most common practical questions.
- {doc}`references` collects further reading and the online tools used in worked examples.

## Scope and disclaimer

This documentation is general guidance, not legal or tax advice. Invoice and tax rules change and vary by country, state and even by industry. Always confirm requirements with a qualified accountant or with your local tax authority before relying on any specific field, format or number in this guide.

```{toctree}
:maxdepth: 2
:caption: Contents

quickstart
field-reference
schema
jurisdictions
workflow
faq
references
```
