string = "mihret"

def reverse(string):
    if len(string) == 1:
        return string
    
    print(string)
    
    return string[-1] + reverse(string[:-1])

print(reverse(string))
print(reverse("all the way"))
print(reverse("to work"))