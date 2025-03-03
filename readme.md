# 📌 Class 01 Assignment - February 24  

## Assignment Overview  
This assignment involves setting up professional social media accounts, reviewing the first class, and learning essential Python concepts.  

## ✨ Tasks  

1. **Create X (Twitter) and LinkedIn Accounts**  
   - Use your real name for the profile.  
   - Add a professional bio and profile picture.  
   - Share a review of the first class.  
   - Attach the profile links below:  

   - 🔗 **X (Twitter):** [X (Twitter)](https://x.com/WaliZafri2005)  
   - 🔗 **LinkedIn:** [LinkedIn](https://www.linkedin.com/in/wali-zafri-profile/)  

2. **Learn Python Data Types & Special Keywords**  
   - Watch and understand the video tutorial.  

3. **Explore Google Colab**  
   - Learn how to use Google Colab for Python programming.  

4. **Submit the Assignment**  
   - Submit the form: [Assignment Submission Form](https://forms.gle/rH8SBsXyFddn6xhL8)  

---

## 📝 Python Code  
Below is the Python script demonstrating **data types and special keywords** covered in this assignment.  

```python
# Displaying Python Keywords
from keyword import kwlist, softkwlist

def display_keywords() -> None:
    print("Python Keywords:")
    for i, kw in enumerate(kwlist, start=1):
        print(f"{i:2}: {kw}")

    print("\nSoft Keywords:")
    for i, skw in enumerate(softkwlist, start=1):
        print(f'{i:2}: {skw}')

# Exploring Data Types
def explore_data_types():
    integer_value = 10       # Integer
    float_value = 3.14       # Float
    string_value = "Hello"   # String
    boolean_value = True     # Boolean
    list_value = [1, 2, 3]   # List
    tuple_value = (4, 5, 6)  # Tuple
    dict_value = {"name": "Alice", "age": 25}  # Dictionary
    set_value = {7, 8, 9}    # Set

    print("\nData Types in Python:")
    print(f"Integer: {integer_value} ({type(integer_value)})")
    print(f"Float: {float_value} ({type(float_value)})")
    print(f"String: {string_value} ({type(string_value)})")
    print(f"Boolean: {boolean_value} ({type(boolean_value)})")
    print(f"List: {list_value} ({type(list_value)})")
    print(f"Tuple: {tuple_value} ({type(tuple_value)})")
    print(f"Dictionary: {dict_value} ({type(dict_value)})")
    print(f"Set: {set_value} ({type(set_value)})")

# Run functions
if __name__ == "__main__":
    display_keywords()
    explore_data_types()
