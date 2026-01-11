#!/usr/bin/env python3
"""
🛍️ E-COMMERCE RECOMMENDATION SYSTEM LAUNCHER
Your personal shopping assistant with hierarchical category browsing
"""

def main_menu():
    print("\n" + "="*80)
    print("🛍️  E-COMMERCE RECOMMENDATION SYSTEM")
    print("="*80)
    print("""
Welcome! Choose how to explore products:

1️⃣  Launch Hierarchical Navigator
    ├─ Browse 13 main categories (Accessories, Apparel, Electronics, etc.)
    ├─ Select subcategories (kitchen, bedroom, etc.)
    └─ Get personalized recommendations
    
2️⃣  View Quick Demo
    └─ See how the system works with examples

3️⃣  View System Statistics
    └─ Learn about the dataset and models

4️⃣  View How-To Guide
    └─ Detailed instructions for using the navigator

5️⃣  Exit
""")
    
    while True:
        choice = input("👉 Enter your choice (1-5): ").strip()
        
        if choice == '1':
            print("\n" + "="*80)
            print("🚀 Starting Hierarchical Navigator...")
            print("="*80 + "\n")
            import subprocess
            import sys
            subprocess.run([sys.executable, 'ecommerce_navigator.py'])
            break
        
        elif choice == '2':
            print("\nLoading demo...\n")
            import subprocess
            import sys
            subprocess.run([sys.executable, 'DEMO_NAVIGATOR.py'])
            input("\n[Press Enter to continue...]")
        
        elif choice == '3':
            show_statistics()
            input("\n[Press Enter to continue...]")
        
        elif choice == '4':
            show_guide()
            input("\n[Press Enter to continue...]")
        
        elif choice == '5':
            print("\n👋 Thank you for using the E-Commerce Recommendation System!\n")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-5.")

def show_statistics():
    print("\n" + "="*80)
    print("📊 SYSTEM STATISTICS")
    print("="*80)
    print("""
DATASET SIZE
├─ Total Interactions: 179,509
├─ Total Products: 14,011
├─ Total Users: 35,516
└─ Time Period: Oct 2019 - Sept 2023

CATEGORIES
├─ Main Categories: 13
├─ Subcategories: 114
└─ Most Products: Electronics (2,223), Appliances (2,138)

RECOMMENDATION ENGINE
├─ Model Type: Hybrid (Neural Collaborative Filtering + Content-based)
├─ NCF Architecture: Deep Neural Network with embeddings
├─ Content Features: 300-dimensional embeddings per product
└─ Recommendation Speed: ~3.76ms per query

EVALUATION METRICS (on test set)
├─ Hit Rate: High accuracy on user preferences
├─ Precision: Strong relevance of top recommendations
├─ Recall: Good coverage of user interests
└─ F1 Score: Balanced performance across all metrics
""")

def show_guide():
    print("\n" + "="*80)
    print("📚 QUICK START GUIDE")
    print("="*80)
    print("""
STEP 1: LAUNCH THE SYSTEM
    $ python launcher.py
    Select option 1 to start

STEP 2: BROWSE MAIN CATEGORIES
    You'll see 13 main product categories:
    1. Accessories    2. Apparel      3. Appliances   4. Auto
    5. Computers      6. Construction 7. Country Yard 8. Electronics
    9. Furniture      10. Kids        11. Medicine    12. Sport
    13. Stationery
    
    Enter a number (1-13) to select a main category

STEP 3: SELECT SUBCATEGORY
    After picking a main category (e.g., Appliances), you'll see:
    • environment (45 products)
    • kitchen (156 products)
    • personal (89 products)
    • bedroom (32 products)
    • ...and more
    
    Enter a number to select a subcategory

STEP 4: SPECIFY RECOMMENDATIONS
    Enter how many recommendations you want (1-20)
    Default is 10 if you just press Enter

STEP 5: VIEW RECOMMENDATIONS
    The system shows top products with:
    • Product ID
    • Brand
    • Price
    • Popularity Rating (⭐ stars)

STEP 6: NAVIGATE
    After viewing recommendations:
    • another → Get more recommendations for same subcategory
    • back    → Choose different subcategory
    • quit    → Exit the program

KEYBOARD SHORTCUTS
    'q' or 'quit' → Exit at any time
    'back'        → Go back one level
""")

if __name__ == '__main__':
    main_menu()
