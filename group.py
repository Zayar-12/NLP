import pandas as pd
import random

def create_ml_optimized_groups(file_path, num_groups=16, iterations=2000):
    # 1. Load dataset
    df = pd.read_csv(file_path, encoding='utf-8')
    df.columns = df.columns.str.strip()
    
    students = df.to_dict('records')
    total_students = len(students)
    
    # Calculate target group sizes dynamically for 16 groups (mix of 4 and 5 members)
    base_size = total_students // num_groups
    extra = total_students % num_groups
    target_sizes = [base_size + 1 if i < extra else base_size for i in range(num_groups)]
    
    best_groups = None
    min_penalty = float('inf')
    
    # 2. Iterative Optimization (Minimizing university clashes under capacity constraints)
    for seed in range(iterations):
        random.seed(seed)
        shuffled_students = list(students)
        random.shuffle(shuffled_students)
        
        groups = [[] for _ in range(num_groups)]
        
        for student in shuffled_students:
            uni = student['တက္ကသိုလ်']
            
            best_group_idx = -1
            min_score = float('inf')
            
            for idx, g in enumerate(groups):
                if len(g) >= target_sizes[idx]:
                    continue # Skip if group is at max capacity
                
                # Check university duplication clash
                has_uni = any(m['တက္ကသိုလ်'] == uni for m in g)
                clash_penalty = 1000 if has_uni else 0
                
                # Balance size penalty
                size_penalty = len(g)
                
                total_score = clash_penalty + size_penalty
                
                if total_score < min_score:
                    min_score = total_score
                    best_group_idx = idx
            
            if best_group_idx != -1:
                groups[best_group_idx].append(student)
            else:
                # Fallback if strict capacities are full
                min_len_idx = min(range(num_groups), key=lambda i: len(groups[i]))
                groups[min_len_idx].append(student)
                
        # Calculate total penalty (duplicates) for this iteration
        current_penalty = 0
        for g in groups:
            unis = [m['တက္ကသိုလ်'] for m in g]
            duplicates = len(unis) - len(set(unis))
            current_penalty += duplicates
            
        if current_penalty < min_penalty:
            min_penalty = current_penalty
            best_groups = groups
            
        if min_penalty == 0:
            break # Perfect solution found
            
    return best_groups

# Execute the grouping for 16 groups
groups = create_ml_optimized_groups('Computer_Science_CS.csv', num_groups=16, iterations=2000)

# 3. Save output cleanly with UTF-8 encoding
with open("groups_output.txt", "w", encoding="utf-8") as f:
    f.write(f"=== ML-Optimized Grouping (16 Groups, Zero Leftovers) ===\n\n")
    for i, g in enumerate(groups, 1):
        unis_in_group = [m['တက္ကသိုလ်'] for m in g]
        unique_count = len(set(unis_in_group))
        f.write(f"=== Group {i} (Members: {len(g)}, Unique Universities: {unique_count}/{len(g)}) ===\n")
        for m in g:
            f.write(f"  - {m['အမည်']} ({m['တက္ကသိုလ်']})\n")
        f.write("\n")

print("16 ML-Optimized groups saved successfully to 'groups_output.txt'! Open that file to view clear Burmese text.")