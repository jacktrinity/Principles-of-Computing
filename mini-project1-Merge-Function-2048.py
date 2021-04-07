"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    def add_missing_zero(a_list):
        """
        Add appropriate number of zeroes at the end of the list.
        """
        while len(a_list) < len(line):
            a_list.append(0)
        return a_list
    
    def non_zero_slide(b_list):
        """
        Iterate over the input and create an output list that has all 
        of the non-zero tiles slid over to the beginning of the list.
        """
        append_list = []
        for dummy_num in b_list:
            if dummy_num > 0:
                append_list.append(dummy_num)
        return append_list
        
    lst1 = non_zero_slide(line)
    lst1 = add_missing_zero(lst1)
    
    # merging numbers
    num = 0
    while num < len(lst1) - 1:
        if lst1[num] == lst1[num + 1]:
            lst1[num] = lst1[num] * 2
            lst1[num + 1] = 0
        num += 1
        
    lst2 = non_zero_slide(lst1)
    lst2 = add_missing_zero(lst2)
        
    return lst2
