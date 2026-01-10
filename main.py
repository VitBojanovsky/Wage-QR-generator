import pandas as pd
import qrcode
import os
import konfigurace

# --- Step 0: Setup ---
hours_file = konfigurace.hours_file
wages_file = konfigurace.wages_file
output_dir = konfigurace.output_dir

os.makedirs(output_dir, exist_ok=True)

# --- Step 1: Load data ---
print("Loading Excel files...")
hours_df = pd.read_excel(hours_file)
wages_df = pd.read_excel(wages_file)

# Clean column names (strip spaces)
hours_df.columns = hours_df.columns.str.strip()
wages_df.columns = wages_df.columns.str.strip()

print("\nHours table head:")
print(hours_df.head())
print("\nWages table head:")
print(wages_df.head())

# --- Step 2: Merge tables on User ID / ID ---
print("\nMerging tables on User ID / ID...")
df = hours_df.merge(wages_df, left_on='User ID', right_on='ID', how='left')

print("\nMerged table head:")
print(df.head())

# --- Step 3: Calculate payment amount ---
print("\nCalculating payment amounts...")
df['PaymentAmount'] = df['Actual Time [Hour]'] * df['Wage']
print(df[['EmployeeName', 'Actual Time [Hour]', 'Wage', 'PaymentAmount']])

# --- Step 4: Function to generate Czech QR payment string ---
def create_qr_string(row):
    if pd.isna(row['IBAN']):
        print(f"Skipping {row['EmployeeName']}: missing IBAN")
        return None
    if row['PaymentAmount'] <= 0:
        print(f"Skipping {row['EmployeeName']}: PaymentAmount <= 0")
        return None
    qr_string = f"SPD*1.0*ACC:{row['IBAN']}*AM:{row['PaymentAmount']:.2f}*CC:CZK*MSG:Payment for {row['EmployeeName']}"
    print(f"Generated QR string for {row['EmployeeName']}: {qr_string}")
    return qr_string

print("\nGenerating QR strings...")
df['QR_String'] = df.apply(create_qr_string, axis=1)

# --- Step 5: Generate QR codes ---
print("\nGenerating QR code images...")
for i, row in df.iterrows():
    if row['QR_String']:
        qr_img = qrcode.make(row['QR_String'])
        safe_name = "".join([c if c.isalnum() else "_" for c in row['EmployeeName']])
        filename = os.path.join(output_dir, f"{safe_name}_QR.png")
        qr_img.save(filename)
        print(f"Saved QR code for {row['EmployeeName']} - {row['PaymentAmount']:.2f} CZK -> {filename}")

print("\nAll QR codes generated in folder:", output_dir)
readline = input("Press Enter to exit...")