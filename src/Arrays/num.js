
var containsDuplicate = function(nums) {
    const set = new Set()

    for(n of nums) {
        if(set.has(n)) {
            return true
        }
        set.add(n)
    }
    return false


};

console.log(containsDuplicate([1,2,3,1]))