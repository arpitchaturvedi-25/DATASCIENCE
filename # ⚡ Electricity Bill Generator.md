# ⚡ Electricity Bill Generator
### Mini Project for Data Analytics Training Program

## 📌 Project Overview
The **Electricity Bill Generator** is a Python-based mini project that calculates electricity bills using **slab-wise billing**, applies **government subsidy**, and adds **GST (Goods and Services Tax)** to generate the final payable amount.

This project demonstrates the use of Python fundamentals such as conditional statements, user input, arithmetic operations, and formatted output. It is suitable for beginners in Python and Data Analytics training programs.

---

## 🎯 Objectives
- Calculate electricity bills based on slab rates.
- Apply government subsidy for eligible units.
- Calculate GST on the payable amount.
- Generate a clear and user-friendly electricity bill.

---

## 🛠️ Technologies Used
- **Programming Language:** Python 3.x
- **IDE:** VS Code 

---

## 📊 Billing Rules

| Units Consumed | Rate per Unit |
|---------------|--------------|
| 0 – 100 Units | ₹5 per unit |
| Above 100 Units | ₹10 per unit |

### Government Subsidy
- First **100 units are subsidized** at ₹5 per unit.
- Maximum subsidy = **₹500**

### GST
- **18% GST** is applied after deducting the subsidy.

---

## 🔄 Algorithm

1. Start the program.
2. Read consumer name.
3. Read electricity units consumed.
4. Calculate the original bill using slab-wise pricing.
5. Calculate the government subsidy.
6. Subtract subsidy from the original bill.
7. Calculate GST (18%).
8. Calculate the final payable amount.
9. Display the complete electricity bill.
10. End the program.

---

## ✨ Features
- Slab-wise electricity billing
- Automatic subsidy calculation
- GST calculation
- User-friendly bill display
- Beginner-friendly Python implementation

---

## 📷 Sample Output

```
========== ELECTRICITY BILL ==========
Consumer Name : Arpit
Units Consumed: 150

Original Bill : ₹1000
Subsidy       : ₹500
Bill After Subsidy : ₹500
GST (18%)     : ₹90

--------------------------------------
Total Payable : ₹590
======================================
```

---

## 📂 Project Structure

```
Electricity-Bill-Generator/
│
├── electricity_bill.py
├── README.md
└── sample_output.png (Optional)
```

---

## 🎓 Learning Outcomes

After completing this project, students will understand:

- Variables and Data Types
- User Input
- Conditional Statements (`if-else`)
- Arithmetic Calculations
- Formatted Output
- Real-world Billing Logic

---

## 🚀 Future Enhancements

- GUI using Tkinter
- Store bills in CSV or Excel
- Database integration
- Monthly bill history
- PDF bill generation
- Graphs and analytics using Pandas & Matplotlib

---

## 👨‍💻 Author

**Arpit Chaturvedi**

**Course:** B.Tech (CSE - Data Science)

**Mini Project:** Electricity Bill Generator

**Training Program:** Data Analytics Training Program

---

## 📜 License

This project is created for educational purposes as part of a **Data Analytics Training Program**.