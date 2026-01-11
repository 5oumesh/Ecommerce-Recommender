#!/usr/bin/env python3
"""
🎯 HIERARCHICAL NAVIGATOR - QUICK REFERENCE CARD
Print this or bookmark it for quick access
"""

def print_reference():
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                  🛍️  E-COMMERCE NAVIGATOR - QUICK REFERENCE               ║
╚════════════════════════════════════════════════════════════════════════════╝

┌─ HOW TO START ──────────────────────────────────────────────────────────────┐
│                                                                              │
│  Method 1: Using Menu Launcher (Recommended)                               │
│  $ python launcher.py                                                       │
│  → Select option 1                                                          │
│                                                                              │
│  Method 2: Direct Navigator                                                │
│  $ python ecommerce_navigator.py                                           │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ 13 MAIN CATEGORIES ────────────────────────────────────────────────────────┐
│                                                                              │
│   1. Accessories      7. Country Yard   13. Stationery                      │
│   2. Apparel          8. Electronics                                        │
│   3. Appliances       9. Furniture      ⭐ Most products:                    │
│   4. Auto           10. Kids              • Electronics (2,223)             │
│   5. Computers      11. Medicine          • Appliances (2,138)              │
│   6. Construction   12. Sport                                              │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ NAVIGATION FLOW ───────────────────────────────────────────────────────────┐
│                                                                              │
│                    ┌─────────────────────────┐                             │
│                    │  LEVEL 1: Main Category │                             │
│                    │   (pick 1-13)           │                             │
│                    └────────┬────────────────┘                             │
│                             │                                               │
│                    ┌────────▼────────────────┐                             │
│                    │ LEVEL 2: Subcategory    │                             │
│                    │  (varies by main)       │                             │
│                    └────────┬────────────────┘                             │
│                             │                                               │
│                    ┌────────▼────────────────┐                             │
│                    │ LEVEL 3: Recommendations│                             │
│                    │  (1-20 products)        │                             │
│                    └────────┬────────────────┘                             │
│                             │                                               │
│                    ┌────────▼────────────────┐                             │
│                    │    Choose Next Action   │                             │
│                    │  another / back / quit  │                             │
│                    └────────────────────────┘                             │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ EXAMPLE SESSION ───────────────────────────────────────────────────────────┐
│                                                                              │
│  $ python launcher.py                                                       │
│  → Select: 1 (Launch Navigator)                                            │
│                                                                              │
│  Shows 13 main categories...                                               │
│  👉 Enter category number: 3 (for Appliances)                              │
│                                                                              │
│  Shows appliance subcategories (27 total)...                               │
│  👉 Enter subcategory: 2 (for Kitchen)                                      │
│                                                                              │
│  👉 How many recommendations? (1-20): 5                                     │
│                                                                              │
│  Shows top 5 kitchen appliances with brand, price, popularity...           │
│                                                                              │
│  👉 What would you like to do? (another/back/quit): back                    │
│                                                                              │
│  Back to subcategory selection...                                          │
│  👉 Enter subcategory: 3 (for Personal)                                     │
│                                                                              │
│  Repeat or quit...                                                          │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ KEYBOARD COMMANDS ─────────────────────────────────────────────────────────┐
│                                                                              │
│  At Category Selection:                                                     │
│  • Enter 1-13 → Select main category                                       │
│  • 'quit'    → Exit program                                                │
│                                                                              │
│  At Subcategory Selection:                                                 │
│  • Enter 1-N → Select subcategory                                          │
│  • 'back'    → Go back to main categories                                  │
│  • 'quit'    → Exit program                                                │
│                                                                              │
│  At Recommendations Display:                                               │
│  • 'another' → Get more recommendations for same subcategory               │
│  • 'back'    → Go back to select different subcategory                     │
│  • 'quit'    → Exit program                                                │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ EXAMPLE SUBCATEGORIES ─────────────────────────────────────────────────────┐
│                                                                              │
│  Appliances (27 subcategories):                                            │
│  • environment, kitchen, personal, bedroom, office, living_room,           │
│    garage, entertainment, storage, cleaning, ...                           │
│                                                                              │
│  Electronics (13 subcategories):                                           │
│  • smartphone, audio, clocks, cameras, laptops, tablets, ...               │
│                                                                              │
│  Furniture (11 subcategories):                                             │
│  • bedroom, kitchen, living_room, office, outdoor, ...                     │
│                                                                              │
│  Computers (15 subcategories):                                             │
│  • components, desktop, notebook, servers, storage, ...                    │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ RECOMMENDATION OUTPUT ─────────────────────────────────────────────────────┐
│                                                                              │
│  Shows:                                                                     │
│  • Product ID (e.g., P12345)                                               │
│  • Brand (e.g., Samsung)                                                    │
│  • Price (e.g., $899.99)                                                    │
│  • Popularity Rating (⭐⭐⭐⭐⭐)                                             │
│                                                                              │
│  Recommendations are ranked by:                                            │
│  • Collaborative Filtering (60%)                                           │
│  • Content Similarity (40%)                                                │
│  • Hybrid Score = Best of both approaches                                  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ SYSTEM STATS ──────────────────────────────────────────────────────────────┐
│                                                                              │
│  Dataset:                      Model:                                      │
│  • 179,509 interactions        • Type: Hybrid (NCF + Content)              │
│  • 14,011 products             • Accuracy: High                            │
│  • 35,516 users                • Speed: <4ms per recommendation            │
│  • 114 subcategories           • Features: 300-dimensional embeddings      │
│  • 13 main categories          • Framework: TensorFlow/Keras               │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

┌─ FILES & DOCUMENTATION ─────────────────────────────────────────────────────┐
│                                                                              │
│  Main Files:                   Documentation:                              │
│  • launcher.py                 • HOW_TO_USE_NAVIGATOR.md                   │
│  • ecommerce_navigator.py      • README_HIERARCHICAL.md                    │
│  • DEMO_NAVIGATOR.py           • SYSTEM_SUMMARY.md                         │
│                                • QUICK_REFERENCE.md (this file)            │
│                                                                              │
│  All files in: /home/soumesh/Desktop/Ecommerce-Recommand/                  │
│                                                                              │
└──────────────────────────────────────────────────────────────────────────────┘

╔════════════════════════════════════════════════════════════════════════════╗
║                     🚀 READY TO BROWSE? START HERE:                        ║
║                                                                            ║
║                     $ python launcher.py                                   ║
║                                                                            ║
║                  Select option 1 to start shopping! 🛍️                     ║
╚════════════════════════════════════════════════════════════════════════════╝
""")

if __name__ == '__main__':
    print_reference()
