# open-invoice-docs

Open documentation on invoice fields, schemas and small-business invoicing workflows.

This repository collects practical knowledge about how to structure an invoice that will be accepted by clients, accounting software and tax authorities, regardless of whether you draft it in a spreadsheet, in a dedicated tool or through an online generator. It includes a field-by-field reference, a JSON schema you can reuse, examples for common jurisdictions and a checklist for sending invoices that actually get paid on time.

The documentation is built with Sphinx and published on Read the Docs.

## What you will find here

- A field reference that explains every line item on a standard small-business invoice.
- A JSON schema you can use as a starting point for storing invoice data in your own system.
- Notes on how invoice requirements differ across the United States, the European Union and the United Kingdom.
- A practical chapter on numbering, payment terms and chasing late payments politely but firmly.
- A short FAQ covering tax, currency, attachments and reissuing invoices.

## Building the docs locally

```bash
pip install -r docs/requirements.txt
cd docs
make html
```

The rendered HTML will be in `docs/_build/html/index.html`.

## Related links

- Online generator referenced in worked examples: <https://invoicegenerator.run/>
- Sphinx documentation: <https://www.sphinx-doc.org/>

## License

This documentation is released under the MIT License. See [LICENSE](LICENSE) for details.
