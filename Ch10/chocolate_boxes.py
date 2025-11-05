# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Michaela Gutermuth
# Simon O'Brien
# Anthony Do
# Will Gipson
# Section: 217
# Assignment: Lab 10 Group Chocolate Boxes
# Date: 28 10 2025
#
#


import random
from itertools import islice

def make_boxes(truffles):
    """
    Fast greedy algorithm to arrange 100 truffles into 25 boxes of 4.
    """
    attrs = {tid: tuple(truffle_list) for tid, truffle_list in truffles.items()}
    
    def conflicts_with(t1, t2):
        """Check if two truffles conflict"""
        a1, a2 = attrs[t1], attrs[t2]
        
        # Same attributes
        if a1 == a2:
            return True
        
        # Rectangle + square
        if (a1[1] == "rectangle" and a2[1] == "square") or \
           (a1[1] == "square" and a2[1] == "rectangle"):
            return True
        
        # Vanilla + caramel
        if (a1[2] == "vanilla" and a2[2] == "caramel") or \
           (a1[2] == "caramel" and a2[2] == "vanilla"):
            return True
        
        # Nuts + sprinkles
        if (a1[3] == "nuts" and a2[3] == "sprinkles") or \
           (a1[3] == "sprinkles" and a2[3] == "nuts"):
            return True
        
        return False
    
    def is_valid_box(box_tids):
        """Check if a box satisfies all constraints"""
        if len(box_tids) != 4:
            return False
        
        # Check pairwise conflicts
        for i in range(len(box_tids)):
            for j in range(i + 1, len(box_tids)):
                if conflicts_with(box_tids[i], box_tids[j]):
                    return False
        
        # Check dark chocolate constraint
        dark_count = sum(1 for tid in box_tids if attrs[tid][0] == "dark")
        if dark_count > 0 and dark_count not in (2, 3):
            return False
        
        return True
    
    def greedy_build_box(remaining, start_idx=0):
        """Greedily build a valid box starting from start_idx"""
        if len(remaining) < 4:
            return None
        
        # Try different starting positions
        for offset in range(min(20, len(remaining))):
            idx = (start_idx + offset) % len(remaining)
            box = [remaining[idx]]
            
            # Greedily add compatible truffles
            for tid in remaining:
                if tid in box:
                    continue
                
                # Check if this truffle conflicts with any in the box
                valid = True
                for existing in box:
                    if conflicts_with(tid, existing):
                        valid = False
                        break
                
                if valid:
                    box.append(tid)
                    if len(box) == 4:
                        # Check dark chocolate constraint
                        if is_valid_box(box):
                            return box
                        else:
                            # Try different combination
                            box.pop()
        
        return None
    
    def solve_greedy(remaining, attempt):
        """Greedy solver with randomization"""
        boxes = []
        remaining = remaining.copy()
        
        for box_idx in range(25):
            # Try to build a box
            box = greedy_build_box(remaining, start_idx=(attempt + box_idx) % len(remaining))
            
            if box is None:
                return None
            
            boxes.append(box)
            # Remove used truffles
            for tid in box:
                remaining.remove(tid)
        
        return boxes if len(remaining) == 0 else None
    
    # Try with different random orderings
    truffle_ids = list(truffles.keys())
    
    for attempt in range(1000):
        random.seed(attempt)
        shuffled = truffle_ids.copy()
        random.shuffle(shuffled)
        
        result = solve_greedy(shuffled, attempt)
        
        if result is not None:
            print(f"Solution found on attempt {attempt + 1}")
            return result
        
        if attempt % 50 == 49:
            print(f"  Still searching... (attempt {attempt + 1}/1000)")
    
    raise Exception("No valid arrangement found after 1000 attempts")


