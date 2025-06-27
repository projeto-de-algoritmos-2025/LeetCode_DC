class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        
        # Criar lista de tuplas (índice, valor) para manter o rastreamento
        indexed_nums = [(i, nums[i]) for i in range(len(nums))]
        result = [0] * len(nums)
        
        def merge_sort(enum):
            """
            Divide e conquista usando merge sort
            enum: lista de tuplas (índice, valor)
            """
            if len(enum) <= 1:
                return enum
            
            # DIVIDE: dividir ao meio
            mid = len(enum) // 2
            left = merge_sort(enum[:mid])
            right = merge_sort(enum[mid:])
            
            # CONQUISTA: mesclar e contar inversões
            return merge(left, right)
        
        def merge(left, right):
            """
            Mescla duas listas ordenadas e conta inversões
            """
            merged = []
            count = 0  # contador de inversões
            
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    # Elemento da esquerda é menor ou igual
                    merged.append(left[i])
                    # Atualizar contador para o elemento da esquerda
                    result[left[i][0]] += count
                    i += 1
                else:
                    # Elemento da direita é menor (inversão!)
                    merged.append(right[j])
                    count += 1  # incrementar contador
                    j += 1
            
            # Adicionar elementos restantes da esquerda
            while i < len(left):
                merged.append(left[i])
                result[left[i][0]] += count
                i += 1
            
            # Adicionar elementos restantes da direita
            while j < len(right):
                merged.append(right[j])
                j += 1
            
            return merged
        
        # Executar o merge sort
        merge_sort(indexed_nums)
        
        return result


# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    nums1 = [5, 2, 6, 1]
    print("Input: {}".format(nums1))
    print("Output: {}".format(solution.countSmaller(nums1)))  # Expected: [2, 1, 1, 0]
    
    # Test case 2
    nums2 = [-1]
    print("\nInput: {}".format(nums2))
    print("Output: {}".format(solution.countSmaller(nums2)))  # Expected: [0]
    
    # Test case 3
    nums3 = [-1, -1]
    print("\nInput: {}".format(nums3))
    print("Output: {}".format(solution.countSmaller(nums3)))  # Expected: [0, 0]
    
    # Additional test case
    nums4 = [3, 2, 2, 6, 1]
    print("\nInput: {}".format(nums4))
    print("Output: {}".format(solution.countSmaller(nums4)))  # Expected: [3, 1, 1, 1, 0]
    
    # Test case with duplicates
    nums5 = [2, 0, 1]
    print("\nInput: {}".format(nums5))
    print("Output: {}".format(solution.countSmaller(nums5)))  # Expected: [2, 0, 0] 