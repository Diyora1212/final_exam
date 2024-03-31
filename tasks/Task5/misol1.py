def length_of_last_word(s: str) -> int:
    words = s.split()
    return len(words[-1])


print(length_of_last_word("Hey axvollaring yaxshimi  "))
print(length_of_last_word("   oy to'lgan kechada borilar uvillashadi "))
print(length_of_last_word("Ustoooz, iltimoos yetarli ball qo'ybeering qo'limdan kelguncha tinmasdan harakat qildim"))