# Testing
def test_boxes():
    chocolates = {}
    choc_types = ["dark", "milk", "white"]
    shapes = ["round", "square", "rectangle", "heart"]
    fillings = ["strawberry", "vanilla", "caramel", "coconut", "toffee"]
    toppings = ["sprinkles", "nuts", "white drizzle", "dark drizzle", "nothing"]
    
    tid = 1
    random.seed(42)
    for _ in range(100):
        chocolates[tid] = [
            random.choice(choc_types),
            random.choice(shapes),
            random.choice(fillings),
            random.choice(toppings)
        ]
        tid += 1
    
    print("Making boxes...")
    import time
    start = time.time()
    boxes = make_boxes(chocolates)
    elapsed = time.time() - start
    print(f"✓ Completed in {elapsed:.2f} seconds\n")
    
    # Verify all constraints
    print("Verifying constraints...")
    all_used = []
    for i, box in enumerate(boxes, 1):
        all_used.extend(box)
        
        box_attrs = [tuple(chocolates[tid]) for tid in box]
        shapes = [chocolates[tid][1] for tid in box]
        fills = [chocolates[tid][2] for tid in box]
        tops = [chocolates[tid][3] for tid in box]
        chocs = [chocolates[tid][0] for tid in box]
        
        # Check all constraints
        assert len(box) == 4, f"Box {i} has {len(box)} truffles"
        assert len(set(box_attrs)) == 4, f"Box {i} has duplicate attributes"
        assert not ("rectangle" in shapes and "square" in shapes), f"Box {i} has both rectangle and square"
        assert not ("vanilla" in fills and "caramel" in fills), f"Box {i} has both vanilla and caramel"
        assert not ("nuts" in tops and "sprinkles" in tops), f"Box {i} has both nuts and sprinkles"
        
        dark_count = chocs.count("dark")
        if dark_count > 0:
            assert dark_count in (2, 3), f"Box {i} has {dark_count} dark chocolates"
    
    assert len(all_used) == 100, f"Only {len(all_used)} truffles used"
    assert len(set(all_used)) == 100, "Some truffles used multiple times"
    
    print("✓ All constraints satisfied!\n")
    
    # Show statistics
    dark_boxes = sum(1 for box in boxes if any(chocolates[tid][0] == 'dark' for tid in box))
    print(f"Statistics:")
    print(f"  Total boxes: {len(boxes)}")
    print(f"  Boxes with dark chocolate: {dark_boxes}")
    
    # Show first 3 boxes
    print("\nFirst 3 boxes:")
    for i in range(3):
        print(f"\nBox {i+1}:")
        for tid in boxes[i]:
            choc = chocolates[tid]
            print(f"  Truffle {tid}: {choc[0]} chocolate, {choc[1]}, {choc[2]} filling, {choc[3]} topping")
    
    return boxes

if __name__ == "__main__":
    test_boxes()

