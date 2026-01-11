#!/usr/bin/env python3
"""
Hierarchical E-Commerce Recommendation System
Browse categories → subcategories → Get recommendations
"""

import pandas as pd
import pickle
import sys
from collections import defaultdict
from src.inference.recommend import hybrid_recommend
from tabulate import tabulate

class EcommerceNavigator:
    def __init__(self):
        """Initialize the navigator"""
        print("\n" + "="*80)
        print("🛍️  Loading E-Commerce Navigator System...")
        print("="*80)
        
        try:
            # Load data
            print("📂 Loading data files...")
            self.interactions = pd.read_csv('data/processed/interactions.csv')
            self.products = pd.read_csv('data/processed/products.csv')
            self.users = pd.read_csv('data/processed/users.csv')
            
            # Load features
            print("🎯 Loading product features...")
            with open('features/product_features.pkl', 'rb') as f:
                self.product_features = pickle.load(f)
            
            # Build category hierarchy
            print("📊 Building category hierarchy...")
            self.build_category_hierarchy()
            
            print(f"✅ System ready!")
            print(f"   • {len(self.interactions):,} interactions loaded")
            print(f"   • {len(self.products):,} products loaded")
            print(f"   • {len(self.users):,} users loaded")
            print(f"   • {len(self.main_categories)} main categories available")
            
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            sys.exit(1)
    
    def build_category_hierarchy(self):
        """Build hierarchical category structure from flat category codes"""
        self.main_categories = {}
        
        # Parse all categories
        for cat_code in self.products['category_code'].unique():
            if not cat_code or cat_code == 'unknown':
                continue
            
            # Split by dots to get hierarchy
            parts = str(cat_code).split('.')
            main_cat = parts[0]
            
            if main_cat not in self.main_categories:
                self.main_categories[main_cat] = {
                    'subcategories': defaultdict(list),
                    'count': 0
                }
            
            # Build subcategory hierarchy
            if len(parts) > 1:
                sub_cat = '.'.join(parts[1:])
                self.main_categories[main_cat]['subcategories'][sub_cat].append(cat_code)
            else:
                self.main_categories[main_cat]['subcategories'][cat_code].append(cat_code)
            
            # Count products
            count = len(self.products[self.products['category_code'] == cat_code])
            self.main_categories[main_cat]['count'] += count
        
        # Sort
        self.main_categories = dict(sorted(self.main_categories.items()))
    
    def display_welcome(self):
        """Display welcome message"""
        print("\n" + "="*80)
        print("🛒 WELCOME TO HIERARCHICAL E-COMMERCE BROWSER 🛒")
        print("="*80)
        print("\n📖 How it works:")
        print("  1️⃣  Browse main product categories")
        print("  2️⃣  Select a category to see subcategories")
        print("  3️⃣  Select a subcategory to see products")
        print("  4️⃣  Get personalized recommendations!")
        print("\n💡 Navigate with simple numbered selections")
        print("   Go back with 'back' or 'b' anytime\n")
        print("-" * 80 + "\n")
    
    def display_main_categories(self):
        """Display main category menu"""
        print("\n" + "="*80)
        print("🏪 MAIN PRODUCT CATEGORIES")
        print("="*80 + "\n")
        
        cat_list = []
        for i, (cat_name, cat_info) in enumerate(self.main_categories.items(), 1):
            cat_list.append([
                i,
                self.format_category_name(cat_name),
                f"{cat_info['count']:,}",
                f"{len(cat_info['subcategories'])} types"
            ])
        
        print(tabulate(
            cat_list,
            headers=['#', 'Category', 'Products', 'Subcategories'],
            tablefmt='grid',
            colalign=('center', 'left', 'center', 'center')
        ))
        print()
    
    def display_subcategories(self, main_cat):
        """Display subcategories for a main category"""
        print("\n" + "="*80)
        print(f"📂 {self.format_category_name(main_cat).upper()} - Subcategories")
        print("="*80 + "\n")
        
        sub_cats = self.main_categories[main_cat]['subcategories']
        sub_list = []
        
        for i, (sub_name, full_cats) in enumerate(sorted(sub_cats.items()), 1):
            # Get product count for this subcategory group
            count = len(self.products[
                self.products['category_code'].isin(full_cats)
            ])
            
            sub_list.append([
                i,
                self.format_category_name(sub_name),
                f"{count:,}"
            ])
        
        print(tabulate(
            sub_list,
            headers=['#', 'Subcategory', 'Products'],
            tablefmt='grid',
            colalign=('center', 'left', 'center')
        ))
        print("\n👉 Enter subcategory number (or 'back' to go back): ")
    
    def get_main_category_selection(self):
        """Get main category from user"""
        self.display_main_categories()
        
        while True:
            try:
                choice = input("👉 Enter category number (or 'quit' to exit): ").strip()
                
                if choice.lower() in ['quit', 'exit', 'q']:
                    return None
                
                choice_num = int(choice)
                main_cats = list(self.main_categories.keys())
                
                if 1 <= choice_num <= len(main_cats):
                    return main_cats[choice_num - 1]
                else:
                    print(f"❌ Please enter a number between 1 and {len(main_cats)}")
            
            except ValueError:
                print("❌ Please enter a valid number")
    
    def get_subcategory_selection(self, main_cat):
        """Get subcategory from user"""
        self.display_subcategories(main_cat)
        
        while True:
            try:
                choice = input().strip()
                
                if choice.lower() in ['back', 'b']:
                    return None
                if choice.lower() in ['quit', 'q']:
                    return 'QUIT'
                
                choice_num = int(choice)
                sub_cats = self.main_categories[main_cat]['subcategories']
                sub_list = sorted(sub_cats.keys())
                
                if 1 <= choice_num <= len(sub_list):
                    selected_sub = sub_list[choice_num - 1]
                    return selected_sub
                else:
                    print(f"❌ Please enter a number between 1 and {len(sub_list)}")
            
            except ValueError:
                print("❌ Please enter a valid number or 'back'")
    
    def get_recommendation_count(self):
        """Get number of recommendations user wants"""
        print("\n")
        while True:
            try:
                num = input("👉 How many recommendations do you want? (1-20, default=10): ").strip()
                
                if not num:
                    return 10
                
                num = int(num)
                
                if 1 <= num <= 20:
                    return num
                else:
                    print("❌ Please enter a number between 1 and 20")
            
            except ValueError:
                print("❌ Please enter a valid number")
    
    def format_category_name(self, cat_code):
        """Format category code to readable name"""
        return cat_code.replace('_', ' ').title()
    
    def get_user_for_categories(self, category_list):
        """Get a user who has interacted with these categories"""
        # Get products in these categories
        products_in_cats = self.products[
            self.products['category_code'].isin(category_list)
        ]['product_id'].values
        
        if len(products_in_cats) == 0:
            return None, None
        
        # Get users who interacted with these products
        interactions_in_cats = self.interactions[
            self.interactions['product_id'].isin(products_in_cats)
        ]
        
        if len(interactions_in_cats) == 0:
            return None, None
        
        # Get a random user and a seed product
        users_in_cats = interactions_in_cats['user_id'].unique()
        selected_user = users_in_cats[0]
        
        # Get a seed product from this user's interactions
        user_products = interactions_in_cats[
            interactions_in_cats['user_id'] == selected_user
        ]['product_id'].values
        
        seed_product = user_products[0] if len(user_products) > 0 else products_in_cats[0]
        
        return selected_user, seed_product
    
    def enrich_recommendations(self, recommendations_df):
        """Add more details to recommendations"""
        enriched = []
        
        for idx, row in recommendations_df.iterrows():
            product_id = row['product_id']
            
            # Get product details from CSV
            prod_info = self.products[
                self.products['product_id'] == product_id
            ]
            
            if len(prod_info) > 0:
                prod = prod_info.iloc[0]
                
                # Get features if available
                features = self.product_features.get(product_id, {})
                
                enriched.append({
                    '🔢': idx + 1,
                    'Product ID': product_id,
                    '🏢 Brand': features.get('brand', 'Unknown')[:20],
                    '💰 Price': f"${features.get('price', 'N/A')}",
                    '⭐ Popularity': f"{features.get('popularity_score', 0):.2f}",
                })
        
        return enriched
    
    def display_recommendations(self, recommendations_df, sub_cat, user_id):
        """Display recommendations in a nice format"""
        if len(recommendations_df) == 0:
            print("\n❌ No recommendations found for this category.")
            return
        
        print("\n" + "="*80)
        print("🎁 TOP PRODUCT RECOMMENDATIONS FOR YOU!")
        print("="*80)
        print(f"\n📍 Category: {self.format_category_name(sub_cat)}")
        print(f"📦 Showing {len(recommendations_df)} products\n")
        
        # Enrich and display
        enriched = self.enrich_recommendations(recommendations_df)
        
        print(tabulate(
            enriched,
            headers=enriched[0].keys() if enriched else [],
            tablefmt='grid',
            maxcolwidths=[3, 12, 20, 12, 15]
        ))
        
        print("\n" + "="*80)
        print("✨ These products are personalized for you based on similar user")
        print(f"   preferences in the {self.format_category_name(sub_cat)} category!")
        print("="*80)
    
    def run(self):
        """Main application loop"""
        self.display_welcome()
        
        while True:
            try:
                # Step 1: Get main category
                main_cat = self.get_main_category_selection()
                
                if main_cat is None:
                    print("\n👋 Thank you for using our e-commerce browser!")
                    print("   Visit again soon!")
                    break
                
                # Step 2: Get subcategory
                while True:
                    sub_cat = self.get_subcategory_selection(main_cat)
                    
                    if sub_cat == 'QUIT':
                        print("\n👋 Thank you for using our e-commerce browser!")
                        return
                    
                    if sub_cat is None:
                        # Go back to main categories
                        break
                    
                    # Step 3: Get number of recommendations
                    num_recs = self.get_recommendation_count()
                    
                    # Step 4: Get categories for this subcategory
                    sub_cats = self.main_categories[main_cat]['subcategories']
                    full_cats = sub_cats[sub_cat]
                    
                    # Step 5: Get user for this category
                    print(f"\n🔍 Finding products in {self.format_category_name(sub_cat)}...")
                    user_id, seed_product = self.get_user_for_categories(full_cats)
                    
                    if user_id is None:
                        print(f"❌ No products found for {self.format_category_name(sub_cat)}")
                        continue
                    
                    # Step 6: Get recommendations
                    print(f"🤖 Generating personalized recommendations...")
                    
                    recommendations = hybrid_recommend(
                        user_id=user_id,
                        seed_product_id=seed_product,
                        top_n=num_recs
                    )
                    
                    # Step 7: Display results
                    self.display_recommendations(recommendations, sub_cat, user_id)
                    
                    # Ask if they want to continue in this subcategory
                    print("\n")
                    while True:
                        choice = input("🔄 What would you like to do? (another/back/quit): ").strip().lower()
                        if choice in ['another', 'a']:
                            break  # Loop subcategory selection
                        elif choice in ['back', 'b']:
                            break  # Go back to subcategory selection
                        elif choice in ['quit', 'q']:
                            print("\n👋 Thank you for using our e-commerce browser!")
                            return
                        else:
                            print("❌ Please enter 'another', 'back', or 'quit'")
                    
                    if choice not in ['another', 'a']:
                        break  # Go back to main categories
            
            except KeyboardInterrupt:
                print("\n\n👋 Thank you for using our e-commerce browser!")
                break
            except Exception as e:
                print(f"\n❌ An error occurred: {e}")
                continue


def main():
    """Main entry point"""
    try:
        app = EcommerceNavigator()
        app.run()
    except Exception as e:
        print(f"\n❌ Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
