# QR Code Generator Script

**License:** The license is in `LICENSE.md`. I strongly recommend reading it.

## Description
This script generates QR codes from two input files: `brigadnici.xls` and `config.xlsx`.

- `brigadnici.xls`: Exported from the program CrossChex; contains IDs and time spent at work.
- `config.xlsx`: Contains IDs, names, and, most importantly, IBANs (international bank account numbers). These are required to create QR payments. There is currently no way to calculate IBANs from local account numbers automatically.

The script produces QR codes suitable for payments in the **Czech Republic**.

## Disclaimer
- This script generates QR payments in **Czech format**. Modifications may be required to deploy it in other countries.
- The script **does not calculate taxes** and **does not generate invoices**. Please consult your local laws before using it.
- For licensing inquiries, contact me at **bojanovsky.vit@protonmail.com**.
