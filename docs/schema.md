# Invoice JSON schema

If you are storing invoices in your own application, the following schema is a sensible starting point. It is intentionally minimal: it captures everything required to render a useful invoice, and leaves room for jurisdiction-specific fields to be added as extensions.

The schema is given in JSON Schema draft-07 syntax. It is also valid input for libraries that generate TypeScript types or Python dataclasses.

## Top-level object

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Invoice",
  "type": "object",
  "required": [
    "invoice_number",
    "issue_date",
    "due_date",
    "currency",
    "seller",
    "buyer",
    "line_items",
    "total"
  ],
  "properties": {
    "invoice_number": { "type": "string" },
    "issue_date":     { "type": "string", "format": "date" },
    "due_date":       { "type": "string", "format": "date" },
    "currency":       { "type": "string", "pattern": "^[A-Z]{3}$" },
    "seller":         { "$ref": "#/definitions/party" },
    "buyer":          { "$ref": "#/definitions/party" },
    "line_items": {
      "type": "array",
      "minItems": 1,
      "items": { "$ref": "#/definitions/line_item" }
    },
    "subtotal":       { "type": "number" },
    "tax": {
      "type": "array",
      "items": { "$ref": "#/definitions/tax_line" }
    },
    "total":          { "type": "number" },
    "payment_instructions": { "type": "string" },
    "notes":          { "type": "string" }
  }
}
```

## Party definition

Used for both seller and buyer.

```json
{
  "party": {
    "type": "object",
    "required": ["name", "address"],
    "properties": {
      "name":           { "type": "string" },
      "trading_name":   { "type": "string" },
      "contact_person": { "type": "string" },
      "email":          { "type": "string", "format": "email" },
      "address":        { "type": "string" },
      "tax_id":         { "type": "string" }
    }
  }
}
```

## Line item definition

```json
{
  "line_item": {
    "type": "object",
    "required": ["description", "quantity", "unit_price"],
    "properties": {
      "description": { "type": "string" },
      "quantity":    { "type": "number", "minimum": 0 },
      "unit":        { "type": "string" },
      "unit_price":  { "type": "number" },
      "tax_rate":    { "type": "number", "minimum": 0, "maximum": 1 },
      "line_total":  { "type": "number" }
    }
  }
}
```

## Tax line definition

```json
{
  "tax_line": {
    "type": "object",
    "required": ["label", "rate", "amount"],
    "properties": {
      "label":  { "type": "string" },
      "rate":   { "type": "number" },
      "amount": { "type": "number" }
    }
  }
}
```

## Worked example

A minimal invoice for two days of consulting work, with VAT at 20 percent, looks like this:

```json
{
  "invoice_number": "2026-0042",
  "issue_date": "2026-03-15",
  "due_date": "2026-04-14",
  "currency": "GBP",
  "seller": {
    "name": "Acme Consulting Ltd",
    "address": "12 Oak Lane, Bristol, BS1 4AB, United Kingdom",
    "email": "billing@acme.example",
    "tax_id": "GB123456789"
  },
  "buyer": {
    "name": "Globex Corp",
    "contact_person": "Accounts Payable",
    "address": "500 Market Street, San Francisco, CA 94110, United States"
  },
  "line_items": [
    {
      "description": "Strategy workshop, 13-14 March 2026",
      "quantity": 2,
      "unit": "day",
      "unit_price": 1200,
      "tax_rate": 0.2,
      "line_total": 2400
    }
  ],
  "subtotal": 2400,
  "tax": [
    { "label": "VAT 20%", "rate": 0.2, "amount": 480 }
  ],
  "total": 2880,
  "payment_instructions": "Bank transfer to Acme Consulting Ltd, sort 00-00-00, account 12345678. Reference: 2026-0042.",
  "notes": "Thank you for your business."
}
```

## Extending the schema

For jurisdictions that require additional fields (for example, the Italian *codice destinatario* for electronic invoicing), add them under a clearly named extension object such as `it_extensions` rather than at the top level. This keeps the core schema portable while supporting local requirements.
