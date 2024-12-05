
def containsDuplicate(nums):
        tuple = set()
        for n in nums:
            if n in tuple:
                return True
            tuple.add(n)
        return False

print(containsDuplicate([1,4,4,7]))