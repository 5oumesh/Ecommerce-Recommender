#!/usr/bin/env python3
"""
Quick demo of the Hierarchical E-Commerce Navigator
Shows what the system displays and how to use it
"""

def show_demo():
    print("\n" + "="*80)
    print("🛍️  E-COMMERCE HIERARCHICAL NAVIGATOR - DEMO")
    print("="*80)
    
    print("\n📍 STEP 1: Browse Main Categories")
    print("-" * 80)
    print("""
================================================================================
🏪 MAIN PRODUCT CATEGORIES
================================================================================

|  #  | Category     |  Products  |  Subcategories  |
+=====+==============+============+=================+
|  1  | Accessories  |    136     |     3 types     |
|  2  | Apparel      |    678     |    14 types     |
|  3  | Appliances   |   2,138    |    27 types     |
|  4  | Auto         |    358     |     7 types     |
|  5  | Computers    |   1,023    |    15 types     |
|  6  | Construction |    425     |     8 types     |
|  7  | Country Yard |     12     |     3 types     |
|  8  | Electronics  |   2,223    |    13 types     |
|  9  | Furniture    |    599     |    11 types     |
| 10  | Kids         |    272     |     6 types     |
| 11  | Medicine     |     7      |     1 types     |
| 12  | Sport        |     82     |     5 types     |
| 13  | Stationery   |     2      |     1 types     |
+-----+--------------+------------+-----------------+

User enters: 3 (for Appliances)
""")
    
    print("\n📍 STEP 2: Browse Subcategories for Selected Main Category")
    print("-" * 80)
    print("""
================================================================================
📂 APPLIANCES SUBCATEGORIES (Select one to get recommendations)
================================================================================

|  #  |        Subcategory        |  Products  |
+=====+===========================+============+
|  1  | environment               |     45     |
|  2  | kitchen                   |    156     |
|  3  | personal                  |     89     |
|  4  | bedroom                   |     32     |
|  5  | office                    |     28     |
|  6  | living_room               |     41     |
|  7  | garage                    |     19     |
|  8  | entertainment             |     35     |
|  9  | storage                   |     23     |
| 10  | cleaning                  |     37     |
...

User enters: 2 (for Kitchen appliances)
""")
    
    print("\n📍 STEP 3: Specify Number of Recommendations")
    print("-" * 80)
    print("""
👉 How many recommendations would you like? (1-20, default=10): 5

(System finding 5 best recommendations for Appliances > Kitchen...)
""")
    
    print("\n📍 STEP 4: View Recommendations")
    print("-" * 80)
    print("""
================================================================================
🎁 TOP RECOMMENDATIONS FOR Appliances > Kitchen
================================================================================

| Product ID | Brand              | Price    | Popularity  |
|=========== |====================|==========|=============|
| P45821     | Samsung            | $899.99  | ⭐⭐⭐⭐⭐  |
| P67234     | LG Electronics     | $749.50  | ⭐⭐⭐⭐   |
| P82956     | Whirlpool          | $599.00  | ⭐⭐⭐⭐⭐  |
| P34567     | KitchenAid         | $1299.99 | ⭐⭐⭐⭐⭐  |
| P56789     | Bosch              | $849.75  | ⭐⭐⭐⭐   |
+--------+----+----+------+

================================================================================
""")
    
    print("\n📍 STEP 5: Choose Next Action")
    print("-" * 80)
    print("""
👉 What would you like to do? (another/back/quit):

Options:
  • another   → Get more recommendations for Appliances > Kitchen
  • back      → Go back and choose different kitchen subcategory
  • quit      → Exit the program

User enters: back
""")
    
    print("\n" + "="*80)
    print("✨ SYSTEM FEATURES")
    print("="*80)
    print("""
✅ 13 Main Categories to browse (Accessories, Apparel, Appliances, etc.)
✅ Multiple subcategories under each main category
✅ 1-20 recommendations per selection
✅ Rich product information (Brand, Price, Popularity rating)
✅ Easy back/forward navigation
✅ Built on 179,509 interactions and 14,011 products
✅ Lightning-fast recommendations (~3.76ms per query)
✅ Hybrid recommendation model for best results
""")
    
    print("\n" + "="*80)
    print("🚀 TO RUN THE ACTUAL SYSTEM")
    print("="*80)
    print("""
1. Make sure you're in the project directory:
   cd /home/soumesh/Desktop/Ecommerce-Recommand

2. Activate the virtual environment:
   source .venv/bin/activate

3. Run the navigator:
   python ecommerce_navigator.py

4. Follow the prompts to browse and get recommendations!
""")
    
    print("\n" + "="*80)
    print("📚 CATEGORY QUICK REFERENCE")
    print("="*80)
    
    categories = {
        "Accessories": ["bag", "umbrella", "wallet"],
        "Apparel": ["costume", "dress", "shoes", "tshirt"],
        "Appliances": ["environment", "kitchen", "personal", "bedroom"],
        "Auto": ["parts", "tires", "batteries"],
        "Computers": ["components", "desktop", "notebook"],
        "Electronics": ["smartphone", "audio", "clocks"],
        "Furniture": ["bedroom", "kitchen", "living_room"],
        "Kids": ["toys", "clothes", "books"],
        "Sport": ["equipment", "apparel", "accessories"],
    }
    
    for cat, subs in categories.items():
        print(f"• {cat:15} → {', '.join(subs[:3])}{'...' if len(subs) > 3 else ''}")
    
    print("\n" + "="*80 + "\n")

if __name__ == "__main__":
    show_demo()
