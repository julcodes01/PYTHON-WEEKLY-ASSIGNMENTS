# Supermarket Discount System

purchase_amount = float(input("Enter total purchase amount: "))

if purchase_amount >= 10000:
    discount = 0.15 * purchase_amount
else:
    discount = 0

final_amount = purchase_amount - discount

print("\n--- Purchase Details ---")
print(f"Purchase Amount: KSh {purchase_amount:.2f}")
print(f"Discount: KSh {discount:.2f}")
print(f"Final Amount: KSh {final_amount:.2f}")
