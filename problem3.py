def spell_out_number(num):
    if num == 0:
        return "zero"
    
    # List of number names for units, tens, and hundreds places
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundreds = ["", "one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
    
    # Divide the number into thousands and hundreds places
    thousands_place = num // 1000
    hundreds_place = num % 1000
    
    # Handle the thousands place if it is greater than zero
    if thousands_place > 0:
        if thousands_place == 1:
            output = "one thousand"
        else:
            output = spell_out_number(thousands_place) + " thousand"
        
        # Add the hundreds place if it is also greater than zero
        if hundreds_place > 0:
            output += " " + spell_out_number(hundreds_place)
    else:
        # Handle the hundreds place if the thousands place is zero
        if hundreds_place >= 100:
            output = hundreds[hundreds_place // 100] + " " + spell_out_number(hundreds_place % 100)
        elif hundreds_place >= 20:
            output = tens[hundreds_place // 10] + "-" + units[hundreds_place % 10]
        elif hundreds_place >= 10:
            output = units[hundreds_place]
        else:
            output = units[hundreds_place]
    
    return output
print(spell_out_number(0)) # zero
print(spell_out_number(5)) # five
print(spell_out_number(8)) # eight
print(spell_out_number(10)) # ten
print(spell_out_number(21)) # twenty-one
print(spell_out_number(77)) # seventy-seven
print(spell_out_number(100)) # one hundred
print(spell_out_number(303)) # three hundred three
print(spell_out_number(555)) # five hundred fifty-five
print(spell_out_number(2000)) # two thousand
print(spell_out_number(3466)) # three thousand four hundred sixty-six
print(spell_out_number(2400)) # two thousand four hundred
print(spell_out_number(5300)) # fifty-three hundred