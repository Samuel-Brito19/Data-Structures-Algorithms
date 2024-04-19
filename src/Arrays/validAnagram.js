function isValidAnagram (s,t) {
    const setLetter = new Set()

    for (i=0; i < s.length; i++) {
        console.log(s[i])
    }
    for (i=0; i < t.length; i++) {
        console.log(t[i])
    }
}

isValidAnagram("rat", "cat")