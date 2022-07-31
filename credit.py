credit_card = int(input("Please enter the 16 digit card number"))

card_number = [int(x) for x in str(credit_card)]
control_number = card_number[15]

odd_numbers_elements = [card_number[0], card_number[2], card_number[4],
                        card_number[6], card_number[8], card_number[10], card_number[12], card_number[14]]
even_number_elements = [card_number[1], card_number[3], card_number[5],
                        card_number[7], card_number[9], card_number[11], card_number[13]]

all_double = []
for odd_numbers in odd_numbers_elements:
    double = odd_numbers * 2
    separate_double = [int(x) for x in str(double)]
    for number in separate_double:
        all_double.append(number)

even_number_sum = sum(even_number_elements)
double_sum = sum(all_double)
total_sum = even_number_sum + double_sum

divide_by_ten = total_sum/10
number_after_decimal = int(str(divide_by_ten).split('.')[1])
final_number = 10-number_after_decimal
if final_number == control_number:
    print("Number is valid")
else:
    print("Number invalid")
