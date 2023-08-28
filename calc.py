print("""

░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝




[1] +
[2] -
[3] *
[4] /
[5] Exit Calculator
""")
while True:
	select = input(", ")

	if select == '1':
		a = input("Enter first digit: ")
		print("+")
		b = input("Enter the second digit: ")
		c = int(a)+int(b)
		print(c)


	if select == '2':
		a = input("Enter first digit: ")
		print("-")
		b = input("Enter the second digit: ")
		c = int(a)-int(b)
		print(c)

	if select == '3':
		a = input("Enter first digit: ")
		print("*")
		b = input("Enter the second digit: ")
		c = int(a)*int(b)
		print(c)

	if select == '4':
		a = input("Enter first digit: ")
		print("/")
		b = input("Enter the second digit: ")
		c = int(a)/int(b)
		print(c)

		if select == '5':
			os.system('exit')