chocolates = {1: ["milk", "round", "toffee", "sprinkles"],
2: ["milk", "square", "coconut", "none"],
3: ["dark", "heart", "strawberry", "white chocolate drizzle"],
4: ["dark", "round", "toffee", "white chocolate drizzle"],
5: ["milk", "square", "caramel", "nuts"],
6: ["milk", "heart", "toffee", "dark chocolate drizzle"],
7: ["dark", "rectangle", "caramel", "none"],
8: ["dark", "heart", "strawberry", "white chocolate drizzle"],
9: ["dark", "heart", "coconut", "white chocolate drizzle"],
10: ["milk", "square", "coconut", "none"],
11: ["milk", "round", "vanilla", "dark chocolate drizzle"],
12: ["milk", "round", "strawberry", "nuts"],
13: ["milk", "rectangle", "caramel", "sprinkles"],
14: ["dark", "rectangle", "toffee", "none"],
15: ["dark", "heart", "toffee", "none"],
16: ["dark", "heart", "coconut", "white chocolate drizzle"],
17: ["dark", "round", "vanilla", "none"],
18: ["dark", "rectangle", "toffee", "dark chocolate drizzle"],
19: ["milk", "round", "toffee", "none"],
20: ["milk", "square", "caramel", "dark chocolate drizzle"],
21: ["milk", "square", "vanilla", "none"],
22: ["dark", "heart", "caramel", "sprinkles"],
23: ["milk", "square", "caramel", "nuts"],
24: ["milk", "round", "caramel", "dark chocolate drizzle"],
25: ["milk", "round", "coconut", "dark chocolate drizzle"],
26: ["dark", "round", "coconut", "dark chocolate drizzle"],
27: ["milk", "rectangle", "strawberry", "sprinkles"],
28: ["white", "heart", "vanilla", "none"],
29: ["dark", "heart", "strawberry", "none"],
30: ["dark", "rectangle", "caramel", "none"],
31: ["white", "round", "caramel", "none"],
32: ["milk", "heart", "vanilla", "none"],
33: ["white", "round", "strawberry", "nuts"],
34: ["milk", "round", "coconut", "none"],
35: ["dark", "rectangle", "coconut", "dark chocolate drizzle"],
36: ["milk", "round", "vanilla", "dark chocolate drizzle"],
37: ["dark", "round", "coconut", "white chocolate drizzle"],
38: ["dark", "round", "coconut", "white chocolate drizzle"],
39: ["dark", "round", "coconut", "dark chocolate drizzle"],
40: ["dark", "round", "strawberry", "dark chocolate drizzle"],
41: ["milk", "rectangle", "toffee", "none"],
42: ["milk", "round", "strawberry", "white chocolate drizzle"],
43: ["milk", "heart", "coconut", "none"],
44: ["white", "round", "strawberry", "white chocolate drizzle"],
45: ["milk", "heart", "toffee", "sprinkles"],
46: ["milk", "rectangle", "strawberry", "none"],
47: ["white", "round", "caramel", "dark chocolate drizzle"],
48: ["white", "square", "toffee", "none"],
49: ["milk", "rectangle", "toffee", "none"],
50: ["dark", "rectangle", "caramel", "none"],
51: ["milk", "square", "vanilla", "none"],
52: ["dark", "round", "toffee", "dark chocolate drizzle"],
53: ["milk", "round", "toffee", "white chocolate drizzle"],
54: ["dark", "square", "strawberry", "none"],
55: ["milk", "heart", "caramel", "dark chocolate drizzle"],
56: ["milk", "heart", "vanilla", "none"],
57: ["milk", "heart", "caramel", "none"],
58: ["milk", "heart", "coconut", "sprinkles"],
59: ["milk", "heart", "vanilla", "sprinkles"],
60: ["dark", "square", "caramel", "none"],
61: ["milk", "rectangle", "vanilla", "none"],
62: ["milk", "heart", "toffee", "none"],
63: ["milk", "heart", "vanilla", "dark chocolate drizzle"],
64: ["white", "round", "coconut", "white chocolate drizzle"],
65: ["milk", "round", "coconut", "nuts"],
66: ["milk", "round", "coconut", "white chocolate drizzle"],
67: ["dark", "heart", "coconut", "none"],
68: ["dark", "square", "toffee", "none"],
69: ["dark", "round", "strawberry", "dark chocolate drizzle"],
70: ["milk", "heart", "caramel", "none"],
71: ["milk", "square", "caramel", "sprinkles"],
72: ["milk", "rectangle", "strawberry", "sprinkles"],
73: ["dark", "heart", "strawberry", "none"],
74: ["dark", "heart", "strawberry", "none"],
75: ["dark", "square", "coconut", "none"],
76: ["dark", "heart", "caramel", "none"],
77: ["dark", "heart", "coconut", "nuts"],
78: ["white", "rectangle", "caramel", "dark chocolate drizzle"],
79: ["milk", "heart", "vanilla", "sprinkles"],
80: ["white", "heart", "strawberry", "none"],
81: ["dark", "round", "toffee", "white chocolate drizzle"],
82: ["dark", "round", "vanilla", "none"],
83: ["white", "square", "coconut", "none"],
84: ["milk", "rectangle", "caramel", "dark chocolate drizzle"],
85: ["white", "heart", "toffee", "none"],
86: ["white", "round", "caramel", "nuts"],
87: ["white", "round", "caramel", "none"],
88: ["dark", "round", "caramel", "none"],
89: ["dark", "square", "coconut", "nuts"],
90: ["milk", "heart", "vanilla", "none"],
91: ["dark", "round", "coconut", "none"],
92: ["dark", "round", "caramel", "none"],
93: ["white", "round", "toffee", "none"],
94: ["milk", "round", "vanilla", "sprinkles"],
95: ["white", "round", "strawberry", "white chocolate drizzle"],
96: ["dark", "square", "strawberry", "nuts"],
97: ["milk", "round", "vanilla", "none"],
98: ["milk", "rectangle", "caramel", "sprinkles"],
99: ["milk", "heart", "vanilla", "none"],
100: ["dark", "rectangle", "strawberry", "white chocolate drizzle"],
}


make_boxes(chocolates)