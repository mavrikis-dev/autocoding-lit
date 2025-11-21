#!/usr/bin/env python3
"""
Test script to verify the new CSV structure with source evidence columns
"""

import pandas as pd
from config import CSV_COLUMNS

def test_csv_structure():
    """Test the new CSV structure with source evidence columns."""
    print("New CSV Column Structure:")
    print("=" * 50)
    
    for i, col in enumerate(CSV_COLUMNS, 1):
        print(f"{i:2d}. {col}")
    
    print(f"\nTotal columns: {len(CSV_COLUMNS)}")
    print(f"Answer columns: {len([col for col in CSV_COLUMNS if '- Source' not in col])}")
    print(f"Source columns: {len([col for col in CSV_COLUMNS if '- Source' in col])}")
    
    # Create a sample row to test CSV generation
    sample_data = {col: "Sample data" if col != "Title" else "Test Paper Title" for col in CSV_COLUMNS}
    
    # Show how the CSV would look
    df = pd.DataFrame([sample_data])
    print("\nSample CSV structure (first 5 columns):")
    print(df.iloc[:, :5].to_string(index=False))

if __name__ == "__main__":
    test_csv_structure()